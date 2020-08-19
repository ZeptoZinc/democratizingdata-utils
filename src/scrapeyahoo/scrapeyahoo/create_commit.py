import os

from git import Repo, Actor

from .get_git_dir import get_git_dir

def create_commit(ticker, date):
  repo = Repo(get_git_dir(date))
  index = repo.index
  index.add([os.path.join(
    f"{ticker}",
    f"{date.strftime('%m')}",
    f"{date.strftime('%d')}.csv"
  )])

  author = Actor("ZeptoZinc Bot", "68169274+ZeptoZinc@users.noreply.github.com")
  committer = Actor("ZeptoZinc Bot", "68169274+ZeptoZinc@users.noreply.github.com")

  index.commit(
    f"[ZeptoZinc Bot] Add {ticker} data for {date.strftime('%Y-%m-%d')}", 
    author=author,
    committer=committer,
  )