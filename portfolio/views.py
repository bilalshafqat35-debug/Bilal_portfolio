from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, ContactInfo, Service, SocialLink
from .forms import ContactForm

def home(request):
    # Contact Form Submit Logic
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully! I will get back to you soon.")
            return redirect('home')
    else:
        form = ContactForm()

    # Data Fetching
    projects = Project.objects.all()
    skills = Skill.objects.all()
    contact_info = ContactInfo.objects.all()
    services = Service.objects.all()
    social_links = SocialLink.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
        'contact_info': contact_info,
        'services': services,
        'social_links': social_links,
        'form': form,
    }
    
    return render(request, 'portfolio/home.html', context)