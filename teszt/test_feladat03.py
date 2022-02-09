from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestEgyenlet(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.elsofoku_egyenlet(1,10)
        elvart = -10
        self.assertEqual(elvart, aktualis, "Az elsőfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat02(self):
        aktualis = feladatok.elsofoku_egyenlet(10,1)
        elvart = -0.1
        self.assertEqual(elvart, aktualis, "Az elsőfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat03(self):
        aktualis = feladatok.elsofoku_egyenlet(100,1567)
        elvart = -15.67
        self.assertEqual(elvart, aktualis, "Az elsőfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat04(self):
        aktualis = feladatok.elsofoku_egyenlet(-100, 1567)
        elvart = 15.67
        self.assertEqual(elvart, aktualis, "Az elsőfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat05(self):
        aktualis = feladatok.elsofoku_egyenlet(0, 1)
        elvart = None
        self.assertEqual(elvart, aktualis, "Az elsőfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat06(self):
        aktualis = feladatok.elsofoku_egyenlet(0, 0)
        elvart = None
        self.assertEqual(elvart, aktualis, "Az elsőfokú egyenlet megoldását nem jól határozta meg!")
