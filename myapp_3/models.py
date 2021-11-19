from django.db import models
from django.db.models import Q



class Model_3_Search(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(desc__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs


class Model_3(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    objects = Model_3_Search()


    class Meta:
        db_table = 'model_3'