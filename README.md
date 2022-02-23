<p align="center"><a href="https://darkreader.org" target="_blank" rel="noreferrer noopener"><img width="250" alt="Dark Reader's mascot" src="img/icon.png"></a></p>
<p align="center">Parking Spaces is used to see the parking spaces near you. (<strong>only</strong> underground car parks and <strong>only</strong> in France)</p>
<br/>


<h2 align="center">Parking Spaces</h2>
<br/>

## Requirements

- Install requirements (`pip install -r requirements.txt`)
<br/>
<br/>

## Usage

Here is an example script:

```python
import parkingSpace

carPark = parkingSpace.Parking("caen")

if carPark.tryConn:

    allTheParkingsInTheCity = carPark.findPark(ifNoParkingSpace = False) 
    
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

else:
    print("City Error")
```

Or more simply...

```python
import parkingSpace

carPark = parkingSpace.Parking("caen")

print(carPark)
```