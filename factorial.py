# Factorial, written as 3! would be 3*2*1


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(10))

"""Good to note from this

Until it reaches the base case, the stack is building up a function of half baked functions

Then, once it reaches the base case, it now knows x * x-1 and can run back down the call stack (starting from the one just before base case)

and call the function and solve the answer.

"""
