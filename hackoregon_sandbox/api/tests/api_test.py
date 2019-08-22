from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class RootEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_response(self):
        response = self.client.get('/sandbox/')
        assert response.status_code == status.HTTP_200_OK

class APIRootEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/sandbox/api/')
        assert response.status_code == status.HTTP_200_OK

class DocsEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/sandbox/docs/')
        assert response.status_code == status.HTTP_200_OK

class SchemaEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/sandbox/schema/')
        assert response.status_code == status.HTTP_200_OK