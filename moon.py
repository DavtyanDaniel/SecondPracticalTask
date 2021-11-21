import time
import ephem
from datetime import datetime, timedelta
from math import pi
from constants import RA_CHANGE_AVERAGE, DEC_CHANGE_AVERAGE


def moon_coordinates_from_ephem(date: datetime) -> tuple:
    moon = ephem.Moon()
    moon.compute(date)
    moon_dec_in_angles = moon.dec / pi * 180
    list_ra = str(moon.ra).split(":")
    moon_ra_in_seconds = float(list_ra[0]) * 3600 + float(list_ra[1]) * 60 + float(list_ra[2])
    moon_coordinates = (moon_ra_in_seconds, moon_dec_in_angles)
    return moon_coordinates


def moon_is_going_up(date: datetime) -> bool:
    moon = ephem.Moon()
    moon.compute(date)
    moon_dec_in_angles1 = moon.dec / pi * 180.0
    moon.compute(date + timedelta(seconds=20))
    moon_dec_in_angles2 = moon.dec / pi * 180.0
    if moon_dec_in_angles2 - moon_dec_in_angles1 > 0:
        return True
    else:
        return False


def manual_moon_coordinates_calculation(ra, dec, is_moon_going_up) -> tuple:
    ra = module_sum(ra, RA_CHANGE_AVERAGE, int(timedelta(days=24).total_seconds()))
    if is_moon_going_up:
        dec = dec + (10 * DEC_CHANGE_AVERAGE) + 0.35
    else:
        dec = dec - (10 * DEC_CHANGE_AVERAGE) - 0.35
    moon = ra, dec
    return moon


def module_sum(number1, number2, module) -> float:
    if number1 + number2 > module:
        return (number1 + number2) % module
    else:
        return number1 + number2


def ra_dec_transformer(ra_in_seconds, dec_in_angles):
    ra_res = f'{int(ra_in_seconds // 3600)}:{int((ra_in_seconds % 3600) // 60)}:' \
             f'{round(float((ra_in_seconds % 3600) % 60), 5)}'
    dec_res = f'{round(float(dec_in_angles), 4)}'
    return {'RA': ra_res,
            'DEC': dec_res}


if __name__ == "__main__":
    moon_coordinates1 = moon_coordinates_from_ephem(datetime.now())
    is_moon_going_up = moon_is_going_up(datetime.now())
    tt = manual_moon_coordinates_calculation(*moon_coordinates1, is_moon_going_up)
    print(tt)
    while True:
        tt = manual_moon_coordinates_calculation(*tt, is_moon_going_up)
        print(tt)
        time.sleep(1)






