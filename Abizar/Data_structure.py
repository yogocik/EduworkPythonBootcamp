#list
my_list = [1,2,3,4,5,'string',[1,2,4,],100]
#update index
my_list.append(1000)

print(my_list)

#Dictionary
my_map = {
    "key_1": 1,
    "key_2": 2
}

# 1. update value
my_map["key_2"]= 3
print(my_map["key_2"])

# 2. update/overlay 2 dictionary
my_map_2 = {
    "key_3": 3,
    "key_4": 4
}
my_map.update(my_map_2)
print(my_map)



