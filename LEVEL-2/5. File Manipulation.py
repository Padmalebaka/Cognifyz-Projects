import string

def count_words_in_file(file_path):
    word_count = {}
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = line.split()
            
            # Count each word
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    # Sort the word count dictionary alphabetically by word
    sorted_word_count = dict(sorted(word_count.items()))
    
    return sorted_word_count

def main():
    file_path = input("Enter the path to the text file: ")
    
    try:
        word_count = count_words_in_file(file_path)
        
        print("\nWord occurrences in alphabetical order:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print("The specified file was not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()