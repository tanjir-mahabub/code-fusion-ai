import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        # Fetch the data from the API
        response = requests.get('https://restcountries.com/v3.1/all')
        countries = response.json()
        
        for country in countries:
            Country.objects.update_or_create(
                cca2=country.get("cca2"),
                defaults={
                    "name": country.get("name", {}).get("common", ""),
                    "capital": country.get("capital", [""])[0] if country.get("capital") else "",
                    "population": country.get("population", 0),
                    "region": country.get("region", ""),
                    "timezones": country.get("timezones", []),
                    "languages": country.get("languages", {}),
                    "flag": country.get("flags", {}).get("png", ""),
                }
            )