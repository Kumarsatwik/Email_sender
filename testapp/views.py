from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def email(request):

	if request.method=="POST":
		email=request.POST.get('email')
		name=request.POST.get('name')
		subject=request.POST.get('subject')
		explain=request.POST.get('explain')
		explain="Hi , I am "+name+" , \n"+explain
		# print(email)
		# print(subject)
		template='index.html'
		send_mail(
			subject,
			explain,
			settings.EMAIL_HOST_USER,
			[email],
			fail_silently=False
			)

	return render(request,'index.html')
# def bulk(request):

# 	if request.method=="POST":
# 		email=request.POST.get('email')
# 		name=request.POST.get('name')
# 		subject=request.POST.get('subject')
# 		explain=request.POST.get('explain')
# 		explain="Hi , I am "+name+" , \n"+explain
# 		# print(email)
# 		# print(subject)
# 		template='index.html'
# 		send_mail(
# 			subject,
# 			explain,
# 			settings.EMAIL_HOST_USER,
# 			[email],
# 			fail_silently=False
# 			)

# 	return render(request,'bulk.html')