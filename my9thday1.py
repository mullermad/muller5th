student_score={
    "harry":81,
    "ron":78,
    "hermela":99,
    "draco":74,
    "neville":62,
}
student_grade={}
for score in student_score:

    if student_score[score]>91:
        student_grade[score]="OUTSTANDING"
    elif student_score[score]>81 :
        student_grade[student] = "EXCEEDS EXPECTATION"

    elif student_score[score]>71 :
        student_grade[score]="acceptable"
    else:
        student_grade[score] = "fail"
print(student_grade)