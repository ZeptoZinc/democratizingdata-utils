import os
import csv
import tempfile

import yfinance as yf
import shutil

from scrapeyahoo.tickers import tickers
from scrapeyahoo.scrape import scrape
from scrapeyahoo.create_file import create_repo_file
from scrapeyahoo.create_commit import create_commit
from scrapeyahoo.push_commits import push_commits

def main():
  last_date = None
  for ticker in tickers:
    data, tmp = scrape(ticker)
    if not data.empty:
      last_date = data.iloc[-1].name.to_pydatetime()
      create_repo_file(data, tmp, ticker)
      create_commit(ticker, last_date)

  if last_date is not None:
    push_commits(last_date)

if __name__ == "__main__":
  main()