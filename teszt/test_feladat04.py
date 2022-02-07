from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestMasodfokuEgyenlet(TestCase):
    def test_feladat01(self):
        aktualis_rendezendo = feladatok.masodfoku_egyenlet(5, -3, -2)
        if (aktualis_rendezendo[0]<aktualis_rendezendo[1]):
            aktualis=[aktualis_rendezendo[1],aktualis_rendezendo[2]]
        else:
            aktualis=aktualis_rendezendo
        elvart = [1,-0.4]
        self.assertEqual(elvart, aktualis, "A másodfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat02(self):
        aktualis_rendezendo = feladatok.masodfoku_egyenlet(1, 1, -2)
        if (aktualis_rendezendo[0]<aktualis_rendezendo[1]):
            aktualis=[aktualis_rendezendo[1],aktualis_rendezendo[2]]
        else:
            aktualis=aktualis_rendezendo
        elvart = [1,-2]
        self.assertEqual(elvart, aktualis, "A másodfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat03(self):
        aktualis_rendezendo = feladatok.masodfoku_egyenlet(5, 0, -80)
        if (aktualis_rendezendo[0]<aktualis_rendezendo[1]):
            aktualis=[aktualis_rendezendo[1],aktualis_rendezendo[2]]
        else:
            aktualis=aktualis_rendezendo
        elvart = [4, -4]
        self.assertEqual(elvart, aktualis, "A másodfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat04(self):
        aktualis_rendezendo = feladatok.masodfoku_egyenlet(1, -9, 0)
        if (aktualis_rendezendo[0]<aktualis_rendezendo[1]):
            aktualis=[aktualis_rendezendo[1],aktualis_rendezendo[2]]
        else:
            aktualis=aktualis_rendezendo
        elvart = [9,0]
        self.assertEqual(elvart, aktualis, "A másodfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat05(self):
        aktualis= feladatok.masodfoku_egyenlet(1, -14, 49)
        elvart = 7
        self.assertEqual(elvart, aktualis, "A másodfokú egyenlet megoldását nem jól határozta meg!")
    def test_feladat06(self):
        aktualis= feladatok.masodfoku_egyenlet(1, -8, 25)
        elvart = None
        self.assertEqual(elvart, aktualis, "A másodfokú egyenlet megoldását nem jól határozta meg!")
