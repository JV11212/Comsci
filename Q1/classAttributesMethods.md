# Class Attributes and Methods 
## Previous Design 
Link to my previous activity: 
[classObjectUML.md](classObjectUML.md) 
## Design Revision 
Describe any changes made to your original class. 
## Visibility Decisions 
| Attribute | Data Type | Visibility | Reason | 
|---|---|---|---| 
|make|string| Public|Identifying info that's safe to read directly; changing it doesn't risk breaking any internal logic. | 
|model | string| Public |	Same reasoning as make descriptive, not tied to the object's internal state. | 
|year |	int |Public |	Static metadata about the car; there's no invariant to protect. | 
|fuellevel | double| Private|Changes constantly through drive()/refuel() and must stay within a valid range. | 
## Updated UML Class Diagram 
![Class Diagram](images/classDiagramSG5.png) 
## Python Implementation
[View Python Source](classImplementation.py) 
## Test Run 
![Test Run](images/classTestRun.png) 
## Object Diagram 
![Object Diagram](images/objectDiagram.png) 
## Analysis 
### Why did you make your chosen attribute private? 
### Which method changes the state of your object? 
### How did your two objects demonstrate that instances are independent? ### What is the difference between your class diagram and your object diagram? 
