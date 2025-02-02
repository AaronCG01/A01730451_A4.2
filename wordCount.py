"""Program 3 of Activity 4.2 - Identify all distinct words in a file and the frequency of them.
   Aarón Cortés García - A01730451
"""

#  pylint: disable=invalid-name

import sys
import time

def read_file(file_path):
    """Reads the content of a file and returns the words as a list."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(process_line(line))  # Process each line and add words to the list
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except (PermissionError, IsADirectoryError) as e:  # Handle other xceptions
        print(f"Error reading file: {e}")
        sys.exit(1)
    return words

def process_line(line):
    """Processes a line by splitting words and handling punctuation."""
    # Replace punctuation with spaces
    cleaned_line = "".join(
        char.lower() if char.isalnum() or char.isspace() else " " for char in line
    )
    return cleaned_line.split()  # Split the line into words

def count_word_frequency(words):
    """Counts the frequency of each word in a list while maintaining order of first appearance."""
    word_count = {}  # Dictionary to store word frequencies
    word_order = []  # List to maintain the order of first appearances
    for word in words:
        if word in word_count:
            word_count[word] += 1  # Increment count if word is already in dictionary
        else:
            word_count[word] = 1  # Initialize count for new word
            word_order.append(word)  # Track order of first appearances
    return word_count, word_order

def write_results(word_count, word_order, execution_time):
    """Writes word count results sorted by frequency and input order to a file and prints them."""
    output_file = "WordCountResults.txt"
    # Sort words by frequency (descending) and maintain input order if frequencies are the same
    sorted_words = sorted(word_order, key=lambda w: (-word_count[w], word_order.index(w)))
    total_words = sum(word_count.values())  # Calculate total words counted
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word in sorted_words:
                line = f"{word}: {word_count[word]}"
                print(line)  # Print result to console
                file.write(line + '\n')  # Write result to file
            total_words_line = f"TOTAL WORDS COUNTED: {total_words}"
            print(total_words_line)  # Print total words counted
            file.write(total_words_line + '\n')  # Write total words counted to file
            time_line = f"EXECUTION TIME: {execution_time:.6f} seconds"
            print(time_line)  # Print execution time
            file.write(time_line + '\n')  # Write execution time to file
    except (PermissionError, OSError) as e:  # Handle exceptions
        print(f"Error writing results: {e}")
        sys.exit(1)

def main():
    """Main function to execute the word count program."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()  # Start execution timer
    words = read_file(file_path)  # Read words from file
    word_count, word_order = count_word_frequency(words)  # Count word occurrences
    execution_time = time.time() - start_time  # Calculate execution time
    write_results(word_count, word_order, execution_time)  # Write and display results

if __name__ == "__main__":
    main()
