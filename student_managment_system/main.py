from student import Student
import json  
students=[]




while True:

    print("\n===============Student Managment System===============")
    print("1. Add Student " )
    print("2. View  Student ")
    print("3. Search  Student ")
    print("4. Delete  Student ")
    print("5. Save student ")
    print("6. Exist ")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        print("ADD STUDENT")
        def get_age():
         while True:
               try:
                     age = int(input("Enter your age :"))
                     if age <= 0:
                           raise ValueError()
                     return age
               except ValueError:
                     print('Invalid age! Please enter a positive number.')
        def get_mark():
            while True:
              try:
                    marks = int(input("Enter your marks :"))
                    if marks < 0 or marks > 100:
                          raise ValueError()
                    return marks
              except ValueError:
                    print("Marks must be between 0 and 100")
                    
        student_id =int(input('Enter your id: '))    
        student_name =input('Enter your name: ')
        student_age = get_age()
        student_marks=get_mark()

        student = Student(
              student_name,student_age,student_id,student_marks
              )
        students.append(student)
              
    elif choice == "2":
        print("View  Student ")
        for student in students:
         student.printdetail()     
    elif choice == "3":
             print("Search  Student ")
             student_id =int(input('Enter your id: ')) 
             found = False 
             for student in students:
                            
                            if student.get_id() == student_id:
                                 student.printdetail()
                                 found =True
                                 print(f"student {student.getname()} found succesfully")
                                 break
             if not found:
                 print("ID Not Found")

              
    elif choice == "4":
                print("Delete  Student ")
                student_id =int(input('Enter your id: ')) 
                found = False 
                for student in students:
                     
                      if student.get_id() == student_id :
                        students.remove(student)
                        found =True
                        print(f"student {student.getname()} deleted succesfully")
                if not found:
                        print("ID Not Found")

    elif choice == "5":
       student_data = []

       for student in students:
         student_data.append(student.to_dict())

       try:
            with open("student.json", "w") as file:
              json.dump(student_data, file, indent=4)

            print("Students saved successfully!")

       except FileNotFoundError:
            print("File not Found")

    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")