from django.test import TestCase
from django.urls import reverse
from .models import Contact

class ContactModelTests(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='1234567890',
            address='123 Main St'
        )

    def test_contact_str(self):
        self.assertEqual(str(self.contact), 'John Doe')

    def test_contact_creation(self):
        contact = Contact.objects.get(email='john.doe@example.com')
        self.assertEqual(contact.first_name, 'John')
        self.assertEqual(contact.last_name, 'Doe')
        self.assertEqual(contact.phone_number, '1234567890')
        self.assertEqual(contact.address, '123 Main St')

class ContactViewTests(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='1234567890',
            address='123 Main St'
        )

    def test_contact_list_view(self):
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertTemplateUsed(response, 'contacts/contact_list.html')

    def test_contact_detail_view(self):
        response = self.client.get(reverse('contact_detail', kwargs={'pk': self.contact.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertContains(response, '123 Main St')
        self.assertTemplateUsed(response, 'contacts/contact_detail.html')

    def test_contact_add_view(self):
        response = self.client.get(reverse('contact_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')

    def test_contact_edit_view(self):
        response = self.client.get(reverse('contact_edit', kwargs={'pk': self.contact.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')

    def test_contact_delete_view(self):
        response = self.client.post(reverse('contact_delete', kwargs={'pk': self.contact.pk}))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion
        self.assertFalse(Contact.objects.filter(pk=self.contact.pk).exists())
