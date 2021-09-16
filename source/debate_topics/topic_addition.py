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
