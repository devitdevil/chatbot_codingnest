from rasa_core_sdk import Action
import requests
import json
import pymongo
from bson import json_util


class action_get_feed(Action):

    def name(self):
        return 'action_get_feed'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        # url = 'https://api.nytimes.com/svc/topstories/v2/{category}.json'.format(category=category)
        # params = {'api-key': "jNl3zkzzvjliODzm8YG2QC8rAtCW5RQg", 'limit': 5}
        # response = requests.get(url, params).text
        # json_data = json.loads(response)['results']
        # i = 0
        # for results in json_data:
        #     i = i+1
        #     message = str(i) + "." + results['abstract']
        #     dispatcher.utter_message(message)
        # return[]
        client=pymongo.MongoClient("mongodb://localhost:27017")
        db=client["chatbot"]
        col=db["chatting"]
        querry={"topic":category}
        q=col.find(querry)

        #for _ in "collection_name".find():
        #return json.dumps(i, indent=4, default=json_util.default)

        for i in q:
            dispatcher.utter_message(i['f_name'])
        return[]


