from dotenv import load_dotenv
import googlemaps
import logger
import os

load_dotenv()
API_KEY = os.environ.get("API_KEY")

try:
    logger.info_log( 'Loading Google Maps Client' )
    G_MAPS = googlemaps.Client( key=API_KEY )

except Exception as e:
    logger.error_log( f'Error Loading Google Maps Client: {e}' )
    exit()


def get_geocode(full_address):
    """ Returns the Geocoded Address """
    
    try:
        return G_MAPS.geocode(full_address)
    except Exception as e:
        logger.error_log( f'Error Extracting the Address: {e}' )
        exit()