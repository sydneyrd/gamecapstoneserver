from gamecapstoneapi.models import SlotUser
from gamecapstoneapi.views.slot_user import SlotUserSerializer
from contextlib import nullcontext
from datetime import datetime
from imp import NullImporter
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def setUp(self):
        """
        Create a new Gamer, collect the auth Token, and create a sample GameType
        """
        # Define the URL path for registering a Gamer
        url = '/register'
        # Define the Gamer properties
        slot_user = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those capstones!!"
        }
        # Initiate POST request and capture the response
        response = self.client.post(url, slot_user, format='json')
        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])
        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user = User.objects.create(
            username="steve00",
            password="Admin8*",
            email="steve@stevebrownlee.com",
            is_superuser=0,
            first_name="Steve",
            last_name="Brownlee",
            date_joined="2022-02-02 12:51:39.989000",
            is_staff=0,
            is_active=1
)
        self.SlotUser = SlotUser.objects.create(
        user=self.user,
        title=None,
        session_score=None,
        score=None
        )

    def test_get_user(self):
        """
        Ensure we can GET users.
        """
        # Define the URL path for getting a single Game
        url = f'/users/{self.user.id}'
        # Initiate GET request and capture the response
        response = self.client.get(url)
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the values are correct
        # self.assertEqual(response.data["gamer"]['id'], self.game.gamer_id)
        self.assertEqual(response.data["score"], self.SlotUser.score)
        self.assertEqual(response.data["session_score"], self.SlotUser.session_score)
        # self.assertEqual(response.data["user"], self.SlotUser.user) why can't i get this to work?
        self.assertEqual(response.data["title"], self.SlotUser.title)

    def test_list_users(self):
        """Test list users
        """
        url = '/users'
        response = self.client.get(url)
        # Get all the games in the database and serialize them to get the expected output
        all_users = SlotUser.objects.all()
        expected = SlotUserSerializer(all_users, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
