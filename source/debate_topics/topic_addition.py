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

def add_topic(
  topic: str
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
  return True
