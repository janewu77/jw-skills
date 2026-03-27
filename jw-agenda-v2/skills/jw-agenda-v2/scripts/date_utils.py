#!/usr/bin/env python3
"""日期与周数计算工具 - 供所有 agenda skill 使用。

用法：
    python3 date_utils.py                  # 输出今天的所有日期信息
    python3 date_utils.py 2026-02-05       # 输出指定日期的信息
    python3 date_utils.py --yesterday      # 输出昨天的信息
    python3 date_utils.py --tomorrow       # 输出明天的信息
    python3 date_utils.py --week-range     # 输出本周一至周日的日期范围
    python3 date_utils.py --next-week      # 输出下周一至周日的日期范围
    python3 date_utils.py --prev-week      # 输出上周一至周日的日期范围
    python3 date_utils.py --month-range    # 输出本月每天的日期范围
    python3 date_utils.py --prev-month     # 输出上月每天的日期范围
    python3 date_utils.py --next-month     # 输出下月每天的日期范围

测试时可设环境变量 DATE_UTILS_TODAY（ISO 日期）固定「今天」。
"""

import os
import sys
from datetime import date, datetime, timedelta
import json


def _today() -> date:
    """Current date; overridable for tests via env DATE_UTILS_TODAY (ISO)."""
    if os.environ.get("DATE_UTILS_TODAY"):
        return date.fromisoformat(os.environ["DATE_UTILS_TODAY"])
    return date.today()


def _parse_date(date_str: str) -> date:
    """Parse date string in multiple formats.
    
    Supported formats:
    - YYYY-MM-DD (ISO format, primary)
    - YYYY/MM/DD (common alternative)
    - YYYY.MM.DD (alternative)
    
    Raises ValueError with friendly error message if parsing fails.
    """
    formats = [
        "%Y-%m-%d",  # ISO format: 2026-02-05
        "%Y/%m/%d",  # Alternative: 2026/02/05
        "%Y.%m.%d",  # Alternative: 2026.02.05
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    
    # If all formats failed, provide helpful error message
    raise ValueError(
        f"Invalid date format: '{date_str}'. "
        f"Accepted formats: YYYY-MM-DD (e.g., 2026-02-05), "
        f"YYYY/MM/DD (e.g., 2026/02/05), or YYYY.MM.DD (e.g., 2026.02.05)."
    )


def get_date_info(d: date) -> dict:
    """计算给定日期的所有相关信息。周：周一至周日；周数为年内第几周（ISO 周，通常 1–52）。"""
    iso_year, iso_week, iso_weekday = d.isocalendar()
    weekday_cn = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

    # 本周一和本周日（周一=0，周日=6）
    monday = d - timedelta(days=d.weekday())
    sunday = monday + timedelta(days=6)

    return {
        "date": d.isoformat(),
        "date_cn": f"{d.year}年{d.month}月{d.day}日",
        "weekday": weekday_cn[d.weekday()],
        "month": d.month,
        "day": d.day,
        "year_week": iso_week,
        "year_week_label": f"Week{iso_week}",
        "week_plan_file": f"Week{iso_week}-plan.md",
        "week_review_file": f"Week{iso_week}-review.md",
        "month_plan_file": f"{d.year}-{d.month:02d}-plan.md",
        "todo_file": f"{d.isoformat()}-todo.md",
        "log_file": f"{d.isoformat()}-log.md",
        "week_monday": monday.isoformat(),
        "week_sunday": sunday.isoformat(),
    }


def _get_week_range(reference_date: date, week_offset: int = 0) -> list:
    """获取指定周的日期范围（周一至周日）。

    Args:
        reference_date: 参考日期
        week_offset: 周偏移量（0=本周，1=下周，-1=上周）
    """
    monday = reference_date - timedelta(days=reference_date.weekday())
    monday = monday + timedelta(weeks=week_offset)
    days = []
    for i in range(7):
        d = monday + timedelta(days=i)
        days.append(get_date_info(d))
    return days


def _get_month_range(reference_date: date) -> list:
    """获取指定月份的所有日期。"""
    from calendar import monthrange

    year, month = reference_date.year, reference_date.month
    _, last_day = monthrange(year, month)

    days = []
    for day in range(1, last_day + 1):
        d = date(year, month, day)
        days.append(get_date_info(d))
    return days


def main():
    args = sys.argv[1:]
    today = _today()

    if "--yesterday" in args:
        target = today - timedelta(days=1)
    elif "--tomorrow" in args:
        target = today + timedelta(days=1)
    elif "--week-range" in args:
        days = _get_week_range(today, week_offset=0)
        print(json.dumps({"week_range": days}, ensure_ascii=False, indent=2))
        return
    elif "--next-week" in args:
        days = _get_week_range(today, week_offset=1)
        print(json.dumps({"week_range": days}, ensure_ascii=False, indent=2))
        return
    elif "--prev-week" in args:
        days = _get_week_range(today, week_offset=-1)
        print(json.dumps({"week_range": days}, ensure_ascii=False, indent=2))
        return
    elif "--month-range" in args:
        days = _get_month_range(today)
        print(json.dumps({"month_range": days}, ensure_ascii=False, indent=2))
        return
    elif "--prev-month" in args:
        prev_month = today.replace(day=1) - timedelta(days=1)  # last day of prev month
        days = _get_month_range(prev_month)
        print(json.dumps({"month_range": days}, ensure_ascii=False, indent=2))
        return
    elif "--next-month" in args:
        from calendar import monthrange
        _, last_day = monthrange(today.year, today.month)
        next_month = today.replace(day=last_day) + timedelta(days=1)  # first day of next month
        days = _get_month_range(next_month)
        print(json.dumps({"month_range": days}, ensure_ascii=False, indent=2))
        return
    elif args and not args[0].startswith("--"):
        try:
            target = _parse_date(args[0])
        except ValueError as e:
            print(f"date_utils: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        target = today

    info = get_date_info(target)

    # 同时输出昨天信息（方便 daily-log 使用）
    yesterday = target - timedelta(days=1)
    info["yesterday"] = get_date_info(yesterday)

    print(json.dumps(info, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
