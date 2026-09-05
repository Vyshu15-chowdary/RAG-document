# RAG Document Question Answering System

## About the Project

This project is a simple **Retrieval-Augmented Generation (RAG)** based document question-answering system.

It allows users to ask questions about a PDF document and receive answers based on the information available in that document.

I built the RAG pipeline from scratch to understand how document processing, embeddings, vector search, prompt creation, and LLM-based answer generation work together.

## Purpose of the Project

The main purpose of this project is to build a system that can:

* Read and process PDF documents
* Find relevant information from the document
* Answer user questions using the retrieved information
* Reduce irrelevant or unsupported answers
* Understand the core RAG workflow without depending on a framework like LangChain

## Project Details

The project follows these steps:

1. Extract text from the PDF using **pypdf**.
2. Split the extracted text into smaller chunks.
3. Convert the chunks into embeddings using **Sentence Transformers**.
4. Store the embeddings and document chunks in **ChromaDB**.
5. Convert the user's question into an embedding.
6. Search ChromaDB to retrieve the most relevant chunks.
7. Add the retrieved chunks to a prompt.
8. Send the prompt to **Llama 3.1** through the Hugging Face Inference API.
9. Generate the final answer and display the source document and chunk information.

### Technologies Used

* Python
* pypdf
* Sentence Transformers
* ChromaDB
* Hugging Face Inference API
* Llama 3.1
* python-dotenv

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Vyshu15-chowdary/RAG-document.git
cd RAG-document
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

For Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Hugging Face Token

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token
```

### 5. Add Your PDF

Place the PDF you want to query inside:

```text
documents/
```

### 6. Run the Project

First process the document and store its embeddings in ChromaDB.

Then run:

```bash
python app/test_rag.py
```

Enter or modify the question in `test_rag.py`:

```python
question = "What is a document database?"
```

The system retrieves relevant content from the PDF and generates an answer using the LLM.

## Example

**Question:**

```text
What is a document database?
```

**Answer:**

```text
A Document Database stores data in the form of documents instead of tables.
```

The system also displays the source file and the retrieved chunk numbers.
