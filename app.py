from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_community.vectorstores import FAISS

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from flask_cors import CORS
# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
CORS(app)

# Get the Google API key from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is None:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Configure the Google Generative AI API key
genai.configure(api_key=google_api_key)


# Helper functions
def get_pdf_text(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(api_key=google_api_key, model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(api_key=google_api_key, model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain


# Flask API endpoints
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    files = request.files.getlist("files")
    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    pdf_text = get_pdf_text(files)
    text_chunks = get_text_chunks(pdf_text)
    get_vector_store(text_chunks)

    return jsonify({"message": "PDF files processed and vector store created"}), 200


@app.route('/ask-question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "Question is required"}), 400

    embeddings = GoogleGenerativeAIEmbeddings(api_key=google_api_key, model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = vector_store.similarity_search(question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

    return jsonify({"reply": response["output_text"]})


if __name__ == '__main__':
    aapp.run(host='0.0.0.0', port=5000)
