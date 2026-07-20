# Word Frequency Counter

## Project Description
This is a Python console application that reads a text file, analyzes its content, and shows how many times each unique word appears. The program handles file input/output, text cleaning (case and punctuation), counting, sorting, and displays summary statistics.

## Requirements
- Python 3.x (no external libraries needed)

## How to Run
1. Save the files together in one folder.
2. Open a terminal/command prompt in that folder.
3. Run the program:
   ```bash
   python word_frequency_counter.py
   ```
4. Enter the path to the text file when prompted (use `info.txt` provided).

## Features
- Prompts user for text file path.
- Handles missing/invalid files gracefully.
- Converts all text to lowercase.
- Removes punctuation and special characters.
- Splits words by whitespace.
- Excludes common stopwords (from stopwords.txt).
- Displays:
  - Total number of words.
  - Total number of unique words.
  - Top N most common words (default N = 10).
- Handles invalid inputs for N.

## Usage Example
Input file content (`info.txt`):
```
Python is a powerful programming language used for data analysis and machine learning.
The Python language is easy to learn and widely used in data science.
Word frequency analysis helps to understand how often each word appears in a text file.
Python makes text processing simple and efficient for beginners.
```

Program run:
```
Enter the path to a text file: info.txt
Total words: 34
Unique words: 27
Enter number of top common words to display (default 10): 5
Top 5 most common words:
python - 3
language - 2
data - 2
analysis - 2
used - 2
```
