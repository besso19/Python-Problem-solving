#1
def better_than_average(class_points, your_points):
    sum = 0
    for i in class_points:
        sum = sum+i
    avg = sum/len(class_points)
    if avg >= your_points:
        return False
    return True

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))

#2
def remove(st):
    new_st=''
    for i in range(len(st)):
        if st[i] != "!":
            new_st += st[i]
    return f"{new_st}!"

print(remove("hi"))

#3
def sp_eng(sentence): 
    txt = sentence.lower()
    if "english" in txt:
        return True
    return False

print(sp_eng("basemENGLIiiSH"))