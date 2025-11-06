from django.contrib.gis.db import models


class Route(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Stop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="stops")
    name = models.CharField(max_length=255)
    location = models.PointField(srid=4326)  # Stores latitude and longitude
    order = models.PositiveIntegerField()  # To define sequence of stops

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} ({self.route.name})"
