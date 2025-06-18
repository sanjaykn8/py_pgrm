import random

# All Data
classes = ["A-class", "B-class", "C-class"]
subjects = ["Math", "English", "Science", "Tamil", "Social", "PT"]
subject_requirements = {"Math": 8, "English": 7, "Science": 8, "Tamil": 7, "Social": 8, "PT":2}
staff_allocation = {"Math": "T1", "English": "T2", "Science": "T3", "Tamil": "T4", "Social": "T5", "PT":"T6"}
periods_per_day = 8
days = 5

# Timetable Initialization
timetable = {
    cls: [[None for _ in range(periods_per_day)] for _ in range(days)]
    for cls in classes
}

class_subject_count = {
    cls: {subject: 0 for subject in subjects}
    for cls in classes
}

daily_subject_limit = {
    cls: [
        {subject: 0 for subject in subjects} for _ in range(days)
    ]
    for cls in classes
}

def print_timetable():
    for cls in classes:
        print(f"\nTimetable for {cls}:")
        for d in range(days):
            row = []
            for p in range(periods_per_day):
                sub = timetable[cls][d][p] or "Empty"
                row.append(f"{sub:7}")
            print(f"Day {d+1}: " + " | ".join(row))
        print("-" * (periods_per_day * 10))

def scheduler(cls, day, period, subject):
    staff = staff_allocation[subject]

    if daily_subject_limit[cls][day][subject] >= 3:
        return False

    row = timetable[cls][day]
    
    if period >= 2 and row[period - 1] == subject and row[period - 2] == subject:
        return False
    
    if period >= 1 and row[period - 1] == subject:
        if period + 1 < periods_per_day and row[period + 1] == subject:
            return False

    if period + 2 < periods_per_day and row[period + 1] == subject and row[period + 2] == subject:
        return False

    for other in classes:
        if other == cls:
            continue
        other_sub = timetable[other][day][period]
        if not other_sub:
            continue
        if other_sub == subject or staff_allocation[other_sub] == staff:
            return False

    return True

def is_complete():
    for cls in classes:
        for sub in subjects:
            if class_subject_count[cls][sub] < subject_requirements[sub]:
                return False
    return True

def find_next_slot():
    for cls in classes:
        if all(class_subject_count[cls][sub] >= subject_requirements[sub] for sub in subjects):
            continue
        for d in range(days):
            for p in range(periods_per_day):
                if timetable[cls][d][p] is None:
                    return cls, d, p
    return None, None, None

def backtrack():
    if is_complete():
        return True

    cls, d, p = find_next_slot()
    if cls is None:
        return False

    subject_choices = subjects[:]
    random.shuffle(subject_choices)

    for sub in subject_choices:
        if class_subject_count[cls][sub] >= subject_requirements[sub]:
            continue
        if not scheduler(cls, d, p, sub):
            continue

        timetable[cls][d][p] = sub
        class_subject_count[cls][sub] += 1
        daily_subject_limit[cls][d][sub] += 1

        if backtrack():
            return True

        timetable[cls][d][p] = None
        class_subject_count[cls][sub] -= 1
        daily_subject_limit[cls][d][sub] -= 1

    return False

def main():
    if backtrack():
        print_timetable()
    else:
        print("No valid timetable could be generated!")

if __name__ == "__main__":
    main()
