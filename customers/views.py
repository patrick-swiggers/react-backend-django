from django.http import JsonResponse
from customers.models import Customer
from customers.serializers import CustomerSerializer

def customers(request):
    # invoke serializer and return new client
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many = True)
    return JsonResponse({'customers': serializer.data})

def customer(request,id):
    data = Customer.objects.get(pk=id)
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})
