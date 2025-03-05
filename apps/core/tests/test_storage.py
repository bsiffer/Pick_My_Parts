import unittest
from apps.core.models.storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage(
            "Samsung", "980 Pro", 987654, 129.99, "SSD", 1024, "NVMe"
        )

    def test_storage_type(self):
        self.assertEqual(self.storage.storage_type, "SSD")

    def test_size(self):
        self.assertEqual(self.storage.size, 1024)

    def test_compatibility(self):
        self.assertEqual(self.storage.compatibility, "NVMe")

if __name__ == '__main__':
    unittest.main()