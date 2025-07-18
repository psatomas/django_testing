import unittest

from app import Superhero


class TestSuperhero(unittest.TestCase):
    def setUp(self):
        self.superhero = Superhero("Superman", strength_level=50)

    def test_stringfy(self):        
        self.assertEqual(str(self.superhero), "Superman")

    def test_is_stronger_than_other_superhero(self):
        other_superhero = Superhero("Batman", strength_level=35)

        self.assertTrue(self.superhero.is_stronger_than(other_superhero))
        self.assertFalse(other_superhero.is_stronger_than(self.superhero))
