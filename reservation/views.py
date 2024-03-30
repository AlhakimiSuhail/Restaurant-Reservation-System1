from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .dummy import *
from datetime import date, datetime

def index(request):
    if 'login' in request.POST:
        try:
            account = LoginCredentials.objects.get(email=request.POST.get('loginEmail'))
            request.session['name'] = account.name
            request.session['accountEmail'] = account.email
            request.session['isRestaurant'] = not account.type
            if(not account.type):
                restaurant = Restaurant.objects.get(login=account)
                request.session['restaurantName'] = restaurant.name

            if account.password == request.POST.get('loginPassword'):
                if account.type == True:
                    return redirect(homepage_user)
                else:
                    return redirect(homepage_restaurant)
            else:
                return render(request, 'reservation/index.html', {'loginFailure': True})
        except:
            return render(request, 'reservation/index.html', {'loginFailure': True})
        
    if 'register' in request.POST:
        if request.POST.get('registerPassword') == request.POST.get('registerPassword2') and not LoginCredentials.objects.filter(email=request.POST.get('registerEmail')).exists():
            new_account = LoginCredentials()
            new_account.name = request.POST.get('fullName')
            new_account.email = request.POST.get('registerEmail')
            new_account.password = request.POST.get('registerPassword')
            new_account.type = True if request.POST.get('registerType') == 'patron' else False
            new_account.save()
            if(not new_account.type):
                new_restaurant = Restaurant()
                new_restaurant.login = new_account
                new_restaurant.name = request.POST.get("restaurantName")
                new_restaurant.description = request.POST.get("restaurantDescription")
                new_restaurant.location = request.POST.get("restaurantLocation")
                new_restaurant.save()
                new_table = Table()
                new_table.restaurantName = new_restaurant
                new_table.twoSeats = 0
                new_table.fourSeats = 0
                new_table.sixSeats = 0
                new_table.eightSeats = 0
                new_table.save()
            return render(request, 'reservation/index.html', {'registerComplete': True})
        else:
            return render(request, 'reservation/index.html', {'registerWarning': True})

    return render(request, 'reservation/index.html')

def homepage_user(request):
    return render(request, 'reservation/user_homepage.html', {'restaurants': Restaurant.objects.exclude(name='').exclude(location='').exclude(description='')})
    ##return render(request, 'reservation/user_homepage.html', {'restaurants': createTestRestaurant()})

def homepage_restaurant(request):
    login = LoginCredentials.objects.get(email=request.session['accountEmail'])
    restaurant = Restaurant.objects.get(login=login)
    today = date.today()
    d3 = today.strftime("%Y-%m-%d")
    print(d3)
    reservations = userReservationInfo.objects.filter(restaurantName=restaurant).filter(reservationDate = d3)
    
    return render(request, 'reservation/restaurant_homepage.html', {'userReservations': reservations})

def table_management(request):
    print(request.POST)
    login = LoginCredentials.objects.get(email=request.session['accountEmail'])
    restaurant = Restaurant.objects.get(login=login)
    table = Table.objects.get(restaurantName=restaurant)
    if("tableSave" in request.POST):
        table.twoSeats = request.POST.get("twoSeat")
        table.fourSeats = request.POST.get("fourSeat")
        table.sixSeats = request.POST.get("sixSeat")
        table.eightSeats = request.POST.get("eightSeat")
        table.save()
    twoSeat = table.twoSeats
    fourSeat = table.fourSeats
    sixSeat = table.sixSeats
    eightSeat = table.eightSeats
    return render(request, 'reservation/table_management.html', {'twoSeat': twoSeat, 'fourSeat': fourSeat, 'sixSeat': sixSeat, 'eightSeat': eightSeat})

def User_Reservations(request):
    login = LoginCredentials.objects.get(email=request.session['accountEmail'])
    reservations = userReservationInfo.objects.filter(userName=login)
    return render(request, 'reservation/User_Reservations.html', {'userReservations': reservations})

def delete_reservation(request, pk):
    reservation = userReservationInfo.objects.filter(id = pk)
    if reservation:
        reservation.delete()
    return redirect(homepage_restaurant)

def user_delete_reservation(request, pk):
    reservation = userReservationInfo.objects.filter(id = pk)
    if reservation:
        reservation.delete()
    return redirect(User_Reservations)

def create_reservation_times(request):
    numberOfReservations = request.POST.get('numberOfReservations')
    print(numberOfReservations)
    number = int(numberOfReservations) if True else 1
    for i in range(number):
        reservation = userReservationInfo()
        login = LoginCredentials.objects.get(email=request.session['accountEmail'])
        reservation.userName = login
        reservation.restaurantName = Restaurant.objects.get(login=login)
        reservation.reservationDate = request.POST.get('startDate')
        reservation.reservationTime = request.POST.get('appt')
        reservation.partySize = request.POST.get('selectPartySize')
        reservation.save()
    return redirect(homepage_restaurant)

def create_reservation_user_times(request):
    login = LoginCredentials.objects.get(email=request.session['accountEmail'])
    restaurantId = request.POST.get('restaurantId')
    restaurant = Restaurant.objects.get(pk=restaurantId)
    ##reservationTime =datetime.strptime(request.POST.get('appt'), '%H:%M').time()
    ##print(reservationTime)
    reservationAtRestaurant = userReservationInfo.objects.filter(restaurantName=restaurant).filter(reservationDate=request.POST.get('startDate'))
    reservationAtRestaurant = reservationAtRestaurant.filter
    reservation = userReservationInfo()
    reservation.userName = login
    reservation.restaurantName = restaurant
    reservation.reservationDate = request.POST.get('startDate')
    reservation.reservationTime = request.POST.get('appt')
    reservation.partySize = request.POST.get('selectPartySize')
    reservation.save()
    return redirect(User_Reservations)