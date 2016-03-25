list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

print("Accessing Values in Lists")


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


print("Updating Lists" )


list = ['physics', 'chemistry', 1997, 2000];

print ("Value available at index 2 : ",list[2])
#print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ",list[2])
 

print("Delete List Elements")


list1 = ['physics', 'chemistry', 1997, 2000];

print (list1)

del list1[2];

print( "\n After deleting value at index 2 : ",list1)
#print list1
print("Basic List Operations")
print("len([1, 2, 3])->",len([1, 2, 3]))

print("[1, 2, 3] + [4, 5, 6] Concatenation -> ",[1, 2, 3] + [4, 5, 6])


print("['Hi!'] * 4 Repetition-> ",['Hi!'] * 4)
print("3 in [1, 2, 3] Membership -> ",3 in [1, 2, 3])

print("\nIteration\n")
for x in [1, 2, 3]:
    print(x)

print("\n Indexing, Slicing, and Matrixes Because lists are sequences, indexing and slicing work the same way for lists as they do for strings.\n")

L = ['spam', 'Spam', 'SPAM!']


print("Offsets start at zero",L[2])
print("Negative: count from the right",L[-2])
print("Slicing fetches sections",L[1:])


help(list)
print("""	Built-in Functions		
abs()	divmod()	input()	open()	staticmethod()
all()	enumerate()	int()	ord()	str()
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
bool()	filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reversed()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()	
delattr()	help()	next()	setattr()	
dict()	hex()	object()	slice()	
dir()	id()	oct()	sorted()""")









