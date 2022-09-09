from gamecapstoneapi.models import SlotUser, Question, Solution
from gamecapstoneapi.views.slot_user import SlotUserSerializer
from gamecapstoneapi.views.question import QuestionSerializer 
from gamecapstoneapi.views.solution import SolutionSerializer
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
        Create a new slotuser, collect the auth Token, and create a sample question
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
            is_staff=0,
            is_active=1
)
        self.SlotUser = SlotUser.objects.create(
        user=self.user,
        title=None,
        session_score=None,
        score=None
        )
        self.solution = Solution.objects.create(
            label="label"
        )
        self.question = Question.objects.create(
            label="label",
            difficulty=1,
            # solution=Solution.set(self.solution)
            
        )
        
#many to many in tests how make work? ?

    def test_get_user(self):
        """
        Ensure we can GET users.
        """
        url = f'/users/{self.user.id}'
        # Initiate GET request and capture the response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["score"], self.SlotUser.score)
        self.assertEqual(response.data["session_score"], self.SlotUser.session_score)
        # self.assertEqual(response.data["user"], self.SlotUser.user) why can't i get this to work?
        self.assertEqual(response.data["title"], self.SlotUser.title)

    def test_list_users(self):
        """Test list users
        """
        url = '/users'
        response = self.client.get(url)
        all_users = SlotUser.objects.all()
        expected = SlotUserSerializer(all_users, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_delete_slot_user(self):
        """
        Ensure we can delete a user account.
        """
        url = f'/users/{self.user.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_question(self):
        """Ensure we can GET a question.
        """
        # Define the URL path for getting a single Game
        url = f'/questions/{self.question.id}'
        # Initiate GET request and capture the response
        response = self.client.get(url)
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the values are correct
        # self.assertEqual(response.data["gamer"]['id'], self.game.gamer_id)
        self.assertEqual(response.data["label"], self.question.label)
        self.assertEqual(response.data["difficulty"], self.question.difficulty)
        # self.assertEqual(response.data["user"], self.SlotUser.user) why can't i get this to work?
        # self.assertEqual(response.data["solution"], self.question.solution) many to many in tests need to ask 

    def test_list_questions(self):
        """Test list users
        """
        url = '/questions'
        response = self.client.get(url)
        all_questions = Question.objects.all()
        expected = QuestionSerializer(all_questions, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_delete_question(self):
        """
        Ensure we can delete a question.
        """
        url = f'/questions/{self.question.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_solution(self):
        """
        Ensure we can GET users.
        """
        url = f'/solutions/{self.solution.id}'
        # Initiate GET request and capture the response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["label"], self.solution.label)

    def test_list_solutions(self):
        """Test list users
        """
        url = '/solutions'
        response = self.client.get(url)
        all_solutions = Solution.objects.all()
        expected = SolutionSerializer(all_solutions, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_delete_solution(self):
        """
        Ensure we can delete a solution.
        """
        url = f'/solutions/{self.solution.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)