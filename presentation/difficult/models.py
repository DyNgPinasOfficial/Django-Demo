from django.db import models

class PageVisit(models.Model):
    page_name = models.CharField(max_length=255, unique=True, default='')
    visit_count = models.IntegerField(default=0)
    envelope_open_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name
