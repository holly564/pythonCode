from unittest import TestCase
from unittest.mock import Mock
import unittest.main
from src.reusabletimer import ReusableTimer
from src.bag import Bag
from random import randint

class MyTestCase(TestCase):
    def test_start(self):
        timer = Mock(spec=ReusableTimer)
        fingerprint = Mock(spec)
        bag = Bag(timer)
        bag.set_location('Ottawa')
        bag.get_temperature() # or we could mock temperature
        self.assertFalse(bag.readiness)
        bag.charge_battery(100 * randint(1, 10))
        bag.place_contents()
        # self.assertAlmostEqual()

    def test_end(self):
        timer = Mock(spec=ReusableTimer)
        bag = Bag()
        bag.remove_contents()


if __name__ == '__main__':
    unittest.main()
