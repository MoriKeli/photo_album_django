from django.shortcuts import render, redirect
from django.contrib import messages

from album.models import UploadedImages
from album.forms import UploadForm

def homepage(request):
    images = UploadedImages.objects.all()

    context = {'uploaded_images': images}

    return render(request, 'homepage.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully.')
            return redirect('user_homepage')
    else:
        form = UploadForm()
    return render(request, 'upload_page.html', {'form': form})

def delete_image(request, pk):
    image = UploadedImages.objects.get(id=pk)
    
    if request.method == 'POST':
        image.delete()
        return redirect('user_homepage')
    
    return render(request, 'delete.html', {'delete': image})
