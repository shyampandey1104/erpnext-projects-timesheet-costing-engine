import unittest
from projects_costing.engine import ERPNextProjectsCostingEngine, ProjectTimesheet

class TestProjectsCosting(unittest.TestCase):
    def test_project_margin_calculation(self):
        engine = ERPNextProjectsCostingEngine()
        timesheets = [
            ProjectTimesheet("TS-01", "EMP-A", 40.0, cost_rate_per_hour=500.0, billing_rate_per_hour=1500.0),
            ProjectTimesheet("TS-02", "EMP-B", 20.0, cost_rate_per_hour=800.0, billing_rate_per_hour=2000.0)
        ]
        # Total billing = 40*1500 + 20*2000 = 60,000 + 40,000 = 100,000
        # Total cost = 40*500 + 20*800 = 20,000 + 16,000 = 36,000
        # Margin = 64,000 (64.0%)
        res = engine.calculate_project_profitability("PROJ-MOBILE-APP", timesheets)
        self.assertEqual(res.total_billable_amount, 100000.0)
        self.assertEqual(res.total_internal_cost, 36000.0)
        self.assertEqual(res.gross_margin_amount, 64000.0)
        self.assertEqual(res.gross_margin_pct, 64.0)

if __name__ == "__main__":
    unittest.main()
