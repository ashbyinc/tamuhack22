import datetime as datetime

def valueexchange(column):
    iter = 0
    arrayop = []
    with open("data/airport.csv", "r", encoding="utf8") as airData:
        for line in airData:
            if iter != 0: 
                workingline = line.split(",")
                arrayop.append(workingline[column].replace('"', ""))
            else:
                pass
            iter += 1
    return(arrayop)

Code = (valueexchange(4))
timeZone = (valueexchange(9))
places = (valueexchange(3))

UTC = int(datetime.datetime.utcnow().strftime('%H%M'))

def timeFinder(depart, arrival, leaving, flightlen):
    timenow = str(UTC + (int(timeZone[Code.index(depart)])*100))
    timenow = datetime.datetime.strptime(timenow,'%H%M').strftime('%I:%M %p')

    flightlen = int(flightlen)

    leaving = int(datetime.datetime.strptime(leaving,'%I:%M %p').strftime('%H%M'))
    UTCthen = leaving - (int(timeZone[Code.index(depart)])*100) 


    print("\nit is currently", timenow)
    flightlen *= 100

    timethen = (UTCthen + flightlen)
    timethen += (int(timeZone[Code.index(arrival)])*100)

    
    while (timethen > 2400):
        timethen = timethen - 2400

    timethen = datetime.datetime.strptime(str(timethen),'%H%M').strftime('%I:%M %p')
    print("based on your travel time, it will be", timethen, "when you arrive at your destination in", places[Code.index(arrival)])
    return(timethen)


timeFinder("LGA", "CDG", "6:00 pm" , 7)

# timeFinder(
#     input("what is your departing airport's IATA code? ",),
#     input("what is your arrival airport's IATA code? ",),
#     input("when are you leaving? ",),
#     input("how long is your flight? ",))

# def sleeper(timetobed, timetowake):
#     # timetobed, timetowake = str(timetobed), str(timetowake)
#     TTB = datetime.datetime.strptime(timetobed,'%I:%M %p').strftime('%H%M')
#     TTW = datetime.datetime.strptime(timetowake,'%I:%M %p').strftime('%H%M')

#     totalTime = TTW-TTB
#     print(totalTime)


# sleeper("10:00 pm", "7:00 am")

# timeFinder(
#     input("what is your departing airport's IATA code? ",),
#     input("what is your arrival airport's IATA code? ",),
#     input("when are you leaving? ",),
#     input("how long is your flight? ",))
