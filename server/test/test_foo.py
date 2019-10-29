import json
import unittest
from app import db
from app.api.models.foo import Foo
from test.base import BaseTestCase

# Helper function to add a sample string to Foo


def create_foo_string(foo_string):
    foo_table_element = Foo(string_field=foo_string)
    db.session.add(foo_table_element)
    db.session.commit()
    return foo_table_element


class TestExampleService(BaseTestCase):
    def test_get_foo(self):
        create_foo_string('foo_string_1')
        create_foo_string('foo_string_2')
        create_foo_string('foo_string_3')
        with self.client:
            response = self.client.get('/api/foo')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['records']), 3)

    def test_post_foo(self):
        test_string = 'I am a test string'
        with self.client:
            response = self.client.post('/api/foo',
                                        data=json.dumps({
                                            'string_field': test_string,
                                        }),
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode())
        self.assertEqual(data['foo']['string_field'], test_string)

    def test_put_foo(self):
        create_foo_string('foo_string_1')
        with self.client:
            response = self.client.put('/api/foo',
                                       data=json.dumps({
                                           'id': 1,
                                           'string_field': 'I am a test string',
                                       }),
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['foo']['string_field'], 'I am a test string')

    def test_delete_foo(self):
        create_foo_string('foo_string_1')
        with self.client:
            response = self.client.delete('/api/foo',
                                          data=json.dumps({
                                              'id': 1,
                                              'string_field': 'I am a test string',
                                          }),
                                          content_type='application/json',
                                          )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())


if __name__ == '__main__':
    unittest.app()
