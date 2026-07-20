import string
from collections import Counter

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return None

def load_stopwords(path="stopwords.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return set(word.strip().lower() for word in f if word.strip())
    except:
        return set()

def clean_text(text, stopwords):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return [w for w in words if w not in stopwords]

def main():
    stopwords = load_stopwords()

    while True:
        path = input("Enter the path to a text file: ")
        text = read_file(path)
        if text is not None:
            break
        else:
            choice = input("File not found. Retry? (y/n): ")
            if choice.lower() != "y":
                return

    words = clean_text(text, stopwords)
    if not words:
        print("The file is empty or contains only stopwords.")
        return

    counter = Counter(words)
    total_words = sum(counter.values())
    unique_words = len(counter)

    print("Total words:", total_words)
    print("Unique words:", unique_words)

    try:
        n = input("Enter number of top common words to display (default 10): ")
        n = int(n) if n.strip() else 10
        if n <= 0 or n > unique_words:
            print("Invalid N. Using default 10.")
            n = 10
    except:
        n = 10

    print(f"Top {n} most common words:")
    for word, freq in counter.most_common(n):
        print(word, "-", freq)

if __name__ == "__main__":
    main()