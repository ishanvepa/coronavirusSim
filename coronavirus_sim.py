import math
from datetime import date



iterate = False
finalPop = 0

#a = derived constant, r = rate of growth/decline, t = time period (staring jan 22), k = peak population, h = shift
def calculate_final_population(a, r, t, k, h):
    population_final = k / (1 + a * math.exp(r * (t + h)))
    return population_final



def print_calendar(mm, dd):
    if mm == 1:
        return "January " + str(dd) + ", " + str(2020)
    elif mm == 2:
        return "February " + str(dd) + ", " + str(2020)
    elif mm == 3:
        return "March " + str(dd) + ", " + str(2020)
    elif mm == 4:
        return "April " + str(dd) + ", " + str(2020)
    elif mm == 5:
        return "May " + str(dd) + ", " + str(2020)
    elif mm == 6:
        return "June " + str(dd) + ", " + str(2020)
    elif mm == 7:
        return "July " + str(dd) + ", " + str(2020)
    elif mm == 8:
        return "August " + str(dd) + ", " + str(2020)
    elif mm == 9:
        return "September " + str(dd) + ", " + str(2020)
    elif mm == 10:
        return "October " + str(dd) + ", " + str(2020)
    elif mm == 11:
        return "November " + str(dd) + ", " + str(2020)
    elif mm == 12:
        return "December" + str(dd) + ", " + str(2020)




while not iterate:
    print("Enter the date you would like to simulate (mm/dd/yy)?")
    time  = input()
    month = int(time[:2])
    day   = int(time[3:5])

    day_of_year = int(date(2020, month, day).timetuple().tm_yday)

    time = day_of_year - 22
    rate = -0.3078108304 #change
    a = 103.7220217 # as of jan 22
    k = 58016

    h = 0
    timePrint = 0

    if time == 26:

        finalPop = 58016
        timePrint = time

    elif time > 26:
            rate *= -1
            h = -45.002
            timePrint = time
            time -= 26
            finalPop = int(calculate_final_population(a, rate, time, k, h))


    elif time < 26:
            timePrint = time
            finalPop = int(calculate_final_population(a, rate, time, k, h))


    #print("In " + str(timePrint) + " days, the population with the covid-19 virus will be " + str(finalPop) + " people.")
    print("On " + str(print_calendar(month, day)) + " , the population with the covid-19 virus will be " + str(finalPop) + " people.")

    print ("\nWould you like to simulate again (y/n)?")
    choice = input()

    if choice.casefold() == "y".casefold():
          iterate = False
    elif choice.casefold() == "n".casefold():
          iterate = True
          choice = input()
    else:
          print("\nYou did not enter an appropriate option.\nTry again.\n")


print("The program has concluded.")

