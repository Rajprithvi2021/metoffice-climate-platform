from celery import shared_task
from climate.models import (
    WeatherMetric,
    MonthlyWeatherFact,
    SeasonalWeatherFact,
    AnnualWeatherFact,
)
from climate.services.metoffice_parser import fetch_and_parse


@shared_task
def ingest_weather_data(url, parameter, region):
    metric, _ = WeatherMetric.objects.get_or_create(
        parameter=parameter,
        region=region
    )

    for row in fetch_and_parse(url):
        year = row["year"]

        for i, v in enumerate(row["monthly"].values(), 1):
            MonthlyWeatherFact.objects.update_or_create(
                metric=metric,
                year=year,
                month=i,
                defaults={"value": v}
            )

        for s, v in row["seasonal"].items():
            SeasonalWeatherFact.objects.update_or_create(
                metric=metric,
                year=year,
                season=s,
                defaults={"value": v}
            )

        AnnualWeatherFact.objects.update_or_create(
            metric=metric,
            year=year,
            defaults={"value": row["annual"]}
        )
