from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Event
from .serializer import EventSerializer

@api_view(['GET',])
def api_event_view(request):
    try:
        obj = Event.objects.all()
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EventSerializer(obj,many=True)
        return Response(serializer.data)

@api_view(['POST',])
def api_event_update_view(request):
    
    obj = Event()

    if request.method == 'POST':
        serializer = EventSerializer(obj,data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)