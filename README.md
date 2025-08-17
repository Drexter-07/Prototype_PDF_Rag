# 📄 Simple PDF RAG Chat Prototype

This is a **terminal-based prototype** of a Retrieval-Augmented Generation (RAG) application.  
It allows you to chat with a PDF document by leveraging a vector database (**Qdrant**) and Large Language Models (**OpenAI**).

---

## ✨ Features
1. **Document Ingestion** – Loads a PDF, splits it into chunks, generates embeddings, and stores them in a Qdrant vector database.  
2. **Interactive Chat** – Provides a command-line interface to ask questions about the document.  
3. **Dynamic Context Retrieval** – Performs semantic search on the vector database to find the most relevant text chunks.  
4. **AI-Powered Answers** – Uses the retrieved context and the user’s question with an OpenAI model (e.g., GPT-4o) to generate contextual answers.  

---

## 📋 Prerequisites
Make sure the following are installed on your local machine:

- Python **3.9+**  
- Docker & Docker Compose  
- Git  

---

## ⚙️ Setup & Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Drexter-07/Prototype_PDF_Rag.git
```

### 2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

### Create the virtual environment
```bash
python -m venv venv
```

### Activate it
```bash
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```


### 3. Install Python Dependencies
Install all the required Python packages from the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
This project requires an OpenAI API key.
```bash
Create a file named .env in the root of the project folder.

Add your API key to this file:

OPENAI_API_KEY="sk-YourSecretApiKeyGoesHere"
```

### 5. Start the Vector Database
The Qdrant vector database runs in a Docker container. Use the provided Docker Compose file to start it. The -d flag runs it in detached mode (in the background).
```bash
docker compose -f docker-compose.db.yml up -d
```

You can check if the container is running with docker ps.

### 6. Place Your PDF
Place the PDF file you want to chat with into the root of the project directory. The script is currently configured to look for a file named nodejs.pdf. You can change this in the RAG_Prototype.py script if you wish.


## 🚀 Running the Application
The application has two main phases: a one-time ingestion and the continuous chat loop.

### 1. First Run: Ingest the Document
The first time you run the script with a new PDF, you need to ingest its content into the database.

- Uncomment the ingestion code block in RAG_Prototype.py.

- Run the script:
```bash
python RAG_Prototype.py
```

Wait for the "Ingestion Done" message.

Once finished, re-comment the ingestion block to avoid running it again unnecessarily.

### 2. Run the Chat
With the ingestion complete, you can now run the script to start chatting with your document.
```bash
python RAG_Prototype.py
```

The terminal will prompt you to ask questions. Type exit to quit the application.

🧹 Cleanup
When you are finished, you can stop the Qdrant database container with the following command:
```bash
docker compose -f docker-compose.db.yml down
```     
