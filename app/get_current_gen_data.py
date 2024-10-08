import requests
from datetime import datetime

def get_current_gen_data()-> dict:

    # create a doctopmary amd record the current time
    current_power_dict = {}
    current_power_dict['gen_datetime'] = datetime.now()

    # all genereation except solar
    url = "https://data.elexon.co.uk/bmrs/api/v1/generation/outturn/current?format=json"
    response = requests.get(url)

    data = response.json()



    for power_dict in data:
        current_power_dict[power_dict['fuelType']] =  power_dict['currentUsage']


    url = "https://api.solar.sheffield.ac.uk/pvlive/api/v4/gsp/0"
    response = requests.get(url)
    data = response.json()
    current_power_dict['SOLAR'] = data['data'][0][2]

    return current_power_dict

if __name__ == "__main__":
    print (get_current_gen_data())
