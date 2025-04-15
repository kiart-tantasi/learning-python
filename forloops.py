def forloop_range():
    for i in range(10):
        print(i)


def forloop_range_backward():
    for i in range(10, 0, -1):
        print(i)


list_example = ["first", "second", "third"]


def forloop_iterable_list():
    for e in list_example:  # can be list or any other iterable
        print(e)


def forloop_enumerate():
    for i, e in enumerate(list):
        print(f"index {i} element {e}")


dict_example = {"firstkey": "firstvalue", "secondkey": "secondvalue"}


def forloop_dict():
    for k, v in dict_example.items():  # enumrate would work as well
        print(f"key {k} value {v}")


list_example_zip = ["zipfirst", "zipsecond"]


def forloop_zip():
    for e1, e2 in zip(list_example, list_example_zip):
        # for-loop stops if there is only 1 list that has current element
        print(f"element1 {e1} element2 {e2}")

def forloop_if():
    evens = [i for i in range(10) if i % 2 == 0] # create a list with if
    for _, e in enumerate(evens):
        print(e)

# forloop_range()

# forloop_range_backward()

# forloop_iterable_list()

# forloop_enumerate()

# forloop_dict()

forloop_zip()

# forloop_if()
