import unittest
from perfect_number import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            get_index = a.get('/')
            self.assertEqual(get_index._status_code, 200)
            post_index_add = a.post('/', data={'start':'1', 'end':'1000', 'submit1': 'List Numbers'})
            post_index_sub = a.post('/', data={'num':'6', 'submit2': 'Is a Perfect Number'})
            self.assertEqual(post_index_add._status_code, 302)
            self.assertEqual(post_index_sub._status_code, 302)

    def test_list(self):
        with app.test_client() as a:
            get_add = a.get('/list', query_string={'start':'1', 'end':'1000'})
            self.assertEqual(get_add._status_code, 200)
            result_string = get_add.get_data(as_text=True)
            self.assertEqual(result_string, 'These are the numbers [6, 28, 496]')

    def test_perfect(self):
        with app.test_client() as a:
            get_sub = a.get('/perfect', query_string={'num':'6'})
            self.assertEqual(get_sub._status_code, 200)
            result_string = get_sub.get_data(as_text=True)
            self.assertEqual(result_string, '6 is a perfect number')

if __name__ == '__main__':
    unittest.main()
