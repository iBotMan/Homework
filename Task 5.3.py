# Task 5.3
# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students


# def get_top_performers(file_path, number_of_top_students=5):
# pass
# print(get_top_performers("students.csv"))
# ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']


#2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age.

# Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53

# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27


def get_top_performers(file_path, number_of_top_students=5):

    with open('data/'+file_path, 'r') as students_txt:
        # header
        students_txt.readline()
        # body
        students = tuple(sorted((line.split(',') for line in students_txt), key=(lambda item: float(item[2])), reverse=True))

    return[students[i][0] for i in range(number_of_top_students)]

"""
    students = {}
    with open('data/' + file_path, 'r') as students_txt:
        # header
        students_txt.readline()
        students = {}
        # body
        for line in students_txt:

            # items
            student = line.split(',')
            name = student[0]
            age  = student[1]
            mark = student[2]

            key = (name, age)
            students[key] = float(mark)

    sorted_students = sorted(students.items(), key=(lambda item: item[1]), reverse=True)
    return [sorted_students[i][0][0] for i in range(number_of_top_students)]
"""


def sorted_by_age(file_path):

    with open('data/'+file_path, 'r') as students_txt:
        # header
        header = students_txt.readline()
        # body
        students = tuple(sorted((line.split(',') for line in students_txt), key=(lambda item: int(item[1])), reverse=True))

    with open('data/sorted_by_age_' + file_path, 'w') as sorted_by_age_students_txt:
        # header
        sorted_by_age_students_txt.write(header)
        # body
        for student in students:
            sorted_by_age_students_txt.write(','.join(student))


if __name__ == '__main__':
    print(get_top_performers("students.csv"))
    #sorted_by_age("students.csv")