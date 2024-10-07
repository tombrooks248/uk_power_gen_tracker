import requests
from datetime import datetime

def get_current_gen_data()-> dict:
    url = "https://data.elexon.co.uk/bmrs/api/v1/generation/outturn/current?format=json"
    response = requests.get(url)

    data = response.json()

    current_power_dict = {}
    current_power_dict['datetime'] = datetime.now()

    for power_dict in data:
        current_power_dict[power_dict['fuelType']] =  power_dict['currentUsage']

    return current_power_dict

if __name__ == "__main__":
    print (get_current_gen_data())
