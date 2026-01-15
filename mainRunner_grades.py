import subFile

student1_name = "Raivene"
student1_grade = "1.5"
student1_subject = "Chemistry"

#call a function from a different file
subFile.print_student_info_function(student1_name, student1_grade, student1_subject)

#call a method from different file
student = subFile.Student("George", 1.0, "Calculus")
student.print_student_info_method()



# ==================================