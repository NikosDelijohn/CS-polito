#!/usr/bin/python3

def main():

    student_id_a = "S50123"
    student_id_b = "S41235"

    if int(student_id_a[1:])> int(student_id_b[1:]):
        print(student_id_a)
        print(student_id_b)
    else: 
        print(student_id_b)
        print(student_id_a)

if __name__ == "__main__":
    main()