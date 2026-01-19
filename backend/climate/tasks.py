from celery import shared_task
from climate.models import WeatherMetric, MonthlyWeatherFact
from climate.services.metoffice_parser import fetch_and_parse

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30, retry_kwargs={'max_retries': 3})
def ingest_weather_data(self, url, parameter, region):
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
