# Lets create a book hash table, or a dictionary in Python

book = dict()

# And lets add some items to the book

book["apple"] = 0.67
book["avocado"] = 1.49
book["milk"] = 1.49


print(book["avocado"])
# Returns 1.49!

# PHONE BOOK

phone_book = {}
phone_book["Jenny"] = 8542456
phone_book["emergency"] = 911

print(phone_book["Jenny"])

# VOTER CHECK

voted = {}


def check_voter(name):
    if voted.get(name):
        print("You've already voted")
    else:
        voted[name] = True
        print("You can vote!")


check_voter("tom")
check_voter("tom")

# CACHE

cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]  # this returns cached data
    else:  # we don't have it cached, make the server do some work!
        data = get_data_from_server(url)
        cache[url] = data  # saves this data in your cache
        return data
