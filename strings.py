singleline = "helloworld"
multiline = """
hello
world
"""


def single_multi_line():
    print(singleline)
    print(multiline)


def simple_concat():
    result = "hello" + " " + "world"
    print(result)  # hello world


def format_string_1():
    name = "John"
    formatted = f"His name is {name}"  # does not work in python2
    print(formatted)  # His name is John


def format_string_2():
    name = "John"
    formatted = "His name is {}".format(name)  # works in both python2 and python3
    print(formatted)  # His name is John


def format_string_3():
    name1 = "John"
    name2 = "Jinny"
    msg = "Their names are %s and %s" % (name1, name2)
    print(msg)  # Their names are John and Jinny


def repetition():
    msg = "a" * 3
    print(msg)  # aaa


def access_char():
    "abc"
    print("abc"[0])  # a


def slice():
    print("abbbc"[1:4])  # bbb


def compare(): # lexicographically ordered
    print("b" > "a") # True
    print("aa" > "a") # True
    print("aa" == "aa") # True
    print("ab" > "aa") # True

def change_case():
    print("upper".upper())
    print("LOWER".lower())
    print("capitalize".capitalize())
    print("thiS iS titlE".title())
    print("upperbyswap".swapcase())
    # UPPER
    # lower
    # Capitalize
    # This Is Title
    # UPPERBYSWAP


# single_multi_line()

# simple_concat()

# format_string_1()

# format_string_2()

# format_string_3()

# repetition()

# access_char()

# slice()

compare()

# change_case()
