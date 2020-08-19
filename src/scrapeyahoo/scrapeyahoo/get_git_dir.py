import os

def get_git_dir(date):
  outfile_directory = os.path.join(
    "..", # src
    "..", # utils
    "..", # project directory
    f"democratizingdata-data-{date.strftime('%Y')}",
  )

  return outfile_directory