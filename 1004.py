# _*_ coding:utf-8 _*_
number = input()
students, student_ID, scores, scores_index = {}, {}, [], []
for i in xrange(number):
    students[i] = raw_input()
    student = students[i].split(' ')
    student_ID[i] = student[:2]
    scores.append(int(student[2]))
scores_index.append(scores.index(max(scores)))
scores_index.append(scores.index(min(scores)))

for i in scores_index:
    print student_ID[i][0],
    print student_ID[i][1]

