# AI Few-shot Implementation Chatbot 
This is a full-stack AI Chatbot. It is built with Streamlit, LangChain, and Google Gemini. The assistant uses Few-Shot Prompting. It provides expert-level advice on implementing AI systems in big tech environments. It maintains a consistent response.

## Features
**Conversational Memory:** The chatbot remembers previous interactions using ConversationBufferMemory.
**Few-Shot Prompting:** High-quality examples guide the chatbot to ensure technical depth and consistent branding.
**Modern Tech Stack:** The chatbot is integrated with Google's Gemini 1.5/2.0 models via LangChain.
**Environment Management:** The chatbot handles secure API keys via python-dotenv.

## 🛠️ Tech Stack
- Frontend: Streamlit
- Orchestration: LangChain
- LLM: Google Gemini (via langchain-google-genai)
- Environment: Python 3.10+
- 
## Installation

### Clone the repository:
```bash
git clone <your-repo-url>
cd chatapp
```


### Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```


### Install dependencies:
```bash
pip install streamlit langchain-google-genai python-dotenv langchain
```

### Set up environment variables:
Create a .env file in the root directory:
```text
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Usage
Run the Streamlit application:
```bash
streamlit run frontend.py
```

## Project Structure

**frontend.py:** This file contains the Streamlit UI logic and session state management.
**backend.py:** This file contains LangChain logic, Few-Shot templates, and model configuration.
**.env:** This file stores secret keys (not tracked in Git).
**.venv/:** This directory contains an isolated Python environment.

## 📝 Example Interaction
User: "How to implement end to end RAG pipeline"
Assistant: "Thanks! For your query, here is a technical implementation plan: 1. Establish a robust data ingestion pipeline for diverse document types and implement advanced chunking strategies (e.g., semantic chunking, fixed-size with overlap) to prepare data, 2. Select and deploy an optimized embedding model (e.g., text-embedding-3-large, bge-large-en-v1.5) and index the generated embeddings into a scalable vector database (e.g., Pinecone, Weaviate) for efficient similarity search, 3. Implement multi-stage retrieval, combining dense (vector search) and sparse (keyword search like BM25) methods, followed by re-ranking (e.g., Cohere Rerank, cross-encoders) to maximize context relevance, 4. Integrate a production-grade LLM (e.g., GPT-4, Llama 3) and apply advanced prompt engineering techniques (e.g., context stuffing, instruction tuning) to effectively utilize retrieved information for generation, and 5. Orchestrate the end-to-end RAG pipeline using a framework like LangChain or LlamaIndex, containerize components with Docker, and deploy on a managed Kubernetes service with auto-scaling and comprehensive observability.