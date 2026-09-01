from django.shortcuts import render

from events.models import Event
from rest_framework import generics

from events.serializers import EventSerializer

from events.permissions import IsOrganizerOrReadOnly


# Create your views here.

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(organizer=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

