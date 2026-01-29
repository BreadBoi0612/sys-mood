def get_mood(cpu, ram):
    load = max(cpu, ram)

    if load < 30:
        return "😎", "Chillin"
    elif load < 60:
        return "🙂", "Working"
    elif load < 80:
        return "😐", "Stressed"
    else:
        return "🔥", "PANIC"
