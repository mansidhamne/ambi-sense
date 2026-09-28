"""Synthetic Nimbus Ward / HelixDose tasks. Invented IDs and units only.

These are not medical advice and must not be read as clinical guidance.
Protocols (HX-7, HX-9) and units (helix-units) are fictional.
"""

from __future__ import annotations

from ambisense.catalog.common import gold, make_task, tool
from ambisense.schemas import Ambiguity, Domain, Task

_SRC = "synthetic:nimbus-ward"

TITRATE = tool(
    "compute_helixdose",
    "Computes a fictional HelixDose titration in helix-units for a chart subject.",
    {
        "subject_id": "Fake chart ID of the form PT-NX-####",
        "protocol": "Fictional protocol code",
        "start_units": "Starting helix-units as a numeral string",
    },
)
FOLLOW = tool(
    "book_nimbus_followup",
    "Books a Nimbus Ward follow-up slot for a chart subject.",
    {"subject_id": "Fake chart ID", "slot_id": "Published ward slot"},
)
FLAG = tool(
    "flag_helix_overlap",
    "Flags an overlap between two fictional HelixDose protocols on one chart.",
    {"subject_id": "Fake chart ID", "protocol_a": "First protocol", "protocol_b": "Second protocol"},
)
LOOKUP = tool(
    "retrieve_nimbus_chart",
    "Retrieves one Nimbus Ward chart by fake ID.",
    {"subject_id": "Fake chart ID"},
)
HOLD_MED = tool(
    "park_helix_token",
    "Parks a fictional Helix token on a pump station (not a real medication).",
    {"subject_id": "Fake chart ID", "station_id": "Pump station ID", "token_id": "Token ID"},
)
SHIFT = tool(
    "assign_nimbus_shift",
    "Assigns a chart subject to a Nimbus observation shift.",
    {"subject_id": "Fake chart ID", "shift_id": "Shift identifier"},
)


def _c(task_id: str, ambiguity: Ambiguity, instruction: str, tools, golds, entities, notes="") -> Task:
    return make_task(
        task_id, Domain.CLINICAL, ambiguity, _SRC, instruction, tools, golds, entities, notes
    )


def clinical_ambiguous() -> list[Task]:
    return [
        _c(
            "c_amb_01",
            Ambiguity.AMBIGUOUS,
            "Nimbus board lists PT-NX-4419 and PT-NX-4420. Compute HelixDose with protocol HX-7 starting at 2 helix-units for the chart subject.",
            [TITRATE],
            [gold("compute_helixdose", subject_id="PT-NX-4419", protocol="HX-7", start_units="2"),
             gold("compute_helixdose", subject_id="PT-NX-4420", protocol="HX-7", start_units="2")],
            ["PT-NX-4419", "PT-NX-4420", "HX-7", "2"],
        ),
        _c(
            "c_amb_02",
            Ambiguity.AMBIGUOUS,
            "Book a Nimbus follow-up for PT-NX-1103. Open slots on the kiosk are NMB-0800 and NMB-1400.",
            [FOLLOW],
            [gold("book_nimbus_followup", subject_id="PT-NX-1103", slot_id="NMB-0800"),
             gold("book_nimbus_followup", subject_id="PT-NX-1103", slot_id="NMB-1400")],
            ["PT-NX-1103", "NMB-0800", "NMB-1400"],
        ),
        _c(
            "c_amb_03",
            Ambiguity.AMBIGUOUS,
            "Flag a Helix overlap on PT-NX-3308. The card shows HX-7 with HX-9 and also HX-7 with HX-12 as candidate pairs.",
            [FLAG],
            [gold("flag_helix_overlap", subject_id="PT-NX-3308", protocol_a="HX-7", protocol_b="HX-9"),
             gold("flag_helix_overlap", subject_id="PT-NX-3308", protocol_a="HX-7", protocol_b="HX-12")],
            ["PT-NX-3308", "HX-7", "HX-9", "HX-12"],
        ),
        _c(
            "c_amb_04",
            Ambiguity.AMBIGUOUS,
            "Retrieve the Nimbus chart. The clipboard has PT-NX-5501 and PT-NX-5502.",
            [LOOKUP],
            [gold("retrieve_nimbus_chart", subject_id="PT-NX-5501"),
             gold("retrieve_nimbus_chart", subject_id="PT-NX-5502")],
            ["PT-NX-5501", "PT-NX-5502"],
        ),
        _c(
            "c_amb_05",
            Ambiguity.AMBIGUOUS,
            "Park Helix token TOK-3 for PT-NX-2207. Stations listed: ST-ALPHA and ST-BETA.",
            [HOLD_MED],
            [gold("park_helix_token", subject_id="PT-NX-2207", station_id="ST-ALPHA", token_id="TOK-3"),
             gold("park_helix_token", subject_id="PT-NX-2207", station_id="ST-BETA", token_id="TOK-3")],
            ["PT-NX-2207", "ST-ALPHA", "ST-BETA", "TOK-3"],
        ),
        _c(
            "c_amb_06",
            Ambiguity.AMBIGUOUS,
            "Assign PT-NX-8804 to a Nimbus observation shift. Posted shifts: SH-AM and SH-PM.",
            [SHIFT],
            [gold("assign_nimbus_shift", subject_id="PT-NX-8804", shift_id="SH-AM"),
             gold("assign_nimbus_shift", subject_id="PT-NX-8804", shift_id="SH-PM")],
            ["PT-NX-8804", "SH-AM", "SH-PM"],
        ),
        _c(
            "c_amb_07",
            Ambiguity.AMBIGUOUS,
            "Compute HelixDose for PT-NX-4419. The tray lists protocol HX-7 starting at 2 helix-units and protocol HX-9 starting at 2 helix-units.",
            [TITRATE],
            [gold("compute_helixdose", subject_id="PT-NX-4419", protocol="HX-7", start_units="2"),
             gold("compute_helixdose", subject_id="PT-NX-4419", protocol="HX-9", start_units="2")],
            ["PT-NX-4419", "HX-7", "HX-9", "2"],
        ),
        _c(
            "c_amb_08",
            Ambiguity.AMBIGUOUS,
            "Book a Nimbus follow-up. Slot NMB-1000 is free for both PT-NX-1103 and PT-NX-1108.",
            [FOLLOW],
            [gold("book_nimbus_followup", subject_id="PT-NX-1103", slot_id="NMB-1000"),
             gold("book_nimbus_followup", subject_id="PT-NX-1108", slot_id="NMB-1000")],
            ["PT-NX-1103", "PT-NX-1108", "NMB-1000"],
        ),
        _c(
            "c_amb_09",
            Ambiguity.AMBIGUOUS,
            "Retrieve a Nimbus chart for the morning huddle. Stickers show PT-NX-6601 and PT-NX-6604.",
            [LOOKUP],
            [gold("retrieve_nimbus_chart", subject_id="PT-NX-6601"),
             gold("retrieve_nimbus_chart", subject_id="PT-NX-6604")],
            ["PT-NX-6601", "PT-NX-6604"],
        ),
        _c(
            "c_amb_10",
            Ambiguity.AMBIGUOUS,
            "Park token TOK-8. The slip names PT-NX-2207 at ST-GAMMA and PT-NX-2211 at ST-GAMMA.",
            [HOLD_MED],
            [gold("park_helix_token", subject_id="PT-NX-2207", station_id="ST-GAMMA", token_id="TOK-8"),
             gold("park_helix_token", subject_id="PT-NX-2211", station_id="ST-GAMMA", token_id="TOK-8")],
            ["PT-NX-2207", "PT-NX-2211", "ST-GAMMA", "TOK-8"],
        ),
        _c(
            "c_amb_11",
            Ambiguity.AMBIGUOUS,
            "Assign a Nimbus observation shift SH-EVE. Eligible chart subjects: PT-NX-8804 and PT-NX-8810.",
            [SHIFT],
            [gold("assign_nimbus_shift", subject_id="PT-NX-8804", shift_id="SH-EVE"),
             gold("assign_nimbus_shift", subject_id="PT-NX-8810", shift_id="SH-EVE")],
            ["PT-NX-8804", "PT-NX-8810", "SH-EVE"],
        ),
        _c(
            "c_amb_12",
            Ambiguity.AMBIGUOUS,
            "Flag a Helix overlap. For PT-NX-3308 the night note mentions HX-9 vs HX-12; for PT-NX-3310 it mentions the same pair.",
            [FLAG],
            [gold("flag_helix_overlap", subject_id="PT-NX-3308", protocol_a="HX-9", protocol_b="HX-12"),
             gold("flag_helix_overlap", subject_id="PT-NX-3310", protocol_a="HX-9", protocol_b="HX-12")],
            ["PT-NX-3308", "PT-NX-3310", "HX-9", "HX-12"],
        ),
        _c(
            "c_amb_13",
            Ambiguity.AMBIGUOUS,
            "Compute HelixDose protocol HX-12 starting at 4 helix-units. Two subjects are tagged: PT-NX-9901 and PT-NX-9902.",
            [TITRATE],
            [gold("compute_helixdose", subject_id="PT-NX-9901", protocol="HX-12", start_units="4"),
             gold("compute_helixdose", subject_id="PT-NX-9902", protocol="HX-12", start_units="4")],
            ["PT-NX-9901", "PT-NX-9902", "HX-12", "4"],
        ),
        _c(
            "c_amb_14",
            Ambiguity.AMBIGUOUS,
            "Book a Nimbus follow-up for PT-NX-7755. Kiosk leftovers: NMB-0900 and NMB-1630.",
            [FOLLOW],
            [gold("book_nimbus_followup", subject_id="PT-NX-7755", slot_id="NMB-0900"),
             gold("book_nimbus_followup", subject_id="PT-NX-7755", slot_id="NMB-1630")],
            ["PT-NX-7755", "NMB-0900", "NMB-1630"],
        ),
        _c(
            "c_amb_15",
            Ambiguity.AMBIGUOUS,
            "Retrieve the Nimbus chart marked 'priority'. The stack has PT-NX-1010 and PT-NX-1012 both marked priority.",
            [LOOKUP],
            [gold("retrieve_nimbus_chart", subject_id="PT-NX-1010"),
             gold("retrieve_nimbus_chart", subject_id="PT-NX-1012")],
            ["PT-NX-1010", "PT-NX-1012"],
        ),
        _c(
            "c_amb_16",
            Ambiguity.AMBIGUOUS,
            "Park Helix token TOK-1 for PT-NX-4040. Stations still open: ST-DELTA and ST-EPSILON.",
            [HOLD_MED],
            [gold("park_helix_token", subject_id="PT-NX-4040", station_id="ST-DELTA", token_id="TOK-1"),
             gold("park_helix_token", subject_id="PT-NX-4040", station_id="ST-EPSILON", token_id="TOK-1")],
            ["PT-NX-4040", "ST-DELTA", "ST-EPSILON", "TOK-1"],
        ),
    ]


def clinical_clean() -> list[Task]:
    return [
        _c(
            "c_cln_01",
            Ambiguity.CLEAN,
            "Compute HelixDose for PT-NX-4419 using protocol HX-7 starting at 2 helix-units.",
            [TITRATE],
            [gold("compute_helixdose", subject_id="PT-NX-4419", protocol="HX-7", start_units="2")],
            ["PT-NX-4419", "HX-7", "2"],
        ),
        _c(
            "c_cln_02",
            Ambiguity.CLEAN,
            "Book a Nimbus follow-up for PT-NX-1103 on slot NMB-0800.",
            [FOLLOW],
            [gold("book_nimbus_followup", subject_id="PT-NX-1103", slot_id="NMB-0800")],
            ["PT-NX-1103", "NMB-0800"],
        ),
        _c(
            "c_cln_03",
            Ambiguity.CLEAN,
            "Flag a Helix overlap on PT-NX-3308 between HX-7 and HX-9.",
            [FLAG],
            [gold("flag_helix_overlap", subject_id="PT-NX-3308", protocol_a="HX-7", protocol_b="HX-9")],
            ["PT-NX-3308", "HX-7", "HX-9"],
        ),
        _c(
            "c_cln_04",
            Ambiguity.CLEAN,
            "Retrieve the Nimbus chart PT-NX-5501.",
            [LOOKUP],
            [gold("retrieve_nimbus_chart", subject_id="PT-NX-5501")],
            ["PT-NX-5501"],
        ),
        _c(
            "c_cln_05",
            Ambiguity.CLEAN,
            "Park Helix token TOK-3 for PT-NX-2207 at station ST-ALPHA.",
            [HOLD_MED],
            [gold("park_helix_token", subject_id="PT-NX-2207", station_id="ST-ALPHA", token_id="TOK-3")],
            ["PT-NX-2207", "ST-ALPHA", "TOK-3"],
        ),
        _c(
            "c_cln_06",
            Ambiguity.CLEAN,
            "Assign PT-NX-8804 to Nimbus observation shift SH-AM.",
            [SHIFT],
            [gold("assign_nimbus_shift", subject_id="PT-NX-8804", shift_id="SH-AM")],
            ["PT-NX-8804", "SH-AM"],
        ),
        _c(
            "c_cln_07",
            Ambiguity.CLEAN,
            "Compute HelixDose for PT-NX-4419 using protocol HX-9 starting at 2 helix-units.",
            [TITRATE],
            [gold("compute_helixdose", subject_id="PT-NX-4419", protocol="HX-9", start_units="2")],
            ["PT-NX-4419", "HX-9", "2"],
        ),
        _c(
            "c_cln_08",
            Ambiguity.CLEAN,
            "Book a Nimbus follow-up for PT-NX-1108 on slot NMB-1000.",
            [FOLLOW],
            [gold("book_nimbus_followup", subject_id="PT-NX-1108", slot_id="NMB-1000")],
            ["PT-NX-1108", "NMB-1000"],
        ),
        _c(
            "c_cln_09",
            Ambiguity.CLEAN,
            "Retrieve the Nimbus chart PT-NX-6601.",
            [LOOKUP],
            [gold("retrieve_nimbus_chart", subject_id="PT-NX-6601")],
            ["PT-NX-6601"],
        ),
        _c(
            "c_cln_10",
            Ambiguity.CLEAN,
            "Park Helix token TOK-8 for PT-NX-2211 at station ST-GAMMA.",
            [HOLD_MED],
            [gold("park_helix_token", subject_id="PT-NX-2211", station_id="ST-GAMMA", token_id="TOK-8")],
            ["PT-NX-2211", "ST-GAMMA", "TOK-8"],
        ),
        _c(
            "c_cln_11",
            Ambiguity.CLEAN,
            "Assign PT-NX-8810 to Nimbus observation shift SH-EVE.",
            [SHIFT],
            [gold("assign_nimbus_shift", subject_id="PT-NX-8810", shift_id="SH-EVE")],
            ["PT-NX-8810", "SH-EVE"],
        ),
        _c(
            "c_cln_12",
            Ambiguity.CLEAN,
            "Flag a Helix overlap on PT-NX-3310 between HX-9 and HX-12.",
            [FLAG],
            [gold("flag_helix_overlap", subject_id="PT-NX-3310", protocol_a="HX-9", protocol_b="HX-12")],
            ["PT-NX-3310", "HX-9", "HX-12"],
        ),
        _c(
            "c_cln_13",
            Ambiguity.CLEAN,
            "Compute HelixDose for PT-NX-9901 using protocol HX-12 starting at 4 helix-units.",
            [TITRATE],
            [gold("compute_helixdose", subject_id="PT-NX-9901", protocol="HX-12", start_units="4")],
            ["PT-NX-9901", "HX-12", "4"],
        ),
        _c(
            "c_cln_14",
            Ambiguity.CLEAN,
            "Book a Nimbus follow-up for PT-NX-7755 on slot NMB-0900.",
            [FOLLOW],
            [gold("book_nimbus_followup", subject_id="PT-NX-7755", slot_id="NMB-0900")],
            ["PT-NX-7755", "NMB-0900"],
        ),
        _c(
            "c_cln_15",
            Ambiguity.CLEAN,
            "Retrieve the Nimbus chart PT-NX-1010.",
            [LOOKUP],
            [gold("retrieve_nimbus_chart", subject_id="PT-NX-1010")],
            ["PT-NX-1010"],
        ),
        _c(
            "c_cln_16",
            Ambiguity.CLEAN,
            "Park Helix token TOK-1 for PT-NX-4040 at station ST-DELTA.",
            [HOLD_MED],
            [gold("park_helix_token", subject_id="PT-NX-4040", station_id="ST-DELTA", token_id="TOK-1")],
            ["PT-NX-4040", "ST-DELTA", "TOK-1"],
        ),
    ]


def clinical_tasks() -> list[Task]:
    return clinical_ambiguous() + clinical_clean()
