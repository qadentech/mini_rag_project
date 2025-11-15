# Mini RAG AI Project

Mini RAG AI is a small Python project that demonstrates how to load documents, split them into sentences, and answer questions using Natural Language Processing (NLP) with NLTK. This project is a simple example of a Retrieval-Augmented Generation (RAG) style workflow.

## Features

- Load multiple text documents into Python.
- Split text into sentences using NLTK's `sent_tokenize`.
- Ask questions and retrieve relevant answers from the documents.
- Works with `.txt` files stored locally.

## Requirements

- Python 3.11+
- NLTK library

Install required Python packages:

```bash
pip install nltk
You will also need to download the NLTK tokenizer:

import nltk
nltk.download('punkt')

Usage

Place your .txt documents in the docs folder.

Run the Python script:
python3 mini_rag.py
Ask questions about the content of your documents in the terminal.

Example:
Ask a question (or type 'exit' to quit): summarize the AI notes
Example Documents

cybersecurity_tips.txt – Basic cybersecurity tips.

ai_notes.txt – Notes from AI experiments.

project_doc.txt – Sample project documentation.

Learning Outcomes

Practice basic NLP techniques using Python and NLTK.
Learn how to process and analyze text data.
Gain experience with RAG-style information retrieval.

Author
Created for educational purposes and portfolio demonstration by qadentech.
