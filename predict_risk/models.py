from django.db import models
from accounts.models import UserProfileInfo
from django.utils import timezone
from django.urls import reverse
# Create your models here.
sex_choices=((0, 'Female'),(1, 'Male'))
cp_choice=((0,'None'),(1, 'Typical Angina'),(2, 'Atypical Angina'),(3, 'Non-Angina'),(4, 'Asymptomatic'))
fasting_blood_sugar_choices=((1,'> 120 mg/dl'),((0,'< 120 mg/dl')))
resting_ecg_choices=((0, 'Normal'),(1, 'Having ST-T wave abnormality'),(2, 'hypertrophy'))
exercise_induced_angina_choices=((0, 'No'),(1, 'Yes'))
st_slope_choices=((1, 'Upsloping'),(2, 'Flat'),(3, 'Down Sloping'))
number_of_vessels_choices=((0, 'None'),(1, 'One'),(2, 'Two'),(3, 'Three'))
thallium_scan_results_choices=((3, 'Normal'),(6, 'Fixed Defect'),(7, 'Reversible Defect'))

class Predictions(models.Model):
    profile = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='predict')
    age = models.IntegerField()
    sex = models.IntegerField(choices=sex_choices, default=0)
    cp = models.IntegerField(choices=cp_choice,default=0)
    resting_bp = models.IntegerField()
    serum_cholesterol = models.IntegerField()
    fasting_blood_sugar = models.IntegerField(choices=fasting_blood_sugar_choices,default=0)
    resting_ecg = models.IntegerField(choices=resting_ecg_choices,default=0)
    max_heart_rate = models.IntegerField()
    exercise_induced_angina = models.IntegerField(choices=exercise_induced_angina_choices,default=0)
    st_depression = models.DecimalField(max_digits=4, decimal_places=2)
    st_slope = models.IntegerField(choices=st_slope_choices)
    number_of_vessels = models.IntegerField(choices=number_of_vessels_choices)
    thallium_scan_results = models.IntegerField(choices=thallium_scan_results_choices)
    predicted_on = models.DateTimeField(default=timezone.now)
    num=models.IntegerField()

    def get_absolute_url(self):
        return reverse('predict:predict', kwargs={'pk': self.profile.pk})
