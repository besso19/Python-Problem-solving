#1
# def format_money(amount):
#     return f"${amount:.2f}"
# print(format_money(0))

#2
# def even_or_odd(number):
#     return "Even" if (number%2 == 0) else "Odd"
# print(even_or_odd(7))

#3
def swap_values(args): 
    args.reverse()
    return args
args=[1, 10]
print(swap_values(args))