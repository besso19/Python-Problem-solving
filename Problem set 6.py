#1
# def rain_amount(rain_amount):
#     if (rain_amount < 40):
#         return f"You need to give your plant {40 - rain_amount}mm of water"
#     else:
#         return "Your plant has had more than enough water for today!"
# print(rain_amount(40))

#2
# def remove(st):
#     newText = st.rstrip("!")
#     return newText
# print(remove("!!!Hi!!!!!"))

#3
def remove(s):
    if s == "":
        return ""
    elif s[-1] =="!":
        s = s[:-1]
    return s
print(remove(""))
