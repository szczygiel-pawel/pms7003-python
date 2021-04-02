#!/usr/bin/env python3

from pms7003 import PMS7003


if __name__ == "__main__":
    sensor = PMS7003('/dev/ttyUSB0')
    output = sensor.read()
    if output:
        print("PM1.0 concentration: %d ug/m3 (corrected to standard conditions)" % output["pm010_std"])
        print("PM2.5 concentration: %d ug/m3 (corrected to standard conditions)" % output["pm025_std"])
        print("PM10 concentration: %d ug/m3 (corrected to standard conditions)" % output["pm100_std"])
        print("PM1.0 concentration: %d ug/m3 (under atmospheric conditions)" % output["pm010_atm"])
        print("PM2.5 concentration: %d ug/m3 (under atmospheric conditions)" % output["pm025_atm"])
        print("PM10 concentration: %d ug/m3 (under atmospheric conditions)" % output["pm100_atm"])
        print("Number of particles with diameter greater than 0.3 um (in 100 ml of air): %d" % output["part003"])
        print("Number of particles with diameter greater than 0.5 um (in 100 ml of air): %d" % output["part005"])
        print("Number of particles with diameter greater than 1.0 um (in 100 ml of air): %d" % output["part010"])
        print("Number of particles with diameter greater than 2.5 um (in 100 ml of air): %d" % output["part025"])
        print("Number of particles with diameter greater than 5.0 um (in 100 ml of air): %d" % output["part050"])
        print("Number of particles with diameter greater than 10 um (in 100 ml of air): %d" % output["part100"])
    else:
        print("Read error!")
