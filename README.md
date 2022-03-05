<p align="center"><img width="250" alt="Parking Space" src="img/icon.png"></p>
<p align="center"><strong>Parking Space</strong> is used to see the parking spaces near you. (<strong>only</strong> underground car parks and <strong>only</strong> in France)</p>
<br/>


<h2 align="center">Parking Space</h2>
<br/>

## Requirements

- Install requirements (`pip install -r requirements.txt`)

## Usage

Here is an example script:

```python
import parkingSpace

carPark = parkingSpace.Parking("caen")

if carPark.tryConn:

    allCityCarParks = carPark.findPark(ifNoParkingSpace = False) 
    
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
```

Or more simply...

```python
import parkingSpace

carPark = parkingSpace.Parking("caen")

if carPark.tryConn:
    print(carPark)
else:
    print("City Error")
```