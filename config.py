
altitude_step_size = 1
torque_plot_scale = 'log'
sc = dict(
    dimensions = None, #meters
    rotx = 0, #degrees CCW from positive y-axis
    roty = 0, #degrees CCW (reference doesn't matter)
    rotz = 0, #degrees CCW from positive y-axis
    thruster_force = 0.9, #newtons
    thruster_lev_arm = 1.2, #meters
    speed = 14868.0, #meters/second #saturn 10000, uranus 14868, titan 5999
    direction = 0.0, #radians from direction of atmospheric motion assuming solid-body rotation
    atmos_lev_arm = [0, 0, 1], #meters
)
planet = dict(
    name = 'uranus',
    ignore_rotation = True, #ignore atmospheric (solid-body) rotation 
    wind_speed = 0.0,  #meters per second
    wind_direction = 0.0, #radians, wind movement relative to s/c velocity
    drag_coeff = 2.1 #dimensionless
)
