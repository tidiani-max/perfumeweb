from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Perfume, Profile, Testimony

# Create your views here.

# shop/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import OwnerSignupForm, TestimonyForm
from .models import Profile

def some_view(request):
    owner_exists = Profile.objects.filter(is_owner=True).exists()
    return render(request, 'your_template.html', {'owner_exists': owner_exists})

# Register owner if no owner exists
def owner_signup(request):
    if Profile.objects.filter(is_owner=True).exists():
        return redirect('login')  # Redirect if an owner already exists

    if request.method == 'POST':
        form = OwnerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in directly after signup
            login(request, user)
            return redirect('index')  # Redirect to homepage or preferred home view
    else:
        form = OwnerSignupForm()

    return render(request, 'owner_signup.html', {'form': form})

# Login view for all users
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

class OwnerLoginView(LoginView):
    template_name = 'owner_login.html'

    def form_valid(self, form):
        user = form.get_user()
        if not Profile.objects.filter(user=user, is_owner=True).exists():
            # Reject login if the user is not an owner
            form.add_error(None, 'Only the owner can log in.')
            return self.form_invalid(form)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('index')
    


# shop/views.py


# Function to check if a user is the owner
def is_owner(user):
    return Profile.objects.filter(user=user, is_owner=True).exists()

#View to list all perfumes for users


from django.conf import settings
#Detail view for a perfume
from urllib.parse import quote  # Import quote from urllib.parse
from .models import Perfume

def perfume_detail(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    
    # Prepare a pre-filled message with product details
    whatsapp_message = f"Hello! I am interested in buying the product '{perfume.name}' priced at ${perfume.price}. Here is the description: {perfume.description}"
    
    # URL-encode the message to handle special characters
    encoded_message = quote(whatsapp_message)
    
    # Construct the WhatsApp link with the owner's phone number and the encoded message
    # Ensure the number in settings.py is in international format (e.g., "1234567890" for +1 234-567-890)
    whatsapp_number = getattr(settings, 'WHATSAPP_OWNER_NUMBER', '')  # Ensure this is set in settings.py
    
    if not whatsapp_number:
        # If the number is missing, you might want to handle the case
        raise ValueError("WhatsApp number is not set in settings.py.")
    
    whatsapp_link = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    context = {
        'perfume': perfume,
        'whatsapp_link': whatsapp_link,  # Pass the dynamically generated link
    }
    return render(request, 'perfume_detail.html', context)

# Owner-only view to add a perfume
from .forms import PerfumeForm  # Assuming you have a form named PerfumeForm
from django.contrib.auth.decorators import login_required
@login_required
@user_passes_test(is_owner)
def add_perfume(request):
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your product has been  successfully added !")
            return redirect('products')  # Redirect after successful form submission
    else:
        form = PerfumeForm()
    return render(request, 'add_perfume.html', {'form': form})
# Owner-only view to edit a perfume
from django.shortcuts import get_object_or_404
@login_required
@user_passes_test(is_owner)
def edit_perfume(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save()
            messages.success(request, "Your product has been  successfully edited !")
            return redirect('products')
    else:
        form = PerfumeForm(instance=perfume)
    return render(request, 'edit_perfume.html', {'form': form})

# Owner-only view to delete a perfume
@login_required
@user_passes_test(is_owner)
def delete_perfume(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    if request.method == 'POST':
        perfume.delete()
        messages.success(request, "Your product has been  successfully deleted !")
        return redirect('products')
    return render(request, 'delete_perfume.html', {'perfume': perfume})

from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Compose email content
        subject = "New Contact Request"
        message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

        # Directly set the recipient email in the send_mail function
        recipient_email = 'tidianidiawara97@gmail.com'  # Replace with the email where you want to receive messages

        # Send email to site owner
        send_mail(
            subject,
            message_body,
            settings.DEFAULT_FROM_EMAIL,  # Sender email
            [recipient_email],            # Recipient email list
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact_us')  # Redirect back to the contact page or a success page

    return render(request, 'contact.html')

def testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()    
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/')  # Redirect after successful form submission
    else:
        form = TestimonyForm()
    return render(request, 'testimony.html', {'form': form})

    

def index(request):
    perfumes = Perfume.objects.all()
    testimonies = Testimony.objects.all()
    return render(request, 'index.html', {'perfumes': perfumes, 'testimonies' : testimonies} )
   

def products(request):
    perfumes = Perfume.objects.all()
    return render(request, 'product.html', {'perfumes': perfumes})

def about(request):
     return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')

