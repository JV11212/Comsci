# SG4 - Understanding Classes and Objects 
## Car
## a car class encapsulates vehicle specs, fuel dynamics, and mileage tracking.  
## Properties
|---|---|---|
| Property | Data Type |     Description       |  
|  make   | string   |  the brand of the car  | 
| model | string  | the specific model name  |   
| year    | int    |  the manufacturing year of the car    |  
| fuellevel | double   | current amount of fuel | 
## Methods 
| Method | Description | 
|---|---|| | |
| drive(distance) | moves a car a given distance | 
| refuel(amount) | adds fuel to the car up to it's tank capacity | 
| getfuellevel() | shows the current fuellevel| 
| honk() | simulates the car honking |
## Class Diagram 
![Class Car](![alt text](image.png))
## Design Explanation 
### The Car class is simple four properties describe the car, four methods let it act. 
### The most important property is fuellevel because it's the only one that changes and drives the object's behavior.
### The most useful method is drive(distance) because it ties fuel consumption and mileage tracking together, the core logic of the class.