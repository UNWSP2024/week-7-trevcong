# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def gatherInputOnRainfall():
    rainfall = []
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    for month in months:
        while True:
            try:
                amount = float(input(f"Enter the rainfall in inches for {month}: "))
                if amount < 0:
                    print("Rain can't be in negative inches")
                else:
                    rainfall.append(amount)
                    break
            except ValueError:
                print(ValueError, "Please enter a number.")
    return rainfall, months

def calculateRainfall(rainfall, months):
    totalRainfall = sum(rainfall)
    averageRainfall = totalRainfall / len(rainfall)
    
    maxRainfall = max(rainfall)
    minRainfall = min(rainfall)
    maxMonth = months[rainfall.index(maxRainfall)]
    minMonth = months[rainfall.index(minRainfall)]
    
    return totalRainfall, averageRainfall, maxRainfall, maxMonth, minRainfall, minMonth

def main():
    rainfall, months = gatherInputOnRainfall()
    total, average, maxRain, maxMonth, minRain, minMonth = calculateRainfall(rainfall, months)
    
    print(f"\nTotal rainfall for the year: {total:.2f}")
    print(f"\nAverage monthly rainfall: {average:.2f}")
    print(f"\nMonth with highest rainfall: {maxMonth} ({maxRain:.2f})")
    print(f"\nMonth with lowest rainfall: {minMonth} ({minRain:.2f})")

if __name__ == "__main__":
    main()