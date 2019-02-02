def do_twice(f,value):
    f(value)
    f(value)

def print_spam(value):
    print(value)

def do_four(n,value):
    do_twice(n,value)
    do_twice(n,value)

do_four(print_spam,"spam")
