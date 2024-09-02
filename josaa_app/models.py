from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class josaa(models.Model):
    Institute=models.CharField(_("Institute"),max_length=250)
    Academic_Program_Name=models.CharField(_("Academic_Program_Name"),max_length=300)
    Seat_Type=models.CharField(_("Seat_Type"),max_length=50)
    Gender=models.CharField(_("Gender"),max_length=50)
    Opening_Rank=models.IntegerField(_("Opening_Rank"),default=0)
    Closing_Rank=models.IntegerField(_("Closing_Rank"),default=0)
    year=models.IntegerField(_("year"))
    round=models.IntegerField(_("round"))


