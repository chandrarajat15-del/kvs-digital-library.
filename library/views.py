from django.shortcuts import render, redirect
from .models import Resource
from django.contrib.auth.decorators import login_required
import datetime

def home(request):
    """The Home page shows the NCERT-style search bar and live time."""
    return render(request, 'library/home.html', {
        'date_now': datetime.datetime.now(),
    })

def search(request):
    """Handles the dropdown search for Class, Subject, and Resource Type."""
    # Getting values from your new NCERT-style dropdowns
    class_val = request.GET.get('class_level')
    subject_val = request.GET.get('subject')
    resource_val = request.GET.get('resource_type')

    results = Resource.objects.all()

    # Apply filters only if the user selected something
    if class_val:
        results = results.filter(class_level=class_val)
    if subject_val:
        results = results.filter(subject__icontains=subject_val)
    if resource_val:
        results = results.filter(resource_type=resource_val)

    return render(request, 'library/search.html', {
        'results': results, 
        'query': class_val
    })

@login_required
def teacher_upload(request):
    """Handles the PDF upload system for teachers."""
    if request.method == 'POST':
        # Grabbing the data and the actual file from the form
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        class_level = request.POST.get('class_level')
        resource_type = request.POST.get('resource_type')
        pdf_file = request.FILES.get('pdf_file') # CRITICAL for file uploads

        if pdf_file:
            Resource.objects.create(
                title=title,
                subject=subject,
                class_level=class_level,
                resource_type=resource_type,
                pdf_file=pdf_file
            )
            return redirect('home') # Success! Go back home.
            
    return render(request, 'library/upload.html')