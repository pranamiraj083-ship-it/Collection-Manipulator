Students=[]
while True:
    print("\n Welcome to the Student Data Orgenizer!")
    
    print("select an option")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. display Subject Offered")
    print("6. Exit")
    
    choice=int(input("Enter your choice:"))
    
    match choice:
        case 1:
            print("\n Enter student details")
            student_id=int(input("Student ID: "))
            name=input("Name: ")
            age=int(input("Age: "))
            Grade=input("Grade:")
            DOB=input("Date Of Of Birth (YYYY-MM-DD): ")
            Subjects=input("Subjects(Comma-saperated: ")
            
            student = {
                "id":student_id ,
                "name":name ,
                "age":age ,
                "Grade":Grade ,
                "DOB":DOB ,
                "subjects":Subjects
                }
            
            Students.append(student)
            
            print("\n Student added successfully!")
            
        case 2:
            print("\n --- Display All Students ---")
            
            if len(Students)==0:
                print("No students found.")
                
            else:
                for student in Students:
                    print(
                        f"Student ID:{student['id']} |"
                        f"name:{student['name']} |"
                        f"age:{student['age']} |"
                        f"grade:{student['Grade']} |"
                        f"Subjects:{student['subjects']} |"
                        
                    )
        case 3:
            student_id=int(input("enter student id to update:"))
            
            found=False
            
            for student in Students:
                if student["id"]==student_id:
                    student["name"]=input("enter new name: ")
                    student["age"]=int(input("enter new age: "))
                    student["grade"]=input("enter new grade: ")
                    student["dob"]=input("enter a new date of birth: ")
                    student["subjects"]=input("enter a new subject: ")
                    
                    print("Student Information Updated Successfully!")
                    
                    found=True
                    break
                if not found:
                    print("student not found.")
        
        case 4:
            student_id=int(input("enter student id to delete"))
            
            found=False
            
            for student in Students:
                if student["id"]==student_id:
                    Students.remove(student)
                    
                    print("student delete successfully!")
                    
                    found=True
                    break
                
                if not found:
                    print("student not found")  
                    
        case 5:
            print("\n --- subject offered ---")
            
            print("math")
            print("science")
            print("English")
            
        case 6:
            print("\n thank you !")
            break
        
        case _:
            print("invalid choice !")
              
                                          
                        
                                                                        
            
              
                    
                
                 
                 
            
            
            