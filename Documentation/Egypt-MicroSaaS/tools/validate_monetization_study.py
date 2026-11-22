#!/usr/bin/env python3
"""Fail-closed study v0.7 integrity + arithmetic checks (not commercial validation)."""
import hashlib
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_SHA = "e12cd8d4076fe0cd1be3a494318d69c8ce543b12"
NEW = ROOT / "Monetization-Opportunity-Registry-v0.7.json"
OLD = ROOT / "Idea-Registry.json"
MODELS = ("ad", "subscription", "hybrid")
EXPECTED_TOP = {"ad": "EG-050", "subscription": "EG-047", "hybrid": "EG-060"}
REQUIRED_DOCS = (
    "Monetization-Expansion-2026-11-22-v0.7.md",
    "Monetization-Evidence-2026-11-22-v0.7.md",
    "Monetization-Unit-Economics-2026-11-22-v0.7.md",
    "Monetization-Validation-Plan-2026-11-22-v0.7.md",
)

def github_blob_hash(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def ad_revenue(dau, impressions_per_dau_day, realized_ecpm, days=30):
    if min(dau, impressions_per_dau_day, realized_ecpm, days) < 0:
        raise ValueError("Non-negative values required")
    return dau * impressions_per_dau_day * days * realized_ecpm / 1000

def web_revenue(monetized_pageviews, page_rpm):
    if min(monetized_pageviews, page_rpm) < 0:
        raise ValueError("Non-negative values required")
    return monetized_pageviews * page_rpm / 1000

class StudyIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw_old = OLD.read_bytes()
        cls.old = json.loads(cls.raw_old)
        cls.new = json.loads(NEW.read_text(encoding="utf-8"))

    def test_legacy_blob_unchanged(self):
        self.assertEqual(github_blob_hash(self.raw_old), OLD_SHA)
        self.assertEqual(len(self.old["ideas"]), 48)
        self.assertEqual(len(self.old["ranked_ids"]), 41)
        self.assertEqual(len({i["id"] for i in self.old["ideas"]}), 48)
        self.assertEqual(
            self.new["historical_registry"]["locked_git_blob_sha"], OLD_SHA
        )
        self.assertEqual(self.new["historical_registry"]["count"], 48)

    def test_new_ids_distinct_and_not_reused(self):
        new_ideas = self.new["new_ideas"]
        self.assertEqual(len(new_ideas), 14)
        existing = {i["id"] for i in self.old["ideas"]}
        expected = {f"EG-{i:03}" for i in range(49, 63)}
        actual = {i["id"] for i in new_ideas}
        self.assertEqual(actual, expected)
        self.assertTrue(existing.isdisjoint(actual))

    def test_provisional_scoring_and_no_fake_commercial_measurements(self):
        self.assertEqual(self.new["global_status"], "RESEARCH_ONLY_NO_PRODUCTS_TESTED_NO_AD_REVENUE_NO_PAYMENTS")
        scores = self.new["scoring"]
        for model in MODELS:
            self.assertAlmostEqual(sum(scores["weights"][model].values()), 1.0)
        for idea in self.new["new_ideas"]:
            self.assertEqual(idea["revenue"], "NOT_MEASURED")
            self.assertEqual(idea["retention"], "NOT_MEASURED")
            self.assertEqual(idea["validation_state"], "NOT_TESTED")
            for model in MODELS:
                val = idea["model_scores"][model]
                self.assertIsInstance(val, (float, int))
                self.assertGreaterEqual(val, 0)
                self.assertLess(val, 9.0)
        for item in self.new["legacy_model_overlays"]:
            self.assertIn(item["id"], {x["id"] for x in self.old["ideas"]})

    def test_evidence_and_ranking_consistency(self):
        n = self.new
        evidence_ids = {s["id"] for s in n["evidence_sources"]}
        self.assertEqual(len(evidence_ids), len(n["evidence_sources"]))
        self.assertTrue(all(s["url"].startswith("https://") for s in n["evidence_sources"]))
        for idea in n["new_ideas"]:
            self.assertTrue(set(idea["evidence_ids"]).issubset(evidence_ids))
        all_scores = {
            x["id"]: x["model_scores"]
            for x in n["new_ideas"] + n["legacy_model_overlays"]
        }
        self.assertEqual(len(all_scores), 22)
        for model in MODELS:
            ordered = n["rankings"][model]
            self.assertEqual(len(ordered), len(all_scores))
            self.assertEqual({r["id"] for r in ordered}, set(all_scores))
            self.assertEqual(ordered[0]["id"], EXPECTED_TOP[model])
            for row in ordered:
                self.assertEqual(row["score"], all_scores[row["id"]][model])
            self.assertEqual(
                ordered,
                sorted(ordered, key=lambda r: (-r["score"], r["id"]))
            )

    def test_documentation_files_exist(self):
        for name in REQUIRED_DOCS:
            self.assertTrue((ROOT / name).is_file(), name)
            self.assertGreater((ROOT / name).stat().st_size, 1000)

class UnitEconomics(unittest.TestCase):
    def test_ad_scenarios(self):
        self.assertAlmostEqual(ad_revenue(1000, .6, .15), 2.7)
        self.assertAlmostEqual(ad_revenue(10000, 1.5, .5), 225)
        self.assertAlmostEqual(ad_revenue(50000, 2.5, 1.5), 5625)
        self.assertAlmostEqual(ad_revenue(10000, .8, .5), 120)
        self.assertEqual(math.ceil(1000 / (30 * 1.5 * .5 / 1000)), 44445)

    def test_ads_break_even_and_paid_hypothesis(self):
        revenue_per_acquired = 20 * 1.5 * .50 / 1000
        self.assertAlmostEqual(revenue_per_acquired, .015)
        self.assertEqual(math.ceil(.1 / (1.5 * .5 / 1000)), 134)
        self.assertAlmostEqual(10000 * .03 * 79, 23700)

    def test_web_rpm_separate(self):
        for rpm, expected in [(.30, 9), (1, 30), (2, 60)]:
            self.assertAlmostEqual(web_revenue(30000, rpm), expected)

    def test_invalid_revenue_inputs(self):
        with self.assertRaises(ValueError):
            ad_revenue(-1, 1, .5)
        with self.assertRaises(ValueError):
            web_revenue(-30, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
