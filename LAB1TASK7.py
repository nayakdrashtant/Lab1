def print_spam():
    print("SPAM!!!")

def do_n(n):
    for n in range(int(n)):
        print_spam()

n = input("Enter n input to call function:")
do_n(n)
