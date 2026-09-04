from rest_framework import serializers

from bookings.models import Booking


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

        read_only_fields = ('amount','status','created_at','user')
