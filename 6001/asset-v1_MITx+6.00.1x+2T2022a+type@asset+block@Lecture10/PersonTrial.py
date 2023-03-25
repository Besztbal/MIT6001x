# -*- coding: utf-8 -*-
"""
Created on Wed May 18 07:51:28 2016

@author: ericgrimson
"""

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    # other methods

    def __str__(self):
        """return self's name"""
        return self.name
    
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')


personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)
    
personList.sort()

print()

for e in personList:
    print(e)
        
class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
    
    def getIdNumName(self):        
            return str(self.idNum), (self.name)
        
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year
        
    def speak(self, utterance):
        return MITPerson.speak(self, " Yo Bro, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj,Student)



class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
        
    def speak(self, utterance):
        newUtterance = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, newUtterance + utterance)
        
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)
    


class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}    # maps idNum -> list of grades
        self.isSorted = True # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')


    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] 
        #return copy of list of students
        
    def allStudentsGen(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted=True
        for s in self.students:
            yield print(s)



def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)
    
    
ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)


six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

#print()
#
#print(gradeReport(six00))

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print()



        

faculty = Professor('Doctor Arrogant', 'six')
    
s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')


studentList = [s1, s2, s3, s4, s5]





print(s1)

print(s1.getClass())

print(s1.speak('where is the quiz?'))

print(s2.speak('I have no clue!'))

M1 = MITPerson('John')
M2 = MITPerson('Guttag')

MIT_PersonList=[M1,M2]

for e in MIT_PersonList:
    print(e.getIdNumName())




    

