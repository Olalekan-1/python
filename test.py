def do_twice(f):
    f()
    f()


def print_spam():
    print("spam", end=' ')


# do_twice(print_spam)
def do_four(f):
    do_twice(f)
    do_twice(f)

# do_four(print_spam)

def print_row():
    print('+ - - - -', end=' ')

def print_rows():
    do_twice(print_row)
    print('+')

def print_bar():
    print('|        ', end=' ')

def print_bars():
    do_twice(print_bar)
    print('|')

def print_grid():
    print_rows()
    do_four(print_bars)
    print_rows()

print_grid()
print()
print()

def do_thrice(f):
    do_twice(f)
    f()

def print_4row():
    do_thrice(print_row)
    print('+')

def print_4bars():
    do_thrice(print_bar)
    print('|')

def print_4grid():
    print_4row()
    do_four(print_4bars)

print_4grid()
