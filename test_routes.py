import bottle
import unittest
from boddle import boddle
from routes import home, about

class TestHome(unittest.TestCase):
    def test_home_exists(self):
        with boddle(path='/'):
            self.assertEqual(bottle.request.path, '/')

    def test_home_status(self):
        with boddle(path='/'):
            home()
            self.assertEqual(bottle.response.status_code, 200)     

    def test_home_page_content(self):
        with boddle():
            expected = "You don't need toast for breakfast"
            output = home()
            self.assertIn(expected, output)

class TestAbout(unittest.TestCase):
    def test_about_exists(self):
        with boddle(path='/about'):
            self.assertEqual(bottle.request.path, '/about')

    def test_about_status(self):
        with boddle(path='/about'):
            about()
            self.assertEqual(bottle.response.status_code, 200)

    def test_about_page_content(self):
        with boddle():
            expected = "Let us begin with your health."
            output = about()
            self.assertIn(expected, output)

if __name__ == '__main__':
    unittest.main()