import debate_topics
from debate_topics import Client

client = Client("token here")

topics = client.get_topic_by_categories(
          categories=[
            "philsophy",
            "misc"
          ],
          3
         )

print(
  topics[1]
)

print(
  topics
)

#excepcted output

#Morality is objective.
#['When a majority of the public seeks to abolish their democracy through democracy, it is legitimate.', 'Morality is objective.', 'THW rather be uncomfortably cold than uncomfortably warm.']
