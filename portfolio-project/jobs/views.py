from django.shortcuts import render
from .models import Job
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request): 
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})


def contact(request):

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
			['dennisivy11@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'jobs/email_sent.html')