import git
import os
import time
from datetime import datetime, timedelta

# Initialize Git repo
repo_dir = '.'
repo = git.Repo(repo_dir)
# repo = git.Repo.init(repo_dir)

# Define the penis shape with commit times
penis_times = [
    datetime(2024, 6, 22, 12, 0),  # Tip
    datetime(2024, 6, 21, 12, 0),
    datetime(2024, 6, 20, 12, 0),
    datetime(2024, 6, 19, 11, 0), datetime(2024, 6, 19, 13, 0), # Shaft
    datetime(2024, 6, 18, 11, 0), datetime(2024, 6, 18, 13, 0),
    datetime(2024, 6, 17, 11, 30), datetime(2024, 6, 17, 12, 30),
    datetime(2024, 6, 16, 12, 0), # Base
    datetime(2024, 6, 15, 12, 0), datetime(2024, 6, 15, 12, 0)  # Balls
]

# Commit and push with adjusted times
for commit_time in penis_times:
    file_path = os.path.join(repo_dir, 'README.md')
    with open(file_path, 'a') as file:
        file.write(f'Commit at {commit_time}\n')
    repo.git.add('.')
    
    # Adjust system time for commit
    os.environ['GIT_AUTHOR_DATE'] = commit_time.isoformat()
    os.environ['GIT_COMMITTER_DATE'] = commit_time.isoformat()
    
    repo.git.commit('-m', 'Phallic commit')
    # time.sleep(1)  # Delay for visualization

# Reset system time and push
os.unsetenv('GIT_AUTHOR_DATE')
os.unsetenv('GIT_COMMITTER_DATE')

origin = repo.remote('origin')
origin.push('master')


