# University-Registration-System
This project is built using python to register or unregister a student to a course
## Data Structures Used:
Below are examples the data used:

```json
colleges = [{"id": 1, "name": "Agriculture" }, { "id": 2, "name": "Medicine" }]
```
```json
departments = [{"id":1,"name":"dept1","collegeId":1},{"id":2,"name":"dept2","collegeId":1}]
```
```json
courses = [{"id": 1,"name": "crs 1","departmentId": 1, "firstNode": None},   {"id": 2,"name": "crs 2",     "departmentId": 1   , "firstNode": None}]
```
```json
students = [{"id": 1,"name": "Sophia Alvarez","departmentId": 1 , "firstNode": None},   {     "id": 2,     "name": "Jerry Powell",     "departmentId": 1   , "firstNode": None}]
```

## and below is the Node used for registration:
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/1.%20node.png?raw=true)
 
Other values are as college Id, Department Id, grade

## UML Diagram:
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/2.%20UML.png?raw=true)

## Folder Structure:
*****
<table>
    <thead>
        <tr>
            <th></th>
            <th></th>
        </tr>
    </thead>
    <tbody>
      <tr>
         <td> UI.ipynb </td>
         <td> The file that the user deal with within JupyterLab </td>
      </tr>
     <tr>
        <td> registrationNode.py </td>
        <td> The node class </td>       
      </tr>
     <tr>
        <td> registrationLL.py </td>
        <td> The Linked List class having the following functions: 
           <table>
              <tbody>
               <tr> 
                <td> length </td> <td> getting the total number of registrations </td>
               </tr>
                  <tr>
                   <td> addNewRegistration </td> <td> add new Registration having the following inputs: student dictionary, college Id, department Id, course dictionary </td>
                  </tr>
                  <tr>
                    <td> getRegisteredStudentsInCourse </td> <td> get list & count of students registered in a course given the following inputs: course dictionary, course Id, list of students, instance of the helper class </td>                   
                  </tr>
                  <tr>
                   <td> getCoursesRegisteredByStudent </td> <td> get list & count of courses registered by a student given the following inputs: student dictionary, student Id, list of courses, instance of the helper class </td>
                  </tr>
               <tr>
                   <td> deleteRegistration </td> <td> delete a registration of a student in a course </td>
                  </tr>
              </tbody>
           </table>
        </td>       
      </tr>
     <tr>
      <td> Helper.py </td>
        <td> A class having functions to help in logic; it is used from UI.ipynb to call functions in registrationLL.py
           <table>
              <tbody>
               <tr> 
                <td> getDataById </td> <td> get any of the data; colleges, departments, students or courses by passing its list and the id to search for </td>
               </tr>
                  <tr>
                   <td> getAllItemsOfData </td> <td> Print all elements of a data list </td>
                  </tr>
                  <tr>
                    <td> isInputsValid </td> <td> validate the student Id and Course Id given </td>                   
                  </tr>
                  <tr>
                   <td> addNewRegister </td> <td> add new register for a student in a course by passing student Id & course Id </td>
                  </tr>
               <tr>
                   <td> getAllRegistrationsDone </td> <td> get total # of registrations </td>
                  </tr>
               <tr>
                   <td> getRegisteredStudentsInCourse </td> <td> get list & count of students registered in a course </td>
                  </tr>
               <tr>
                   <td> getCoursesRegisteredByStudent </td> <td> get list & count of courses registered by a student </td>
                  </tr>
               <tr>
                   <td> deleteRegistration </td> <td> delete a registration of a student in a course </td>
                  </tr>
              </tbody>
           </table>
        </td>   
      </tr>
    </tbody>
</table>

## Algorithms Used:
#### Here is the algorithm made to add a new registration of a student in a course:
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/3.%20add%20a%20new%20registration.png?raw=true)

#### And below is the algorithm used to get the registered students in a course (getting the courses registered by a student uses same algorithm with only different inputs and variables)
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/4.%20get%20the%20registered%20students.png?raw=true)

#### And the delete registration algorithm:
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/5.%20delete%20registration.png?raw=true)


## Use Cases:
Assume having the below registrations
 # |  1 | 2 | 3 | 4 | 5 | 6 | 7
--- | --- | --- | --- | --- | --- | --- | ---
1|*| *| *| | | | |
2|*|  |  | *| *| | *|
3| | *| *| | *| *| |
4| | *| | *| | *| *|
5| | | *| *| | *| *| 
____

First importing that Helper class
```python
from helper import Helper
```
creating an instance of the Helper Class
```python
helper = Helper(colleges, departments, students, courses)
```
To add registration e.g: passing student Id, Course Id
```python
helper.addNewRegister(1, 2)
```
to get total # of registrations:
```python
helper.getAllRegistrationsDone()
```
To get list & count of students registered in a course: passing course Id 
```python
helper.getRegisteredStudentsInCourse(5) 
```
To get list & count of courses registered by a student: passing student Id 
```python
helper.getCoursesRegisteredByStudent(7)
```
To delete a registration: passing student Id, Course Id
```python
helper.deleteRegistration(3, 3)
```

## Screen shots:
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/6.%20s1.png?raw=true)
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/7.%20s2.png?raw=true)
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/8.%20s3.png?raw=true)
