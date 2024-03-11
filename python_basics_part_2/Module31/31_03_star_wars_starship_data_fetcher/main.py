import json
from typing import Dict, Optional

import requests

X_WING_ID = 12
STARSHIP_ENDPOINT = f"https://swapi.dev/api/starships/{X_WING_ID}/"


def get_api_data(url: str) -> Optional[Dict]:
    """
    Fetch data from the given URL using the requests library.

    Args:
        url (str): The URL from which to fetch the data.

    Returns:
        dict: Parsed JSON data from the response if the request is successful.
        None: If the request fails or an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None


def get_starship_data() -> Optional[Dict]:
    """
    Retrieve data for the X-wing starship from the Star Wars API.

    Returns:
        dict: A dictionary of the starship's data if the request is successful.
        None: If the request fails or an error occurs.
    """
    return get_api_data(STARSHIP_ENDPOINT)


def get_pilot_data(pilot_url: str) -> Optional[Dict]:
    """
    Retrieve data for a single pilot from the Star Wars API.

    Args:
        pilot_url (str): The API URL for fetching pilot data.

    Returns:
        dict: A dictionary containing pilot information if the request is successful.
        None: If the request fails or an error occurs.
    """
    pilot_data = get_api_data(pilot_url)
    if pilot_data:
        homeworld_name = get_homeworld_name(pilot_data['homeworld'])
        return {
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'mass': pilot_data['mass'],
            'homeworld': homeworld_name,
            'homeworld_url': pilot_data['homeworld']
        }
    return None


def get_homeworld_name(homeworld_url: str) -> Optional[str]:
    """
    Retrieve the name of a homeworld from the Star Wars API.

    Args:
        homeworld_url (str): The API URL for fetching homeworld data.

    Returns:
        str: The name of the homeworld if the request is successful.
        None: If the request fails or an error occurs.
    """
    homeworld_data = get_api_data(homeworld_url)
    return homeworld_data['name'] if homeworld_data else None


def main() -> None:
    """
    Main execution function to fetch data for the X-wing starship and its pilots,
    serialize the data to a JSON file, and print it to the console.
    """
    x_wing_data = get_starship_data()
    if x_wing_data:
        pilots_info = [get_pilot_data(url) for url in x_wing_data['pilots'] if get_pilot_data(url)]

        x_wing_info = {
            'ship_name': x_wing_data['name'],
            'max_atmosphering_speed': x_wing_data['max_atmosphering_speed'],
            'starship_class': x_wing_data['starship_class'],
            'pilots': pilots_info
        }

        # Serialize the data into a JSON file with proper file handling
        with open('x_wing_pilots.json', 'w', encoding='utf-8') as file:
            json.dump(x_wing_info, file, indent=4, ensure_ascii=False)

        # Print to console
        print(json.dumps(x_wing_info, indent=4, ensure_ascii=False))
    else:
        print("Failed to get data for the X-wing starfighter.")


if __name__ == "__main__":
    main()
