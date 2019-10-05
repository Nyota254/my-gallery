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
