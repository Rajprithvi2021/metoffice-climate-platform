from django.core.management.base import BaseCommand
from climate.models import *
from climate.services.metoffice_parser import fetch_and_parse

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--url", required=True)
        parser.add_argument("--parameter", required=True)
        parser.add_argument("--region", required=True)

    def handle(self, *args, **opts):
        metric, _ = WeatherMetric.objects.get_or_create(
            parameter=opts["parameter"],
            region=opts["region"]
        )

        for row in fetch_and_parse(opts["url"]):
            y = row["year"]

            for i, v in enumerate(row["monthly"].values(), 1):
                MonthlyWeatherFact.objects.get_or_create(
                    metric=metric, year=y, month=i, defaults={"value": v}
                )

            for s, v in row["seasonal"].items():
                SeasonalWeatherFact.objects.get_or_create(
                    metric=metric, year=y, season=s, defaults={"value": v}
                )

            AnnualWeatherFact.objects.get_or_create(
                metric=metric, year=y, defaults={"value": row["annual"]}
            )

        self.stdout.write("Ingestion completed.")
