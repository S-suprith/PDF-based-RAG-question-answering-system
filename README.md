# PDF RAG – Question Answering System

A PDF-based Retrieval-Augmented Generation (RAG) system that allows users to ask questions about PDF documents and receive concise, context-aware answers with source and page references.

## Features

* Load and process PDF documents
* Split documents into meaningful chunks
* Generate semantic embeddings using Hugging Face
* Store and retrieve embeddings using ChromaDB
* Perform similarity-based document retrieval
* Generate answers using Groq LLM
* Conversational memory using LangGraph
* Display source documents and page references
* Interactive chat interface using Streamlit
* Dependency management using `uv`

## Technologies Used

* Python
* LangChain
* LangGraph
* ChromaDB
* Hugging Face Embeddings
* Groq LLM
* Streamlit
* PyPDF
* uv

## Project Structure

```text
PDF-RAG-QA/
│
├── data/
│   └── your_document.pdf
│
├── docs/
│   └── chroma/
│
├── app.py
├── ingest.py
├── config.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

## System Workflow

```text
PDF Document
     |
     v
PDF Loading
     |
     v
Text Chunking
     |
     v
Embedding Generation
     |
     v
ChromaDB
     |
     v
Similarity Search
     |
     v
Relevant Context
     |
     v
Groq LLM
     |
     v
Generated Answer
     |
     v
Source and Page Reference
```

## Configuration

The main configuration is defined in `config.py`.

```python
PDF_SOURCE_DIRECTORY = "data"
CHROMA_PERSIST_DIRECTORY = "docs/chroma"
EMBEDDING_MODEL_NAME = "intfloat/multilingual-e5-large"
CHUNK_SIZE = 2028
CHUNK_OVERLAP = 250
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/S-suprith/PDF-based-RAG-question-answering-system
```

### 2. Install uv

```bash
pip install uv
```

Verify the installation:

```bash
uv --version
```

### 3. Create the Virtual Environment

```bash
uv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit the `.env` file to GitHub.

## Add PDF Documents

Place PDF documents inside the `data` directory:

```text
data/
└── embedded-systems.pdf
```

## Create the Vector Database

Run the ingestion script:

```bash
uv run ingest.py
```

The ingestion process:

1. Loads PDF documents.
2. Extracts the text.
3. Splits the text into chunks.
4. Generates embeddings.
5. Stores the embeddings in ChromaDB.

The vector database is stored in:

```text
docs/chroma/
```

## Run the Application

Start the Streamlit application:

```bash
uv run streamlit run app.py
```

The application will provide a local URL that can be opened in a web browser.

## Example

User question:

```text
What is an embedded system?
```

The system retrieves relevant content from the PDF and generates an answer using the Groq LLM.

The application also displays the corresponding source document and relevant page numbers.

## How the System Works

### 1. PDF Loading

PDF documents are loaded using `PyPDFLoader`.

### 2. Text Chunking

The extracted document content is divided into smaller chunks using a recursive text splitter.

### 3. Embedding Generation

Each chunk is converted into a vector representation using:

```text
intfloat/multilingual-e5-large
```

### 4. Vector Storage

The generated embeddings are stored in ChromaDB.

### 5. Similarity Search

When a user submits a question, the system performs a similarity search to retrieve the most relevant document chunks.

### 6. Answer Generation

The retrieved context and user question are provided to the Groq LLM to generate the final response.

### 7. Source References

The application displays the source document and relevant page numbers used during retrieval.

## Security

The following files and directories should not be committed to GitHub:

```text
.env
.venv/
__pycache__/
docs/chroma/
```

Recommended `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.env
docs/chroma/
.vscode/
```

## Notes

* An internet connection is required when downloading the Hugging Face embedding model for the first time.
* Groq API access requires an internet connection.
* Run `ingest.py` again after adding or modifying PDF documents.
* Keep the Groq API key private.

## Future Enhancements

* Hybrid search
* Metadata filtering
* Reranking
* Query rewriting
* RAG evaluation
* Multi-document conversational RAG
* Improved source citations
* Agentic RAG
* Cloud deployment

## Author

**Suprith**

B.Tech – Computer Science and Engineering (AI & Data Science)

## GitHub Repository Description

> PDF-based Retrieval-Augmented Generation (RAG) question-answering system using LangChain, LangGraph, ChromaDB, Hugging Face embeddings, Groq LLM, and Streamlit.
