# 🤖 Agentic AI & Advanced RAG Hub

Welcome to the **Agentic AI & Advanced RAG Hub**! This repository is a comprehensive workspace for practicing, implementing, and mastering modern AI Agent workflows and advanced Retrieval-Augmented Generation (RAG) architectures.

It features hands-on implementations of **LangGraph**, **LangChain**, and a complete end-to-end **RAG Course** covering document processing, vector databases, advanced retrieval algorithms, and agentic/graph-based RAG.

---

## 📂 Repository Structure

The workspace is organized into three core modules:

```text
├── 🕸️ LangGraph/            # Multi-agent systems, state graphs & tool calling
│   ├── client.py            # Async MultiServerMCPClient using LangGraph & Gemini
│   ├── mathserver.py        # Custom MCP server for mathematical computations
│   └── weather.py           # Custom MCP server for weather querying
│
├── 🦜 Langchain/            # LangChain integrations and Jupyter notebooks
│   └── m4_middlewares.ipynb  # Notebook exploring LangChain middlewares and configurations
│
└── 📚 RAG_Course/           # Step-by-step advanced RAG implementations
    ├── 1_Document_Loaders/  # PDF, CSV, TXT loaders & OCR image-text extraction (Tesseract/RapidOCR)
    ├── 7_RAG_Hyde/          # Hypothetical Document Embeddings (HyDE)
    └── 11_Advanced_Retrievers/ # Advanced retrieval techniques (parent-child chunking, re-ranking)
```

---

## 🚀 Modules Overview

### 1. 🕸️ LangGraph & Model Context Protocol (MCP)
Focuses on building stateful, multi-agent systems that can utilize external tools through the **Model Context Protocol (MCP)**:
- **`client.py`**: Runs a LangGraph agent (`create_agent`) that asynchronously coordinates tool calls across multiple servers (Math and Weather).
- **Custom Servers**: Implements stdio-based and HTTP SSE-based servers for extending agent capabilities.

### 2. 🦜 LangChain Foundations
Contains practical implementations of LangChain components, including prompts, memory, custom parsers, and middleware interfaces for orchestrating LLM interactions.

### 3. 📚 Advanced RAG Course
A deep dive into building production-ready RAG systems:
- **Document Loading & OCR**: Processing complex documents (PDFs, CSVs) and using OCR (`Tesseract` / `RapidOCR`) to extract textual information from charts, graphs, and images.
- **Advanced Retrieval**: Implementing semantic search enhancements like **HyDE** (generating hypothetical answers to boost retrieval accuracy) and **Parent Document Retrieval** (storing small chunks for search but retrieving large context for generation).
- **Graph RAG & Agents**: Exploring Graph-based knowledge retrieval and Agentic routing.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Python 3.12+**
- **Tesseract OCR Engine** (Required for PDF image/chart OCR text extraction):
  - **Windows**: Install Tesseract from UB Mannheim and add it to your System PATH or reference it directly in your notebooks:
    ```python
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

### 2. Installation
Clone the repository and install the dependencies in a virtual environment:

```bash
# Clone the repository
git clone https://github.com/RatishPatil37/Agentic_AI.git
cd Agentic_AI

# Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your API keys:

```ini
GOOGLE_API_KEY="your-gemini-api-key"
GROQ_API_KEY="your-groq-api-key"
TAVILY_API_KEY="your-tavily-api-key"
HUGGING_FACE_API="your-huggingface-token"
```

*Note: Make sure `.env` is listed in `.gitignore` to avoid exposing your API keys on GitHub.*

---

## 💻 Tech Stack
- **Frameworks**: LangGraph, LangChain, Model Context Protocol (MCP)
- **Models**: Gemini (via `langchain-google-genai`), Groq, HuggingFace
- **OCR Engines**: Tesseract OCR, RapidOCR
- **Data Tools**: PyPDF, PDFPlumber, PDFMiner, Pandas, Jupyter
