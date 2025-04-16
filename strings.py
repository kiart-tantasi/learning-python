

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
    print(result)

def format_string_1():
    name = "John"
    formatted = f"His name is {name}" # does not work in python2
    print(formatted)

def format_string_2():
    name = "John"
    formatted = "His name is {}".format(name) # works in both python2 and python3
    print(formatted)

# single_multi_line()

# simple_concat()

# format_string_1()

format_string_2()