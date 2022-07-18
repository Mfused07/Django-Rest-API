# Response class (this python obj will take in any data or already serialzed data passed to it and we will render it out as json data)
from rest_framework.response import Response

# need api_vew because we will use function based views 
from rest_framework.decorators import api_view

# import Item model
from base.models import Item

# class to serialize data
from .serializers import Itemserializer

# out first view get Data


@api_view(['GET'])
def getData(request):
    # this person dict passed in Response(person) will output a  json
    # person = {
    #     'name' : 'Mubashir',
    #     'age' : '23',
    #     'role' : 'Software Engineer'
    # }
    items = Item.objects.all()
    serializer = Itemserializer(items, many = True)

    return Response(serializer.data)


# add Item and serialize it and check if its valid then add it to database
@api_view(['POST'])
def addItem(request):
     serialzer =  Itemserializer(data = request.data)
     if serialzer.is_valid():
        serialzer.save()
     return Response(serialzer.data)
# need end-point to see what it outputs -> go url.py file