# This program prompts for a user to enter a paragraph,
# Split a paragraph into individual sentences even if they begin with numbers
# Display each sentence on a new line
# and show the total count of sentences

import re

def split_into_sentences(paragraph):
    # Regex to match sentence boundaries
    # It looks for '.', '?', or '!' followed by a space or end of string
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pattern, paragraph,flags=re.DOTALL | re.MULTILINE)
    return sentences

def display_sentences(sentences):
    print("\n--- Individual Sentences ---\n")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")
    
def main():

    paragraph = input("Enter a paragraph (your sentences may start with numbers):\n")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)
    


if __name__ =="__main__":
    main()
