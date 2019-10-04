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

    def test_post_example(self):
    def test_put_example(self):
    def test_delete_example(self):


class TestSpeciesService(BaseTestCase):
    # Basic happy path, ensure the /species route behaves correctly
    def test_get_species(self):
        example_string_1 = create_example_string('example_string_1')
        example_string_2 = create_example_string('example_string_2')
        example_string_3 = create_example_string('example_string_3')
        with self.client:
            response = self.client.get('/api/example_endpoint')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            print(data)
            # self.assertEqual(len(data['species']), 1)
            # self.assertIn('Norway rat', data['species'][0]['name'])
            # self.assertIn('Rattus norvegicus', data['species'][0]['latin'])
            # self.assertIn('Brown or dark grey in colour.',
            #               data['species'][0]['description'])
            # self.assertIn('1880-01-01', data['species'][0]['introduction'])
            # self.assertIn(category.name, data['species'][0]['category'])


    # # Basic happy path, ensure the /species route behaves correctly for POST
    # def test_species_creation(self):
    #     category = create_category('Plant')
    #     with self.client:
    #         response = self.client.post('/api/v1/species',
    #                                     data=json.dumps({
    #                                         'name': 'Giant hogweed',
    #                                         'latin': 'Heracleum mantegazzianum',
    #                                         'introduction': '1920-01-01',
    #                                         'description': 'Small white flower clusters in an umbrella-shaped head.',
    #                                         'category': 'Plant'
    #                                     }),
    #                                     content_type='application/json',
    #                                     )
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('Successfully created species.', data['status'])
    #     self.assertIsNotNone(data['species']['id'])
    #     self.assertIn('Giant hogweed', data['species']['name'])
    #     self.assertIn('Heracleum mantegazzianum', data['species']['latin'])
    #     self.assertIn('1920-01-01', data['species']['introduction'])
    #     self.assertIn('Small white flower clusters in an umbrella-shaped head.',
    #                   data['species']['description'])
    #     self.assertIn('Plant', data['species']['category'])
    # # Basic happy path, ensure the /species/<id> route behaves correctly
    # def test_get_single_species(self):
    #     category = create_category('Mammal')
    #     species = create_species('Norway rat', 'Rattus norvegicus',
    #                              'Brown or dark grey in colour.', '1880-01-01', category.id)
    #     with self.client:
    #         response = self.client.get('/api/v1/species/%d' % species.id)
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 200)
    #         self.assertEqual(species.id, data['id'])
    #         self.assertIn('Norway rat', data['name'])
    #         self.assertIn('Rattus norvegicus', data['latin'])
    #         self.assertIn('Brown or dark grey in colour.', data['description'])
    #         self.assertIn('1880-01-01', data['introduction'])
    #         self.assertIn(category.name, data['category'])
    # # Basic happy path, ensure the /species/<id> PUT route behaves correctly
    # def test_put_single_species(self):
    #     category = create_category('Mammal')
    #     species = create_species('Norway rat', 'Rattus norvegicus',
    #                              'Brown or dark grey in colour.', '1880-01-01', category.id)
    #     with self.client:
    #         response = self.client.put('/api/v1/species/%d' % species.id,
    #                                    data=json.dumps({
    #                                        'id': species.id,
    #                                        'name': 'Norway rat',
    #                                        'latin': 'Rattus norvegicus',
    #                                        'description': 'Brown or dark grey in colour with a lighter undercoat.',
    #                                        'introduction': '1880-01-01',
    #                                        'category': category.name
    #                                    }),
    #                                    content_type='application/json',
    #                                    )
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn('Successfully updated species.', data['status'])
    #         self.assertEqual(species.id, data['species']['id'])
    #         self.assertIn('Norway rat', data['species']['name'])
    #         self.assertIn('Rattus norvegicus', data['species']['latin'])
    #         self.assertIn('Brown or dark grey in colour with a lighter undercoat.',
    #                       data['species']['description'])
    #         self.assertIn('1880-01-01', data['species']['introduction'])
    #         self.assertIn(category.name, data['species']['category'])
    # # Basic happy path, ensure the /species/<id> DELETE route behaves correctly
    # def test_delete_single_species(self):
    #     category = create_category('Mammal')
    #     species = create_species('Norway rat', 'Rattus norvegicus',
    #                              'Brown or dark grey in colour.', '1880-01-01', category.id)
    #     with self.client:
    #         response = self.client.delete('/api/v1/species/%d' % species.id)
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn('Successfully deleted species.', data['status'])
if __name__ == '__main__':
    unittest.main()
