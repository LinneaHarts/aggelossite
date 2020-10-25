from django.db import models
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.company_name

#class User(models.Model):
#    email = models.CharField(max_length=100)
#    first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
#    password = models.CharField(max_length=50)
#    user_company = models.ForeignKey(Company, on_delete=models.CASCADE)
#    USER_ROLES = (
#        ('C', 'CEO'),
#        ('T', 'Trader'),
#        ('B', 'Broker'),
#        ('D', 'Data Analyst'),
#    )
#    user_role = models.CharField(max_length=1, choices=USER_ROLES)
#
#    def __str__(self):
#        return (self.first_name + self.last_name)


class Job(models.Model):
    job_desc = models.CharField(max_length=500)
    job_date = models.DateTimeField('job date')
    job_min_bid = models.FloatField(default=0)
    job_final_bid = models.FloatField(default=0)
    job_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_desc


class Bid(models.Model):
    bid_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bid_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    bid_amount = models.FloatField()

    def __str__(self):
        return (self.bid_company.company_name + ' ' + self.bid_job.job_desc + ' ' + str(self.bid_amount))

# Create your models here.
