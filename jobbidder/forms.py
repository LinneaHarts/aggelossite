from django.utils.timezone import datetime
import pytz

from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Company, Job


class AddJobForm2(ModelForm):
    def clean_job_desc(self):
        data = self.cleaned_data['job_desc']

        if len(str(data)) == 0:
            raise ValidationError(_('Job description cannot be blank'))

        return data

    def clean_job_date(self):
        data = self.cleaned_data['job_date']
        utc = pytz.UTC
        if data < utc.localize(datetime.today()):
            raise ValidationError(_('Invalid date - job date in the past'))
        return data

    class Meta:
        model = Job
        fields = {'job_desc', 'job_date', 'job_min_bid', 'job_company'}
        labels = {'job_desc': _('Job description'),
                  'job_date': _('Date of job'),
                  'job_min_bid': _('Minimum Bid'),
                  'job_company': _('Company')}
        widgets = {
            'job_date': forms.DateInput(format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                               'type': 'date'}),
        }
        help_texts = {'job_desc': _('Enter a description of your job')}


class AddJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['job_desc', 'job_date', 'job_min_bid']


class AddCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_address']
