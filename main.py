# Author: Joshua McIntyre jjm7410@psu.print

def getGradePoint(grade): 
  if(grade == "A"):
    return 4.0
  elif(grade == "A-"):
    return 3.67
  elif(grade == "B+"):
    return 3.33
  elif(grade == "B"):
    return 3.0
  elif(grade == "B-"):
    return 2.67
  elif(grade == "C+"):
    return 2.33
  elif(grade == "C"):
    return 2.00
  elif(grade == "D"):
    return 1.0
  else:
    return 0.0


    
def run():


  grade1 = input("Enter your course 1 letter grade: ")
  grade1 = getGradePoint(grade1)
  credit1 = input("Enter your course 1 credit: ")
  credit1 = float(credit1)
  print(f"Grade Point for course 1 is : {grade1}")
  grade2 = input("Enter your course 2 credit: ")
  grade2 = getGradePoint(grade2)
  credit2 = input("Enter your course 2 credit: ")
  credit2 = float(credit2)
  print(f"Grade point for course 2 is: {grade2}")
  grade3 = input("Enter your course 3 letter grade: ")
  grade3 = getGradePoint(grade3)
  credit3 = input("Enter your course 3 credit: ")
  credit3 = float(credit3)
  print(f"Grade point for course 3 is: {grade3}")

  grade1 = float(grade1)
  grade2 = float(grade2)
  grade3 = float(grade3)

  gpa = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)
  print(f"Your GPA is: {gpa}") 


if __name__ == "__main__":
  run()
  