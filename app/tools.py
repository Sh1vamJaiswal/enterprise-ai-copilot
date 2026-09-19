from typing import Optional

from langchain_core.tools import tool


@tool
def create_it_ticket(
    employee_id: str,
    issue: str,
    priority: str = "medium",
) -> str:
    """Create an IT support ticket for an employee's technical issue."""

    valid_priorities = {"low", "medium", "high", "critical"}

    if priority.lower() not in valid_priorities:
        return (
            f"Invalid priority '{priority}'. "
            f"Choose from: {', '.join(sorted(valid_priorities))}."
        )

    ticket_id = "IT-" + employee_id[-4:] + "-001"

    return (
        f"** IT ticket created successfully.**\n\n"
        f"**Ticket ID:** {ticket_id}\n"
        f"**Employee ID:** {employee_id}\n"
        f"**Issue:** {issue}\n"
        f"**Priority:** {priority.lower().capitalize()}"
    )


@tool
def check_ticket_status(ticket_id: str) -> str:
    """Check the current status of an IT support ticket."""

    demo_tickets = {
        "IT-1025-001": {
            "status": "Open",
            "priority": "High",
            "assigned_to": "IT Support Team",
        },
        "IT-2048-001": {
            "status": "In Progress",
            "priority": "Medium",
            "assigned_to": "Network Support Team",
        },
    }

    ticket = demo_tickets.get(ticket_id)

    if not ticket:
        return f"No ticket found with ID {ticket_id}."

    return (
        f"Ticket ID: {ticket_id}\n"
        f"Status: {ticket['status']}\n"
        f"Priority: {ticket['priority']}\n"
        f"Assigned to: {ticket['assigned_to']}"
    )

@tool
def calculate_expense(
    amount: float,
    category: str,
    tax_rate: float = 0.0,
) -> str:
    """Calculate the final reimbursable expense amount after applying tax.

tax_rate must be provided as a percentage value, such as 18 for 18%,
not as a decimal such as 0.18.
"""

    if amount < 0:
        return "Expense amount cannot be negative."

    if tax_rate < 0 or tax_rate > 100:
        return "Tax rate must be between 0 and 100."

    tax_amount = amount * (tax_rate / 100)
    total_amount = amount + tax_amount

    return (
        f"Expense calculation completed.\n"
        f"Category: {category}\n"
        f"Base amount: {amount:.2f}\n"
        f"Tax: {tax_amount:.2f}\n"
        f"Total amount: {total_amount:.2f}"
    )


@tool
def search_knowledge_base(question: str) -> str:
    """Search the enterprise knowledge base and answer questions using company documents."""

    from app.rag import answer_question

    return answer_question(question)