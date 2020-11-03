from django.shortcuts import render
from .models import Job
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def send_mail(request):

	if request.method == 'POST':

		template = render_to_string('jobs/contact.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['tsagarikon@hotmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'jobs/email_sent.html')
