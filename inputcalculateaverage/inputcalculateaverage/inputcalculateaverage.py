count = int(input("How many Students you have : "))

totalgrade = 0
index = 0

while index < count:
    grade = float(input("{0}{1}{2}".format("Student", index+1, "'s Score : ")))
    if grade > 100:
        print("Invalid Score")
        continue
    index += 1
    totalgrade = totalgrade + grade

averagegrade = totalgrade/(index)

print("{0}{1}".format("Average class grade : ", averagegrade))

if averagegrade < 50:
    print("Average score is a  Fail")
elif averagegrade >= 50:
    print("Average score is a Pass")