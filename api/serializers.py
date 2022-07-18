# in this file we gona need to create model serializer cz the Response() obj cannot handle
# complex data types such as django model instances so we First Serialize the Data
# before we render it out 

# 1- we will create serializer for out item model and this will convert instancexs of our items from objects into data 
# type the response obj can understand

from rest_framework import serializers
from base.models import Item

# item serializer inherit from model serializer
class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'