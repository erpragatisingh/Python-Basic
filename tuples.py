# A tuple is an immutable list, i.e.
#a tuple cannot be changed in any way once it has been created. A tuple is defined analogously to lists, except that the set of elements is enclosed in
#parentheses instead of square brackets. The rules for indices are the same as for lists. Once a tuple has been created,
#you can't add elements to a tuple or remove elements from a tuple. 

#Where is the benefit of tuples?
#Tuples are faster than lists.
#If you know that some data doesn't have to be changed,
#you should use tuples instead of lists, because this protects your data against accidental changes.
#Tuples can be used as keys in dictionaries, while lists can't.
#The following example shows how to define a tuple and how to access a tuple.
#Furthermore we can see that we raise an error, if we try to assign a new value to an element of a tuple:

t = ("tuples", "are", "immutable")
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
## Tuples are immutable:
print('Tuples are immutable:')

  # comented for test next step t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)


