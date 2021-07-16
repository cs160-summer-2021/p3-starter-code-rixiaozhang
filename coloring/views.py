from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

# You'll have to update coloring/views.py to create a function for each route 
# and coloring/urls.py to update views.index to the appropriate new functions you created.

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def gallery(request):
    return render(request, 'coloring/gallery.html')

def triangles(request):
    return render(request, 'coloring/triangles.html')

def mandala_simple(request):
    return render(request, 'coloring/mandala_simple.html')
