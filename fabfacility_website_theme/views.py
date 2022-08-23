from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from .forms import SubscripForm, ContactForm
from .models import SubscriptionEmail, Gallery

import json


class FabfacilityWebsiteTheme:

    def home(self):
        return render(self, 'home')

    def subscription(self):
        if self.method == 'POST' and self.is_ajax():
            post_data = json.load(self)
            form = SubscripForm(post_data)
            if form.is_valid():
                if SubscriptionEmail.objects.filter(email=post_data['email']).exists():
                    return JsonResponse({'error': 'Email Already Exists.'})
                else:
                    form.save()
                    return JsonResponse({'success': 'Thank you for subscriptions.'})
            else:
                return JsonResponse({'error': 'Valid Email Required.'})

    def about(self):
        return render(self, 'about')

    def gallery(self):
        gallery = Gallery.objects.all()
        paginator = Paginator(gallery, 30)
        page_number = self.GET.get('page')
        context = {
            'galleries': paginator.get_page(page_number)
            }
        return render(self, 'gallery', context)

    def contact(self):
        if self.method == 'POST':
            form = ContactForm(self.POST)
            if form.is_valid():
                mail = f"Hello admin,\n\
I am {form.cleaned_data['name']},\n\
My Email: {form.cleaned_data['email']},\n\
My phone number: {form.cleaned_data['phone']},\n\
I want to talk on: {form.cleaned_data['service']},\n\
Message: {form.cleaned_data['message']}"
                send_mail(
                    f"Message from {get_current_site(self).domain}",
                    mail,
                    settings.EMAIL_HOST_USER,
                    ['mdshariffoysalshoron@gmail.com'],
                    fail_silently=False
                )
                print(mail)
                messages.success(self, f"Thank you for your inquiry! We will get back to you within 48 hours.")
                return redirect('contact')
        else:
            form = ContactForm()
        context = {
            'form': form
        }
        return render(self, 'contact', context)

    # Services Pages

    def lease_cleaning_melbourne(self):
        return render(self, 'lease_cleaning_melbourne.html')

    def carpet_steam_cleaning(self):
        return render(self, 'carpet_steam_cleaning.html')

    def after_builder_cleaning(self):
        return render(self, 'after_builder_cleaning.html')

    def windown_cleaning(self):
        return render(self, 'windown_cleaning.html')
    
    def oven_cleaning(self):
        return render(self, 'oven_cleaning.html')

    def once_off_cleaning_or_Spring_clean(self):
        return render(self, 'once_off_cleaning_or_Spring_clean.html')

    def pressure_washing(self):
        return render(self, 'pressure_washing.html')

    def tile_grout_cleaning(self):
        return render(self, 'tile_grout_cleaning.html')

    def stripping_sealing(self):
        return render(self, 'stripping_ealing.html')

    # Airbnb Property

    def airbnb_cleaning(self):
        return render(self, 'airbnb_cleaning.html')

    def airbnb_carpet_steam_cleaning(self):
        return render(self, 'airbnb_carpet_steam_cleaning.html')

    def handyman_services(self):
        return render(self, 'handyman_services.html')

    def pri_listing_cleaning(self):
        return render(self, 'pri_listing_cleaning.html')

    def linens_supply(self):
        return render(self, 'linens_supply.html')

    def key_delivery(self):
        return render(self, 'key_delivery.html')

    def emergency_service(self):
        return render(self, 'emergency_service.html')

    # For Business

    def real_estate_agent(self):
        return render(self, 'real_estate_agent.html')

    def airbnb_short_stay_management(self):
        return render(self, 'airbnb_short_stay_management.html')

    def commercial_office_cleaning(self):
        return render(self, 'commercial_office_cleaning.html')

    def property_maintenance(self):
        return render(self, 'property_maintenance.html')
