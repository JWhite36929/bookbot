from stats import get_num_words, get_report
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        result = f.read()
    return result
  
def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    print("============ BOOKBOT ============")
    text = get_book_text(book)
    print("Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    get_report(text)
    print("============= END ===============")


main()
