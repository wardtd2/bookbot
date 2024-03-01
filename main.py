def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(f"Word count: {word_count(text)}")
    print(f"Counts of each character: {letter_count(text)}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    letters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


main()