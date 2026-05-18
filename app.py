print("📚 SMART STUDY PLANNER")

subjects = []
hours = []

n = int(input("How many subjects do you have? "))

for i in range(n):
    sub = input("Enter subject name: ")
    hr = int(input(f"How many hours for {sub}? "))

    subjects.append(sub)
    hours.append(hr)

print("\n📝 YOUR STUDY PLAN\n")

for i in range(n):
    print(f"{subjects[i]} --> {hours[i]} hours daily")

print("\n✅ Stay focused and avoid distractions!")