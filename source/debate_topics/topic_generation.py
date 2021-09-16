from random import *

import typing

topic_files = [
  'data/philosophy.txt',
  'data/politics.txt',
  'data/misc.txt'
]

topic_categories = [
  'philosophy',
  'politics',
  'misc
]

topic_filepaths = {
  'philosophy': 'data/philosophy.txt',
  'politics': 'data/politics.txt',
  'misc': 'data/misc.txt'
}
  
def parse_topic_file(
  filepath: str
) -> typing.List(str):
  
  with open(filepath, "r+") as f:
    file_lines = f.read().split('\n')
  
  for line in file_lines:
    if line.startswith("#") or line.startswith("//"):
      file_lines.remove(line)
    continue
  
  return file_lines

def get_topic() -> str:
  return choice(parse_topic_file(choice(topic_files)))

def get_selected_topic(
  topic: str
) -> str:
  return choice(parse_topic_file(topic_filepaths[topic]))

def get_topic_from_selections(
  selections: typing.List(str)
) -> str:
  return choice(parse_topic_file(topic_filepaths[choice(selections)]))
