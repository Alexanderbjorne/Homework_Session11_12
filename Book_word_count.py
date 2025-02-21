def count_unique_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = text.split()
            unique_words = set(words)
            return len(unique_words)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return 0

book1 = "AdamSmith.txt"
book2 = "KarlMarx.txt"

book1_unique_count = count_unique_words(book1)
book2_unique_count = count_unique_words(book2)

print(f"Unique words in {book1}: {book1_unique_count}")
print(f"Unique words in {book2}: {book2_unique_count}")

if book1_unique_count > book2_unique_count:
    print(f"{book1} (Adam Smith) used more unique words.")
elif book2_unique_count > book1_unique_count:
    print(f"{book2} (Karl Marx) used more unique words.")
else:
    print("Both authors used the same number of unique words.")

