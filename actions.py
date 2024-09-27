# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# actions.py
import openai
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

class ActionRespondToNutritionQuestion(Action):
    def name(self) -> Text:
        return "respond_to_nutrition_question"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Store user's nutrition question in the slot
        nutrition_question = tracker.latest_message['text']
        dispatcher.utter_message("Here's the answer to your nutrition question.")
        return [SlotSet("nutrition_question", nutrition_question)]

class ActionRespondToExercisesQuestion(Action):
    def name(self) -> Text:
        return "respond_to_exercises_question"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Store user's exercises question in the slot
        exercises_question = tracker.latest_message['text']
        dispatcher.utter_message("Here's the information about exercises for pregnant women.")
        return [SlotSet("exercises_question", exercises_question)]

class ActionRespondToCareQuestion(Action):
    def name(self) -> Text:
        return "respond_to_care_question"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Store user's care question in the slot
        care_question = tracker.latest_message['text']
        dispatcher.utter_message("Here's the information about taking care during pregnancy.")
        return [SlotSet("care_question", care_question)]

class ActionRespondToDoctorConvo(Action):
    def name(self) -> Text:
        return "respond_to_doctor_convo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Store user's doctor conversation question in the slot
        doctor_convo_question = tracker.latest_message['text']
        dispatcher.utter_message("You can ask any health-related question.")
        return [SlotSet("doctor_convo_question", doctor_convo_question)]
