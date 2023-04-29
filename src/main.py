import logger
from constants import ST_START_NUMBER, ST_NAME, ST_STEP, LOCALITY
from geocode import get_geocode


def main() -> None:
    """ App entry point """
    
    full_address = f"{ST_START_NUMBER} {ST_NAME}, {LOCALITY}"
    geocode = get_geocode(full_address)
    coordinates = get_coordinates(geocode)

    print("/*---------------------------------------*\\")
    print( f"Step 1 results: \n {full_address}\n Latitude: {coordinates.get('lat')}\n Longitude: {coordinates.get('lng')}" )
    print( f"Step 2 results:\n Finding neigborhood" )
    neigborhood = get_neigborhood(geocode) 
    print( f"Step 3 results: \n Neigborhood: {neigborhood}" ) 
    print( f"Step 4 results:\n Applying recursion " )
    result = skip_street(ST_START_NUMBER)
    print(f"Step 5: \n New address: {result.get('new_address')}\n New neigborhood: {result.get('new_neigborhood')}\n Street steps: {calculate_distance(result.get('new_number'))} steps of {ST_STEP} meters")
    print("/*---------------------------------------*\\") 


def calculate_distance(new_number:int):
    """ Calculate the distance between starting point and the ending point in steps """
    return int((new_number - ST_START_NUMBER) / ST_STEP)


def get_coordinates(geocode):
    """ Obtain the coordinates from the provided Geocode """
    return geocode[0].get("geometry").get("location")


def get_neigborhood(geocode) -> str:
    """ Extracts the neighborhood from the Google response """
    address_components = geocode[0].get("address_components")
    
    for component in address_components:
        if "neighborhood" in component.get("types"):
            return component.get("long_name")


def skip_street(st_number:int, neigborhood:str = None) -> dict:
    """ Recursive method, skip the street until find a new neigborhood """
    logger.info_log( f'Skipping street, actual number: {st_number}' )
    full_address = f"{st_number} {ST_NAME}, {LOCALITY}"
    geocode = get_geocode(full_address)
    new_neigborhood = get_neigborhood(geocode)
   
    if new_neigborhood == neigborhood or neigborhood == None :
        return skip_street(st_number + ST_STEP, new_neigborhood)
    
    logger.info_log( f'Found new neigborhood, Old: {neigborhood}, New: {new_neigborhood}' )
    return {"new_address":full_address, "new_neigborhood": new_neigborhood, "new_number": st_number}


if __name__ == "__main__":
    main()