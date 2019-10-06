import json
import unittest
from main import db
from main.api.models import ExampleTable
from test.base import BaseTestCase

# Helper function to add a sample string to the example_table


def create_example_string(example_string):
    example_table_element = ExampleTable(string_field=example_string)
    db.session.add(example_table_element)
    db.session.commit()
    return example_table_element

# TODO test get
# TODO test post
# TODO test put
# TODO test get


class TestExampleService(BaseTestCase):
    def test_get_example(self):
        example_string_1 = create_example_string('example_string_1')
        example_string_2 = create_example_string('example_string_2')
        example_string_3 = create_example_string('example_string_3')
        with self.client:
            response = self.client.get('/api/example_endpoint')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        print(data)
        # TODO CHECK THAT THE LENGTH OF THE DATA IS 2

    def test_post_example(self):
        with self.client:
            response = self.client.post('/api/example_endpoint',
                                        data=json.dumps({
                                            'string_field': 'I am a test string',
                                        }),
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode())
        self.assertEqual(data['string_field'], 'I am a test string')
        # TODO USE GET METHOD TO CONFIRM DB CONTENT (OR CHECK DIRECTLY)

    def test_put_example(self):
        example_string_1 = create_example_string('example_string_1')
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
        self.assertEqual(data['string_field'], 'I am a test string')
        # TODO USE GET METHOD TO CONFIRM DB CONTENT (OR CHECK DIRECTLY)

    def test_delete_example(self):
        example_string_1 = create_example_string('example_string_1')
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
        self.assertEqual(data['string_field'], 'I am a test string')
        # TODO USE GET METHOD TO CONFIRM DB CONTENT (OR CHECK DIRECTLY)


if __name__ == '__main__':
    unittest.main()
