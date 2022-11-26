from django.db import models

# from app.models import JobPost


# Create your models here.

gender = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
races = [("American Indian or Alaska Native", "American Indian or Alaska Native"),
         ("Asian", "Asian"),
         ("Black or African American", "Black or African American"),
         ("Hispanic or Latino", "Hispanic or Latino."),
         ("Native Hawaiian or Other Pacific Islander", "Native Hawaiian or Other Pacific Islander"),
         ("White", "White")]
veteranStatus = [("veteran", "I a am veteran"), ("~Not a veteran", "I am not a veteran"),
                 ("Declined to self-identity", "Declined to self-identity")]


class ApplyForm(models.Model):
    submit_CV = models.FileField(upload_to='Files')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    current_company = models.CharField(max_length=200)
    linkedin = models.URLField()
    twitter = models.URLField()
    github = models.URLField()
    portfolio = models.URLField()
    cover_letter = models.CharField(max_length=200)
    Gender = models.CharField(max_length=20, choices=gender, default='Male')
    race = models.CharField(max_length=200, choices=races, default='Asian')
    veteran_status = models.CharField(max_length=200, choices=veteranStatus, default='veteran')
    # date = models.DateTimeField(auto_now_add=True)

    # job_id = models.ForeignKey('app.JobPost', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
