import unittest

from ambisense.catalog.build import all_canonical_tasks
from ambisense.classify.pipeline import classify_response
from ambisense.schemas import (
    AgentOutcome,
    RawResponse,
    SilentFailure,
    SurfaceForm,
    ToolCall,
)


def _task(task_id: str):
    return next(t for t in all_canonical_tasks() if t.task_id == task_id)


class ClassifierTests(unittest.TestCase):
    def test_clarify(self) -> None:
        task = _task("g_amb_01")
        raw = RawResponse(
            task_id=task.task_id,
            model_id="fixture",
            surface=SurfaceForm.CANONICAL,
            text="Which itinerary should I reserve?",
        )
        pred = classify_response(task, raw)
        self.assertEqual(pred.outcome, AgentOutcome.CLARIFY)

    def test_act_and_invented(self) -> None:
        task = _task("c_cln_01")
        raw = RawResponse(
            task_id=task.task_id,
            model_id="fixture",
            surface=SurfaceForm.CANONICAL,
            text="",
            tool_calls=[
                ToolCall(
                    name="compute_helixdose",
                    arguments={
                        "subject_id": "PT-NX-0000",
                        "protocol": "HX-7",
                        "start_units": "2",
                    },
                )
            ],
        )
        pred = classify_response(task, raw)
        self.assertEqual(pred.outcome, AgentOutcome.ACT)
        self.assertEqual(pred.silent_failure, SilentFailure.INVENTED_ENTITY)


if __name__ == "__main__":
    unittest.main()
