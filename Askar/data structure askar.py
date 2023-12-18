
number : int = 20
number_2 : float = 15.5
boolean_var = True
string_var = "my string"

my_list = [1,2,3,4,'string',[1,2,4],100]
my_map = {
    'key_1' : 1,
    'key_2' : 2
}
my_map_2 = {
    'key_2' : 3,
    'key_4' : 4
}

if __name__ == '__main__':
    # print(number + number_2)
    # print(number + boolean_var)
    # print(number + string_var)
    # my_list.append(1000)
    # print(my_map['key_2'])
    # print(my_list[-1])
    my_map.update(my_map_2)
    print(my_map)
