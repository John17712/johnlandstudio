from django.shortcuts import render, redirect
from django.core.mail import send_mail


def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		
		message_subject = request.POST['message-subject']
		your_message = request.POST['your-message']
		

		send_mail(
			message_subject, # subject
			your_message, # message	
			your_name, # from sender							
			['johnitezbean8@gmail.com'], # To Email
			)

		return render(request, 'contact.html', {
			'your_name': your_name,
			'your_email': your_email,
			
			'message_subject': message_subject,
			'your_message': your_message,
			})

	else:
		return render(request, 'contact.html', {})

def service(request):
	return render(request, 'service.html')

def shop(request):
	return render(request, 'shop.html')

def appointment(request):
	
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_phone = request.POST['your-phone']
		your_time = request.POST['your-time']
		your_date = request.POST['your-date']
		your_service = request.POST['your-service']
		


		# Send an email
		appointment = " Name: " + your_name + "\n" + " Phone: " + your_phone + "\n" + " Email: " + your_email + "\n" + " Date: " + your_date + "\n" + " Time: " + your_time + "\n" + " Service: " +  your_service



		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_name,	# from email
			['johnitezbean8@gmail.com'], # To Email
			)

		return render(request, 'appointment2.html', {
		   'your_name': your_name,
		   'your_phone': your_phone,
		   'your_email': your_email,
		   'your_date': your_date,
		   'your_time': your_time,
		   'your_service': your_service,		   
			})

	else:
		return render(request, 'appointment.html', {})

