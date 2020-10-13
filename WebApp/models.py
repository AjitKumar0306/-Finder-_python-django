from django.db import models


class Search(models.Model):
    search_filed = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search_filed)

    class Meta:
        verbose_name_plural = 'Searches'
