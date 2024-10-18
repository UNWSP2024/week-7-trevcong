import math

def distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def getPoint():
    while True:
        try:
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            z = float(input("Enter z coordinate: "))
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter numeric values for coordinates.")

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