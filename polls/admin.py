# django imports
from django.contrib import admin

# local imports
from .models import Question

admin.site.register(Question)