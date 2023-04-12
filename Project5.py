import csv

def write_into_csv(info_list):
    with open("student_information_csv","a",newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Section","Roll No","Department","Contact Number"])
        writer.writerow(info_list)

condition=True
student_num=1
while(condition):
    print('Enter the student information for student#',student_num)
    name=input('Enter the name of the student:')
    section=input('Enter the class of the student:')
    roll_no=int(input("Enter the roll no of the student:"))
    department=input('Enter the department of the student:')
    contact=int(input('Enter the contact number of the student'))

    student_info_list=[]
    student_info_list.append(name)
    student_info_list.append(section)
    student_info_list.append(roll_no)
    student_info_list.append(department)
    student_info_list.append(contact)
    print(student_info_list)
    print('Entered information for student#',student_num,' is->\nName:',name,'\nSection:',section,'\nRoll No:',roll_no,'\nDepartment:',department,'\nContact No:',contact)
    choice_check=input('Is the information correct:')
    if choice_check.lower()=='yes':
        write_into_csv(student_info_list)

        condition_check=input('Do you want to enter the information of another student:')
        if condition_check.lower()=='yes':
            condition=True
            student_num+=1
        elif condition_check.lower()=='no':
            condition=False
    elif choice_check.lower()=='no':
        print('Please re-enter the values')
    