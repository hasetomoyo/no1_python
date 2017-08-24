point_list = [75, 80, 91]
total = 0
for print in point_list:
    total += print

number_of_subjects = len(point_list)
average = total / number_of_subjects
print('合計点は{}、平均点は{}です。'.format(total, average))