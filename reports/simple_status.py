from datetime import date
import random
import os

def create_status_report():
    # Define specific output directory
    OUTPUT_DIR = 'daily_status_reports'
    
    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Get today's date and generate random status
    today = date.today().strftime("%Y-%m-%d")
    project_status = random.choice(['On Track 🟢', 'At Risk 🟡', 'Delayed ⭕'])
    team_members = random.randint(3, 8)
    
    # Create the report file in the specific directory
    filename = os.path.join(OUTPUT_DIR, f"status_{today}.txt")
    with open(filename, 'w') as f:
        f.write(f"Daily Status Report - {today}\n")
        f.write("=" * 30 + "\n\n")
        f.write(f"Project Status: {project_status}\n")
        f.write(f"Team Members Present: {team_members}\n")
        f.write(f"Report Generated at: {date.today().strftime('%A, %B %d, %Y')}\n")
    
    print(f"Status report created: {filename}")

if __name__ == "__main__":
    create_status_report() 