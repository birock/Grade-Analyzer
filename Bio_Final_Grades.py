"""
Author: Ben Rock

Analysis of Principles of Biology I Grades

"""
filename = input("Enter the filename (Bio_Final_Grades, Bio_Course_Grades, Bio_Midterm1_Grades, Bio_Midterm2_Grades): ")
filename += ".txt"

try:
                 
    file_object = open(filename,'r')

except:

    print("That file was not found.")

else:

    grades = file_object.read()

    grades_split = grades.split("\n")

    grades_split_float = []
    for i in grades_split:
        grades_split_float.append(float(i))

    A = 0
    A_minus = 0
    B_plus = 0
    B = 0
    B_minus = 0
    C_plus = 0
    C = 0
    C_minus = 0
    D_plus = 0
    D = 0
    F = 0

    print()
    print("ANALYZING")

    for i in grades_split_float:
        
        if i >= 85.0 and i <= 100.0:
            A += 1
        elif i >= 80.0 and i <= 84.9:
            A_minus += 1
        elif i >= 75.0 and i <= 79.9:
            B_plus += 1
        elif i >= 70.0 and i <= 74.9:
            B += 1
        elif i >= 65.0 and i <= 69.9:
            B_minus += 1
        elif i >= 60.0 and i <= 64.9:
            C_plus += 1
        elif i >= 55.0 and i <= 59.9:
            C += 1
        elif i >= 50.0 and i <= 54.9:
            C_minus += 1
        elif i >= 45.0 and i <= 49.9:
            D_plus += 1
        elif i >= 40.0 and i <= 44.9:
            D += 1
        else:
            F += 1

    total = A + A_minus + B_plus + B + B_minus + C_plus + C + C_minus + D_plus + D + F
    percent_A = (A / total) * 100
    percent_A_minus = (A_minus / total) * 100
    percent_B_plus = (B_plus / total) * 100
    percent_B = (B / total) * 100
    percent_B_minus = (B_minus / total) * 100
    percent_C_plus = (C_plus / total) * 100
    percent_C = (C / total) * 100
    percent_C_minus = (C_minus / total) * 100
    percent_D_plus = (D_plus / total) * 100
    percent_D = (D / total) * 100
    percent_F = (F / total) * 100

    f_percent_A = format(percent_A, ".2f")
    f_percent_A_minus = format(percent_A_minus, ".2f")
    f_percent_B_plus = format(percent_B_plus, ".2f")
    f_percent_B = format(percent_B, ".2f")
    f_percent_B_minus = format(percent_B_minus, ".2f")
    f_percent_C_plus = format(percent_C_plus, ".2f")
    f_percent_C = format(percent_C, ".2f")
    f_percent_C_minus = format(percent_C_minus, ".2f")
    f_percent_D_plus = format(percent_D_plus, ".2f")
    f_percent_D = format(percent_D, ".2f")
    f_percent_F = format(percent_F, ".2f")

    print()
    print("Grade breakdown:")
    print()
    print("A: ", A, " (",f_percent_A,"%)", sep = "")
    print("A-: ", A_minus, " (",f_percent_A_minus,"%)", sep = "")
    print("B+: ", B_plus, " (",f_percent_B_plus,"%)", sep = "")
    print("B: ", B, " (",f_percent_B,"%)", sep = "")
    print("B-: ", B_minus, " (",f_percent_B_minus,"%)", sep = "")
    print("C+: ", C_plus, " (",f_percent_C_plus,"%)", sep = "")
    print("C: ", C, " (",f_percent_C,"%)", sep = "")
    print("C-: ", C_minus, " (",f_percent_C_minus,"%)", sep = "")
    print("D+: ", D_plus, " (",f_percent_D_plus,"%)", sep = "")
    print("D: ", D, " (",f_percent_D,"%)", sep = "")
    print("F: ", F, " (",f_percent_F,"%)", sep = "")

    print()


    print("A ---> ", "|" * A)
    print("A- --> ", "|" * A_minus)
    print("B+ --> ", "|" * B_plus)
    print("B ---> ", "|" * B_minus)
    print("C+ --> ", "|" * C_plus)
    print("C ---> ", "|" * C)
    print("C- --> ", "|" * C_minus)
    print("D+ --> ", "|" * D_plus)
    print("D ---> ", "|" * D)
    print("F ---> ", "|" * F)






