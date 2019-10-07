import json
import unittest
from app import db
from app.api.models import ExampleTable
from test.base import BaseTestCase

# Helper function to add a sample string to the example_table


def create_example_string(example_string):
    example_table_element = ExampleTable(string_field=example_string)
    db.session.add(example_table_element)
    db.session.commit()
    return example_table_element


class TestExampleService(BaseTestCase):
    def test_get_example(self):
        create_example_string('example_string_1')
        create_example_string('example_string_2')
        create_example_string('example_string_3')
        with self.client:
            response = self.client.get('/api/example_endpoint')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['examples']), 3)

    def test_post_example(self):
        test_string = 'I am a test string'
        with self.client:
            response = self.client.post('/api/example_endpoint',
                                        data=json.dumps({
                                            'string_field': test_string,
                                        }),
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode())
        self.assertEqual(data['example']['string_field'], test_string)

    def test_put_example(self):
        create_example_string('example_string_1')
        with self.client:
            response = self.client.put('/api/example_endpoint',
                                       data=json.dumps({
                                           'id': 1,
                                           'string_field': 'I am a test string',
                                       }),
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['example']['string_field'], 'I am a test string')

    def test_delete_example(self):
        create_example_string('example_string_1')
        with self.client:
            response = self.client.delete('/api/example_endpoint',
                                          data=json.dumps({
                                              'id': 1,
                                              'string_field': 'I am a test string',
                                          }),
                                          content_type='application/json',
                                          )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status'], 'Successfully deleted that object.')


if __name__ == '__main__':
    unittest.app()
