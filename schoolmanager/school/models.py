from django.db import models


class GetResult(models.Model):
    raw_file = models.FileField(upload_to='raw_data')
    upload_date = models.DateTimeField()
