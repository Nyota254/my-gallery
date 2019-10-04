from django.shortcuts import render

def index(request):
    '''
    This method will display the home page of the application
    '''
    title = "Home"
    context = {
        "title":title
    }

    return render(request,'index.html',context)
