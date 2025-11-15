# Mini RAG AI Project

Mini RAG AI is a Python project demonstrating how to load text documents, split them into sentences, and answer questions using Natural Language Processing (NLP) with NLTK. This project shows a simple Retrieval-Augmented Generation (RAG) workflow.

## Features
- Load multiple `.txt` documents into Python.
- Split text into sentences using NLTK's `sent_tokenize`.
- Ask questions and retrieve answers from your documents.
- Works with `.txt` files stored locally in a `docs/` folder.

## Requirements
- Python 3.11+
- NLTK library

Install required Python packages:
```bash
pip install nltk
Download NLTK tokenizer:

import nltk
nltk.download('punkt')
Usage
Place your .txt documents inside the docs/ folder (already included in this repo).

Run the Python script:

python3 mini_rag.py
Ask questions about the content in your terminal. Type exit to quit.

Example:

Ask a question (or type 'exit' to quit): summarize the AI notes
Example Documents

cybersecurity_tips.txt – Basic cybersecurity tips.

ai_notes.txt – Notes from AI experiments.

project_doc.txt – Sample project documentation.

Learning Outcomes
Practice basic NLP techniques using Python and NLTK.
Process and analyze text data.
Learn how RAG-style information retrieval works.

Author
Created for educational purposes and portfolio demonstration by qadentech.
