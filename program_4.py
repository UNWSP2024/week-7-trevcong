#AUTHOR: Trevor Conger
#DATE: 10/18/24
#TITLE: Math!
import math

#FUNCTION to calculate the distance from point 1 to 2
#PARAM point1 (x2,y2,z2)
#param point2 (x2,y2,z2)
#return calculation for distance from point 1 to 2
def distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

#FUNCTION to get point1 and point2
#keep trying till the user enters the correct format
#RETURN (x,y,z) for n point
def getPoint():
    while True:
        try:
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            z = float(input("Enter z coordinate: "))
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter numeric values for coordinates.")
#MAIN 
#get point1
#get point2
#try to call distance function
#print distance from point1 to point2
def main():
    print("Enter coordinates for the first point:")
    point1 = getPoint()
    
    print("\nEnter coordinates for the second point:")
    point2 = getPoint()
    
    try:
        result = distance(point1, point2)
        print(f"\nThe distance between {point1} and {point2} is: {result:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating the distance: {e}")

if __name__ == "__main__":
    main()