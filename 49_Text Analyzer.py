
name = input("Enter your name: ")
paragraph = input("Enter your paragraph: ")
search_word = input("Enter the word to search: ")

def analyze_text(paragraph, search_word):
    if not paragraph:
        return None

    words = paragraph.split()
    total_words = len(words)
    total_characters = 0
    total_vowels = 0
    total_digits = 0
    occurrences = 0

    longest_word = words[0]
    shortest_word = words[0]

    for char in paragraph:
        if char != " ":
            total_characters += 1

        if char.lower() in "aeiou":
            total_vowels += 1

        if char.isdigit():
            total_digits += 1

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

        if word.lower() == search_word.lower():
            occurrences += 1

    return total_words, total_characters, total_vowels, total_digits, longest_word, shortest_word, occurrences

result = analyze_text(paragraph, search_word)

if result is None:
    print("No text entered.")
else:
    total_words, total_characters, total_vowels, total_digits, longest_word, shortest_word, occurrences = result

    print("========== TEXT ANALYSIS ==========")
    print("Name:", name)
    print("Total Words:", total_words)
    print("Total Characters:", total_characters)
    print("Total Vowels:", total_vowels)
    print("Total Digits:", total_digits)
    print("Longest Word:", longest_word)
    print("Shortest Word:", shortest_word)
    print("Occurrences:", occurrences)
