from django.core.mail import send_mail
from django.http import Http404, HttpResponse


def contact_me(request):
    if request.is_ajax():
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # if name and email and phone and message:
        subject = '[New Contact] {0} submitted a contact form'.format(name)
        comp_message = '{name}\n{email}\n{phone}\n\n{message}'.format(
            name=name, email=email, phone=phone, message=message
        )
        status = send_mail(subject, comp_message, 'scott@scottmedwards.com', ['scott@scottmedwards.com'])

        if status == 1:
            return HttpResponse()
        else:
            return HttpResponse(status=500)
    else:
        raise Http404()
