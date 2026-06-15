import requests 
import time
from config import BASE_URL


def fetch_characters():

    master_list = []
    page = 1
    max_page = 25

    while page <= max_page:

        url = f"{BASE_URL}?page={page}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json().get('results',[])

        master_list.extend(data)

        time.sleep(1)

        page += 1

    return master_list  

