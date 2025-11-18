'''
    Author: Constantine Lekkos
    Created Date: 18/11/2025
    Purpose: Implementation of Student class
'''

from clear_console import cls

cls()

class Student:
    """
    A class that represents a student with an id, a firstname, and a lastname.
    
    Attributes:
      id (int): The id of the student.
      firstname (str): The first name of the student.
      lastname (str): The last name of the student.
    """
    __id = 0 # Private id as int to increment by 1, in every new student.
    __processed_count = 0 # Private counter as int to increment by 1, when a student is modified.

    def __init__(self, firstname: str, lastname: str) -> None:
        """
        The constructor of the Student() class.

        Args:
          id (int): The id of the student as a private property.
          firstname (str): The first name of the student as a private property.
          lastname (str): The last name of the student as a private property.
        
        Returns:
          None
        """
        Student.__id += 1
        self.__firstname = firstname
        self.__lastname = lastname
    
    def __repr__(self) -> str:
        """
        Debugging usage

        Returns:
          str
        """
        return f"Student Profile {Student.get_id_count()}:\nID: {self.__id}\nFirst Name: {self.__firstname}\nLast Name: {self.__lastname}"
    
    def __str__(self) -> str:
        """
        Str represenation

        Returns:
          str
        """
        return f"Student Profile {Student.get_id_count()}:\nID: {self.__id}\nFirst Name: {self.__firstname}\nLast Name: {self.__lastname}"
    
    @classmethod
    def get_id_count(cls) -> int:
        """
        A class method that is used to display the number of the created students.

        Returns:
          int
        """
        return cls.__id
    
    @classmethod
    def get_processed_count(cls) -> int:
        """
        A class method that is used to display the number of the processed students.

        Returns:
          int
        """
        return cls.__processed_count
    
    # Getters
    @property
    def id(self) -> int:
        """
        Getter of the id property.

        Returns:
          int
        """
        return self.__id
    
    @property
    def firstname(self) -> str:
        """
        Getter of the firstname property.

        Returns:
          str
        """
        return self.__firstname
    
    @property
    def lastname(self) -> str:
        """
        Getter of the lastname property.

        Returns:
          str
        """
        return self.__lastname
    
    # Setters
    @id.setter
    def id(self, id: int) -> None:
        """
        Setter of the id property.

        Returns:
          None
        """
        Student.__processed_count += 1 # At least, this is set to one place that triggers the process.
        self.__id = id
    
    @firstname.setter
    def firstname(self, firstname: str) -> None:
        """
        Setter of the firstname property.

        Returns:
          None
        """
        self.__firstname = firstname
    
    @lastname.setter
    def lastname(self, lastname: str) -> None:
        """
        Setter of the lastname property.

        Returns:
          None
        """
        self.__lastname = lastname

def main() -> None:
    """
    A main entry point that tests scenarios.

    Returns:
      None
    """
    print(f"Total created students so far: {Student.get_id_count()}")
    print()
    students = []
    student_1 = Student("A Name", "A Surname")
    print(student_1)
    print(f"Passed: Id: {student_1.id}, First Name: {student_1.firstname}, and Last Name: {student_1.lastname}")

    print()

    student_2 = Student("John", "Doe")
    print(student_2)
    print(f"Passed: Id: {student_1.id}, First Name: {student_1.firstname}, and Last Name: {student_1.lastname}")

    # User input different values to test the functionality of the getters and setters.
    print()
    id = int(input("Please, enter the new ID of the student; for test purposes only!: "))
    firstname = input("Please, enter the new First Name of the student; for test purposes only!: ")
    lastname = input("Please, enter the new Last Name of the student; for test purposes only!: ")
    student_1.id = id
    student_1.firstname = firstname
    student_1.lastname = lastname

    print()

    print(f"Processed: Id: {student_1.id}, First Name: {student_1.firstname}, and Last Name: {student_1.lastname}")

    print()
    print(f"Total created students so far: {Student.get_id_count()}")
    print(f"Total processed students so far: {Student.get_processed_count()}")

    # Appends the students into a list
    students.append(student_1)
    students.append(student_2)

    print()

    for student in students:
        students_dictionary = {"ID": student.id,"First Name": student.firstname, "Last Name":student.lastname}
        print(students_dictionary)

if __name__ == "__main__":
    main()
