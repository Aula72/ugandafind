from .models import Contact
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import ContactsForm
class ContactCreateView(CreateView):
    model = Contact
    fields = ['name' ,'mail', 'subject', 'content']

class ContactDetails(DetailView):
    model = Contact    
    template_name = "contacts/details.html"  
class ContactView(CreateView):
    model = Contact
    fields = ['name' ,'mail', 'subject', 'content']

def send_message(request):
    form = ContactsForm()
    if form.is_valid():
        form = ContactsForm(request.POST)
        form.save()
        return redirect('ugandafind/contact-us/')
    return render(request, 'contacts/form.html', {'form':form})