def is_normalized_palindrome(word):
    word = word.lower().replace(" ","")
    if word == word[::-1]:
        return True
    else:
        return False
user= input("Enter your words: ")
result =(is_normalized_palindrome(user))
if result ==  True:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")