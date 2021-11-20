import time
import ephem
from datetime import datetime
from math import pi
from constants import RA_CHANGE_AVERAGE, DEC_CHANGE_AVERAGE
from moon import Moon
import constants


def main():
    moon_obj = Moon()
    while True:
        print(moon_obj.computing_the_coordinates())
        time.sleep(1)


if __name__ == '__main__':
    main()


