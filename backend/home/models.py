from django.conf import settings
from django.db import models
class P2Test(models.Model):
    'Generated Model'
    reg46 = models.BigIntegerField()
    rel_user_n_n = models.ManyToManyField("users.User",blank=True,related_name="p2test_rel_user_n_n",)
    regre46p2a = models.CharField(max_length=20,null=True,blank=True,)
