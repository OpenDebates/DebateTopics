import debate_topics
import utils

from Flask import *

app = Flask(__name___)
app.config["DEBUG"] = True

class TokenRequiredError(Exception):
  def __repr__(self) -> str:
    return "A token is required when making API calls."

#home
@app.route(
  '/',
  methods=[
    'GET',
    'POST'
  ]
)
def _home():
  return "<h1>OpenDebates Debate Topics API</h1> <p>version - 1.0-alpha</p1>", 200

#version route
@app.route(
  '/version',
  methods=[
    'GET',
    'POST'
  ]
)
def _home():
  if utils.check_token() == False:
    raise TokenRequiredError()
  return "<h1>OpenDebates Debate Topics API</h1> <p>version - 1.0-alpha</p1>", 200

#get topic
@app.route(
  '/get_topic',
  methods = [
    'GET',
    'POST'
  ])
def _get_topic()
  if utils.check_token() == False:
    raise TokenRequiredError()
  if "amount" not in request.args:
    return jsonify([{
      "topic": debate_topics.get_topic()
    }]), 200
  else:
    topics = []
    for i in range(request.args):
      topics.append(debate_topics.get_topic())
    return jsonify([{
      "topics": topics
    }]), 200
  
  app.run("0.0.0.0")
