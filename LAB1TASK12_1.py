def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def checkfun(choice,word):
    if choice == "first":
        first(word)
    elif choice == "last":
        last(word)
    elif choice == "middle":
        middle(word)
    else:
        return word

choice = input("Enter your choice:")
word = input("Enter word:")
print(checkfun(choice,word))
