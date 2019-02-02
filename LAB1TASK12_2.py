def is_palindrome(string):
    string = string.lower()
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False

string = input("Enter string to check its palindrome or not:")
print(is_palindrome(string))
