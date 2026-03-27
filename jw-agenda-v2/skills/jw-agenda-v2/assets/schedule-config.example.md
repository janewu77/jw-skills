# Schedule Configuration

> **This is an EXAMPLE file** — Copy to `{agendaRoot}/schedule-config.md` and adjust time slots to match your schedule.

daily-todo reads this file to get time slot configuration when generating schedules. Modify this file to adjust all future generated schedules.

## Time Slots

| Time | Default Activity |
|------|-----------------|
| 09:00-10:00 | (Fill with daily tasks) |
| 10:00-12:00 | (Fill with daily tasks) |
| 12:00-12:30 | Fixed activity (e.g., lunch break) |
| 12:30-16:00 | (Fill with daily tasks) |
| 16:00-17:00 | Fixed activity (e.g., commute/rest) |
| 17:00-19:00 | Fixed activity (e.g., dinner & rest) |
| 19:00- | (Fill with daily tasks) |

## Configuration Notes

- **Default Activity column**: Write fixed activities (e.g., lunch break, commute, meals). daily-todo will not overwrite these.
- **(Fill with daily tasks)**: These slots are automatically filled by daily-todo based on priority.
- You can modify time slots, add/remove rows, or adjust times. daily-todo will generate schedules according to this file's structure.
