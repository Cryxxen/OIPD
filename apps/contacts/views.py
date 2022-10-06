from rest_framework import viewsets

from apps.contacts.models import ContactUs
from apps.contacts.serailizer import ContactUsSerializer


class EnglishContactUsApiViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.filter(language='english').all()
    serializer_class = ContactUsSerializer


class RussianContactUsApiViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.filter(language='russian').all()
    serializer_class = ContactUsSerializer

