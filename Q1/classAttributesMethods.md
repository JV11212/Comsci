# Class Attributes and Methods 
## Previous Design 
Link to my previous activity: 
[classObjectUML.md](classObjectUML.md) 
## Design Revision 
Changes from my previous design:
- Renamed fuellevel to fuel_level and getfuellevel() to get_fuel_level() to follow Python naming style.
- Added a private mileage attribute so drive() can actually track distance travelled.
- Added a private tank_capacity so refuel() can enforce the "up to its tank capacity" rule from my original description.
- Added get_mileage() so the private mileage can be read safely.
## Visibility Decisions 
| Attribute | Data Type | Visibility | Reason | 
|---|---|---|---| 
|make|string| Public|Identifying info that is safe to read anywhere.| 
|model | string| Public |Identifying info that is safe to read anywhere.| 
|year |	int |Public |Identifying info that is safe to read anywhere. |
|fuel_level | double| Private| Must only change through drive() and refuel() so it can never go negative or exceed the tank. |
|mileage|double|private|An odometer should only go up through drive(), never be set freely.|
|tank_capacity|double|private|Fixed internal limit used by refuel().|
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
