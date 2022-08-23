from django.urls import path

from .views import FabfacilityWebsiteTheme as theme


urlpatterns = [
    path('', theme.home, name='home'),
    path('subscriptions/', theme.subscription, name='subscriptions'),
    path('about/', theme.about, name='about'),
    path('gallery/', theme.gallery, name='gallery'),
    path('contact/', theme.contact, name='contact'),
    # Services Pages
    path('lease-cleaning-melbourne/', theme.lease_cleaning_melbourne, name='lease_cleaning_melbourne'),
    path('carpet-steam-cleaning/', theme.carpet_steam_cleaning, name='carpet_steam_cleaning'),
    path('after-builder-cleaning/', theme.after_builder_cleaning, name='after_builder_cleaning'),
    path('windown-cleaning/', theme.windown_cleaning, name='windown_cleaning'),
    path('oven-cleaning/', theme.oven_cleaning, name='oven_cleaning'),
    path('once-off-cleaning-or-Spring-clean/', theme.once_off_cleaning_or_Spring_clean, name='once_off_cleaning_or_Spring_clean'),
    path('pressure-washing/', theme.pressure_washing, name='pressure_washing'),
    path('tile-grout-cleaning/', theme.tile_grout_cleaning, name='tile_grout_cleaning'),
    path('stripping-sealing/', theme.stripping_sealing, name='stripping_sealing'),
    # Airbnb Property
    path('airbnb-cleaning/', theme.airbnb_cleaning, name='airbnb_cleaning'),
    path('airbnb-carpet-steam-cleaning/', theme.airbnb_carpet_steam_cleaning, name='airbnb_carpet_steam_cleaning'),
    path('handyman-services/', theme.handyman_services, name='handyman_services'),
    path('pri-listing-cleaning/', theme.pri_listing_cleaning, name='pri_listing_cleaning'),
    path('linens-supply/', theme.linens_supply, name='linens_supply'),
    path('key-delivery/', theme.key_delivery, name='key_delivery'),
    path('emergency-service/', theme.emergency_service, name='emergency_service'),
    # For Business
    path('real-estate-agent/', theme.real_estate_agent, name='real_estate_agent'),
    path('airbnb-short-stay-management/', theme.airbnb_short_stay_management, name='airbnb_short_stay_management'),
    path('commercial-office-cleaning/', theme.commercial_office_cleaning, name='commercial_office_cleaning'),
    path('property-maintenance/', theme.property_maintenance, name='property_maintenance'),
]
