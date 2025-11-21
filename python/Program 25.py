# A spell checker can be a helpful tool for people who struggle to spell words correctly. In this exercise, you will write a program that reads a file and displays all of the words in it 
# that are misspelled. Misspelled words will be identified by checking each word in the file against a list of known words. Any words in the user’s file that do not appear in the list of 
# known words will be reported as spelling mistakes. The user will provide the name of the file to check for spelling mistakes as a command line parameter. Your program should display 
# an appropriate error message if the command line parameter is missing. An error message should also be displayed if your program is unable to open the user’s file. Words followed by 
# a comma, period or other punctuation mark are not reported as spelling mistakes. Ignore the capitalization of the words when checking their spelling.

import sys
import string

def load_dictionary():
    return {
        "a", "able", "about", "above", "after", "again", "against", "all", "am", "an", "and",
        "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between",
        "both", "but", "by", "could", "did", "do", "does", "down", "during", "each", "few",
        "for", "from", "further", "had", "has", "have", "he", "her", "here", "him", "his",
        "how", "i", "if", "in", "into", "is", "it", "its", "just", "know", "like", "make",
        "many", "may", "me", "more", "most", "my", "no", "not", "now", "of", "on", "one", "only",
        "or", "other", "our", "out", "over", "said", "same", "see", "she", "should", "so", "some",
        "such", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this",
        "those", "through", "to", "too", "under", "up", "very", "was", "we", "were", "what",
        "when", "where", "which", "while", "who", "will", "with", "you", "your"
    }

def main():
    if len(sys.argv) < 2:
        print("Error: Missing filename parameter.")
        print("Usage: python spell_checker.py <filename>")
        return

    filename = sys.argv[1]

    try:
        file = open(filename, "r")
    except:
        print(f"Error: Unable to open the file '{filename}'.")
        return

    dictionary = load_dictionary()
    misspelled_words = set()

    for line in file:
        words = line.split()

        for word in words:
            cleaned = word.strip(string.punctuation).lower()

            if cleaned and cleaned not in dictionary:
                misspelled_words.add(cleaned)

    file.close()

    if misspelled_words:
        print("Misspelled words:")
        for w in sorted(misspelled_words):
            print(w)
    else:
        print("No spelling mistakes found.")

if __name__ == "__main__":
    main()









