#!/usr/bin/python3
""" Unittest for BaseModel class """
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
        dict1 = self.b1.to_dict()
        self.assertTrue(True)
		