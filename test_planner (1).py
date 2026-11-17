import unittest
from datetime import date
from planner import *
T = date(2026,11,17)
class Tests(unittest.TestCase):
    def test_tc01_register_ok(self): self.assertTrue(register({}, "a@b.com", "password1"))
    def test_tc02_bad_email(self):
        with self.assertRaises(ValueError): register({}, "ab.com", "password1")
    def test_tc03_weak_pw(self):
        with self.assertRaises(ValueError): register({}, "a@b.com", "123")
    def test_tc04_duplicate(self):
        with self.assertRaises(KeyError): register({"a@b.com":"x"}, "a@b.com", "password1")
    def test_tc05_priority_order(self):
        r = prioritize([{"title":"Far","due":date(2026,12,20),"difficulty":2},
                        {"title":"Near","due":date(2026,11,18),"difficulty":2}], T)
        self.assertEqual(r[0]["title"], "Near")
    def test_tc06_overdue_max_urgency(self):
        r = prioritize([{"title":"Late","due":date(2026,11,1),"difficulty":1}], T)
        self.assertEqual(r[0]["score"], 11)
    def test_tc07_difficulty_range(self):
        with self.assertRaises(ValueError): prioritize([{"title":"x","due":T,"difficulty":9}], T)
    def test_tc08_empty_title(self):
        with self.assertRaises(ValueError): prioritize([{"title":"","due":T,"difficulty":2}], T)
    def test_tc09_schedule_split(self):
        p = build_schedule([{"title":"A","due":date(2026,11,19),"difficulty":3,"hours":5}], T, 3)
        self.assertEqual(p["2026-11-17"], [("A",3)]); self.assertEqual(p["2026-11-18"], [("A",2)])
    def test_tc10_zero_hours(self):
        with self.assertRaises(ValueError): build_schedule([], T, 0)
    def test_tc11_empty_list(self): self.assertEqual(prioritize([], T), [])
    def test_tc12_wrong_type(self):
        with self.assertRaises(TypeError): prioritize("abc", T)
if __name__ == "__main__": unittest.main(verbosity=2)
