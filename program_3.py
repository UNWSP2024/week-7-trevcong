#AUTHOR: Trevor Conger
#DATE: 10/18/24
#TITLE: States population

def main():
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
              "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
              "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
              "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
              "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
              "New Hampshire", "New Jersey", "New Mexico", "New York",
              "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
              "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
              "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
              "West Virginia", "Wisconsin", "Wyoming"]
    
    all_entered_values = []
    
    while True:
        exitProgram = input("Do you want to add another year? YES or NO: ")
        if exitProgram.lower() == "no":
            break

        gg = []

        while True:
            try:
                userInputYear = int(input("Enter the year: "))
                if userInputYear > 2024:
                    raise ValueError("We need a year less than 2024")
                gg.append(userInputYear)
                break
            except ValueError as e:
                print(e)

        while True:
            stateInput = input("Enter a state: ")
            if stateInput not in states:
                print("Enter a state in the USA")
            else:
                gg.append(stateInput)
                break

        while True:
            try:
                populationInput = int(input("Enter the population: "))
                if populationInput < 0:
                    raise ValueError("Please enter a population greater than 0")
                gg.append(populationInput)
                break
            except ValueError as e:
                print(e)
        
        all_entered_values.append(gg)
 
    while(True):        
        try:
            userInputYearSum = int(input("Enter the year: "))
            if userInputYear > 2024:
                raise ValueError("We need a year less than 2024")
            sum_population_for_year(all_entered_values, userInputYearSum)
            break
        except ValueError as e:
            print(e)    

    print(all_entered_values)
#FUNCTION sum population for the year
#param all_entered_values : array with population for year and state
#param year_to_sum : sum population for that year
#print population for the year selected 
def sum_population_for_year(all_entered_values, year_to_sum):
    sum = 0
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            sum += entry[2]
    print(f"The population for the year {year_to_sum} is {sum}")
    
if __name__ == '__main__':
    main()