#importing the linkedlist
from registrationLL import RegistrationLinkedList

class Helper:
    #constructor having inputs: list of colleges, departments, students, courses
    def __init__(self, colleges, departments, students, courses):
        #colleges, departments, students, courses saved as self variables
        self.colleges = colleges
        self.departments = departments
        self.students = students
        self.courses = courses
        
        # create an instance of the linkedlist class
        self.reg = RegistrationLinkedList()

    def getAllItemsOfData(self, dataList):
        for x in range(len(dataList)): 
            print(dataList[x])
        
    # get any of the data; colleges, departments, students or courses by passing its list and the id to search for    
    def getDataById(self, dataList, _id):
        # iterating the data for that id
        data = next((item for item in dataList if item["id"] == _id), None)
        return data
    
    # validate the student Id and Course Id given
    def isInputsValid(self, stId, crsId):
        self.student = Helper.getDataById(self, self.students, stId)
        self.course = Helper.getDataById(self, self.courses, crsId)
        if self.student == None:
            return 'enter a valid Student ID'
        elif self.course == None:
            return 'enter a valid Course ID'
        else:
            return 'valid'
        
    # add new register for a student in a course by passing student Id & course Id
    def addNewRegister(self, stId=0, crsId=0):
        if stId == 0 or crsId == 0:
            return 'please insert correct arguments e.g. helper.addNewRegister(1, 1)'
        else:
            # first check inputs validity
            isInputsValid = Helper.isInputsValid(self, stId, crsId)

            if isInputsValid != 'valid':
                return isInputsValid
            
            else: 
                # if inputs are valid; prepare the complete data for the Registration Node 
                # college Id
                clgId = Helper.getDataById(self, self.colleges, stId)["id"]
                # dept Id
                deptId = Helper.getDataById(self,self.departments, stId)["id"]

                # call the addNewRegistration from the instance of the linkedlist class
                self.reg.addNewRegistration(self.student, clgId, deptId, self.course)

                # after finishing adding
                return 'student registered successfully'
    
    # get total # of registrations
    def getAllRegistrationsDone(self):
        return self.reg.length()
    
    # get list & count of students registered in a course
    def getRegisteredStudentsInCourse(self, crsId):
        # get the course by its Id
        course = Helper.getDataById(self, self.courses, crsId)
        # check validity
        if course == None:
            return 'enter a valid Course ID'
        else:
            # call the getRegisteredStudentsInCourse function from the instance of the linkedlist class
            self.reg.getRegisteredStudentsInCourse(course, crsId, self.students, self)
            
    # get list & count of courses registered by a student        
    def getCoursesRegisteredByStudent(self, stId):
        # get the student by his/her Id
        student = Helper.getDataById(self, self.students, stId)
        # check validity
        if student == None:
            return 'enter a valid Student ID'
        else:
            # call the getCoursesRegisteredByStudent function from the instance of the linkedlist class
            self.reg.getCoursesRegisteredByStudent(student, stId, self.courses, self)
     
    # delete a registration of a student in a course
    def deleteRegistration(self, stId=0, crsId=0):
        if stId == 0 or crsId == 0:
            return 'please insert correct arguments e.g. helper.deleteRegistration(1, 1)'
        else:
            isInputsValid = Helper.isInputsValid(self, stId, crsId)
        
            if isInputsValid != 'valid':
                return isInputsValid
            else:
                # get the student by his/her Id
                student = Helper.getDataById(self, self.students, stId)
                # get the course by its Id
                course = Helper.getDataById(self, self.courses, crsId)

                self.reg.deleteRegistration(student, course)        