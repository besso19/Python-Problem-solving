#1
# def generate_range(start, stop, step):
#     i = start
#     list =[]
#     while i >= start and i <= stop :
#         list.append(i)
#         i += step
#     return list
# anthor solve
# def generate_range(min, max, step):
#     return [i for i in range(min, max, step)]

# print(generate_range(0, 50, 1))

#2
# def ensure_question(s):
#     if s =="":
#         return "?"
#     elif s[-1]=="?":
#         return s
#     else:
#         return f"{s}?"

# print(ensure_question(""))

#3
# def same_case(a, b): 
#     if a.isalpha() and b.isalpha():
#         if a.isupper() and b.isupper() or a.islower() and b.islower():
#             return 1
#         else:
#             return 0
#     else:
#         return -1

# print(same_case("?", "A"))