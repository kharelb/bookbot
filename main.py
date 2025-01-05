def main():
    text = get_book_text("./books/frankenstein.txt")
    words_count = count_words(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"There are {words_count} words in the text")
    unique_characters = set(sorted([x.lower() for x in text]))

    for unique_character in unique_characters:
        if not unique_character.isalpha():
            continue
        print(f"The character '{unique_character}' was found {count_characters(unique_character, text)} times")

    print(f"---- End of Report ----")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(character, text):
    count_times = 0
    for charac in text:
        if charac.lower() == character.lower():
            count_times += 1
    
    return count_times


main()

