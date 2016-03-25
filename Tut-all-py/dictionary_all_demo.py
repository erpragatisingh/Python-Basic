print("""Each key is separated from its value by a colon (:),
the items are separated by commas, and the whole thing is enclosed in curly
braces. An empty dictionary without any items is written with just two curly
braces, like this: {}.

Keys are unique within a dictionary while values may not be.
The values of a dictionary can be of any type, but the keys must be of an
immutable data type such as strings, numbers, or tuples.""")


print("Accessing Values in Dictionary:- >")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print("Error will show due to key not found")
# print ("dict['Alice']: ", dict['Alice'])

print("Updating Dictionary->")


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "Pragati Educationl trust"; # Add new entry


print ("dict['Age']: ", dict['Age'])
print( "dict['School']: ", dict['School'])

print("\nDelete Dictionary Elements\n")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

print("Properties of Dictionary Keys")

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};

print(" \n More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. For example − \n")
      
print ("dict['Name']: ", dict['Name'])


print("\n Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example: \n")
      

#dict = {['Name']: 'Zara', 'Age': 7};

#print ("dict['Name']: ", dict['Name'])


help(dict)
      








