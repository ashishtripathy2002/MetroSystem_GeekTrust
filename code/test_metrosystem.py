import unittest
from io import StringIO
import sys
from unittest.mock import patch

from geektrust import *

class TestCardAndStations(unittest.TestCase):
    def setUp(self):
        self.card = CARD("MC1", 600)
        self.station = STATION("AIRPORT")
    
    def test_get_trip_fare_no_discount(self):
        total_fare, discount = self.card.get_trip_fare("ADULT")
        self.assertEqual(total_fare, 200.0)
        self.assertEqual(discount, 0.0)
    
    def test_get_trip_fare_with_discount(self):
        self.card.single_trip_status = True
        total_fare, discount = self.card.get_trip_fare("ADULT")
        self.assertEqual(total_fare, 100.0)
        self.assertEqual(discount, 100.0)
    
    def test_set_wallet_balance_no_recharge(self):
        total_fare = 100.0
        final_total_fare = self.card.set_wallet_balance(total_fare)
        self.assertEqual(final_total_fare,100.0)
    
    def test_set_wallet_balance_with_recharge(self):
        total_fare = 700.0
        final_total_fare = self.card.set_wallet_balance(total_fare)
        self.assertEqual(final_total_fare, 702.0)
    
    def test_put_traveller_entry(self):
        self.station.put_traveller_entry("ADULT", 200.0, 0.0)
        self.assertEqual(self.station.passenger_age_cnt["ADULT"], 1)
        self.assertEqual(self.station.total_sale, 200.0)
        self.assertEqual(self.station.total_discount, 0.0)

class TestInputManager(unittest.TestCase):
    def test_card_manager(self):
        card_db = card_manager("MC1", 600, {})
        self.assertEqual(len(card_db), 1)
        self.assertIn("MC1", card_db)
    
    def test_get_trip_summary(self):
        card = CARD("MC1", 600)
        total_fare, discount, updated_card = get_trip_summary(card, "ADULT")
        self.assertEqual(total_fare, 200.0)
        self.assertEqual(discount, 0.0)
    
    @patch("sys.stdout", new_callable=StringIO)
    def test_input_manager(self, mock_stdout):
        lines = [
            "BALANCE MC1 600\n",
            "CHECK_IN MC1 ADULT AIRPORT\n",
            "PRINT_SUMMARY\n"
        ]
        input_manager(lines)
        output = mock_stdout.getvalue()
        self.assertIn("TOTAL_COLLECTION AIRPORT", output)
        self.assertIn("PASSENGER_TYPE_SUMMARY", output)
        self.assertIn("ADULT 1", output)
    
if __name__ == "__main__":
    unittest.main()
