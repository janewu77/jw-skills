#!/usr/bin/env python3
"""日期与周数计算工具 - 供所有 agenda skill 使用。

用法：
    python3 date_utils.py                  # 输出今天的所有日期信息
    python3 date_utils.py 2026-02-05       # 输出指定日期的信息
    python3 date_utils.py --yesterday      # 输出昨天的信息
    python3 date_utils.py --week-range     # 输出本周一至周日的日期范围
"""

import sys
from datetime import date, timedelta
from math import ceil
import json


def get_date_info(d: date) -> dict:
    """计算给定日期的所有相关信息。"""
    month_week = ceil(d.day / 7)  # 月内周 = ceil(day/7)
    iso_year, iso_week, iso_weekday = d.isocalendar()
    weekday_cn = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

    # 本周一和本周日
    monday = d - timedelta(days=d.weekday())
    sunday = monday + timedelta(days=6)

    return {
        "date": d.isoformat(),
        "date_cn": f"{d.year}年{d.month}月{d.day}日",
        "weekday": weekday_cn[d.weekday()],
        "month": d.month,
        "day": d.day,
        "month_week": month_week,
        "month_week_label": f"Week{month_week}",
        "week_plan_file": f"Week{month_week}-plan.md",
        "week_review_file": f"Week{month_week}-review.md",
        "month_plan_file": f"{d.year}-{d.month:02d}-plan.md",
        "todo_file": f"todo-{d.isoformat()}.md",
        "log_file": f"{d.isoformat()}.md",
        "week_monday": monday.isoformat(),
        "week_sunday": sunday.isoformat(),
    }


def main():
    args = sys.argv[1:]

    if "--yesterday" in args:
        target = date.today() - timedelta(days=1)
    elif "--week-range" in args:
        today = date.today()
        monday = today - timedelta(days=today.weekday())
        days = []
        for i in range(7):
            d = monday + timedelta(days=i)
            days.append(get_date_info(d))
        print(json.dumps({"week_range": days}, ensure_ascii=False, indent=2))
        return
    elif args and not args[0].startswith("--"):
        target = date.fromisoformat(args[0])
    else:
        target = date.today()

    info = get_date_info(target)

    # 同时输出昨天信息（方便 daily-log 使用）
    yesterday = target - timedelta(days=1)
    info["yesterday"] = get_date_info(yesterday)

    print(json.dumps(info, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
