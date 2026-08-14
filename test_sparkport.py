# test_sparkport.py
"""
Tests for SparkPort module.
"""

import unittest
from sparkport import SparkPort

class TestSparkPort(unittest.TestCase):
    """Test cases for SparkPort class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkPort()
        self.assertIsInstance(instance, SparkPort)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkPort()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
