from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to render the index page """
    return render(request, 'index.html')


def about_us(request):
    """ A view to render the About Us page """
    return render(request, 'about-us.html')
