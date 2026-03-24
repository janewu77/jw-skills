#!/usr/bin/env python3
"""date_utils.py 测试用例"""

import json
import os
import sys
import unittest
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "jw-agenda-v2", "scripts"))

from date_utils import get_date_info, _get_week_range, _get_month_range, _parse_date


def _with_today(iso_str):
    """设置 DATE_UTILS_TODAY 环境变量，返回 context manager。"""
    class _Ctx:
        def __enter__(self):
            os.environ["DATE_UTILS_TODAY"] = iso_str
        def __exit__(self, *_):
            del os.environ["DATE_UTILS_TODAY"]
    return _Ctx()


class TestGetDateInfo(unittest.TestCase):
    """测试 get_date_info 基本信息计算"""

    def test_basic_date(self):
        d = date(2026, 2, 5)  # 周四
        info = get_date_info(d)
        self.assertEqual(info["date"], "2026-02-05")
        self.assertEqual(info["weekday"], "周四")
        self.assertEqual(info["year_week"], 6)
        self.assertEqual(info["year_week_label"], "Week6")
        self.assertEqual(info["month"], 2)
        self.assertEqual(info["week_plan_file"], "Week6-plan.md")
        self.assertEqual(info["week_review_file"], "Week6-review.md")
        self.assertEqual(info["month_plan_file"], "2026-02-plan.md")
        self.assertEqual(info["todo_file"], "2026-02-05-todo.md")
        self.assertEqual(info["log_file"], "2026-02-05-log.md")
        self.assertEqual(info["week_monday"], "2026-02-02")
        self.assertEqual(info["week_sunday"], "2026-02-08")

    def test_monday(self):
        d = date(2026, 3, 23)  # 周一
        info = get_date_info(d)
        self.assertEqual(info["weekday"], "周一")
        self.assertEqual(info["week_monday"], "2026-03-23")
        self.assertEqual(info["week_sunday"], "2026-03-29")

    def test_sunday(self):
        d = date(2026, 3, 29)  # 周日
        info = get_date_info(d)
        self.assertEqual(info["weekday"], "周日")
        self.assertEqual(info["week_monday"], "2026-03-23")
        self.assertEqual(info["week_sunday"], "2026-03-29")


class TestCrossYearWeek(unittest.TestCase):
    """测试跨年周（ISO 周以周四所在年份为准）"""

    def test_2025_12_29_belongs_to_2026_week1(self):
        """2025-12-29（周一）至 2026-01-04（周日），周四为 2026-01-01 → 2026 Week1"""
        d = date(2025, 12, 29)
        info = get_date_info(d)
        self.assertEqual(info["year_week"], 1)
        self.assertEqual(info["year_week_label"], "Week1")

    def test_2025_12_28_belongs_to_2025_week52(self):
        """2025-12-28（周日）属于 2025 年最后一周"""
        d = date(2025, 12, 28)
        info = get_date_info(d)
        self.assertEqual(info["year_week"], 52)

    def test_2026_01_01_belongs_to_2026_week1(self):
        """2026-01-01（周四）→ 2026 Week1"""
        d = date(2026, 1, 1)
        info = get_date_info(d)
        self.assertEqual(info["year_week"], 1)

    def test_2026_01_04_belongs_to_2026_week1(self):
        """2026-01-04（周日）→ 2026 Week1"""
        d = date(2026, 1, 4)
        info = get_date_info(d)
        self.assertEqual(info["year_week"], 1)

    def test_2026_01_05_belongs_to_2026_week2(self):
        """2026-01-05（周一）→ 2026 Week2"""
        d = date(2026, 1, 5)
        info = get_date_info(d)
        self.assertEqual(info["year_week"], 2)


class TestLeapYear(unittest.TestCase):
    """测试闰年 2 月 29 日"""

    def test_leap_year_feb29(self):
        d = date(2028, 2, 29)  # 2028 是闰年
        info = get_date_info(d)
        self.assertEqual(info["date"], "2028-02-29")
        self.assertEqual(info["month"], 2)
        self.assertEqual(info["day"], 29)

    def test_leap_year_month_range(self):
        """闰年 2 月应有 29 天"""
        d = date(2028, 2, 1)
        days = _get_month_range(d)
        self.assertEqual(len(days), 29)
        self.assertEqual(days[-1]["date"], "2028-02-29")

    def test_non_leap_year_month_range(self):
        """非闰年 2 月应有 28 天"""
        d = date(2026, 2, 1)
        days = _get_month_range(d)
        self.assertEqual(len(days), 28)
        self.assertEqual(days[-1]["date"], "2026-02-28")


class TestWeekRange(unittest.TestCase):
    """测试 --prev-week / --next-week 边界"""

    def test_current_week(self):
        d = date(2026, 2, 5)  # 周四，Week6，周一 2026-02-02，周日 2026-02-08
        days = _get_week_range(d, week_offset=0)
        self.assertEqual(len(days), 7)
        self.assertEqual(days[0]["date"], "2026-02-02")  # 周一
        self.assertEqual(days[6]["date"], "2026-02-08")  # 周日

    def test_prev_week(self):
        d = date(2026, 2, 5)  # 上周：2026-01-26 至 2026-02-01
        days = _get_week_range(d, week_offset=-1)
        self.assertEqual(days[0]["date"], "2026-01-26")
        self.assertEqual(days[6]["date"], "2026-02-01")

    def test_next_week(self):
        d = date(2026, 2, 5)  # 下周：2026-02-09 至 2026-02-15
        days = _get_week_range(d, week_offset=1)
        self.assertEqual(days[0]["date"], "2026-02-09")
        self.assertEqual(days[6]["date"], "2026-02-15")

    def test_prev_week_cross_year(self):
        """跨年：2026-01-05（Week2）的上一周应为 2025 年最后一周"""
        d = date(2026, 1, 5)
        days = _get_week_range(d, week_offset=-1)
        self.assertEqual(days[0]["date"], "2025-12-29")
        self.assertEqual(days[6]["date"], "2026-01-04")

    def test_next_week_cross_year(self):
        """跨年：2025-12-29（Week1/2026）的下一周"""
        d = date(2025, 12, 29)
        days = _get_week_range(d, week_offset=1)
        self.assertEqual(days[0]["date"], "2026-01-05")
        self.assertEqual(days[6]["date"], "2026-01-11")


class TestMonthRange(unittest.TestCase):
    """测试月份范围计算"""

    def test_month_range_31_days(self):
        d = date(2026, 1, 15)
        days = _get_month_range(d)
        self.assertEqual(len(days), 31)
        self.assertEqual(days[0]["date"], "2026-01-01")
        self.assertEqual(days[-1]["date"], "2026-01-31")

    def test_month_range_30_days(self):
        d = date(2026, 4, 10)
        days = _get_month_range(d)
        self.assertEqual(len(days), 30)

    def test_prev_month(self):
        """上月：从当月第一天减一天得到上月末，再用 _get_month_range"""
        from datetime import timedelta
        today = date(2026, 3, 15)
        prev_month = today.replace(day=1) - timedelta(days=1)
        days = _get_month_range(prev_month)
        self.assertEqual(days[0]["date"], "2026-02-01")
        self.assertEqual(days[-1]["date"], "2026-02-28")

    def test_next_month(self):
        """下月：从当月末加一天得到下月首日，再用 _get_month_range"""
        from calendar import monthrange
        from datetime import timedelta
        today = date(2026, 3, 15)
        _, last_day = monthrange(today.year, today.month)
        next_month = today.replace(day=last_day) + timedelta(days=1)
        days = _get_month_range(next_month)
        self.assertEqual(days[0]["date"], "2026-04-01")
        self.assertEqual(days[-1]["date"], "2026-04-30")

    def test_prev_month_jan_crosses_year(self):
        """1 月的上月应为上一年 12 月"""
        from datetime import timedelta
        today = date(2026, 1, 10)
        prev_month = today.replace(day=1) - timedelta(days=1)
        days = _get_month_range(prev_month)
        self.assertEqual(days[0]["date"], "2025-12-01")
        self.assertEqual(days[-1]["date"], "2025-12-31")

    def test_next_month_dec_crosses_year(self):
        """12 月的下月应为下一年 1 月"""
        from calendar import monthrange
        from datetime import timedelta
        today = date(2025, 12, 15)
        _, last_day = monthrange(today.year, today.month)
        next_month = today.replace(day=last_day) + timedelta(days=1)
        days = _get_month_range(next_month)
        self.assertEqual(days[0]["date"], "2026-01-01")
        self.assertEqual(days[-1]["date"], "2026-01-31")


class TestParseDate(unittest.TestCase):
    """测试日期格式解析"""

    def test_iso_format(self):
        d = _parse_date("2026-02-05")
        self.assertEqual(d, date(2026, 2, 5))

    def test_slash_format(self):
        d = _parse_date("2026/02/05")
        self.assertEqual(d, date(2026, 2, 5))

    def test_dot_format(self):
        d = _parse_date("2026.02.05")
        self.assertEqual(d, date(2026, 2, 5))

    def test_invalid_format_raises(self):
        with self.assertRaises(ValueError):
            _parse_date("05-02-2026")  # DD-MM-YYYY not supported

    def test_invalid_date_raises(self):
        with self.assertRaises(ValueError):
            _parse_date("2026-02-30")  # Feb 30 doesn't exist

    def test_not_a_date_raises(self):
        with self.assertRaises(ValueError):
            _parse_date("hello")


class TestEnvOverride(unittest.TestCase):
    """测试 DATE_UTILS_TODAY 环境变量覆盖"""

    def test_env_override(self):
        from date_utils import _today
        with _with_today("2026-01-01"):
            d = _today()
            self.assertEqual(d, date(2026, 1, 1))

    def test_env_override_affects_week_range(self):
        """通过 env 固定今天后，_get_week_range 应以指定日期为基准"""
        with _with_today("2026-02-05"):
            from date_utils import _today
            d = _today()
            days = _get_week_range(d, week_offset=0)
            self.assertEqual(days[0]["date"], "2026-02-02")


if __name__ == "__main__":
    unittest.main()
