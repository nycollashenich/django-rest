from app.models import Tod
from app.serializers import TodSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def tod_list(request):
    if request.method == 'GET':    
        tod = Tod.objects.all()
        serializer = TodSerializer(tod, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
