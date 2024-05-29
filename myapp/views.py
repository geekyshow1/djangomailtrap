from django.shortcuts import render
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
import mailtrap as mt
import base64
from decouple import config


def home(req):
    return render(req, 'myapp/home.html')


def send_test_email(req):  # Send Test Email (Dev)
    subject = 'Test Email'
    name = 'User'
    html_message = render_to_string(
        'myapp/email_template.html', {'name': name})
    plain_message = strip_tags(html_message)
    from_email = 'admin@example.com'
    to_email = ['user@example.com']

    # # Create email with Plain Text Message
    # email = EmailMessage(subject=subject, body=plain_message,
    #                      from_email=from_email, to=to_email)

    # # Create email with HTML Content
    # email = EmailMessage(subject=subject, body=html_message,
    #                      from_email=from_email, to=to_email)
    # email.content_subtype = 'html'  # Set the email content type to HTML

    # Create the email message with both plain text and HTML content
    email = EmailMultiAlternatives(
        subject=subject, body=plain_message, from_email=from_email, to=to_email)
    email.attach_alternative(html_message, "text/html")

    # Attach File to EMail
    with open('myfile.pdf', 'rb') as file:
        email.attach('myfile.pdf', file.read(), 'application/pdf')

    # Send the email
    email.send()

    return HttpResponse('Test email with Plain Message,  HTML Content and Attachment sent successfully.')


def send_prod_smtp_email(req):  # For Production using SMTP
    subject = 'Test SMTP Email'
    name = 'User'
    html_message = render_to_string(
        'myapp/email_template.html', {'name': name})
    plain_message = strip_tags(html_message)
    from_email = 'admin@demomailtrap.com'
    to_email = ['xafiga9133@fresec.com']

    # # Create email with Plain Text Message
    # email = EmailMessage(subject=subject, body=plain_message,
    #                      from_email=from_email, to=to_email)

    # # Create email with HTML Content
    # email = EmailMessage(subject=subject, body=html_message,
    #                      from_email=from_email, to=to_email)
    # email.content_subtype = 'html'  # Set the email content type to HTML

    # Create the email message with both plain text and HTML content
    email = EmailMultiAlternatives(
        subject=subject, body=plain_message, from_email=from_email, to=to_email)
    email.attach_alternative(html_message, "text/html")

    # Attach File to EMail
    with open('myfile.pdf', 'rb') as file:
        email.attach('myfile.pdf', file.read(), 'application/pdf')

    # Send the email
    email.send()

    return HttpResponse('SMTP Email with HTML and attachment sent successfully.')


def send_prod_api_email(req):  # For Production using API
    subject = 'Test API Email'
    name = 'User'
    html_message = render_to_string(
        'myapp/email_template.html', {'name': name})
    plain_message = strip_tags(html_message)
    from_email = 'admin@demomailtrap.com'
    to_email = 'xafiga9133@fresec.com'

    # Attach File to EMail
    with open('myfile.pdf', 'rb') as file:
        file_content = base64.b64encode(file.read())

    myfile = mt.Attachment(
        content=file_content,
        filename="myfile.pdf",
        mimetype="application/pdf"
    )

    mail = mt.Mail(
        sender=mt.Address(email=from_email, name="Admin"),
        to=[mt.Address(email=to_email, name=name)],
        subject=subject,
        text=plain_message,
        html=html_message,
        category="OTP Emails",
        attachments=[myfile]
    )

    client = mt.MailtrapClient(token=config('MAILTRAP_API_TOKEN'))
    client.send(mail)

    return HttpResponse('API Email with HTML and attachment sent successfully.')
