# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
def update_damages():
    new_damages = []
    for damage in damages:
        if (damage[-1] == 'M') or (damage[-1] == 'B'):
            new_damages.append(float(damage[:len(damage)-1]) * float(conversion.get(damage[-1])))
        else:
            new_damages.append(damage)            
    return new_damages

# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
damages = update_damages()
print(damages)

# 2 
# Create a Table
# 2
# Create a Table
hurricanes = {}
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dict_hurricanes = dict()
    num_index = len(names)
    for ind in range(num_index):
        dict_hurricanes[names[ind]] = {
            'Name':names[ind],
            'Month':months[ind],
            'Year':years[ind],
            'Max_Sustained_Wind':max_sustained_winds[ind],
            'Areas_Affected':areas_affected[ind],
            'Damages':damages[ind],
            'Deaths':deaths[ind]
        }
        
    return dict_hurricanes


# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricanes)
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def create_hurricanes_year(hurricanes):
    dict_hurricanes_year = dict()
    for hurricane in hurricanes:
        #get the current year by selecting 'Year' key, then get the hurricane details
        current_year = hurricanes[hurricane]['Year']
        current_hurricane = hurricanes[hurricane]
        #group the hurricane read through the hurricanes dictionary to hurricanes_year dictionary.
        #make sure to check if to insert or update the hurricanes_year dictionary
        if current_year not in dict_hurricanes_year:
            dict_hurricanes_year[current_year] = [current_hurricane]
        else:
            dict_hurricanes_year[current_year].append(current_hurricane)
    return dict_hurricanes_year

hurricanes_year = create_hurricanes_year(hurricanes)
#display what hurricanes occurred in 1932 as stated in the example
print(hurricanes_year[1932])

# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes):
    """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areaas as keys."""
    affected_areas_count = dict()
    for hurricane in hurricanes:
        for area in hurricanes[hurricane]['Areas_Affected']:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_affected_areas(hurricanes)
print(affected_areas_count)


# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(affected_areas_count):
    """Find most affected area and the number of hurricanes it was involved in."""
    max_area = 'Central America'
    max_area_count = 0
    for area in affected_areas_count:
        if affected_areas_count[area] > max_area_count:
            max_area = area
            max_area_count = affected_areas_count[area]
    return max_area, max_area_count

# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = most_affected_area(affected_areas_count)
print(max_area, max_area_count)


# 6
# Calculating the Deadliest Hurricane
def highest_mortality(hurricanes):
    """Find the highest mortality hurricane and the number of deaths it caused."""
    "Set initial value, get the higher value while browsing in the loop"
    max_mortality_hurricane = 'Cuba I'
    max_mortality = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Deaths'] > max_mortality:
            max_mortality_hurricane = hurricane
            max_mortality = hurricanes[hurricane]['Deaths']
    return max_mortality_hurricane, max_mortality

# find highest mortality hurricane and the number of deaths
max_mortality_hurricane, max_mortality = highest_mortality(hurricanes)
print(max_mortality_hurricane, max_mortality)

# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricanes):
    """Categorize hurricanes by mortality and return a dictionary."""
    mortality_scale = {0: 0,
                      1: 100,
                      2: 500,
                      3: 1000,
                      4: 10000}
    hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricanes:
        num_deaths = hurricanes[hurricane]['Deaths']
        if num_deaths == mortality_scale[0]:
            hurricanes_by_mortality[0].append(hurricanes[hurricane])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(hurricanes[hurricane])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(hurricanes[hurricane])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(hurricanes[hurricane])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(hurricanes[hurricane])
        elif num_deaths > mortality_scale[4]:
            hurricanes_by_mortality[5].append(hurricanes[hurricane])
    return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricanes)
print(hurricanes_by_mortality[5])


# 8
# Calculating Hurricane Maximum Damage
def highest_damage(hurricanes):
    """Find the highest damage inducing hurricane and its total cost."""
    max_damage_hurricane = 'Cuba I'
    max_damage = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Damages'] == "Damages not recorded":
            pass
        elif hurricanes[hurricane]['Damages'] > max_damage:
            max_damage_hurricane = hurricane
            max_damage = hurricanes[hurricane]['Damages']
    return max_damage_hurricane, max_damage

# find highest damage inducing hurricane and its total cost
max_damage_hurricane, max_damage = highest_damage(hurricanes)
print(max_damage_hurricane, max_damage)

# 9
# Rating Hurricanes by Damage
def categorize_by_damage(hurricanes):
    """Categorize hurricanes by damage and return a dictionary."""
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricanes:
        total_damage = hurricanes[hurricane]['Damages']
        if total_damage == "Damages not recorded":
            hurricanes_by_damage[0].append(hurricanes[hurricane])
        elif total_damage == damage_scale[0]:
            hurricanes_by_damage[0].append(hurricanes[hurricane])
        elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricanes[hurricane])
        elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricanes[hurricane])
        elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
            hurricanes_by_damage[3].append(hurricanes[hurricane])
        elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricanes[hurricane])
        elif total_damage > damage_scale[4]:
            hurricanes_by_damage[5].append(hurricanes[hurricane])
    return hurricanes_by_damage

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = categorize_by_damage(hurricanes)
print(hurricanes_by_damage[5])

