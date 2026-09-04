from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import generics, request
from bookings.serializers import BookingsSerializer
from rest_framework.permissions import IsAuthenticated

from bookings.models import Booking
from rest_framework.views import APIView

from bookings.permissions import IsCustomerOnly


# Create your views here.
# class BookingAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookingsSerializer(data=request.data)
#
#     if serializer.is_valid():
#         event = serializer.validated_data['event']
#         seats = serializer.validated_data['seats']
#
#         amount = event.price * seats
#         u = request.user
#
#         serializer.save(user=u,amount=amount)

class BookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsCustomerOnly]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        seats = serializer.validated_data['seats']
        amount = event.price * seats
        u = self.request.user
        serializer.save(user=u,amount=amount)