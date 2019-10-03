import json
import unittest
from main import db
from main.api.models import User
from test.base import BaseTestCase

# Tests for the User Service
class TestUserService(BaseTestCase):
    # Basic happy path, ensure the /users route behaves correctly
    def test_user_creation(self):
        with self.client:
            response = self.client.post('/api/v1/users',
                data=json.dumps({
                    'gid': '1234567890',
                    'username': 'example',
                    'email': 'example@freshworks.io',
                    'access_token': '12345678900987654321'
                }),
                content_type='application/json',
            )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn('Successfully created user.', data['status'])
        self.assertEqual(1234567890, data['user']['gid'])
        self.assertIn('example', data['user']['username'])
        self.assertIn('example@freshworks.io', data['user']['email'])
        self.assertEqual('12345678900987654321', data['user']['access_token'])

if __name__ == '__main__':
    unittest.main()