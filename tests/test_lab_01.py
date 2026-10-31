import unittest

from labs.lab_01_python_basics.starter import convert_temperature


class TemperatureTests(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(convert_temperature(0), 32)

    def test_negative_temperature(self):
        self.assertAlmostEqual(convert_temperature(-40), -40)


if __name__ == "__main__":
    unittest.main()
