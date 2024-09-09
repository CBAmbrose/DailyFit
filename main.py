#Program that relays weather information to create a potential outfit.

from weather import getTemp
from outfitfit import layers

class main:
    current_temp = getTemp()
    fit = layers(current_temp)
    print("Temperature Outside is", current_temp)
    print("The Fit is:\n", fit)

