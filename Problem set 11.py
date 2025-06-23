#1
# def who_is_paying(name):
#     nameList = []
#     nameList.append(name)

#     if len(name) <= 2:
#         return nameList
#     else:
#         nameList.append(name[:2])
#     return nameList

# print(who_is_paying(""))

#2
# def whose_move(last_player, win):
#     if win == True:
#         return last_player
#     if win == False:
#         if last_player == "black":
#             return "white"
#         else:
#             return "black"
# print(whose_move("black", False))

#3
def stringy(size):
    string = ''
    length = 0
    for i in range(int(size/2)):
        string += "1"
        length += 1
        if length <= size/2:
            string += "0"
    if size%2 != 0:
        string +="1"
    return string
print(stringy(1))