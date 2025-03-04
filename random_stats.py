import random
from datetime import date
import json

def generate_daily_report():
    # Generate some random daily statistics
    daily_data = {
        "date": date.today().strftime("%Y-%m-%d"),
        "tasks_completed": random.randint(3, 12),
        "coffee_cups": random.randint(1, 6),
        "lines_of_code": random.randint(100, 1000),
        "bugs_fixed": random.randint(0, 5),
        "mood": random.choice(["Happy 😊", "Focused 🎯", "Tired 😴", "Excited 🚀"])
    }
    
    # Create filename with today's date
    filename = f"daily_report_{daily_data['date']}.json"
    
    # Write to file
    with open(filename, 'w') as f:
        json.dump(daily_data, f, indent=2)
    
    print(f"Report generated: {filename}")
    print("Summary:")
    print(f"Tasks completed: {daily_data['tasks_completed']}")
    print(f"Coffee consumed: {daily_data['coffee_cups']} cups")
    print(f"Current mood: {daily_data['mood']}")

if __name__ == "__main__":
    generate_daily_report() 