from .models import *


def createTestRestaurant() -> list():
    restaurantList = []
    for i in range(18):
        restaurant = Restaurant()
        restaurant.name = "Restaurant " + str(i)
        restaurant.location = str(i) + " Test street"
        restaurant.description = "Qui excepteur sunt consequat elit ad dolor cillum mollit deserunt incididunt magna mollit."
        restaurantList.append(restaurant)
    return restaurantList


