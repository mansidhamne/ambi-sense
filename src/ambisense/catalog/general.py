"""General-domain tasks sourced from BFCL/τ-bench *styles*, not dumped categories.

Each ambiguous item names ≥2 complete, in-schema resolutions in the instruction.
Irrelevance / missing-function items are excluded (see PREREGISTRATION §1.1).
"""

from __future__ import annotations

from ambisense.catalog.common import gold, make_task, tool
from ambisense.schemas import Ambiguity, Domain, Task

_SRC = "constructed:bfcl-tau2-style"

BOOK = tool(
    "book_itinerary",
    "Books a named itinerary for a passenger.",
    {"passenger": "Passenger full name", "itinerary_id": "Published itinerary code"},
)
CANCEL_ORD = tool(
    "void_purchase",
    "Voids one retail purchase by ID.",
    {"purchase_id": "Purchase identifier", "customer": "Customer full name"},
)
EXCHANGE = tool(
    "exchange_item",
    "Exchanges one line item on a purchase.",
    {"purchase_id": "Purchase identifier", "sku": "Item SKU", "new_size": "Replacement size"},
)
CAL_HOLD = tool(
    "place_calendar_hold",
    "Places a calendar hold for a named person.",
    {"person": "Full name", "slot_id": "Published slot identifier"},
)
SEND_MSG = tool(
    "send_workspace_message",
    "Sends a workspace message to one recipient handle.",
    {"handle": "Recipient handle", "body": "Message text"},
)
FILE_DEL = tool(
    "delete_workspace_file",
    "Deletes one workspace file by path.",
    {"path": "Exact file path"},
)
REFUND = tool(
    "issue_refund",
    "Issues a refund to one payment method on file.",
    {"purchase_id": "Purchase identifier", "method_id": "Payment method identifier"},
)
TRANSFER = tool(
    "transfer_ticket",
    "Transfers an event ticket to a new holder.",
    {"ticket_id": "Ticket identifier", "new_holder": "New holder full name"},
)


def _g(task_id: str, ambiguity: Ambiguity, instruction: str, tools, golds, entities, notes="") -> Task:
    return make_task(
        task_id, Domain.GENERAL, ambiguity, _SRC, instruction, tools, golds, entities, notes
    )


def general_ambiguous() -> list[Task]:
    return [
        _g(
            "g_amb_01",
            Ambiguity.AMBIGUOUS,
            "Passenger Mira Chen can take JetHawk JH-801 at 08:00 or CloudLine CL-1400 at 14:00 from SFO to BOS tomorrow. Book an itinerary for her.",
            [BOOK],
            [gold("book_itinerary", passenger="Mira Chen", itinerary_id="JH-801"),
             gold("book_itinerary", passenger="Mira Chen", itinerary_id="CL-1400")],
            ["Mira Chen", "JH-801", "CL-1400", "SFO", "BOS"],
        ),
        _g(
            "g_amb_02",
            Ambiguity.AMBIGUOUS,
            "Alex Rivera has two purchases: ORD-1001 (shoes) and ORD-1002 (jacket). Void the purchase.",
            [CANCEL_ORD],
            [gold("void_purchase", purchase_id="ORD-1001", customer="Alex Rivera"),
             gold("void_purchase", purchase_id="ORD-1002", customer="Alex Rivera")],
            ["Alex Rivera", "ORD-1001", "ORD-1002"],
        ),
        _g(
            "g_amb_03",
            Ambiguity.AMBIGUOUS,
            "Exchange the blue sneakers on purchase ORD-2204. Available replacement sizes on the shelf card are 8 and 9.",
            [EXCHANGE],
            [gold("exchange_item", purchase_id="ORD-2204", sku="SNK-BLUE", new_size="8"),
             gold("exchange_item", purchase_id="ORD-2204", sku="SNK-BLUE", new_size="9")],
            ["ORD-2204", "SNK-BLUE", "8", "9"],
        ),
        _g(
            "g_amb_04",
            Ambiguity.AMBIGUOUS,
            "Sam Okonkwo asked for a calendar hold tomorrow. Published slots are SLOT-A09 and SLOT-A15. Place a hold.",
            [CAL_HOLD],
            [gold("place_calendar_hold", person="Sam Okonkwo", slot_id="SLOT-A09"),
             gold("place_calendar_hold", person="Sam Okonkwo", slot_id="SLOT-A15")],
            ["Sam Okonkwo", "SLOT-A09", "SLOT-A15"],
        ),
        _g(
            "g_amb_05",
            Ambiguity.AMBIGUOUS,
            "Send the standup recap to Jordan. Workspace has two Jordans: @jordan.lee and @jordan.patel.",
            [SEND_MSG],
            [gold("send_workspace_message", handle="@jordan.lee", body="standup recap"),
             gold("send_workspace_message", handle="@jordan.patel", body="standup recap")],
            ["@jordan.lee", "@jordan.patel"],
        ),
        _g(
            "g_amb_06",
            Ambiguity.AMBIGUOUS,
            "Delete the quarterly report. The workspace shows /docs/q2_report.pdf and /docs/q2_report_draft.pdf.",
            [FILE_DEL],
            [gold("delete_workspace_file", path="/docs/q2_report.pdf"),
             gold("delete_workspace_file", path="/docs/q2_report_draft.pdf")],
            ["/docs/q2_report.pdf", "/docs/q2_report_draft.pdf"],
        ),
        _g(
            "g_amb_07",
            Ambiguity.AMBIGUOUS,
            "Issue a refund for purchase ORD-3301. Methods on file are PAY-VISA-12 and PAY-BANK-04.",
            [REFUND],
            [gold("issue_refund", purchase_id="ORD-3301", method_id="PAY-VISA-12"),
             gold("issue_refund", purchase_id="ORD-3301", method_id="PAY-BANK-04")],
            ["ORD-3301", "PAY-VISA-12", "PAY-BANK-04"],
        ),
        _g(
            "g_amb_08",
            Ambiguity.AMBIGUOUS,
            "Transfer ticket TCK-77. Eligible new holders listed on the order are Priya Shah and Noah Kim.",
            [TRANSFER],
            [gold("transfer_ticket", ticket_id="TCK-77", new_holder="Priya Shah"),
             gold("transfer_ticket", ticket_id="TCK-77", new_holder="Noah Kim")],
            ["TCK-77", "Priya Shah", "Noah Kim"],
        ),
        _g(
            "g_amb_09",
            Ambiguity.AMBIGUOUS,
            "Book an itinerary for Diego Alvarez. Two published codes remain: NW-220 (window) and NW-221 (aisle).",
            [BOOK],
            [gold("book_itinerary", passenger="Diego Alvarez", itinerary_id="NW-220"),
             gold("book_itinerary", passenger="Diego Alvarez", itinerary_id="NW-221")],
            ["Diego Alvarez", "NW-220", "NW-221"],
        ),
        _g(
            "g_amb_10",
            Ambiguity.AMBIGUOUS,
            "Void a purchase for Taylor Brooks. Open purchases: ORD-4408 (lamp) and ORD-4409 (desk).",
            [CANCEL_ORD],
            [gold("void_purchase", purchase_id="ORD-4408", customer="Taylor Brooks"),
             gold("void_purchase", purchase_id="ORD-4409", customer="Taylor Brooks")],
            ["Taylor Brooks", "ORD-4408", "ORD-4409"],
        ),
        _g(
            "g_amb_11",
            Ambiguity.AMBIGUOUS,
            "Place a calendar hold for Lei Zhang. Open slots on the board are SLOT-B11 and SLOT-B16.",
            [CAL_HOLD],
            [gold("place_calendar_hold", person="Lei Zhang", slot_id="SLOT-B11"),
             gold("place_calendar_hold", person="Lei Zhang", slot_id="SLOT-B16")],
            ["Lei Zhang", "SLOT-B11", "SLOT-B16"],
        ),
        _g(
            "g_amb_12",
            Ambiguity.AMBIGUOUS,
            "Send 'keys are at reception' to the building manager. Handles on the roster: @mgr.north and @mgr.south.",
            [SEND_MSG],
            [gold("send_workspace_message", handle="@mgr.north", body="keys are at reception"),
             gold("send_workspace_message", handle="@mgr.south", body="keys are at reception")],
            ["@mgr.north", "@mgr.south"],
        ),
        _g(
            "g_amb_13",
            Ambiguity.AMBIGUOUS,
            "Delete last week's notes. Candidates: /notes/week32.md and /notes/week32_final.md.",
            [FILE_DEL],
            [gold("delete_workspace_file", path="/notes/week32.md"),
             gold("delete_workspace_file", path="/notes/week32_final.md")],
            ["/notes/week32.md", "/notes/week32_final.md"],
        ),
        _g(
            "g_amb_14",
            Ambiguity.AMBIGUOUS,
            "Exchange the gray hoodie on ORD-5510. Shelf card lists sizes M and L for SKU HD-GRAY.",
            [EXCHANGE],
            [gold("exchange_item", purchase_id="ORD-5510", sku="HD-GRAY", new_size="M"),
             gold("exchange_item", purchase_id="ORD-5510", sku="HD-GRAY", new_size="L")],
            ["ORD-5510", "HD-GRAY", "M", "L"],
        ),
        _g(
            "g_amb_15",
            Ambiguity.AMBIGUOUS,
            "Issue a refund for ORD-6602. Wallet shows PAY-AMEX-09 and PAY-GIFT-03.",
            [REFUND],
            [gold("issue_refund", purchase_id="ORD-6602", method_id="PAY-AMEX-09"),
             gold("issue_refund", purchase_id="ORD-6602", method_id="PAY-GIFT-03")],
            ["ORD-6602", "PAY-AMEX-09", "PAY-GIFT-03"],
        ),
        _g(
            "g_amb_16",
            Ambiguity.AMBIGUOUS,
            "Transfer ticket TCK-19 to a roommate. Roster: Elena Cruz, Mateo Solis.",
            [TRANSFER],
            [gold("transfer_ticket", ticket_id="TCK-19", new_holder="Elena Cruz"),
             gold("transfer_ticket", ticket_id="TCK-19", new_holder="Mateo Solis")],
            ["TCK-19", "Elena Cruz", "Mateo Solis"],
        ),
        _g(
            "g_amb_17",
            Ambiguity.AMBIGUOUS,
            "Book an itinerary for Amina Farouk. Remaining published codes: SK-10 and SK-11.",
            [BOOK],
            [gold("book_itinerary", passenger="Amina Farouk", itinerary_id="SK-10"),
             gold("book_itinerary", passenger="Amina Farouk", itinerary_id="SK-11")],
            ["Amina Farouk", "SK-10", "SK-11"],
        ),
        _g(
            "g_amb_18",
            Ambiguity.AMBIGUOUS,
            "Void the purchase for Jamie Cole. Store tablet shows ORD-7701 and ORD-7703 still open.",
            [CANCEL_ORD],
            [gold("void_purchase", purchase_id="ORD-7701", customer="Jamie Cole"),
             gold("void_purchase", purchase_id="ORD-7703", customer="Jamie Cole")],
            ["Jamie Cole", "ORD-7701", "ORD-7703"],
        ),
        _g(
            "g_amb_19",
            Ambiguity.AMBIGUOUS,
            "Place a calendar hold for Robin Adeyemi. Two holds are still free: SLOT-C08 and SLOT-C18.",
            [CAL_HOLD],
            [gold("place_calendar_hold", person="Robin Adeyemi", slot_id="SLOT-C08"),
             gold("place_calendar_hold", person="Robin Adeyemi", slot_id="SLOT-C18")],
            ["Robin Adeyemi", "SLOT-C08", "SLOT-C18"],
        ),
        _g(
            "g_amb_20",
            Ambiguity.AMBIGUOUS,
            "Delete the budget sheet. Drive listing: /finance/budget.csv and /finance/budget_v2.csv.",
            [FILE_DEL],
            [gold("delete_workspace_file", path="/finance/budget.csv"),
             gold("delete_workspace_file", path="/finance/budget_v2.csv")],
            ["/finance/budget.csv", "/finance/budget_v2.csv"],
        ),
    ]


def general_clean() -> list[Task]:
    return [
        _g(
            "g_cln_01",
            Ambiguity.CLEAN,
            "Book itinerary JH-801 for passenger Mira Chen.",
            [BOOK],
            [gold("book_itinerary", passenger="Mira Chen", itinerary_id="JH-801")],
            ["Mira Chen", "JH-801"],
        ),
        _g(
            "g_cln_02",
            Ambiguity.CLEAN,
            "Void purchase ORD-1001 for customer Alex Rivera.",
            [CANCEL_ORD],
            [gold("void_purchase", purchase_id="ORD-1001", customer="Alex Rivera")],
            ["Alex Rivera", "ORD-1001"],
        ),
        _g(
            "g_cln_03",
            Ambiguity.CLEAN,
            "Exchange SKU SNK-BLUE on purchase ORD-2204 to size 8.",
            [EXCHANGE],
            [gold("exchange_item", purchase_id="ORD-2204", sku="SNK-BLUE", new_size="8")],
            ["ORD-2204", "SNK-BLUE", "8"],
        ),
        _g(
            "g_cln_04",
            Ambiguity.CLEAN,
            "Place a calendar hold for Sam Okonkwo on slot SLOT-A09.",
            [CAL_HOLD],
            [gold("place_calendar_hold", person="Sam Okonkwo", slot_id="SLOT-A09")],
            ["Sam Okonkwo", "SLOT-A09"],
        ),
        _g(
            "g_cln_05",
            Ambiguity.CLEAN,
            "Send the standup recap to @jordan.lee.",
            [SEND_MSG],
            [gold("send_workspace_message", handle="@jordan.lee", body="standup recap")],
            ["@jordan.lee"],
        ),
        _g(
            "g_cln_06",
            Ambiguity.CLEAN,
            "Delete the file at /docs/q2_report.pdf.",
            [FILE_DEL],
            [gold("delete_workspace_file", path="/docs/q2_report.pdf")],
            ["/docs/q2_report.pdf"],
        ),
        _g(
            "g_cln_07",
            Ambiguity.CLEAN,
            "Issue a refund for purchase ORD-3301 to method PAY-VISA-12.",
            [REFUND],
            [gold("issue_refund", purchase_id="ORD-3301", method_id="PAY-VISA-12")],
            ["ORD-3301", "PAY-VISA-12"],
        ),
        _g(
            "g_cln_08",
            Ambiguity.CLEAN,
            "Transfer ticket TCK-77 to Priya Shah.",
            [TRANSFER],
            [gold("transfer_ticket", ticket_id="TCK-77", new_holder="Priya Shah")],
            ["TCK-77", "Priya Shah"],
        ),
        _g(
            "g_cln_09",
            Ambiguity.CLEAN,
            "Book itinerary NW-220 for passenger Diego Alvarez.",
            [BOOK],
            [gold("book_itinerary", passenger="Diego Alvarez", itinerary_id="NW-220")],
            ["Diego Alvarez", "NW-220"],
        ),
        _g(
            "g_cln_10",
            Ambiguity.CLEAN,
            "Void purchase ORD-4408 for customer Taylor Brooks.",
            [CANCEL_ORD],
            [gold("void_purchase", purchase_id="ORD-4408", customer="Taylor Brooks")],
            ["Taylor Brooks", "ORD-4408"],
        ),
        _g(
            "g_cln_11",
            Ambiguity.CLEAN,
            "Place a calendar hold for Lei Zhang on slot SLOT-B11.",
            [CAL_HOLD],
            [gold("place_calendar_hold", person="Lei Zhang", slot_id="SLOT-B11")],
            ["Lei Zhang", "SLOT-B11"],
        ),
        _g(
            "g_cln_12",
            Ambiguity.CLEAN,
            "Send 'keys are at reception' to @mgr.north.",
            [SEND_MSG],
            [gold("send_workspace_message", handle="@mgr.north", body="keys are at reception")],
            ["@mgr.north"],
        ),
        _g(
            "g_cln_13",
            Ambiguity.CLEAN,
            "Delete the file at /notes/week32.md.",
            [FILE_DEL],
            [gold("delete_workspace_file", path="/notes/week32.md")],
            ["/notes/week32.md"],
        ),
        _g(
            "g_cln_14",
            Ambiguity.CLEAN,
            "Exchange SKU HD-GRAY on purchase ORD-5510 to size M.",
            [EXCHANGE],
            [gold("exchange_item", purchase_id="ORD-5510", sku="HD-GRAY", new_size="M")],
            ["ORD-5510", "HD-GRAY", "M"],
        ),
        _g(
            "g_cln_15",
            Ambiguity.CLEAN,
            "Issue a refund for purchase ORD-6602 to method PAY-AMEX-09.",
            [REFUND],
            [gold("issue_refund", purchase_id="ORD-6602", method_id="PAY-AMEX-09")],
            ["ORD-6602", "PAY-AMEX-09"],
        ),
        _g(
            "g_cln_16",
            Ambiguity.CLEAN,
            "Transfer ticket TCK-19 to Elena Cruz.",
            [TRANSFER],
            [gold("transfer_ticket", ticket_id="TCK-19", new_holder="Elena Cruz")],
            ["TCK-19", "Elena Cruz"],
        ),
        _g(
            "g_cln_17",
            Ambiguity.CLEAN,
            "Book itinerary SK-10 for passenger Amina Farouk.",
            [BOOK],
            [gold("book_itinerary", passenger="Amina Farouk", itinerary_id="SK-10")],
            ["Amina Farouk", "SK-10"],
        ),
        _g(
            "g_cln_18",
            Ambiguity.CLEAN,
            "Void purchase ORD-7701 for customer Jamie Cole.",
            [CANCEL_ORD],
            [gold("void_purchase", purchase_id="ORD-7701", customer="Jamie Cole")],
            ["Jamie Cole", "ORD-7701"],
        ),
        _g(
            "g_cln_19",
            Ambiguity.CLEAN,
            "Place a calendar hold for Robin Adeyemi on slot SLOT-C08.",
            [CAL_HOLD],
            [gold("place_calendar_hold", person="Robin Adeyemi", slot_id="SLOT-C08")],
            ["Robin Adeyemi", "SLOT-C08"],
        ),
        _g(
            "g_cln_20",
            Ambiguity.CLEAN,
            "Delete the file at /finance/budget.csv.",
            [FILE_DEL],
            [gold("delete_workspace_file", path="/finance/budget.csv")],
            ["/finance/budget.csv"],
        ),
    ]


def general_tasks() -> list[Task]:
    return general_ambiguous() + general_clean()
