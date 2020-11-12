import unittest
import main


class GetPowerDaysTest(unittest.TestCase):

    def test_get_days_of_power(self):
        days = main.get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
        self.assertEqual(days, 141)
        days = main.get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
        self.assertEqual(days, 17)
        days = main.get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
        self.assertEqual(days, 5)
        days = main.get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
        self.assertEqual(days, 1)


if __name__ == '__main__':
    unittest.main()
