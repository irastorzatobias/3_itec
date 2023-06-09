from django.db import models

# Create your models here.


class CovidInfoModel(models.Model):
    date = models.CharField(max_length=100)
    positive = models.IntegerField()
    negative = models.IntegerField()

    def create_covid_info(self, date, positive, negative):
        self.date = date
        self.positive = positive
        self.negative = negative
        self.save()
        return self
