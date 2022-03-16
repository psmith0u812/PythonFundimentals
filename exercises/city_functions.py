





def get_city_country(city, country, population=' '):
    # return City, Country pair correct formatting
    if population:
        city_country = f"{city}, {country} - Population {population}"
    else:
        city_country = f'{city}, {country}'
    return city_country.title()



