from django.shortcuts import render
from .models import Image,Location,Tag,Category

def index(request):
    '''
    This method will display the home page of the application
    '''
    images = Image.get_all_images()
    title = "Home"
    context = {
        "title":title,
        "images":images
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