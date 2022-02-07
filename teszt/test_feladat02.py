from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestGomb(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.gomb_felszin(1)
        elvart = 12.5664
        self.assertEqual(elvart, aktualis, "A gömb felszínét nem jól határozta meg!")
    def test_feladat02(self):
        aktualis = feladatok.gomb_felszin(1.1111)
        elvart = 15.5137
        self.assertEqual(elvart, aktualis, "A gömb felszínét nem jól határozta meg!")