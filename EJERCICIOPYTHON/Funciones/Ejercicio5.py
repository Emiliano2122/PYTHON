def circle_area(radius):
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    return circle_area(radius)*high
print(cilinder_volume(3,5))