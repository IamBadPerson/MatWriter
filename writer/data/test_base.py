from unittest import TestCase
from .base import Data

from tinydb_base import DatabaseBase

class BaseTest(TestCase):

    def test_init(self):

        obj = Data(test=True)
        
        self.assertIsInstance(obj, DatabaseBase)
