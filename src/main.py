import requests
import logger
import json
 
from constants import API_URL, SP_REFERENCE, ST_START_NUMBER, ST_NAME, ST_STEP, LOCALITY
from geocode import get_geocode, get_coordinates


def main() -> None:
    """ App entry point """
    
    full_address = f"{ST_START_NUMBER} {ST_NAME}, {LOCALITY}"
    geocode = get_geocode(full_address)
    coordinates = get_coordinates(geocode)

    print("/*---------------------------------------*\\")
    print( f"Step 1 results: \n {full_address}\n Latitude: {coordinates.get('lat')}\n Longitude: {coordinates.get('lng')}" )
    print( f"Step 2 results:\n Finding neighborhood" )
    neighborhood = get_neighborhood(geocode) 
    print( f"Step 3 results: \n Neighborhood: {neighborhood}" ) 
    print( f"Step 4 results:\n Applying recursion ", end='', flush=True )
    result = skip_street(ST_START_NUMBER)
    print(f"\nStep 5: \n New address: {result.get('new_address')}  \n New neighborhood: {result.get('new_neighborhood')}\n Street steps: {calculate_distance(result.get('new_number'))} steps of {ST_STEP} meters")
    print("/*---------------------------------------*\\") 


def calculate_distance(new_number:int):
    """ Calculate the distance between starting point and the ending point in steps """
    return int((new_number - ST_START_NUMBER) / ST_STEP)


def get_neighborhood(geocode) -> str:
    """ Obtain the neighborhood from the Portland Maps API """

    coordinates = get_coordinates(geocode)
    lat = coordinates.get('lat')
    lng = coordinates.get('lng')

    try:
        request = requests.get(f'{API_URL}/query?geometryType=esriGeometryPoint&returnGeometry=false&f=pjson&geometry={lng}%2C{lat}%0D%0A&inSR={SP_REFERENCE}')
        data = json.loads(request.text)
        neighborhood = data.get("features")[0].get("attributes").get("NAME").title()

    except Exception as e:
        logger.error_log( f'Error Getting the neighborhood: {e}' )
        exit()

    return neighborhood


def skip_street(st_number:int, neighborhood:str = None) -> dict:
    """ Recursive method, skip the street until find a new neighborhood """
    logger.info_log( f'Skipping street, actual number: {st_number}' )
    
    full_address = f"{st_number} {ST_NAME}, {LOCALITY}"
    geocode = get_geocode(full_address)
    new_neighborhood = get_neighborhood(geocode)
   
    if new_neighborhood == neighborhood or neighborhood == None : 
        print(".", end='', flush=True)
        return skip_street(st_number + ST_STEP, new_neighborhood)
    
    logger.info_log( f'Found new neighborhood, Old: {neighborhood}, New: {new_neighborhood}' )
    return {"new_address":full_address, "new_neighborhood": new_neighborhood, "new_number": st_number}


if __name__ == "__main__":
    main()