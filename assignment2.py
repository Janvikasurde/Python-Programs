#Question - take diameter of input from user and calculate the area of circle 

diameter = int(input("Enter diamter of circle:"))
radius = diameter / 2
area = 3.14*(radius**2)
print("Area of circle is:", area)
print("Radius of the circle is:",radius)