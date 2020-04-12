"""Call Stack

The computer uses a stack internally called the call stack.

"""


def greet(name):
    print(f"Hello, {name}!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

# The function above calls two functions, that are below


def greet2(name):
    print(f"how are you, {name}?")


def bye():
    print("okay bye!")


greet("maggie")

# When you call a function from another function, the calling function is paused in a partially completed state
