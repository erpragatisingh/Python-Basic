##Using a list, tuple, or dict is by far the most common way to do this:

import pickle
PIK = "pickle.dat"
#PIK = "pickle.xls"
#PIK = "pickle.txt"

data = ["A", "b", "C", "d"]
with open(PIK, "wb") as f:
    pickle.dump(data, f)
with open(PIK, "rb") as f:
    print (pickle.load(f))


##However, a pickle file can contain any number of pickles.
##Here's code producing the same output. But note that it's harder to write and to understand:
with open(PIK, "wb") as f:
    pickle.dump(len(data), f)
    for value in data:
        pickle.dump(value, f)
data2 = []
with open(PIK, "rb") as f:
    for _ in range(pickle.load(f)):
        data2.append(pickle.load(f))
print (data2)
##If you do this, you're responsible for knowing how many pickles are in the file you write out.
##The code above does that by pickling the number of list objects first.

    
##First, you need not store the number of items you pickled separately if you use the following idiom for loading:

def load(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

items = load(myfilename)
##Second, this way, you do not get a list but rather a generator.
##This will hold only one item in memory at a time, which is useful if the dumped data is very large -- one possible reason why you may have wanted to pickle multiple items separately in the first place. You can still iterate over items with a for loop as if it were a list.


#I will give an object-oriented demo using pickle to store and restore one or multi object:#


class Worker(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def __str__(self):
        string = u'[<Worker> name:%s addr:%s]' %(self.name, self.addr)
        return string

# output one item
with open('testfile.bin', 'wb') as f:
    w1 = Worker('tom1', 'China')
    pickle.dump(w1, f)

# input one item
with open('testfile.bin', 'rb') as f:
    w1_restore = pickle.load(f)
print ('item: %s' %w1_restore)

# output multi items
with open('testfile.bin', 'wb') as f:
    w1 = Worker('tom2', 'China')
    w2 = Worker('tom3', 'China')
    pickle.dump([w1, w2], f)

# input multi items
with open('testfile.bin', 'rb') as f:
    w_list = pickle.load(f)

for w in w_list:
    print ('item-list: %s' %w)


##output:
##
##item: [<Worker> name:tom1 addr:China]
##item-list: [<Worker> name:tom2 addr:China]
##item-list: [<Worker> name:tom3 addr:China]

##It's easy if you use klepto, which gives you the ability to transparently store objects in files or databases. It uses a dict API, and allows you to dump and/or load specific entries from an archive (in the case below, serialized objects stored one entry per file in a directory called scores).

##>>> import klepto
##>>> scores = klepto.archives.dir_archive('scores', serialized=True)
##>>> scores['Guido'] = 69 
##>>> scores['Fernando'] = 42
##>>> scores['Polly'] = 101
##>>> scores.dump()
##>>> # access the archive, and load only one 
##>>> results = klepto.archives.dir_archive('scores', serialized=True)
##>>> results.load('Polly')
##>>> results
##dir_archive('scores', {'Polly': 101}, cached=True)
##>>> results['Polly']
##101
##>>> # load all the scores
##>>> results.load()
##>>> results['Guido']
##69
##>>>
