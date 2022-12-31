import os
import subprocess
from datetime import datetime, timedelta
import random

# Initial setup
start_date = datetime(2022, 12, 12)
end_date = datetime(2023, 8, 2)
file_name = "dummy.txt"

# Create a dummy file if it does not exist
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("Initial content")

# Set the probability to skip (85%)
skip_probability = 0.85

# Set the range for the number of commits per day
min_commits = 1  # Minimum number of commits per day
max_commits = 7  # Maximum number of commits per day

# Iterate over each date from start_date to end_date
current_date = start_date
while current_date <= end_date:
    # Decide randomly whether to skip this date
    if random.random() > skip_probability:
        # Generate a random number of commits for the current day
        num_commits = random.randint(min_commits, max_commits)
        
        for commit_num in range(num_commits):
            # Modify the file to make each commit unique
            with open(file_name, "a") as f:
                f.write(f"Commit on {current_date.strftime('%Y-%m-%d')} - Commit #{commit_num + 1}\n")

            # Generate a random time within the day for each commit
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            date_str = current_date.strftime(f'%Y-%m-%dT{hour:02d}:{minute:02d}:{second:02d}')
            
            # Run the git commit command with the specific date and time
            subprocess.run(["git", "add", file_name])
            subprocess.run(["git", "commit", "--date", date_str, "-m", f"Random commit #{commit_num + 1} on {current_date.strftime('%Y-%m-%d')}"])

    # Move to the next day
    current_date += timedelta(days=1)
