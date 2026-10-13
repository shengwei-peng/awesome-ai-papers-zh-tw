"""Self-test for check_coverage.py (stdlib only): python3 -m unittest discover -s .github/scripts"""

import io
import tempfile
import unittest
import urllib.error
from datetime import date
from pathlib import Path
from unittest import mock

import check_coverage as cc

TODAY = date(2026, 10, 13)


def fake_hf(lists: dict[date, list[str]]):
    return lambda day: lists.get(day, [])


class TranslatedIdsTest(unittest.TestCase):
    def test_reads_arxiv_ids_from_markdown_file_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ["2610.00001_A_Paper.md", "2610.00002_B.md", "notes.txt"]:
                (Path(tmp) / name).write_text("x")

            self.assertEqual(cc.translated_ids(Path(tmp)), {"2610.00001", "2610.00002"})


class CheckTest(unittest.TestCase):
    def test_passes_when_the_settled_day_is_fully_translated(self):
        hf = fake_hf({date(2026, 10, 10): ["a", "b"], date(2026, 10, 12): ["c"]})

        problems = cc.check(TODAY, hf, translated={"a", "b", "c"}, max_missing=0)

        self.assertEqual(problems, [])

    def test_reports_missing_papers_from_the_settled_day(self):
        hf = fake_hf({date(2026, 10, 10): ["a", "b", "c"], date(2026, 10, 12): ["d"]})

        problems = cc.check(TODAY, hf, translated={"a", "d"}, max_missing=0)

        self.assertEqual(len(problems), 1)
        self.assertIn("2026-10-10", problems[0])
        self.assertIn("2/3", problems[0])
        self.assertIn("b, c", problems[0])

    def test_tolerates_up_to_max_missing(self):
        hf = fake_hf({date(2026, 10, 10): ["a", "b"], date(2026, 10, 12): ["c"]})

        self.assertEqual(cc.check(TODAY, hf, translated={"a", "c"}, max_missing=1), [])

    def test_flags_a_run_that_did_not_happen_at_all(self):
        # Yesterday is still being re-swept, but zero coverage means the translator never ran
        hf = fake_hf({date(2026, 10, 12): ["x", "y"]})

        problems = cc.check(TODAY, hf, translated=set(), max_missing=0)

        self.assertEqual(len(problems), 1)
        self.assertIn("2026-10-12", problems[0])
        self.assertIn("none of 2", problems[0])

    def test_partial_coverage_of_yesterday_is_fine(self):
        hf = fake_hf({date(2026, 10, 12): ["x", "y"]})

        self.assertEqual(cc.check(TODAY, hf, translated={"x"}, max_missing=0), [])

    def test_days_without_papers_are_fine(self):
        self.assertEqual(cc.check(TODAY, fake_hf({}), translated=set(), max_missing=0), [])

    def test_a_given_date_is_held_to_the_settled_standard(self):
        hf = fake_hf({date(2026, 10, 1): ["a", "b"]})

        problems = cc.check(TODAY, hf, translated={"a"}, max_missing=0, only=date(2026, 10, 1))

        self.assertEqual(len(problems), 1)
        self.assertIn("2026-10-01", problems[0])


class HfIdsTest(unittest.TestCase):
    def test_a_date_hf_has_not_opened_yet_has_no_papers(self):
        body = b'{"error":"\\"date\\" must be less than or equal to \\"2026-10-12T00:00:00.000Z\\""}'
        error = urllib.error.HTTPError("url", 400, "Bad Request", {}, io.BytesIO(body))
        with mock.patch.object(cc.urllib.request, "urlopen", side_effect=error):
            self.assertEqual(cc.hf_ids(date(2026, 10, 13)), [])

    def test_other_http_errors_propagate(self):
        error = urllib.error.HTTPError("url", 500, "Server Error", {}, io.BytesIO(b"boom"))
        with mock.patch.object(cc.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(urllib.error.HTTPError):
                cc.hf_ids(date(2026, 10, 1))


if __name__ == "__main__":
    unittest.main()
