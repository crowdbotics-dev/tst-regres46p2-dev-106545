from django.conf import settings
from django.db import models
class SlokVt(models.Model):
    'Generated Model'
    vinay = models.TextField()
    rel_user_n_n = models.ManyToManyField("users.User",blank=True,related_name="p2test_rel_user_n_n",)
    vinay88 = models.CharField(max_length=20,null=True,blank=True,)
