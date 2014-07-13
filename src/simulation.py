# STARTUP (Don't edit, typically)
from __future__ import division
from visual import *
import base as physutil
import csv
import sys

# CLASS FOR THE FUNCTIONS FOR THE MOVEMENT OF THE PLANETS
# =======================================================

def gravity(position, velocity, mass, position2): #This is the main function for computing the gravity
    G=6.67E-11
    dist=position - position2
    dist_squared = (mag(dist)*mag(dist))

    Fg = ((-G*mass*sun.m)/(dist_squared))*norm(dist)
    velocity = velocity + (Fg/mass)*deltat
    return(velocity)


def keyInput(evt): #This is the function for zooming into the planets
    s = evt.key
    rate(5)
    if s == "e":
        scene.center = earth.pos
        scene.range = 1E11
    elif s == "p":
        scene.center = pluto.pos
        scene.range = 5E10

# INITIALIZATION ELEMENTS
# =================================
text = raw_input("Enter 1 if you wish to see the inner Solar System. \nIf you wish to see the outer Solar System, enter 2.\n")


if text=="1":
    rangeint =  3E11
    sunsize = 6.955E9
    deltatime = 3600
    maxtime = 60*60*24*688

elif text =="2":
    rangeint = 8E12
    sunsize = 6.955E10
    deltatime = 864000
    maxtime = 864000 * 36.5 * 250

else:
    sys.exit()



# VISUALIZATION & GRAPH SETUP
# ===========================================
# Setup Display window for visualization
scene = display(width = 800, height = 750, background = color.black, title = "The Solar System", range=rangeint, center = vector(0,0,0))

# Create objects for visualization

# Other Bodies
pluto = sphere(color = color.red, radius=1.195E8)
halleys_comet = sphere(color = color.red, radius=1E8)
# Just Planets
neptune = sphere(color = color.blue, radius=2.476E9)
uranus = sphere(color = color.cyan, radius=2.55E9)
saturn = sphere(color = color.orange, radius=6.026E9)
jupiter = sphere(color = color.red, radius=7.149E9)
mars = sphere(color = color.orange, radius=1.693E9)
earth = sphere(color = color.blue, radius=3.185E9)
venus = sphere(color = color.orange, radius=3.025E9)
mercury = sphere(color = color.red, radius=1.220E9)
sun = sphere(color = color.yellow, radius=sunsize)
# Create a trail behind the object as it moves
trail_halleys_comet = curve(color = color.white)
trail_pluto = curve(color = color.white)
trail_neptune = curve(color = color.red)
trail_uranus = curve(color = color.green)
trail_saturn = curve(color = color.yellow)
trail_jupiter = curve(color = color.cyan)
trail_mars = curve(color = color.magenta)
trail_earth = curve(color = color.green)
trail_venus = curve(color = color.red)
trail_mercury = curve(color = color.blue)
# Create sphere to mark the origin in Display window
origin = sphere(pos=vector(0,0,0), color = color.black)



# SYSTEM PROPERTIES AND DATA
# ===========================================
# Other bodies
pluto.m = 1.31E22
halleys_comet.m = 2.2E14
#Masses of Planets
neptune.m = 1.0242E26
uranus.m = 8.6816E25
saturn.m = 5.683E26
jupiter.m = 1.898E27
mars.m = 6.39E23
earth.m = 5.972E24
venus.m = 4.86732E24
mercury.m = 3.285E23
sun.m = 1.989E30

#Positions of the Planets (nearest position; perihelion)
halleys_comet.pos = vector(87664352200,0,0)
pluto.pos = vector(-4436820000000,0,0)
neptune.pos = vector(0,4444450000000,0)
uranus.pos = vector(2741300000000,0,0)
saturn.pos = vector(0,-1352550000000,0)
jupiter.pos = vector(-740520000000,0,0)
mars.pos = vector(0,-206669000000,0)
earth.pos = vector(147098290000, 0, 0)
venus.pos = vector(0,107477000000,0)
mercury.pos = vector(-46001200000,0,0)
sun.pos = vector(0,0,0)

#Velocities of the Planets (fastest velocity)
halleys_comet.vel = vector(0,54000,0)
pluto.vel = vector(0,-6100,0)
neptune.vel = vector(-5500,0,0)
uranus.vel = vector(0,7110,0)
saturn.vel = vector(10180,0,0)
jupiter.vel = vector(0,-13720,0)
mars.vel = vector(26500,0,0)
earth.vel = vector(0,30290,0)
venus.vel = vector(-35260,0,0)
mercury.vel = vector(0,58980,0)
sun.vel = vector(0,0,0)

#Initial Aphelions
aphelion_halleys_comet = 0
aphelion_pluto = 0
aphelion_neptune = 0
aphelion_uranus = 0
aphelion_saturn = 0
aphelion_jupiter = 0
aphelion_mars = 0
aphelion_earth = 0
aphelion_venus = 0
aphelion_mercury =0


#Specify time interval between imported data points
# ===========================================
deltat = deltatime #one hour in seconds

#Specify time for first observation data point; Default choice, time t=0
# ===========================================
t = 0



# CALCULATION LOOP (Calculate Positions)
# ======================================================
while t < maxtime:  #iterate over data values
##    halleys_comet.vel = gravity(halleys_comet.pos, halleys_comet.vel, halleys_comet.m, sun.pos)
##    halleys_comet.pos = halleys_comet.pos + (pluto.vel*deltat)
##    trail_halleys_comet.append(pos = halleys_comet.pos)

    pluto.vel = gravity(pluto.pos, pluto.vel, pluto.m, sun.pos)
    pluto.pos = pluto.pos + (pluto.vel*deltat)
    trail_pluto.append(pos = pluto.pos)

    neptune.vel = gravity(neptune.pos, neptune.vel, neptune.m, sun.pos)
    neptune.pos = neptune.pos + (neptune.vel*deltat)
    trail_neptune.append(pos = neptune.pos)

    uranus.vel = gravity(uranus.pos, uranus.vel, uranus.m, sun.pos)
    uranus.pos = uranus.pos + (uranus.vel*deltat)
    trail_uranus.append(pos = uranus.pos)

    saturn.vel = gravity(saturn.pos, saturn.vel, saturn.m, sun.pos)
    saturn.pos = saturn.pos + (saturn.vel*deltat)
    trail_saturn.append(pos = saturn.pos)

    jupiter.vel = gravity(jupiter.pos, jupiter.vel, jupiter.m, sun.pos)
    jupiter.pos = jupiter.pos + (jupiter.vel*deltat)
    trail_jupiter.append(pos = jupiter.pos)

    mars.vel = gravity(mars.pos, mars.vel, mars.m, sun.pos)
    mars.pos = mars.pos + (mars.vel*deltat)
    trail_mars.append(pos = mars.pos)

    earth.vel = gravity(earth.pos, earth.vel, earth.m, sun.pos)
    earth.pos = earth.pos + (earth.vel*deltat)
    trail_earth.append(pos = earth.pos)

    venus.vel = gravity(venus.pos, venus.vel, venus.m, sun.pos)
    venus.pos = venus.pos + (venus.vel*deltat)
    trail_venus.append(pos = venus.pos)

    mercury.vel = gravity(mercury.pos, mercury.vel, mercury.m, sun.pos)
    mercury.pos = mercury.pos + (mercury.vel*deltat)
    trail_mercury.append(pos = mercury.pos)

        
    if mag(halleys_comet.pos) > aphelion_halleys_comet:
        aphelion_halleys_comet = mag(halleys_comet.pos)

    if mag(pluto.pos) > aphelion_pluto:
        aphelion_pluto = mag(pluto.pos)

    if mag(neptune.pos) > aphelion_neptune:
        aphelion_neptune = mag(neptune.pos)

    if mag(uranus.pos) > aphelion_uranus:
        aphelion_uranus = mag(uranus.pos)

    if mag(saturn.pos) > aphelion_saturn:
        aphelion_saturn = mag(saturn.pos)

    if mag(jupiter.pos) > aphelion_jupiter:
        aphelion_jupiter = mag(jupiter.pos)

    if mag(mars.pos) > aphelion_mars:
        aphelion_mars = mag(mars.pos)

    if mag(earth.pos) > aphelion_earth:
        aphelion_earth = mag(earth.pos)

    if mag(venus.pos) > aphelion_venus:
        aphelion_venus = mag(venus.pos)

    if mag(mercury.pos) > aphelion_mercury:
        aphelion_mercury = mag(mercury.pos)

    t = t + deltat


    rate(1000)
    print(t)

    #EDIT THIS: to print out desired quantities

print(aphelion_halleys_comet, aphelion_pluto, aphelion_neptune, aphelion_uranus, aphelion_saturn, aphelion_jupiter, aphelion_mars, aphelion_earth, aphelion_venus, aphelion_mercury)

