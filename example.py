import parkingSpace

carPark = parkingSpace.Parking("caen")

if carPark.tryConn:

    allCityCarParks = carPark.findPark(ifNoParkingSpace = False, seeWorking = True) # 'ifNoParkingSpace': It's  if no parking space counter in this car park {'place':None}
    
    for i in allCityCarParks:
        print(f"""
              name: {i}
              title: {allCityCarParks[i]["title"]}
              city: {allCityCarParks[i]["city"]}
              street: {allCityCarParks[i]["street"]}
              latitude: {allCityCarParks[i]["lat"]}
              longitude: {allCityCarParks[i]["lng"]}
              total spots: {allCityCarParks[i]["totalSpots"]}
              frees spots: {allCityCarParks[i]["freesSpots"]}
              -----------------------------\n\n""")

else:
    print("City Error")
