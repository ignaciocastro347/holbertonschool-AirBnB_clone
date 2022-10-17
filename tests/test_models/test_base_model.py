#!/usr/bin/python3
""" Unittest for BaseModel class """
from pyexpat import model
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.b1 = BaseModel()

    def test_save(self):
        old_updated_at = self.b1.updated_at
        self.b1.save()
        self.assertTrue(old_updated_at != self.b1.updated_at)

    def test_to_dict(self):
        self.assertTrue(self.b1.to_dict(), self.b1.to_dict())
		
    def __str__(self):
        self.assertEqual(
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
            , model.__str__()
            )

if __name__ == "__main__":
    unittest.main()