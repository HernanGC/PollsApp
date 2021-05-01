from django.contrib import admin
from . import models

my_models = [
    models.Question,
    models.Choice
]
admin.site.register(my_models)
