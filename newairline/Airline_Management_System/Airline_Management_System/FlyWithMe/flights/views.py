from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Flight
from .forms import FlightForm,MyLoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def landing_page(request):
    return render(request, 'landing_page.html')


def flight_list(request):
    search_id = request.GET.get('search_id', '')
    if search_id:
        flights = Flight.objects.filter(flight_id__icontains=search_id)
    else:
        flights = Flight.objects.all()

    return render(request, 'flights/flight_list.html', {'flights': flights, 'search_id': search_id})


def search_flight(request):
    if request.method == 'GET':
        query = request.GET.get('flight_id')
        flight = Flight.objects.filter(flight_id=query).first()
        return render(request, 'flights/search_result.html', {'flight': flight})


def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flights/add_flight.html', {'form': form})


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flights/edit_flight.html', {'form': form})


def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'flights/delete_flight.html', {'flight': flight})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('flight_list')  # Redirect to flight list or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'flights/login.html', {'form': form})