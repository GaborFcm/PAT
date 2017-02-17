# _*_ coding:utf-8 _*_
def rank(x):        # exceeding time
    size = len(x)
    for i in xrange(size):
        for j in xrange(i+1, size):
            if x[i][3] < x[j][3]:
                y = x[i]
                x[i] = x[j]
                x[j] = y
            elif x[i][3] == x[j][3] and x[i][1] < x[j][1]:
                y = x[i]
                x[i] = x[j]
                x[j] = y
            elif x[i][3] == x[j][3] and x[i][1] == x[j][1] and x[i][0] > x[j][0]:
                y = x[i]
                x[i] = x[j]
                x[j] = y
    return x
numbers = raw_input().split(' ')
top1, top2, top3, top4 = [], [], [], []
students = []
num, L, H = int(numbers[0]), int(numbers[1]), int(numbers[2])
for k in xrange(num):
    student = raw_input().split(' ')
    student = map(int, student)
    student.append(student[1]+student[2])
    if student[1] >= H and student[2] >= H:
        top1.append(student)
    elif student[1] >= H and student[2] >= L:
        top2.append(student)
    elif student[1] >= student[2] >= L:
        top3.append(student)
    elif 80 > student[1] >= 60 and student[1] < student[2]:
        top4.append(student)
students.append(rank(top1))
students.append(rank(top2))
students.append(rank(top3))
students.append(rank(top4))
print len(students[0])+len(students[1])+len(students[2])+len(students[3])
for i in xrange(len(students)):
    for j in students[i]:
        print j[0], j[1], j[2]
