class Student:
    def __init__(self,student_name,student_age,student_id,marks):
        self.__student_name = student_name
        self.__student_id = student_id
        self.__student_age = student_age
        self.__marks= marks
    def getname(self):
        return self.__student_name 
    def get_id(self):
            return self.__student_id 
    def get_age(self):
             return self.__student_age 
        
    def get_marks(self):
          return self.__marks
    def calculate_grade(self):
          if self.__marks >= 90:
                print("Grade A")
          elif self.__marks >= 80:
                print("Grade B")
          elif self.__marks >= 70:
                print("Grade C")     
          elif self.__marks >= 60:
                print("Grade D")
          elif self.__marks >= 30:
                print("Grade E")
          elif self.__marks >= 30:
                print("Grade E")
          else:
                print("Ops! You cannot pass this test!")
    def printdetail(self):
      print("-----------------------------")
      print("ID :", self.get_id())
      print("NAME :", self.getname())
      print("AGE :", self.get_age())
      print("Marks :", self.get_marks())
      self.calculate_grade()
      print("-----------------------------")
    def to_dict(self):
     return {
        "name": self.getname(),
        "id": self.get_id(),
        "age": self.get_age(),
        "marks": self.get_marks()
    }