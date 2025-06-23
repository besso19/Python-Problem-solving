#1
# def triple_trouble(one, two, three):
#     combination =''
#     for i in range(len(one)):
#         combination += one[i]
#         combination += two[i]
#         combination += three[i]

#     return combination
# print(triple_trouble("aa", "bb", "cc"))

#2
# def validate_hello(greetings):
#     list=["hello", "ciao", "salut", "hola", "hallo", "ahoj", "czesc"]
#     for word in list:
#         if word in greetings.lower():
#             return True
#     return False

#3
def add_length(str_):
    result = []
    lst = str_.split()
    for word in lst:
        result.append(f"{word} {len(word)}")
    return result
print(add_length("abc def"))
