# 07_countries.py

countries = {
    "Irsko": 4593100,
    "Chorvatsko": 4290612,
    "Moldavsko": 3559500,
    "Litva": 2941953,
    "Albánie": 2821977,
    "Slovensko": 5415949,
    "Norsko": 5109056,
    "Itálie": 59943933,
    "Španělsko": 46609700,
    "Ukrajina": 45426200,
    "Polsko": 38502396,
    "Makedonie": 2062294,
    "Slovinsko": 2061963,
    "Lotyšsko": 2003900,
    "Kosovo": 1815606,
    "Estonsko": 1311870,
    "Rusko": 143700000,
    "Německo": 80619000,
    "Turecko": 76667864,
    "Francie": 65844000,
    "Velká Británie": 63705000,
    "Portugalsko": 10487289,
    "Maďarsko": 9906000,
    "Švédsko": 9651531,
    "Bělorusko": 9468100,
    "Rakousko": 8504850,
    "Švýcarsko": 8112200,
    "Bulharsko": 7282041,
    "Srbsko": 7181505,
    "Dánsko": 5627235,
    "Finsko": 5452821,
    "Rumunsko": 20121641,
    "Nizozemsko": 16842200,
    "Belgie": 11132269,
    "Řecko": 10815197,
    "Česko": 10513800,
}

def analyze_european_population(data: dict):
    """
    Analyzes population data and returns:
    - Average population
    - Lowest population count
    - Highest population count
    """
    try:
        country_count = len(data)
        total_population = sum(data.values())
        average_population = total_population // country_count
        
        lowest_populated_country = min(data.values())
        highest_populated_country = max(data.values())

        return average_population, lowest_populated_country, highest_populated_country
    
    except ValueError as e:
        print(f"Error processing given data: {e}")
        return None, None, None

def get_boundary_points(data: dict, lowest_populated_country: int, highest_populated_country: int):
    """
    Finds the countries with the lowest and highest populations.
    """
    country_1 = None
    country_2 = None
    for key, value in data.items():
        if value == lowest_populated_country:
            country_1 = key
        if value == highest_populated_country:
            country_2 = key
    return country_1, country_2

def main():
    # Analyze data
    average, lowest, highest = analyze_european_population(countries)
    if average is None:
        print("Population analysis failed.")
        return

    # Find boundary countries
    country_1, country_2 = get_boundary_points(countries, lowest, highest)

    # Print results
    print(
        f"The average population is {average} people.\n"
        f"The smallest population is in {country_1}: {lowest} people.\n"
        f"The largest population is in {country_2}: {highest} people."
    )

if __name__ == '__main__':
    main()
