from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Drink
from .serializers import DrinkSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .forms import MyForm
from .models import Drink
from django.views.decorators.csrf import csrf_exempt

"""
<form method="post">
  {% csrf_token %}
    {{form.my_string}}
    <button type="submit">Submit</button>
</form>
"""
@csrf_exempt
def index(request):
    Latitud = Drink.objects.filter(name="LATITUD")[0].description
    Longitud = Drink.objects.filter(name="LONGITUD")[0].description

    Increase = Drink.objects.filter(name="RIGHT")[0].description
    Decrease = Drink.objects.filter(name="LEFT")[0].description

    if request.method == 'POST':



        form = MyForm(request.POST)

        if form.is_valid():
            my_string = form.cleaned_data['my_string']
            Drink.objects.create(name=my_string)
        else:
            form = MyForm()
    
    context = {"Latitud": Latitud, "Longitud":Longitud, "left":Decrease,"right":Increase}

    return render(request, 'polls/index.html', context)


@csrf_exempt
def update_variable(request):
    # Process data or update variable here
    updated_variable =  Drink.objects.filter(name="LATITUD")[0].description # Replace with your logic
    updated_variable2 =  Drink.objects.filter(name="LONGITUD")[0].description # Replace with your logic

    # Return the updated data as JSON
    return JsonResponse({'updated_variable': updated_variable,'updated_variable2': updated_variable2 })

@csrf_exempt
def update_variable4(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        Increase = data.get('Increase')
        Decrease = data.get('Decrease')
        if Increase=='Increase':
            Water=Drink.objects.filter(name="LEFT")[0]
            Milk=Drink.objects.filter(name="RIGHT")[0]
            Water.description=str(int(Water.description) + 1)
            Water.save()
            return JsonResponse({'Decrease': Water.description, 'Increase':Milk.description })
        elif Increase=="Decrease":
            Water=Drink.objects.filter(name="LEFT")[0]
            Milk=Drink.objects.filter(name="RIGHT")[0]
            Water.description=str(int(Water.description) - 1)
            Water.save()
            return JsonResponse({'Decrease': Water.description, 'Increase':Milk.description })
        
        elif Increase=="IncreaseY":
            Water=Drink.objects.filter(name="LEFT")[0]
            Milk=Drink.objects.filter(name="RIGHT")[0]
            Milk.description=str(int(Milk.description) + 1)
            Milk.save()
            return JsonResponse({'Decrease': Water.description, 'Increase':Milk.description })
        
        else:
            Water=Drink.objects.filter(name="LEFT")[0]
            Milk=Drink.objects.filter(name="RIGHT")[0]
            Milk.description=str(int(Milk.description) - 1)
            Milk.save()
            return JsonResponse({'Decrease': Water.description, 'Increase':Milk.description })
 
def update_variable3(request,):
    Water=Drink.objects.filter(name="LEFT")[0]
    Water.description=str(int(Water.description) - 1)
    Water.save()

    # Process data or update variable here
    Decrease = Drink.objects.filter(name="LEFT")[0].description
    # Return the updated data as JSON
    return JsonResponse({'Decrease': Decrease })


def update_variable2(request,):
    Water=Drink.objects.filter(name="RIGHT")[0]
    Water.description=str(int(Water.description) + 1)
    Water.save()
    Increase = Drink.objects.filter(name="RIGHT")[0].description
    return JsonResponse({'Increase': Increase })

@api_view(['GET','POST'])
def drink_list(request):

    if request.method=='GET':
        drinks=Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data}, safe=False)

    if request.method =='POST':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, satus=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])        
def drink_detail(request,id):
    drink=Drink.objects.get(pk=id)

    """
    try:
        drink=Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    """

    if request.method=='GET':
        serializer=DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    