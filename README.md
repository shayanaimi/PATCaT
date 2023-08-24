# Preliminary Atmospheric Torque Calculation Tool (PATCaT)
Tool developed by Shaya Naimi during my summer 2023 JPL internship with Mark Hofstadter to determine atmospheric torque applied on a spacecraft at various altitudes.


## Project Description
The Preliminary Atmospheric Torque Calculation Tool (PATCaT) is a software tool designed as part of Shaya Naimi's 2023 JPL summer internship to determine how deep into Uranus's atmosphere the Uranus Flagship can fly while maintaining attitude control. While we desire to fly deep into the atmosphere to avoid ring particles, the dense atmosphere poses the threat of applying torque to the spacecraft. If the spacecraft's center of mass and center of pressure are misaligned with respect to its direction of motion, it experiences atmospheric torque. This torque is often small enough to be counteracted by the thrusters in the spacecraft's reaction control system, but if atmospheric torque becomes too great, the spacecraft will not be able to counteract it and lose control.

The objective of this tool is to provide an easily tweakable, rough-cut estimation of the torque a spacecraft experiences for the Uranus Flagship and future missions. Its parameters and atmospheric density profiles can easily be changed to experiment with different conditions. 

PATCaT is a very simply python tool that uses mostly standard libraries and draws upon previous similar studies on Cassini to calculate the atmospheric torque a spacecraft experiences given basic user-defined parameters about the spacecraft, its motion, and the planet and its atmosphere. The calculation it uses is mostly based on Andrade et al.'s equation (referenced below) and the default spacecraft is modeled based on Cassini. 

## How to Install and Run
Running PATCaT on your machine is very simple. Use Python 3 and follow the instructions below:

1. In Terminal, [clone the Github repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and navigate to the PATCaT directory.
2. Once in PATCaT, install the simple requirements for the program: ``` pip install -r requirements.txt ```
3. Then, simply run the Jupyter notebook! ``` jupyter notebook```
4. The Jupyter notebook should open in your browser. Open the file `patcat.ipynb` and run all of the cells. The first run may take longer than expected. You should see the visual output throughout the notebook and at the end.

### Tip for Changing Parameters
To change parameters such as planet name and spacecraft properties, open `config.py` in the same Jupyter browser window and make edits on the spot. When you finish, make sure to save and **restart the patcat.ipynb kernel* in order to see your changes reflected in the program.

## How to Use 
### Understanding the System
   The spacecraft is modeled as a rectangular prism defined by three user-provided dimensions. *The direction of motion is always defined as the positive y direction in a right-handed coordinate system.* Rotations about the x and z axes are defined counter-clockwise with respect to the positive y-axis, and rotation about the y axis is irrelevant to the program but included for the sake of thoroughness. 
### Parameters in config.py
   The parameters listed below should be changed in config.py by the user to fit the problem.
   * `altitude_step_size`: int; km; describes the desired step size in cubic spline interpolation
   * `torque_plot_scale`: str; usually 'log' or 'linear'; describes the desired type of scaling in matplotlib for torque plot
   * `dimensions`: list of floats; meters; [x, y, z] dimensions of spacecraft, set to None for default Cassini-like
   * `rotx`: float; degrees; counterclockwise rotation about the x-axis with respect to the positive y-axis
   * `roty`: float; degrees; counterclockwise rotation about the y-axis, reference is irrelevant
   * `rotz`: float; degrees; counterclockwise rotation about the z-axis with respect to the positive y-axis
   * `thruster_force`: float; newtons; describes maximum force the thrusters provide
   * `thruster_lev_arm`: float; meters; distance between thrusters and center of mass
   * `speed: float`; meters/second; s/c speed
   * `direction: float`; radians; angle between direction of s/c motion and planet's spin (direction of atmosphere's motion)
   * `atmos_lever_arm`: list of floats; meters; vector representation of s/c lever arm (center of mass to center of pressure) when spacecraft's rotation is 0; set to None for Cassini-like
   * `name`: str; name of planet or moon in lowercase
   * `ignore_rotation`: boolean; true if user desires to ignore atmospheric rotation, false assumes solid-body rotation of atmosphere with planet
   * `wind_speed`: float; meters/second; self-explanatory 
   * `wind_direction`: float; radians; angle between direction of wind motion and direction of spacecraft motion
   * `drag coefficient`: float; dimensionless; usually 2.1, can sometimes be 2.06 or 2.07 depending on s/c model
### Adding New Planets/Atm. Density Profiles
PATCaT has atmospheric density profiles for Saturn, Titan, and Uranus built-in. Each atmospheric density profile has its own function to read in data because they are all different. It is easy to add new planets/moons using the following steps:
1. Upload an atmospheric density profile for the desired planet to the PATCaT directory. It should include altitude and density.
2. In the atmos_importer.py file, create a new function to read in the atmospheric density profile that you uploaded. Convention is to name the function `planetname_atmos()` (Jupiter example: `jupiter_atmos()`). The function should not take in any arguments. It should read in the file and return two lists of equal length: altitudes and densities (all float values), that contain data points representing altitude (km from the 1-bar level) and density (kg/m^3) at different points in the atmosphere. It should not matter if altitude goes from low to high or vice versa. This function will probably look similar to the existing atmosphere reading files except for a few small changes in parsing the data.
3. In the atmos_importer.py file, make the following additions:
    1. In the `get_atmos()` function, add your planet and the new function you just created to the dictionary `atmos_dict` using lowercase letters for the new dictionary key. For example, if adding the planet Jupiter, you may add the following item to the dictionary: `'jupiter': jupiter_atmos`. 
    2. In the `get_bar_radius()` function, add your new planet and its corresponding equatorial radius (km) at the 1-bar level to the dictionary titled `equatorial_radii`. This will be used to adjust the spacecraft's velocity due to atmospheric rotation later on. For example, for Jupiter, you might add to the dictionary `'jupiter': 71492`. If the altitude values in your atmospheric density profile are already measured from the center of the planet, add 0.
    3. In the `get_angular_velocity()` function, add your new planet and its corresponding day length (hours) to the dictionary `day_lengths_hours`. This dictionary contains the amount of time it takes for each planet to complete one full rotation (one day) and is used later on to calculate atmospheric rotation. For example, for Jupiter, you might add to the dictionary `'jupiter': 10.0` since a day on Jupiter is 10 hours long.
4. Now that you have made these changes, you can simply change the planet name in config.py to your new planet in lowercase (ex. 'jupiter') and run the program with your new atmospheric density profile! 


## Credits
### Atmospheric Density Profile Sources
* Uranus: provided by Dr. Julie Moses of SSI in July 2023, her file designation pzuran15lat3n.out
* Titan: "eyeballed" from Sarani et al. by Shaya, only has 5 data points and is really just meant for testing/validating estimations.
* Saturn: provided by Damon Landau, originally sourced from Langley Research Center based on edl_traj_161024_DAC1_LaRC_MC_v2 Nominal Atmosphere
  
### References
+ Sarani, S., “Titan Atmospheric Density Reconstruction Using Cassini Guidance, Navigation, and Control Data,” Paper AIAA-
2009-5763, Proceedings of the AIAA Guidance, Navigation, and Control Conference and Exhibit, Chicago, Illinois, USA, August 10-13, 2009. 
+ Burk, T.A., “Cassini at Saturn Proximal Orbits – Attitude Control Challenges,” Paper AIAA-2013-4710, Proceedings of the
AIAA Guidance, Navigation, and Control Conference and Exhibit, Boston, Massachusetts, USA, August 19-22, 2013.
+ Andrade, L. G., "Skimming through Saturn’s Atmosphere: The Climax of the Cassini Grand Finale Mission," Paper AIAA-Sci-Tech Forum, 2018 AIAA Guidance, Navigation, and Control Conference

### Acknowledgements
* Mark Hofstadter
* Reza Karimi
* Damon Landau
* Dylan Wilbur
