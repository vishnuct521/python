# SET in python
#
# A set is an unordered collection of unique elements.
# we can create a set using curly braces{} or the set()

# step 1
# creating a set
# my_set = {1,2,3,4,5}
# print((my_set))


# step 2
# adding element to a set  :- it will create a new set also
# my_set.add(6)
# print(my_set)


# step 3
# removing an element from a set
# my_set.remove(3)
# print(my_set)

# commonly used to perfom mathamatical set operation union interseption and .........
# they are also remove duplicate elements from a set



# step 4
# set operation -union -> it will concadinate two sets and it will remove the duplicate also
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# union_set = set1.union(set2)
# print(union_set) #{1,2,3,4,5,6,7,8}


# intersection_set = set1.intersection(set2)
# print(intersection_set) # {4,5}

# difference_set = set1.difference(set2)
# print(difference_set) # {1,2,3}

# print(2 in set1) # True
# print(9 in )

# in pyhton sets are unordered collections so they dont support indexing and slicing like sequence such as in list or trees
# there for isn't direct method to reverse the set
# how ever you want to reverse the elements of a set you ca convert the set to a list and reverse the list and then
#  convert back in to list

original_set = {1,2,3,4,4,5}
print("original set:",original_set)


# convert set to list, reverse the list and convert it back to the set
# reversed_set = set(reversed(list(original_set)))
# print("reversed set",reversed_set)

