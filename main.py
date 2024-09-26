def get_char_count(book_text):
    #returns number of times each character appears in the string
    #remove all whitespace
    #use a dictionary {char : count}
    cleaned_string = "".join(book_text.split()).lower()
    dict = {}
    for char in cleaned_string:
        #isaplha line we remove all special characters
        #if you want special character count remove this if statement
        if char.isalpha():
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict

def get_word_count(book_text):
    return len(book_text.split())

def styled_dict(book_text):
    char_count_dict = get_char_count(book_text)
    for key, value in char_count_dict.items():
        print(f"The {key} character was found {value} times")

def main():
    filepath = "books/frankenstein.txt"
    file = open(filepath, "r")
    book = file.read()

    word_count = get_word_count(book)
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document")
    styled_dict(book)
    print("--- End report ---")

main()