from rest_framework import generics

from apps.contacts.models import ContactUs, Bid
from apps.contacts.serailizer import ContactUsSerializer, BidSerializer


class ContactUsApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class BidApiView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
