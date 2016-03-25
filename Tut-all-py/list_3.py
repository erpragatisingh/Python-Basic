languages = ["Python", "C", "C++", "Java", "Perl"]
print(languages[0] + " and " + languages[1] + " are quite different!") 
print("Accessing the last element of the list: " + languages[-1]) 

print("Accessing the last element of the list: " + languages[-2]) 
group = ["Bob", 23, "George", 72, "Myriam", 29]

print("Mixed list is "+group[2])

person = [["Marc","Mayer"],["17, Oxford Str", "12345","London"],"07876-7876"]
print("person list ",person)
name = person[0]

print("person[0]",name)

first_name = person[0][0]

print("person[0][0]"+first_name)

last_name = person[0][1]

print("[0][1]"+last_name)

address = person[1]
street = person[1][0]

print(street)
#.......................Compleas list


complex_list = [["a",["b",["c","x"]]]]
print(complex_list)
complex_list = [["a",["b",["c","x"]]],42]
print(complex_list)
complex_list[0][1]
complex_list[0][1][1][0]


