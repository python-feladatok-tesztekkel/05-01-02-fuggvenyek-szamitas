from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestMertani(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.mertani_kozep(4,5)
        elvart = 4.47
        self.assertEqual(elvart, aktualis, "A mértani közepet nem jól határozta meg!")
    def test_feladat02(self):
        aktualis = feladatok.mertani_kozep(1,5)
        elvart = 2.24
        self.assertEqual(elvart, aktualis, "A mértani közepet nem jól határozta meg!")