def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(f"Word count: {word_count(text)}")
    print(f"Counts of each character: {letter_count(text)}")
    print(f"--- Begin report of {path} ---")
    print(f"{word_count(text)} words found in the document")
    letters = split_letters(letter_count(text))
    for letter in letters:
         print(f"The '{letter["character"]}' character was found {letter["count"]} times")
    print("--- End report ---")
    

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


def split_letters(dict):
    letters = []
    for character in dict:
        if character.isalpha():
            letters.append({"character": character, "count" : dict[character]})
    letters.sort(reverse=True, key=sort_on)
    return letters



def sort_on(dict):
    return dict["count"]


main()