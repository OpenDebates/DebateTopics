from random import *

import typing

topic_files = [
  'climate_change.txt',
  'morals.txt',
  'gun_control.txt',
  'education.txt',
  'human_rights.txt'
]

topic_categories = [
  'climate_change',
  'morals',
  'gun_control',
  'education',
  'human_rights'
]

topic_filepaths = {
  'climate_change': 'climate_change.txt',
  'morals': "morals.txt",
  'gun_control': "gun_control.txt",
  'education: "education.txt"',
  'human_rights: "human_rights.txt"'
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
