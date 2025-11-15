import os
import nltk

# Download sentence tokenizer (only the first time)
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

# Path to your docs folder
DOCS_FOLDER = "docs"

# Read all .txt files and split them into sentences
documents = {}
for filename in os.listdir(DOCS_FOLDER):
    if filename.endswith(".txt"):
        with open(os.path.join(DOCS_FOLDER, filename), "r") as f:
            text = f.read()
            documents[filename] = sent_tokenize(text)

print("Files loaded:", list(documents.keys()))
print("You can now ask questions about the content.\n")

while True:
    query = input("Ask a question (or type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    query_words = query.lower().split()
    found = False

    for filename, sentences in documents.items():
        relevant_sentences = []
        for sentence in sentences:
            if any(word in sentence.lower() for word in query_words):
                relevant_sentences.append(sentence)

        if relevant_sentences:
            found = True
            print(f"\n--- {filename} ---")
            for s in relevant_sentences:
                print("-", s)

    if not found:
        print("No matches found. Try asking differently.")

