def highest_marks(marks):
    big = 0
    for i in range(len(marks)):
        if(marks[i]>big):
            big = marks[i]
    return big
def total_marks(marks):
    total = 0
    for i in range(len(marks)):
        total+=marks[i]
    return total

marks = [40, 50, 13, 90]
max_mark = highest_marks(marks)
total_mark = total_marks(marks)
avg_mark = total_mark/4

print(f"Maximum mark is : {max_mark}")
print(f"Total marks is : {total_mark}")
print(f"Average marks is : {avg_mark}")