import debate_topics
from debate_topics import Client

#initializes client
client = Client("insert_token_here")

print(
  #gets a topic from the aoi
  client.get_topic(
  ).content#gets the content attribute of the returned topid (note: if amount is more than 1 get_topic() will return an array of topics.
)

#example output
#THP a one-state of Israel to Israel and Palestine as separate entities.
