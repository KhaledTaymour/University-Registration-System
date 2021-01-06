#Class of the registration node: having 2 pointers; one for next student node while the other for next course node
class RegistrationNode:
    #constructor
    def __init__(self, studentId=None, collegeId=None, departmentId=None, courseId=None, nextStudentNode=None, nextCourseNode=None):
        self.studentId = studentId 
        self.collegeId = collegeId
        self.departmentId = departmentId
        self.courseId = courseId        
        self.nextStudentNode = nextStudentNode
        self.nextCourseNode = nextCourseNode
        self.grade = ""