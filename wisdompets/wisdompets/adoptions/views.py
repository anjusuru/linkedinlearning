from django.shortcuts import render
from .models import Pet
from django.http import Http404


# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets

                                         })


def pet_detail(request,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except pet.DoesNotExist:
        raise Http404('pet does not found')
    return render(request, 'pet_detail.html', {'pet': pet})
