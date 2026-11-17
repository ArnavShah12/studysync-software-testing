from datetime import date, timedelta

def prioritize(tasks, today):
    """Score = urgency (days left) + difficulty weight; higher first."""
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")
    out = []
    for t in tasks:
        if not t.get("title"):
            raise ValueError("title required")
        if not 1 <= t.get("difficulty", 0) <= 5:
            raise ValueError("difficulty must be 1-5")
        days = (t["due"] - today).days
        urgency = 10 if days <= 0 else max(0, 10 - days)
        out.append({**t, "score": urgency + t["difficulty"]})
    return sorted(out, key=lambda x: -x["score"])

def build_schedule(tasks, today, hours_per_day):
    if hours_per_day <= 0:
        raise ValueError("hours_per_day must be positive")
    plan, day, left = {}, today, hours_per_day
    for t in prioritize(tasks, today):
        need = t["hours"]
        while need > 0:
            use = min(need, left)
            plan.setdefault(day.isoformat(), []).append((t["title"], use))
            need -= use; left -= use
            if left == 0:
                day += timedelta(days=1); left = hours_per_day
    return plan

def register(users, email, pw):
    if "@" not in email: raise ValueError("invalid email")
    if len(pw) < 8: raise ValueError("weak password")
    if email in users: raise KeyError("exists")
    users[email] = pw
    return True
