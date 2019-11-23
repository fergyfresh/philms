from celery import task
from philms_genre import philms_genre

from genre.models import Genre


@task(bind=True)
def sync_latest_top_movie_genres(self):
    top_genres = philms_genre.scrape_top_movies()
    Genre.objects.bulk_create([Genre(type=i) for i in top_genres])
