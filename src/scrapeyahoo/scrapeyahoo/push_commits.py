import os

from git import Repo, Actor

from .get_git_dir import get_git_dir

def push_commits(date):
  repo = Repo(get_git_dir(date))
  origin = repo.remotes.origin
  origin.push()