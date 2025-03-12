#!/usr/bin/env python3
class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major

    @property
    def name(self):
        print("Getter for name called","\n")
        return self._name

    @name.setter
    def name(self, name):
        print("Setter for name called","\n")
        self._name = name
       
    @property
    def major(self):
        print("Getter for major called","\n")
        return self._major

    @major.setter
    def major(self, major):
        self._major = major
    
    def __str__(self):
        return "{} : {}".format(self.name,self.major)
    
    def __eq__(self, obj):
        if type(obj) != Student:
            return False
        else:
            return self.name == obj.name and self.major == obj.major

def main():
    jeff = Student("Jeff", "American History")
    robert = Student("Jeff", "American History")
    # print(jeff.name, ":", jeff.major)
    # jeff.name = "Jeffrey"
    # print(jeff.name, ":", jeff.major)
    print(jeff == robert)
    


if __name__ == "__main__":
    main()