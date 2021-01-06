# import the RegistrationNode
from registrationNode import RegistrationNode

class RegistrationLinkedList:
    #Constructor
    def __init__(self):
        self.head = None
        self.size = 0

    #getting the total number of registrations
    def length(self):
        return self.size

    # add new Registration having the following inputs: student dictionary, college Id, department Id, course dictionary 
    def addNewRegistration(self, student, clgId, deptId, course):
        # create the new Node using the provided inputs
        newNode = RegistrationNode(student["id"], clgId, deptId, course["id"])
        
        # check if this registration is the first course for that student -> set the value of 'firstNode' to our newNode
        if student['firstNode'] == None:
            student['firstNode'] = newNode             
        else:
            studentNode = student['firstNode']
            #loop till reach last node (that has nextCourseNode == None)
            while studentNode.nextCourseNode != None:
                studentNode = studentNode.nextCourseNode
            
            # set last node's nextCourseNode value = newNode 
            studentNode.nextCourseNode = newNode
        
        # check if this registration is the first student for that course -> set the value of 'firstNode' to our newNode
        if course['firstNode'] == None:
            course['firstNode'] = newNode          
        else:
            courseNode = course['firstNode']            
            #loop till reach last node (that has nextStudentNode == None)
            while courseNode.nextStudentNode != None:
                    courseNode = courseNode.nextStudentNode

            # set last node's nextStudentNode value = newNode
            courseNode.nextStudentNode = newNode
        
        #increment Size
        self.size += 1      
    
    # get list & count of students registered in a course given the following inputs: course dictionary, course Id, list of students, instance of the helper class
    def getRegisteredStudentsInCourse(self, course, crsId, students, helper):
        if course['firstNode'] == None:
            return "No students are registered in course" + course["name"]
        else:
            print(f"Registered Students in Course: {course['name']}:-")
            count = 1
            node = course['firstNode']
            curStudentId = node.studentId
            firstStudent = helper.getDataById(students, curStudentId)
            print(f"* student Id: {firstStudent['id']}, student Name: {firstStudent['name']}")
            #loop through the nodes and print its values
            while node.nextStudentNode != None:
                curNode = node.nextStudentNode
                curStudentId = curNode.studentId
                curStudent = helper.getDataById(students, curStudentId)
                print(f"* student Id: {curStudent['id']}, student Name: {curStudent['name']}")                
                count += 1
                node = node.nextStudentNode
            print(f"total # students registered in {course['name']}: {count}")
   
    # get list & count of courses registered by a student given the following inputs: student dictionary, student Id, list of courses, instance of the helper class
    def getCoursesRegisteredByStudent(self, student, stId, courses, helper):
        if student['firstNode'] == None:
            print(f"{student['name']} has not yet registered in any courses")
        else:
            print(f"Course Registered by: {student['name']}:-")

            count = 1
            node = student['firstNode']
            curCourseId = node.courseId
            firstCourse = helper.getDataById(courses, curCourseId)
            print(f"* course Id: {firstCourse['id']}, course Name: {firstCourse['name']}")
            #loop through the nodes and print its values
            while node.nextCourseNode != None:
                curNode = node.nextCourseNode
                curCourseId = curNode.courseId
                curCourse = helper.getDataById(courses, curCourseId)
                print(f"* course Id: {curCourse['id']}, course Name: {curCourse['name']}")                
                count += 1
                node = node.nextCourseNode
            print(f"total # courses registered bt {student['name']}: {count}")

    # delete a registration of a student in a course
    def deleteRegistration(self, student, course):
        #if the 'firstNode' has no value; report to the user
        if student['firstNode'] == None or course['firstNode'] == None:
            print(f"This registration does not exist")
        else:
            studentNode = student['firstNode']
            # if 'firstNode' has same course Id as the one provided
            if studentNode.courseId == course['id']:
                if studentNode.nextCourseNode == None:
                    student['firstNode'] = None
                else:
                    # if having nextCourseNode -> set 'firstNode' value to point to the 'nextCourseNode'
                    student['firstNode'] = studentNode.nextCourseNode
                    
            else:
                deletionDone = False
                #loop the nodes till finding the node having same course Id
                while studentNode.nextCourseNode != None and deletionDone != True:
                    prevNode = studentNode
                    curNode = studentNode.nextCourseNode
                
                    if curNode.courseId == course['id']:
                        # changing the pointer of next Course Node from the "to be deleted course" to its next
                        if curNode.nextCourseNode != None:
                            prevNode.nextCourseNode = curNode.nextCourseNode
                            deletionDone = True
                        else:
                            prevNode.nextCourseNode = None
                            deletionDone = True
                    studentNode = studentNode.nextCourseNode
                        
            courseNode = course['firstNode']
            if courseNode.studentId == student['id']:
                if courseNode.nextStudentNode == None:
                    course['firstNode'] = None
                else:
                    # if having nextStudentNode -> set 'firstNode' value to point to the 'nextStudentNode'
                    course['firstNode'] = courseNode.nextStudentNode
            else:
                deletionDone = False
                #loop the nodes till finding the node having same student Id
                while courseNode.nextStudentNode != None and deletionDone != True:
                    prevNode = courseNode
                    curNode = courseNode.nextStudentNode
                    if curNode.studentId == student['id']:
                        # changing the pointer of next Student Node from the "to be deleted student" to its next
                        if curNode.nextStudentNode != None:
                            prevNode.nextStudentNode = curNode.nextStudentNode
                            deletionDone = True
                        else:
                            prevNode.nextStudentNode = None
                            deletionDone = True
                    courseNode = courseNode.nextStudentNode
            #decrement Size
            self.size -= 1