import unittest
from main import is_prime, get_primes

class TestPrimeFunctions(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))

    def test_get_primes(self):
        self.assertEqual(get_primes(10), [2, 3, 5, 7])

if __name__ == "__main__":
    unittest.main()
