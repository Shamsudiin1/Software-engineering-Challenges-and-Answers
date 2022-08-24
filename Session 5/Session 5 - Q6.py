classes_held = float(input('number of classes held?: '))
classes_attended = float(input('How many classes attended?: '))

perscentage = (classes_attended/classes_held)*100

if perscentage > 75:
    print('Student is allowed to sit the exam')
else:
    print('Student is not allowed to sit the exam')

