const apiBaseUrl = "http://localhost:5000";  // Adjust the base URL if necessary

// Function to handle PDF upload
async function uploadPDF(files) {
    const formData = new FormData();
    files.forEach(file => formData.append("files", file));

    try {
        const response = await fetch(`${apiBaseUrl}/upload-pdf`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        document.getElementById("response").textContent = data.message || "Files uploaded and processed!";
    } catch (error) {
        console.error("Error uploading PDF files:", error);
        document.getElementById("response").textContent = "Error uploading files. Please try again.";
    }
}

// Function to handle question submission
async function askQuestion(question) {
    try {
        const response = await fetch(`${apiBaseUrl}/ask-question`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();
        document.getElementById("response").textContent = data.reply || "No reply available.";
    } catch (error) {
        console.error("Error asking question:", error);
        document.getElementById("response").textContent = "Error fetching answer. Please try again.";
    }
}

// Button handlers
function handleUpload() {
    const files = Array.from(document.getElementById('pdfFiles').files);
    if (files.length > 0) {
        uploadPDF(files);
    } else {
        document.getElementById("response").textContent = "Please select at least one PDF file.";
    }
}

function handleQuestion() {
    const question = document.getElementById('question').value;
    if (question.trim()) {
        askQuestion(question);
    } else {
        document.getElementById("response").textContent = "Please enter a question.";
    }
}
