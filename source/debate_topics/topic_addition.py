topic_files = [
  'data/climate_change.txt',
  'data/morals.txt',
  'data/gun_control.txt',
  'data/education.txt',
  'data/human_rights.txt'
]

topic_categories = [
  'climate_change',
  'morals',
  'gun_control',
  'education',
  'human_rights'
]

topic_filepaths = {
  'climate_change': 'data/climate_change.txt',
  'morals': "data/morals.txt",
  'gun_control': "data/gun_control.txt",
  'education: "data/education.txt"',
  'human_rights: "data/human_rights.txt"'
}

def add_topic(
  topic: str,
  category: str
) -> bool:
  for topic in topic_filepaths.keys():
    with open(topic_filepaths[topic], "r+") as f:
      lines = f.read().split('\n')
    for line in lines:
      if line.startswith("#") or line.startswith("//"):
        lines.remove(line)
      continue
    if topic in lines:
      return False
  with open(topic_filepaths[category], "a") as f:
    f.write(topic + "\n")
    f.close()
  return True
