from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import *
from datetime import date

class flights_view(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

class bookings_view(ListAPIView):
	queryset = Booking.objects.filter(date__gte = date.today())
	serializer_class = BookingSerializer
