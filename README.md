# Python library for PMS7003 sensor

## Dependencies 
This software requires `pyserial` library. 

Installation: `pip3 install -r requirements.txt` or `pip3 install pyserial`.

## Quick start
1. Download this repository and copy the `pms7003.py` file to your project directory.
2. Import the module: `from pms7003 import PMS7003`
3. Create a new object: `sensor = PMS7003('/dev/ttyUSB0')`
    >**Note:**  Depending on number of connected devices and used operating system PMS7003 may be labeled differently e.g. `ttyUSB1`, `COM0`, `COM1`, etc. 
4. Read data: `sensor.read()`

## Output data format
The `read()` function returns a dictionary with the following set of keys:
* `pm010_std` - PM1.0 concentration in μg/m3 (corrected to standard conditions)
* `pm025_std` - PM2.5 concentration in μg/m3 (corrected to standard conditions)
* `pm100_std` - PM10 concentration in μg/m3 (corrected to standard conditions)
* `pm010_atm` - PM1.0 concentration in μg/m3 (under atmospheric conditions)
* `pm025_atm` - PM2.5 concentration in μg/m3 (under atmospheric conditions)
* `pm100_atm` - PM10 concentration in μg/m3 (under atmospheric conditions)
* `part003` - number of particles with diameter greater than 0.3 μm (in 100 ml of air)
* `part005` - number of particles with diameter greater than 0.5 μm (in 100 ml of air)
* `part010` - number of particles with diameter greater than 1.0 μm (in 100 ml of air)
* `part025` - number of particles with diameter greater than 2.5 μm (in 100 ml of air)
* `part050` - number of particles with diameter greater than 5.0 μm (in 100 ml of air)
* `part100` - number of particles with diameter greater than 10 μm (in 100 ml of air)

>**Note:** The datasheet recommends to use *data corrected to standard conditions* in industrial environment.

>**Note:** Data labeled as *under atmospheric conditions* are not corrected due to atmospheric pressure.
> It means that even with a constant number of PM particles in the air the readout may vary if the atmospheric pressure changes. 

## Example 1
```python
#!/usr/bin/env python3

from pms7003 import PMS7003


sensor = PMS7003('/dev/ttyUSB0')
output = sensor.read()
if output:
    print(output)
else:
    print("Read error!")

```
**Example output:**
```
{'pm010_std': 11, 'pm025_std': 11, 'pm100_std': 17, 'pm010_atm': 11, 'pm025_atm': 11, 'pm100_atm': 17, 'part003': 219, 'part005': 50, 'part010': 38, 'part025': 6, 'part050': 6, 'part100': 4}
```

## Example 2
```python
#!/usr/bin/env python3

from pms7003 import PMS7003


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

```
**Example output:**
```
PM1.0 concentration: 2 ug/m3 (corrected to standard conditions)
PM2.5 concentration: 3 ug/m3 (corrected to standard conditions)
PM10 concentration: 3 ug/m3 (corrected to standard conditions)
PM1.0 concentration: 2 ug/m3 (under atmospheric conditions)
PM2.5 concentration: 3 ug/m3 (under atmospheric conditions)
PM10 concentration: 3 ug/m3 (under atmospheric conditions)
Number of particles with diameter greater than 0.3 um (in 100 ml of air): 159
Number of particles with diameter greater than 0.5 um (in 100 ml of air): 189
Number of particles with diameter greater than 1.0 um (in 100 ml of air): 12
Number of particles with diameter greater than 2.5 um (in 100 ml of air): 2
Number of particles with diameter greater than 5.0 um (in 100 ml of air): 0
Number of particles with diameter greater than 10 um (in 100 ml of air): 0
```