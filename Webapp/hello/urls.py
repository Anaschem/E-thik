from django.urls import path
from .views import index, epicerie, boulangerie, efrigo, casiers, contacte
urlpatterns = [
    path("", index, name="index"),
    path("test", index, name="test"),
    path("epicerie", epicerie, name="epicerie"),
    path("boulangerie", boulangerie, name="boulangerie"),
    path("e-frigo", efrigo, name="e-frigo"),
    path("casiers", casiers, name="casiers"),
    path("contactez-nous", contacte, name="contacte"),
]