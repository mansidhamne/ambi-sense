"""Respect Groq free-tier RPM with a process-local gate."""

from __future__ import annotations

import time
from threading import Lock


class RequestPacer:
    def __init__(self, min_interval_sec: float) -> None:
        self.min_interval_sec = min_interval_sec
        self._lock = Lock()
        self._last = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            sleep_for = self.min_interval_sec - (now - self._last)
            if sleep_for > 0:
                time.sleep(sleep_for)
            self._last = time.monotonic()
