#1 fix the loop
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

#2
def get_number_from_string(st):
    string =''
    for x in st:
        if x.isdigit():
            string += x
    return int(string)

print(get_number_from_string("basem123mafa22hmoud321"))

#3
def between(a,b):
    i = a
    list= []
    while i <= b:
        list.append(i)
        i += 1
    return list

print(between(1, 16))