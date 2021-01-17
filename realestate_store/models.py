from django.db import models
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)

    def __str__(self): return self.name

    def get_absolute_url(self):
        return reverse('realestate_list', args=[str(self.id)])

class RealEstate(models.Model):
    sity = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=200, db_index=True)
    type = models.ForeignKey(Type, related_name='realestates', on_delete=models.CASCADE,)
    areasqm = models.IntegerField()
    image = models.ImageField(upload_to = 'realestates/%Y/%m/%d', blank=True)
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    class Meta:
        ordering = ('sity','address',)
        index_together = (('id', 'type'),)
        verbose_name_plural = 'realestates'

    def __str__(self):
        return self.sity + ", " + self.address

    def get_absolute_url(self):
        return reverse('realestate_detail', args=[self.id, self.type])
