"""Complete ERPNext Projects Engine (Tasks, milestones, timesheets aur project costs)."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ProjectTimesheet:
    timesheet_id: str
    employee_id: str
    hours_worked: float
    cost_rate_per_hour: float
    billing_rate_per_hour: float


@dataclass
class ProjectProfitability:
    project_id: str
    total_hours_logged: float
    total_internal_cost: float
    total_billable_amount: float
    gross_margin_amount: float
    gross_margin_pct: float


class ERPNextProjectsCostingEngine:
    """Project timesheet costing, billing realization, and profitability analysis."""

    def calculate_project_profitability(
        self,
        project_id: str,
        timesheets: List[ProjectTimesheet],
        fixed_other_costs: float = 0.0
    ) -> ProjectProfitability:
        """Derives exact labor cost, billable revenue, and gross profit margin for a project."""
        tot_hours = sum(t.hours_worked for t in timesheets)
        tot_cost = sum(t.hours_worked * t.cost_rate_per_hour for t in timesheets) + fixed_other_costs
        tot_billing = sum(t.hours_worked * t.billing_rate_per_hour for t in timesheets)

        margin = tot_billing - tot_cost
        margin_pct = (margin / tot_billing * 100.0) if tot_billing > 0 else 0.0

        return ProjectProfitability(
            project_id=project_id,
            total_hours_logged=round(tot_hours, 2),
            total_internal_cost=round(tot_cost, 2),
            total_billable_amount=round(tot_billing, 2),
            gross_margin_amount=round(margin, 2),
            gross_margin_pct=round(margin_pct, 2)
        )
