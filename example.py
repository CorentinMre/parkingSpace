import parkingSpace

carPark = parkingSpace.Parking("caen")

if carPark.tryConn:

    allTheParkingsInTheCity = carPark.findPark(ifNoParkingSpace = False) # 'ifNoParkingSpace': It's  if no parking space counter in this car park {'place':None}
    
    for i in allTheParkingsInTheCity:
        print(f"""
              name: {i}
              title: {allTheParkingsInTheCity[i]["title"]}
              city: {allTheParkingsInTheCity[i]["city"]}
              street: {allTheParkingsInTheCity[i]["street"]}
              latitude: {allTheParkingsInTheCity[i]["lat"]}
              longitude: {allTheParkingsInTheCity[i]["lng"]}
              total spots: {allTheParkingsInTheCity[i]["totalSpots"]}
              frees spots: {allTheParkingsInTheCity[i]["freesSpots"]}
              -----------------------------\n\n""")
    
    ################################################
    #OR
    ################################################
    print(carPark)

else:
    print("City Error")