from rest_framework import generics

from apps.contacts.models import ContactUs
from apps.contacts.serailizer import ContactUsSerializer


class ContactUsApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


