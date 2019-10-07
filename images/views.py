from django.shortcuts import render,redirect
from .models import Image,Location,Tag,Category
import pyperclip

def index(request):
    '''
    This method will display the home page of the application
    '''
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = "Home"
    context = {
        "title":title,
        "images":images,
        "locations":locations
    }

    return render(request,'index.html',context)

def search_results(request):
    '''
    This method will display the searched results of the user
    '''
    if 'images' in request.GET and request.GET['images']:
        searched_category = request.GET.get('images')
        searched_images = Image.search_image_by_category(searched_category)
        message = f'{searched_category}'
        context = {
            "searched_images":searched_images,
            "message":message
        }
        return render(request,'search.html',context)

    else:
        message = "you have not searched for any term"
        return render(request,'search.html',{"message":message})

def single_image(request,image_id):
    '''
    Display single image
    '''
    try:
        single_image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    title=f'{single_image.image_name}'
    
    return render(request,"image.html", {"title":title,"image":single_image})

def filter_location(request):
    if 'location' in request.GET and request.GET['location']:
        filterd_location = request.GET.get('location')
        found_images = Image.filter_by_location(filterd_location)
        message = f'{filterd_location}'
        locations = Location.objects.all()
        context = {
            "found_images":found_images,
            "message":message,
            "locations":locations
        }
        return render(request,'location.html',context)
    else:
        locations = Location.objects.all()
        message = "No selection made"
        context = {
            "message":message,
            "locations":locations
        }
        return render(request,'location.html',context)