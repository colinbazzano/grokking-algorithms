"""Recursion

The first few functions are simple introductions to recursion, and follows the chapter of the book as you
continue through the code.

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key!")
"""
"""
"""
# Example of a infinite recurisve function


# def countdown(i):
#     print(i)
#     countdown(i-1)

# Now, let's add a base case to that function

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)


countdown(90)
