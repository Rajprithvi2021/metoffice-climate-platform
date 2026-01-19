from django.core.management.base import BaseCommand
from climate.tasks import ingest_weather_data

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--url",
            default="https://metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"
        )
        parser.add_argument("--parameter", default="Tmax")
        parser.add_argument("--region", default="UK")

    def handle(self, *args, **opts):
        ingest_weather_data.delay(
            opts["url"],
            opts["parameter"],
            opts["region"]
        )

        self.stdout.write(self.style.SUCCESS(
            "Weather ingestion task triggered asynchronously."
        ))
