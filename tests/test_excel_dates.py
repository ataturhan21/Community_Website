"""Exercise workbook loading without launching Streamlit or making network calls."""

import importlib.util
import sys
import tempfile
import types
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pandas as pd


def load_utils():
    # Caching/UI rendering is outside the data-conversion unit under test.
    streamlit = types.ModuleType("streamlit")
    streamlit.cache_data = lambda function: function
    path = (
        Path(__file__).resolve().parents[1]
        / "community_website/modules/utils.py"
    )
    spec = importlib.util.spec_from_file_location("community_utils", path)
    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, {"streamlit": streamlit}):
        spec.loader.exec_module(module)
    return module


utils = load_utils()


class ExcelDateTests(unittest.TestCase):
    def read_frame(self, frame, columns):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "calendar.xlsx"
            frame.to_excel(path, index=False, sheet_name="Sheet1")
            return utils.load_excel(path, columns)

    def test_native_dates_and_strings_keep_rows_aligned(self):
        data = pd.DataFrame(
            {
                "Tarih": [datetime(2026, 10, 3), "01.10.2026", "02.10.2026"],
                "Event": ["third", "first", "second"],
            }
        )
        actual = self.read_frame(data, ["Tarih"])
        self.assertEqual(
            actual["Event"].tolist(), ["first", "second", "third"]
        )
        self.assertEqual(actual["Tarih"].dt.day.tolist(), [1, 2, 3])

    def test_multiple_date_columns_sort_by_start_then_end(self):
        data = pd.DataFrame(
            {
                "Start": ["02.10.2026", "01.10.2026", "01.10.2026"],
                "End": ["02.10.2026", "03.10.2026", "02.10.2026"],
                "Task": ["last", "middle", "first"],
            }
        )
        actual = self.read_frame(data, ["Start", "End"])
        self.assertEqual(actual["Task"].tolist(), ["first", "middle", "last"])
        self.assertEqual(actual.index.tolist(), [0, 1, 2])

    def test_blank_dates_sort_last(self):
        data = pd.DataFrame(
            {
                "Date": [None, "01.10.2026"],
                "Task": ["unscheduled", "scheduled"],
            }
        )
        actual = self.read_frame(data, ["Date"])
        self.assertEqual(actual["Task"].tolist(), ["scheduled", "unscheduled"])
        self.assertTrue(pd.isna(actual.loc[1, "Date"]))

    def test_invalid_date_is_rejected(self):
        with self.assertRaises(ValueError):
            self.read_frame(pd.DataFrame({"Date": ["31.02.2026"]}), ["Date"])

    def test_no_date_columns_preserves_data(self):
        frame = pd.DataFrame({"Name": ["A", "B"], "Value": [2, 1]})
        pd.testing.assert_frame_equal(self.read_frame(frame, None), frame)


if __name__ == "__main__":
    unittest.main()
