# List
myList = [1,2,3,4,5,'string',[1,2,3]]

# Indexing
myList[0] = 'Juggernaut'
print(myList[0])  # elemen list selalu dimulai dari indeks 0
print(myList[-1]) #  -<indeks> akan mengakses elemen list secara backwards (dimulai dari 1)

'''
List adalah data stucture yang bersifat mutable yang berarti elemennya dapat diubah dengan metode 
indexing.
'''

# Method .append() pada list
myList.append('stormSpirit')
print(myList)

# Dictionary
myDictionary = {
    'key_1' : 1,
    'key_2' : 2
}

# menambahkan elemen Dictionary 
myDictionary['key_3'] = 3
print(myDictionary)

# Mengubah elemen Dictionary --> key (immutable), value (mutable)
myDictionary['key_2'] = 'Invoker'
print(myDictionary)

# Dictionary concatenate dengan method .update()
myDict = {
    'key_4' : 4,
    'key_5' : 5
}

myDictionary.update(myDict)
print(myDictionary)
