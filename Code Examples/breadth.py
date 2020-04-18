"""Breadth-first search

How do you express a relationship like you -> bob?

A data structure that lets you express relationships? A Hash Table!



"""

from collections import deque
graph = {}
# the first-degree connections related to YOU
graph["you"] = ["alice", "bob", "claire"]
# second-degree connections related to alice, bob, and claire
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()  # creates a new queue
search_queue += graph["you"]  # adds all of your neighbors to the search queue

# You are above adding YOUR connections to the queue.

# Rest of the code


def person_is_seller(person_name):
    if person_name[-1] == "m":
        return f"{person_name} is a mango seller!"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # this array is how you keep track of which people you've searched before
    while search_queue:  # While the queue isn't empty
        person = search_queue.popleft  # grabs the first person off of the queue
        # ONLY search this person if you haven't already searched them.
        if not person in searched:
            if person_is_seller(person):  # checks whether the person is a mango seller
                print(f"{person} is a mango seller!")  # yep, mango seller!
                return True
            else:
                # nope, not a mango seller. add all of this person's friends to the search queue
                search_queue += graph[person]
                searched.append(person)  # mark this person as searched
    return False  # If you reached here, no one in the queue was a mango seller


search("you")


# Runtime: O(number of edges) O(n) + )(number of people)

# O(V + E) - V for number of vertices, E for number of edges.
