from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Todo

class TodoAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a token for the user
        self.token = Token.objects.create(user=self.user)
        # Include the token in the client's headers
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Create a test todo item
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='Test Description',
            completed=False
        )

    def test_list_todos(self):
        response = self.client.get(reverse('todo-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        data = {'title': 'New Todo', 'description': 'New Description', 'completed': False}
        response = self.client.post(reverse('todo-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_todo(self):
        response = self.client.get(reverse('todo-detail', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        data = {'title': 'Updated Todo', 'description': 'Updated Description', 'completed': True}
        response = self.client.put(reverse('todo-detail', kwargs={'pk': self.todo.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        response = self.client.delete(reverse('todo-detail', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)