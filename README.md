# University-Registration-System
This project is built using python to register or unregister a student to a course
##Data Structures Used:
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
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/1. node.png?raw=true)
KhaledTaymour/University-Registration-System/blob/main/images/1. node.png
 
Other values are as college Id, Department Id, grade

## UML Diagram:
![alt text](https://github.com/KhaledTaymour/University-Registration-System/blob/main/images/2. UML.png?raw=true)

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
*****

## Use Cases:

## Screen shots:
