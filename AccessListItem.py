# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# Negative Indexing

# print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])
print(thislist[4:-1])
print(thislist[-4:])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")