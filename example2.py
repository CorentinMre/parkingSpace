import parkingSpace

carPark = parkingSpace.Parking("caen")

if carPark.tryConn:
    print(carPark)
else:
    print("City Error")