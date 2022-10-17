#!/usr/bin/python3
""" Unittest for FileStorage class """
import unittest
from os.path import exists
from models.engine.file_storage import FileStorage
from models.user import User

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.f1 = FileStorage()

    def test_save(self):
        self.f1.save()
        self.assertTrue(exists("file.json"))

    def test_all(self):
        self.assertEqual(len(self.f1.all()), 0)
        user = User()
        self.assertEqual(len(self.f1.all()), 1)

    def test_new(self):
        self.assertTrue(True)

    def test_reload(self):
        self.assertTrue(True)
