import time
import ephem
from datetime import datetime
from math import pi
from constants import RA_CHANGE_AVERAGE, DEC_CHANGE_AVERAGE


class Moon:
    def __init__(self):
        self.start_date = datetime.now()
        moon = ephem.Moon()
        moon.compute(self.start_date)
        self.dec_from_ephem = moon.dec / pi * 180.0
        self.list_ra = str(moon.ra).split(":")
        self.ra_from_ephem = float(self.list_ra[0]) * 3600 + float(self.list_ra[1]) * 60 + float(self.list_ra[2])
        self.start_ra = self.ra_from_ephem
        self.start_dec = self.dec_from_ephem

    def computing_the_coordinates(self):
        counter = 0
        if counter % 10 == 0 and counter != 0:
            self.start_ra += 0.35

        self.start_ra += RA_CHANGE_AVERAGE
        self.start_dec += DEC_CHANGE_AVERAGE

        result_ra = f'{int(self.start_ra // 3600)}:{int((self.start_ra % 3600) // 60)}:' \
                    f'{round(float((self.start_ra % 3600) % 60), 2)}'

        moon = {'ra': result_ra,
                'dec': self.start_dec
                }
        counter += 1
        return moon


if __name__ == '__main__':
    while True:
        moon_obj = Moon()
        print(moon_obj.computing_the_coordinates())
        time.sleep(1)





