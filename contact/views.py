from django.shortcuts import render
from .models import Contact
from services.models import Category
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['template-contactform-name']
        email = request.POST['template-contactform-email']
        phone = request.POST['template-contactform-phone']
        msg = request.POST['template-contactform-message']
        if phone == '' or phone.isalpha():
            send = 'Información:' + '\n' + '\n' + 'Nombre del cliente: ' + name.title() + '\n' + 'Correo del cliente: ' + email + '\n' + 'Teléfono del cliente: ' + "Dato no enviado" + '\n' + 'Mensaje: ' + msg
            send_mail('Acrigrabados Contacto', send, 'no-reply@acrigrabados.com', ['comercial@acrigrabados.com'],
                    fail_silently=False)
        else:
            send = 'Información:' + '\n' + '\n' + 'Nombre del cliente: ' + name.title() + '\n' + 'Correo del cliente: ' + email + '\n' + 'Teléfono del cliente: ' + phone + '\n' + 'Mensaje: ' + msg
            send_mail('Acrigrabados Contacto', send, 'no-reply@acrigrabados.com', ['comercial@acrigrabados.com'],
                    fail_silently=False)
        contact = Contact()
        if phone != '' and not phone.isalpha():
            contact.phone = phone
        contact.name = name
        contact.email = email
        contact.msg = msg
        contact.save()
    context = {"categories": categories}
    return render(request, 'contact/contact.html', context)
