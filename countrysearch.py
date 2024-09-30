import requests

def search_countries_by_name(search_term):
    try:
        # Make a GET request to the restcountries API
        url = f"https://restcountries.com/v2/name/{search_term}"
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            countries = response.json()

            # Print country details
            if len(countries) == 0:
                print(f"No matching countries found for: {search_term}")
            else:
                for country in countries:
                    name = country.get("name", "N/A")
                    capital = country.get("capital", "N/A")
                    population = country.get("population", "N/A")
                    region = country.get("region", "N/A")
                    subregion = country.get("subregion", "N/A")
                    currencies = ', '.join([c["name"] for c in country.get("currencies", []) if "name" in c])
                    languages = ', '.join([l["name"] for l in country.get("languages", []) if "name" in l])

                    # Print country details
                    print(f"Country: {name}")
                    print(f"Capital: {capital}")
                    print(f"Population: {population}")
                    print(f"Region: {region}")
                    print(f"Subregion: {subregion}")
                    print(f"Currencies: {currencies}")
                    print(f"Languages: {languages}")
                    print("-" * 40)
        else:
            print(f"Error: Unable to fetch data for {search_term}. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    search_term = input("Enter part of a country name to search: ")
    search_countries_by_name(search_term)
