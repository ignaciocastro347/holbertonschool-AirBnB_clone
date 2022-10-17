#!/usr/bin/python3
""" Unittest for Review class """

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review(self):
        model = Review()
        self.assertTrue(type(model.name) is str)

if __name__ == "__main__":
    unittest.main()