with open("artifacts01.txt", 'r+') as f:
    t = f.readline()

print(t)

with open("artifacts02.txt", "w+") as f1:
    f1.write(t+"added")

print("************")
print("end of stage 03")
