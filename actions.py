from rasa_core_sdk import Action
import requests
import json


class action_get_feed(Action):

    def name(self):
        return 'action_get_feed'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        url = 'https://api.nytimes.com/svc/topstories/v2/{category}.json'.format(category=category)
        params = {'api-key': "jNl3zkzzvjliODzm8YG2QC8rAtCW5RQg", 'limit': 5}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return[]


