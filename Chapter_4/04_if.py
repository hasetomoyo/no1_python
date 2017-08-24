your_point = input('点数をカンマ区切りで入力してください： ')
point_list = your_point.split(',')
total = 0

for point in point_list:
    total += int(point)

subject_number = len(point_list)
excellent = subject_number * 100 * 0.8
good = subject_number * 100 * 0.65
if total >= excellent:
    evalution = 'Excellent!'
elif total >= good:
    evalution = 'Good'
else:
    evalution = 'Bad'

print('点数の評価は{}です。'.format(evalution))