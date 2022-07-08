from django.test import TestCase
from bellezasys.views import MainPage
from .models import Belleza_Info
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'mainpage.html')

    # def test_responding_post_request(self): 
    #   resp = self.client.post('/', data={'name' :'newName',
    #       'email': 'newEmail', 
    #       'experience': 'newExperience'})
    #   self.assertIn('newName', resp.content.decode())
    #   self.assertTemplateUsed(resp, 'mainpage.html')
    def test_save_POST_request(self):
        response = self.client.post('/', {'bname': 'Rosenda Madriaga',
            'bemail': 'rosenda.madriaga@gmail.com', 
            'baddress': 'Datu Esmael Dasmarinas Cavite',
            'bconcern': 'Question',
            'messageText': 'How can I order?',})
        self.assertEqual(Belleza_Info.objects.count(), 1)
        newCustomer = Belleza_Info.objects.first()
        self.assertEqual(newCustomer.YourName, 'Rosenda Madriaga')
        self.assertEqual(newCustomer.YourEmail, 'rosenda.madriaga@gmail.com')
        self.assertEqual(newCustomer.YourAddress, 'Datu Esmael Dasmarinas Cavite')
        self.assertEqual(newCustomer.YourConcern, 'Question')
        self.assertEqual(newCustomer.YourMessage, 'How can I order?')
    def test_save_POST_redirect(self):
        response = self.client.post('/', {'bname': 'Rosenda Madriaga',
            'bemail': 'rosenda.madriaga@gmail.com', 
            'baddress': 'Datu Esmael Dasmarinas Cavite',
            'bconcern': 'Question',
            'messageText': 'How can I order?',})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], '/')
    def test_only_saves_items_if_necessary(self):
        self.client.get('/')
        self.assertEqual(Belleza_Info.objects.count(), 0)

class ORMTEST(TestCase):
    def test_saving_retriv(self):
        
        Cus1 = Belleza_Info()
        Cus1.YourName = 'Rosenda Madriaga'
        Cus1.YourEmail= 'rosenda.madriaga@gmail.com'
        Cus1.YourAddress= 'Datu Esmael Dasmarinas Cavite'
        Cus1.YourConcern = 'Question'
        Cus1.YourMessage = 'How can I order?'
        Cus1.save()

        Cus2 = Belleza_Info()
        Cus2.YourName = 'Joselle Sacriz'
        Cus2.YourEmail= 'joselle.sacriz@gmail.com'
        Cus2.YourAddress= 'Area 1 Dasmarinas Cavite'
        Cus2.YourConcern = 'Order Complaints'
        Cus2.YourMessage = 'Issue about my ordered clothes.'
        Cus2.save()

        Guest = Belleza_Info.objects.all()
        self.assertEqual(Guest.count(), 2)

        Cus1 = Guest[0]
        Cus2 = Guest[1]

        self.assertEqual(Cus1.YourName, 'Rosenda Madriaga')
        self.assertEqual(Cus1.YourEmail, 'rosenda.madriaga@gmail.com')
        self.assertEqual(Cus1.YourAddress, 'Datu Esmael Dasmarinas Cavite')
        self.assertEqual(Cus1.YourConcern, 'Question')
        self.assertEqual(Cus1.YourMessage, 'How can I order?')
        self.assertEqual(Cus2.YourName, 'Joselle Sacriz')
        self.assertEqual(Cus2.YourEmail, 'joselle.sacriz@gmail.com')
        self.assertEqual(Cus2.YourAddress, 'Area 1 Dasmarinas Cavite')
        self.assertEqual(Cus2.YourConcern, 'Order Complaints')
        self.assertEqual(Cus2.YourMessage, 'Issue about my ordered clothes.')
