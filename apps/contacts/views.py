from rest_framework import viewsets

from apps.contacts.models import ContactUs
from apps.contacts.serailizer import ContactUsSerializer


class ContactUsApiViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
