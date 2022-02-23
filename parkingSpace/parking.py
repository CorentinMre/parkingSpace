
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table



class Parking:
    
    """
    PARKINGS.
    
    Parameters
    ----------
    city : str

    Attributes
    ----------
    city : str
        The name of the city in lower case and with "-" instead of spaces 
    tryConn : bool
        If there is no error
    """
    
    def __init__(self,city:str):
        self.city = city.replace(" ","-").lower()
        self.parkindigoUrl = f"https://fr.parkindigo.com/parkings/{self.city}-france"
        self.placesUrl  = "https://fr.parkindigo.com/api/freeslots/"
        
        # start session
        self.session = requests.Session()
        self.response = self.session.get(self.parkindigoUrl)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.tryConn = self.response.url != "https://fr.parkindigo.com/erreur/indisponibilite"
        


    def findPark(self, ifNoParkingSpace:bool = False):
        
        """
        Get informations about a car park.
        
        ifNoParkingSpace : None
            It's  if no parking space counter in this car park {'place':None}

        Returns
        -------
        Dict[CarPark]
             A dictionary of parking lots found in the city with information on them
        """
        
        result = self.soup.find_all("li",{"class":"list__result__item"})
        dico = {}
        null = None
        for i in range(len(result)):
        
            dico[result[i].text.strip('\n')] = {"park-code":result[i]['data-park-code'],
                                                "title":result[i]['data-title'],
                                                "city":result[i]['data-city'],
                                                "street":result[i]['data-street'],
                                                "lat":result[i]['data-lat'],
                                                "lng":result[i]['data-lng'],
                                                "totalSpots": result[i]['data-total-slots']}
        console = Console()
        with console.status("[bold green]Working...") as status:
            for i in dico:
                freeSpots = eval(self.session.get(self.placesUrl+dico[i]["park-code"]).text)["free_spots"]
                dico[i]["freesSpots"] = freeSpots if freeSpots != None or ifNoParkingSpace == False else "No parking space counter in this car park."
                

                console.print(f"{list(dico).index(i)+1}/{len(dico)} | {i}")
                
            
        if dico == {}:
            print("Unfortunately, there is no Indigo parking in this area. Please search again.")
            exit()
        return dico
    
    
    def __repr__(self):
        
        
        
        table = Table(title="Parking space")


        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Title", style="green", no_wrap=True)
        table.add_column("City", style="green", no_wrap=True)
        table.add_column("Street", style="green", no_wrap=True)
        table.add_column("Latitude", style="green", no_wrap=True)
        table.add_column("Longitude", style="green", no_wrap=True)
        table.add_column("Total spots", style="green", no_wrap=True)
        table.add_column("Frees spots", style="green", no_wrap=True)

        allTheParkingsInTheCity = self.findPark()
        
        for i in allTheParkingsInTheCity:

            table.add_row(i, \
                allTheParkingsInTheCity[i]["title"], \
                allTheParkingsInTheCity[i]["city"], \
                allTheParkingsInTheCity[i]["street"], \
                str(allTheParkingsInTheCity[i]["lat"]), \
                str(allTheParkingsInTheCity[i]["lng"]), \
                str(allTheParkingsInTheCity[i]["totalSpots"]), \
                str(allTheParkingsInTheCity[i]["freesSpots"]))


        console = Console()
        console.print(table, justify="center")
        return ""

            



