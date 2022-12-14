import board
import analogio
import simpleio

class Throttle(object):
    """Throttle"""
    def __init__(self, adc_pin, min = 65535/2, max = 65535):
        """Throttle
        :param ~microcontroller.Pin adc_pin: ADC pin used for throttle
        :param int min: the min ADC value (should be a little higher than throttle lowest value)
        :param max min: the max ADC value, usually 65535. Defaults to 65535.
        """
        # configure ADC input for throttle signal
        self.__adc_throttle = analogio.AnalogIn(adc_pin)
        self.__min = min
        self.__max = max

    def read_adc(self):
        """Read the throttle ADC value
        return: throttle ADC value
        """
        return self.__adc_throttle.value

    @property
    def value(self):
        """Read the throttle
        return: throttle [0 - 1000]
        """
        # map throttle to 0 --> 1000
        throttle = simpleio.map_range(self.__adc_throttle.value, self.__min, self.__max, 0, 1000)
        return throttle
