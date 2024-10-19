#AUTHOR: Trevor Conger
#DATE: 10/18/24
#TITLE: Rainfall


#Function to gather rainfall for the 12 months in the year
#RETURN: rainfall array, months array 
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

#FUNCTION to calculate the rainfall for the months
#RETURN totalrainfall sum, average rainfall, maxrainfall, month with max rainfall, 
# min rainfall month, month with min rainfall
def calculateRainfall(rainfall, months):
    totalRainfall = sum(rainfall)
    averageRainfall = totalRainfall / len(rainfall)
    
    maxRainfall = max(rainfall)
    minRainfall = min(rainfall)
    maxMonth = months[rainfall.index(maxRainfall)]
    minMonth = months[rainfall.index(minRainfall)]
    
    return totalRainfall, averageRainfall, maxRainfall, maxMonth, minRainfall, minMonth

#MAIN
#call gatherInputOnRainfall
#call calculateRainfall
#print totalrainfall
#print average monthly rainfall
#print month with highest rainfall
#print month with the lowest rainfall
def main():
    rainfall, months = gatherInputOnRainfall()
    total, average, maxRain, maxMonth, minRain, minMonth = calculateRainfall(rainfall, months)
    
    print(f"\nTotal rainfall for the year: {total:.2f}")
    print(f"\nAverage monthly rainfall: {average:.2f}")
    print(f"\nMonth with highest rainfall: {maxMonth} ({maxRain:.2f})")
    print(f"\nMonth with lowest rainfall: {minMonth} ({minRain:.2f})")

if __name__ == "__main__":
    main()