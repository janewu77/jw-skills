# Schedule Configuration / 作息时间配置

daily-todo reads this file to get time slot configuration when generating schedules. Modify this file to adjust all future generated schedules.

daily-todo 生成时间表时读取本文件获取时段配置。修改本文件即可调整所有未来生成的时间表。

## Time Slots / 时段定义

| Time / 时间 | Default Activity / 默认安排 |
|-------------|----------------------------|
| 09:00-10:00 | (Fill with daily tasks) / （填入当日任务） |
| 10:00-12:00 | (Fill with daily tasks) / （填入当日任务） |
| 12:00-12:30 | Fixed activity (e.g., lunch break/out) / 固定活动（如午休/外出） |
| 12:30-16:00 | (Fill with daily tasks) / （填入当日任务） |
| 16:00-17:00 | Fixed activity (e.g., commute/rest) / 固定活动（如通勤/休息） |
| 17:00-19:00 | Fixed activity (e.g., dinner & rest) / 固定活动（如用餐与休息） |
| 19:00- | (Fill with daily tasks) / （填入当日任务） |

## Configuration Notes / 配置说明

- **Default Activity column**: Write fixed activities (e.g., lunch break, commute, meals). daily-todo will not overwrite these.
  - 「默认安排」列中写固定活动（如午休、通勤、用餐），daily-todo 不会覆盖这些
- **(Fill with daily tasks)**: These slots are automatically filled by daily-todo based on priority.
  - 「（填入当日任务）」表示该时段由 daily-todo 根据优先级自动填入具体事项
- You can modify time slots, add/remove rows, or adjust times. daily-todo will generate schedules according to this file's structure.
  - 修改时段、增删行、调整时间均可，daily-todo 会按本文件的结构生成时间表
