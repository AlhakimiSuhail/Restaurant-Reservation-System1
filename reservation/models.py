from django.db import models

class LoginCredentials(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.BooleanField()

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    login = models.ForeignKey(LoginCredentials, on_delete=models.CASCADE, default=None)
    ##image = models.ImageField()

class Table(models.Model):
    restaurantName = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None)
    twoSeats = models.IntegerField()
    fourSeats = models.IntegerField()
    sixSeats = models.IntegerField()
    eightSeats = models.IntegerField()

class userReservationInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    userName = models.ForeignKey(LoginCredentials, on_delete=models.CASCADE, default=None)
    restaurantName = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None)
    reservationTime = models.CharField(max_length=200)
    reservationDate = models.CharField(max_length=200)
    partySize = models.IntegerField()
