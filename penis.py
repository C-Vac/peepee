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
    datetime(2024, 6, 8, 12, 0),
    datetime(2024, 6, 15, 12, 0),
    datetime(2024, 6, 22, 12, 0),
    datetime(2024, 6, 28, 11, 0),
    datetime(2024, 6, 30, 13, 0),
    datetime(2024, 6, 23, 11, 0),
    datetime(2024, 6, 16, 13, 0),
    datetime(2024, 6, 9, 11, 30),
    datetime(2024, 6, 2, 12, 30),
    datetime(2024, 5, 27, 12, 0),
    datetime(2024, 5, 28, 12, 0),
    datetime(2024, 5, 29, 12, 0),
    datetime(2024, 5, 30, 12, 0),
    datetime(2024, 5, 31, 12, 0),
    datetime(2024, 5, 26, 12, 0),
    datetime(2024, 7, 4, 12, 0),
    datetime(2024, 7, 18, 12, 0),
    datetime(2024, 7, 25, 12, 0),
    datetime(2024, 7, 28, 12, 0),
    datetime(2024, 7, 21, 12, 0),
    datetime(2024, 7, 14, 12, 0),
    datetime(2024, 7, 7, 12, 0),
    datetime(2024, 7, 30, 12, 0),
    datetime(2024, 8, 1, 12, 0),
    datetime(2024, 8, 5, 12, 0),
    datetime(2024, 8, 6, 12, 0),
    datetime(2024, 8, 7, 12, 0)
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


