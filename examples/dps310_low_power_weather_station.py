# configure the sensor for continuous measurement for a
# low power weather station as recommended in the datasheet:
# https://www.infineon.com/dgdl/Infineon-DPS310-DS-v01_00-EN.pdf)

# (disable pylint warnings for adafruit_dps310.{SampleCount,Rate,Mode}.*
# as they are generated dynamically)
# pylint: disable=no-member

import time
import board
import busio
import adafruit_dps310

i2c = busio.I2C(board.SCL, board.SDA)

dps310 = adafruit_dps310.DPS310(i2c)

dps310.reset()
dps310.pressure_oversample_count = adafruit_dps310.SampleCount.COUNT_2
dps310.pressure_rate = adafruit_dps310.Rate.RATE_1_HZ
dps310.temperature_oversample_count = adafruit_dps310.SampleCount.COUNT_16
dps310.temperature_rate = adafruit_dps310.Rate.RATE_1_HZ
dps310.mode = adafruit_dps310.Mode.CONT_PRESTEMP
dps310.wait_temperature_ready()
dps310.wait_pressure_ready()

while True:
    print("Temperature = %.2f *C" % dps310.temperature)
    print("Pressure = %.2f hPa" % dps310.pressure)
    print("")
    time.sleep(10.0)
