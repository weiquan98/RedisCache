# test_rediscache.py
"""
Tests for RedisCache module.
"""

import unittest
from rediscache import RedisCache

class TestRedisCache(unittest.TestCase):
    """Test cases for RedisCache class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RedisCache()
        self.assertIsInstance(instance, RedisCache)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RedisCache()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
