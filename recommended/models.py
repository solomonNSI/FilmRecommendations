# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movies(models.Model):
    index = models.IntegerField(blank=True, null=True)
    adult = models.TextField(blank=True, null=True)
    belongs_to_collection = models.TextField(blank=True, null=True)
    budget = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    #id = models.TextField(blank=True, null=True)
    imdb_id = models.TextField(blank=True, null=True)
    original_language = models.TextField(blank=True, null=True)
    original_title = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    popularity = models.TextField(blank=True, null=True)
    poster_path = models.TextField(blank=True, null=True)
    production_companies = models.TextField(blank=True, null=True)
    production_countries = models.TextField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    revenue = models.TextField(blank=True, null=True)
    runtime = models.TextField(blank=True, null=True)
    spoken_languages = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    vote_average = models.TextField(blank=True, null=True)
    vote_count = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    cast_size = models.TextField(blank=True, null=True)
    crew_size = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    castkey = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'
