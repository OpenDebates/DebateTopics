import debate_topics
import utils

from Flask import *

app = Flask(__name___)
app.config["DEBUG"] = False

class TokenRequiredError(Exception):
  def __repr__(self) -> str:
    return "A token is required when making API calls."

class CategoryRequiredError(Exception):
  def __repr__(self) -> str:
    return "Category is a required argument that is missing."

class InvalidCategoryError(Exception):
  def __repr__(self) -> str:
    return "The category you provided is not a valid category. Please request '/categories' to see a list of categories"
 
class TopicRequiredError(Exception):
  def __repr__(self) -> str:
    return "Topic is a required argument that is missing.

class TopicExistsError(Exception):
  def __init__(self, topic: str) -> None:
    self.topic=topic
    
  def __repr__(self) -> str:
    return "The topic {} already exists.".format(self.topic)
  
#home
@app.route(
  '/',
  methods=[
    'GET',
    'POST'
  ]
)
def _home() - > str:
  if utils.check_token(request.json) == False:
    raise TokenRequiredError()
  return "<h1>OpenDebates Debate Topics API</h1> <p>version - 1.0-alpha</p1>", 200

#version route
@app.route(
  '/version',
  methods=[
    'GET',
    'POST'
  ]
)
def _home() -> str:
  if utils.check_token(request.json) == False:
    raise TokenRequiredError()
  return "<h1>OpenDebates Debate Topics API</h1> <p>version - 1.0-alpha</p1>", 200

#get topic
@app.route(
  '/get_topic',
  methods = [
    'GET',
    'POST'
  ]
)
def _get_topic() -> dict:
  if utils.check_token(request.json) == False:
    raise TokenRequiredError()
  if "amount" not in request.json:
    return jsonify([{
      "topic": debate_topics.get_topic()
    }]), 200
  else:
    topics = []
    for i in range(request.json["amount"]):
      topics.append(debate_topics.get_topic())
    return jsonify([{
      "topics": topics
    }]), 200
  
  
@app.route(
  '/get_topic/category',
  methods =[
    'GET',
    'POST'
  ]
)
def _get_topic_category()-> dict:
  if utils.check_token(request.json) == False:
    raise TokenRequiredError()
  if "category" not in request.json:
    raise CategoryRequiredError()
  if request.json["category"] not in debate_topics.topic_categories:
    raise InvalidCategoryError()
    
    
  if "amount" not in request.json:
    return jsonify([{
      "topic": debate_topics.get_selected_topic(
        request.json["category"]
      )
    }]), 200
  
  else:
    topics = []
    for i in range(request.json["amount"]):
      topics.append(debate_topics.get_selected_topic(
        request.json["category"]
      ))
    return jsonify([{
      "topics": topics
    }]), 200
  
@app.route(
  '/get_topic/categories',
  methods=[
    'GET',
    'POST'
  ]
)
def _get_topic_categories() -> dict:
  if utils.check_token(request.json) == False:
    raise TokenRequiredError()
  if "categories" not in request.json:
    raise CategoryRequiredError()
  if len(request.json['categories']) == 0 or len(request.json['categories']) == 1:
    raise CategoryRequiredError()
  for category in request.json['categories']:
    if category not in debate_topics.topic_categories:
      raise InvalidCategoryError()
    
    
  if "amount" not in request.json:
    return jsonify([{
      "topic": debate_topics.get_topic_from_selections(
        request.json["categories"]
      )
    }]), 200
  
  else:
    topics = []
    for i in range(request.json["amount"]):
      topics.append(debate_topics.get_topic_from_selections(
        request.json["categories"]
      ))
    return jsonify([{
      "topics": topics
    }]), 200
  
@app.route(
  '/add_topic',
  methods = [
    'GET',
    'POST'
  ]
)
def _add_topic() -> dict:
  if utils.check_token(request.json) == False:
    raise TokenRequiredError()
  if "category" not in request.json:
    raise CategoryRequiredError()
  if request.json["category"] not in debate_topics.topic_categories:
    raise InvalidCategoryError()
  if "topic" not in request.json:
    raise TopicRequiredError()
    
  if debate_topics.add_topic(request.json["topic"], request.json["category"]):
    return jsonify([{
      "topic": request.json["topic"]
    }]), 200
  
  else:
    raise TopicExistsError(request.json['topic'])
  
  app.run("0.0.0.0")
