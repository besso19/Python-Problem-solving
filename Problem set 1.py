#1
def digitize(n):
    x = str(n)
    str_list =[i for i in x]
    int_list =[int(y) for y in str_list]
    reversed_list = []
    n = len(int_list)-1
    while n < len(int_list) and n >= 0:
        reversed_list.append(int_list[n])
        n = n - 1
    return reversed_list

print(digitize(254663214589))

#2
def temple_strings(obj, feature): 
    return f"{obj} are {feature}"

print(temple_strings("You","Special"))
#3
def double_char(s):
    double_s= ""
    for char in s:
        double_s += char
        double_s += char
    return double_s

print(double_char("String"))