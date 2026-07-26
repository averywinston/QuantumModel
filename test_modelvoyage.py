# test_modelvoyage.py
"""
Tests for ModelVoyage module.
"""

import unittest
from modelvoyage import ModelVoyage

class TestModelVoyage(unittest.TestCase):
    """Test cases for ModelVoyage class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelVoyage()
        self.assertIsInstance(instance, ModelVoyage)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelVoyage()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
