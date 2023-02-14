#!/usr/bin/python3
"""
test_base module
Tests the Base class and inherent methods
"""
import unittest
from models.base import Base


class Test_BaseClass(unittest.TestCase):
    """ Tests an instance of the base class """

    def test_id_none(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_int(self):
        base1 = Base(5)
        self.assertTrue(base1.id == 5)

    def test_id_any(self):
        base1 = Base("5")
        self.assertTrue(base1.id == "5") 
        
        
