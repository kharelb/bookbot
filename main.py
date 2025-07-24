import sys
from stats import get_num_words, get_chars_dict, sort_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    print(f"{'='*10} BOOKBOT {'='*10}")
    print(f"Analyzing book found at {filepath}...")
    get_num_words(book_text)
    print(f"{'-'*10} Character Count {'-'*10}")
    chars_dict = get_chars_dict(book_text)
    sorted_list = sort_chars_dict(chars_dict)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")
    
    print(f"{'='*10} END {'='*10}")




if __name__ == "__main__":
    main()