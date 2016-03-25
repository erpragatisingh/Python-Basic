# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket )
print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words
print("# Demonstrate set operations on unique letters from two words")


a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a ^ b )

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
