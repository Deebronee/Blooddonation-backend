from rest_framework import status
from rest_framework.test import APITestCase
from backend.models import blood_donation_appointments

# writing unit tests
# Create your tests here.


# Testing post requests to database appointments
class TestPostAppointments(APITestCase):
    url = '/blood_donation_free_appointments/'

    def testPost(self):
        """
        Ensure we can create a new blood_donation_appointment object.
        """
        data =  {
                    "date": "2022-01-01",
                    "time": "10:00:00",
                    "last_name": "Mustermann",
                    "first_name": "Max",
                    "reserved": False,
                    "assigned": False
                }
        response = self.client.post(self.url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(blood_donation_appointments.objects.count(), 1)
        self.assertEqual(blood_donation_appointments.objects.get().last_name, "Mustermann")



# Testing get requests to database appointments
class TestGetAppointments(APITestCase):
    url = '/blood_donation_free_appointments/'

    def setUp(self):
        blood_donation_appointments.objects.create(
            date = "2022-01-01",
            time = "10:00:00",
            last_name = "Mustermann",
            first_name = "Max",
            reserved = False,
            assigned = False
            )

    def testGet(self):
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['last_name'], "Mustermann")


""""
# Testing get requests to database appointments
class TestGetAppointments(APITestCase):
    url = '/blood_donation_free_appointments/'

    def testPut(self):
        data =  {
                    "date": "2022-01-02",
                    "time": "12:00:00",
                    "last_name": "Cena",
                    "first_name": "John",
                    "reserved": False,
                    "assigned": False
                }

        response = self.client.put(self.url + f"/1", data, format = 'json')
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result[0]['last_name'], "Cena")
"""

"""
# Testing get requests to database appointments
class TestDeleteAppointments(APITestCase):
    url = '/blood_donation_free_appointments/'

    def testDelete(self):
        response = self.client.patch(self.url, data, format = 'json')
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result[0]['last_name'], "Cena")

"""
