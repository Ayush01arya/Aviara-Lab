# AI Chat Application with PDF Knowledge Base

An AI-powered chat application that allows users to upload PDF files and interact with an AI to ask questions based on the PDF content. The project includes:
- A **Streamlit-based chat interface** for interacting with PDF content.
- A **Flask API with frontend integration** that connects to a large language model (LLM) using Gemini API or Hugging Face models.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [Flask Backend Setup](#flask-backend-setup)
  - [Streamlit Application Setup](#streamlit-application-setup)
- [Usage](#usage)
  - [Frontend Setup (for Flask Application)](#frontend-setup-for-flask-application)
  - [Sample Fetch API Code](#sample-fetch-api-code)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [License](#license)

---

## Project Overview

This application allows users to:
1. Upload PDFs to serve as a knowledge base.
2. Interact with an AI chat interface by asking questions related to the PDF content.
3. Receive responses generated by an LLM model, integrated through Retrieval-Augmented Generation (RAG) for enhanced accuracy.

## Features

- **AI Chat Interface**: A user-friendly chat interface in Streamlit for PDF-based Q&A.
- **LLM Integration**: Connects to Gemini or Hugging Face API to process user queries.
- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval and AI content generation.
- **Flask API**: Provides REST endpoints for PDF uploads and queries.
- **Unit Testing**: Includes unit tests for robust and accurate functionality.

## Requirements

- Python 3.7+
- Virtual environment tools (e.g., `venv` or `conda`)
- [Streamlit](https://streamlit.io/)
- [Flask](https://flask.palletsprojects.com/)
- PyPDF2
- Requests
- API account on [Gemini](https://gemini.api.com) or [Hugging Face](https://huggingface.co)

## Setup Instructions

### Flask Backend Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ayush01arya/Aviara-Lab.git
   cd your-repository
Set Up Virtual Environment

```bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install Requirements

```bash

  pip install -r requirements.txt
Environment Variables

