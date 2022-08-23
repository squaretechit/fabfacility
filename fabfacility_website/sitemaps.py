from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            'home',
            'about',
            'gallery',
            'contact',
            'lease_cleaning_melbourne',
            'carpet_steam_cleaning',
            'after_builder_cleaning',
            'windown_cleaning',
            'oven_cleaning',
            'once_off_cleaning_or_Spring_clean',
            'pressure_washing',
            'tile_grout_cleaning',
            'stripping_sealing',
            'airbnb_cleaning',
            'airbnb_carpet_steam_cleaning',
            'handyman_services',
            'pri_listing_cleaning',
            'linens_supply',
            'key_delivery',
            'emergency_service',
            'real_estate_agent',
            'airbnb_short_stay_management',
            'commercial_office_cleaning',
            'property_maintenance'
                ]

    def location(self, item):
        return reverse(item)
