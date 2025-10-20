import re

def get_sentences(paragraph):
    """
    Splits the input paragraph into sentences using regex.
    Sentences can start with numbers and end with ., !, or ?.
    """
    pattern = r'(?<=[.!?])\s+'  # split on punctuation followed by whitespace
    sentences = re.split(pattern, paragraph.strip())
    return [s for s in sentences if s]  # remove empty strings

def display_sentences(sentences):
    """
    Prints each sentence and displays the total count.
    """
    print("\nIndividual Sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    """
    Main driver function.
    """
    paragraph = input("Enter a paragraph: ")
    sentences = get_sentences(paragraph)
    display_sentences(sentences)

if __name__ == "__main__":
    main()
