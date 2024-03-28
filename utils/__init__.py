from typing import List
from datetime import date

# define the endpoint
ENDPOINT = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

# define the column selection
DEFAULT_COLUMNS = ['kenteken', 'merk', 'handelsbenaming', 'catalogusprijs', 'datum_tenaamstelling']

# define the default column names
DEFAULT_COLUMN_NAMES = {'handelsbenaming': 'model',
                        'catalogusprijs': 'prijs', 
                        'datum_tenaamstelling': 'datum'}


# define the default data types
DEFAULT_DATA_TYPES = {
    'catalogusprijs': float,
    'bruto_bpm': float,
    'datum_tenaamstelling': date
}