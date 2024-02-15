#! /usr/bin/python3

"""Module providing a funtion printing and saving emails from wanted country to file"""

import sys
import requests

def get_api(country_input):
    """Fetches email adress from the API for the given country."""
    response = requests.get('https://randomuser.me/api', timeout=10)
    country = response.json()['results'][0]['location']['country']
    email = response.json()['results'][0]['email']

    if country == country_input:
        return email
    return None

def save_to_file(email, filename):
    """Saves the email adress to the specified file."""
    with open(filename, 'a', encoding="utf-8") as file:
        if file.tell():
            file.write("\n")
        file.write(email)

def main():
    """Main function to run the script."""
    if len(sys.argv) < 2:
        print("Forgot to enter country?\nUsage: emails 'Country'")
        sys.exit(1)

    country_input = sys.argv[1]
    filename = f"{country_input}_email_list.txt"

    counter = 0

    try:
        while counter < 5:
            email = get_api(country_input)
            if email:
                print(email)
                save_to_file(email, filename)
                counter += 1
    except KeyboardInterrupt:
        print("\nScript interrupted.")

if __name__ == "__main__":
    main()
