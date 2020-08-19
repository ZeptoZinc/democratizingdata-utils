import os
import shutil

from .get_git_dir import get_git_dir

def create_repo_file(data, tmp, ticker):
  first_t = data.iloc[-1].name.to_pydatetime()
  outfile_directory = os.path.join(
    get_git_dir(first_t),
    f"{ticker}",
    f"{first_t.strftime('%m')}",
  )

  outfile_name = os.path.join(
    outfile_directory,
    f"{first_t.strftime('%d')}.csv"
  )

  if not os.path.exists(outfile_directory):
    os.makedirs(outfile_directory)

  shutil.copyfile(tmp.name, outfile_name)
