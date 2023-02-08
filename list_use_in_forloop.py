marks=[1,2,3,4,5]

for score in marks:
    print(score*score)

    #for addition of element in list



marks.append(6)
print(marks)

marks.insert(0,3)
print(marks)

print(99 in marks)
print(3 in marks)


i=0
while i<len(marks):
    print(marks[i])
    i=i+1

    marks.clear()
    print(marks)