#URANUS

import math

def get_atmos(planet: str, norotation = False):
    #returns a list of altitudes, densities, and the angular velocity and equatorial 1-bar radius of the target planet
    atmos_dict = {'uranus': uranus_atmos, 'titan': titan_atmos, 'saturn': saturn_atmos}
    if planet in atmos_dict:
        altitudes, densities = atmos_dict[planet]()
        angular_velocity = get_angular_velocity(planet, norotation)
        bar_radius = get_bar_radius(planet)
        return altitudes, densities, angular_velocity, bar_radius
    else:
        print("PLANET NOT FOUND. DEFAULTING TO URANUS WITH NO ROTATION")
        altitudes, densities = atmos_dict["uranus"]
        angular_velocity = 0
        bar_radius = 25559
        return altitudes, densities, angular_velocity, bar_radius

def get_bar_radius(planet: str) -> int:
    #return the equatorial radius at one-bar level
    equatorial_radii = {'uranus': 25559, 'saturn': 60268, 'titan': 2575}
    if (planet in equatorial_radii) == True:
        return equatorial_radii[planet]
    else:
        print("PLANET NOT FOUND. DEFAULTING TO URANUS'S EQUATORIAL RADIUS")
        return 25559
    
def get_angular_velocity(planet: str, norotation: bool) -> float:
    #returns the angular velocity of the planet
    day_lengths_hours = {'uranus': 17.23, 'earth': 24.0, 'titan': 382.0, 'saturn': 10.5} #length of each planet's day in hours
    if norotation: #if user desires to ignore atmospheric rotation
        return 0.0
    elif( planet in day_lengths_hours) == False:
        print("PLANET NOT FOUND. DEFAULTING TO ZERO ANGULAR VELOCITY.")
        return 0.0
    day_hours = day_lengths_hours[planet] #locate planet and its corresponding day length in above dictionary
    ang_vel_rads = (2.0*math.pi) / (day_hours * 3600.0) #radians per second
    return ang_vel_rads

def uranus_atmos():
    #returns lists containing altitudes and densities at different points in uranus's atmosphere
    #atmospheric density profile provided by Julie Moses, see more in README
    file = "uranus_atmosphere.out"
    f = open(file,"r")
    lines = f.readlines()[3:] 
    altitudes_str = []
    densities_str = []
    bmasses_str = []
    for line in lines:
        line_split = line.split(' ')
        line_split = [item for item in line_split if item != '']
        altitudes_str.append(line_split[1])
        densities_str.append(line_split[3])
        bmasses_str.append(line_split[8])
    f.close()
    #prepare data for use, converting units and doing simple computations
    
    altitudes = []
    altitudes = [float(val) for val in altitudes_str] #string to float
    bmass = []
    bmass = [float(val) for val in bmasses_str] #string to float

    densities = []
    for i in range(len(densities_str)):
        num_dens = float(densities_str[i]) #string to float, truncate /n, unit conversion not necessary
        densities.append(num_dens * bmass[i] * 1.66054e-24 / 1000) # density in kg/m^3 is DEN*BMASS*(grams per AMU)*1000
    return altitudes, densities


def titan_atmos():
     #returns lists containing altitudes and densities at different points in titan's atmosphere
     #atmospheric density profile has been eyeballed by Shaya from Sarani et al. only contains a few points
    file = "titan_atmosphere.txt"
    f = open(file,"r")
    lines = f.readlines()[8:] 
    altitudes_str = []
    densities_str = []
    for line in lines:
        line_split = line.split('\t')
        line_split = [item for item in line_split if item != '']
        print(line_split)
        altitudes_str.append(line_split[0])
        densities_str.append(line_split[1])
    f.close()
    #convert all values to floats and density to kg/m^3
    densities = []
    altitudes = []
    densities_str[-1] += "\n"
    for val in densities_str:
        kgm = float(val) #string to float, truncate /n, unit conversion not necessary
        densities.append(kgm)

    altitudes = [float(val) for val in altitudes_str] #string to float
    return altitudes, densities


def saturn_atmos():
    #returns lists containing altitudes and densities at different points in saturn's atmosphere
    #atmospheric density profile sourced from LARC, see more in README file
    file = "saturn_atmosphere.txt"
    f = open(file,"r")
    lines = f.readlines()[6:] 
    altitudes_str = []
    densities_str = []
    for line in lines:
        line_split = line.split('\t')
        line_split = [item for item in line_split if item != '']
        altitudes_str.append(line_split[0])
        densities_str.append(line_split[4])
    f.close()
    #convert all values to floats and density to kg/m^2
    densities = []
    altitudes = []
    for val in densities_str:
        kgm = float(val) #string to float, truncate /n, unit conversion not necessary
        densities.append(kgm)

    altitudes = [float(val) for val in altitudes_str] #string to float   
    return altitudes, densities
