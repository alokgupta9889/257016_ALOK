for i in range(1,11,2):
    print(i)



    #create a code for multi student Grade 
    #inside array multiple students marksk store 
    #According to their particular number marks will be decided 
    #Hint : use for loop and If else .
    # a=(62,75,83,23,45,55,35,88,92,100)

    students_marks = {"Ranchit":62,"vaishnavi":75,"shalni":83,"Amit":23,"Neha":45,"rahul":55,"priya":35,"Ankit":88}
    for students , marks in students_marks.items():
        if marks >=90:
            grade = 'A+'
        elif marks >= 88:
            grade = 'A'
        elif marks >= 70:
            grade = 'B+'
        elif marks >= 60:
            grade = 'B'
        elif marks >=50:
            grade = 'c'
        else:
            grade = 'f'
        print(f"{students} scored {marks} and grade {grade}.")
