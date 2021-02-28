from typing import Any, Text, Dict, List

from datetime import datetime
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker, FormValidationAction
from nlidb.nlidb import SQlServer
from rasa_sdk.events import (
    SlotSet,
    EventType,
    AllSlotsReset
)

HOSTNAME = '0.0.0.0'
USER = 'root'
PWD = 'yourpassword'
DATABASE = 'bookings'
LIMIT = 10
PORT='55009'

# This config can be modified- This is for testing puprose
dict_limt={
    'cubicle':10,
    'conference':10,
    'recreation':3
}


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ValidateBooking(FormValidationAction):
    def name(self) -> Text:
        return "validate_booking_form"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        current_slots = tracker.slots
        current_intent = tracker.latest_message['intent'].get('name')
        form_slots = domain.get("forms", {}).get(self.form_name(), {})
        table = tracker.get_slot("room_type")

        if table is None:
            return [SlotSet("requested_slot", "room_type")]

        filters = []
        response = ConditionalSlotting(form_slots).get_next_requested_slot(
            current_slots=current_slots,
            filters=filters,
            table = table,
            current_intent=current_intent,
            length_of_forms=len(form_slots)
        )

        return response


class ActionBookRoom(Action):

    def name(self) -> Text:
        return "action_book_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        filters = tracker.get_slot("filters")
        table = tracker.get_slot("room_type")

        data = SQlServer(
            host=HOSTNAME,
            user=USER,
            password=PWD,
            database=DATABASE,
            port=PORT
                ).get_data(filters,table)

        if not data:
            occupied, not_sanitized = SQlServer(
                host=HOSTNAME,
                user=USER,
                password=PWD,
                database=DATABASE,
                port=PORT
            ).get_data(filters, table, flag=False)
            if len(occupied) == dict_limt.get('table'):
                dispatcher.utter_message(
                    text="Sorry we could not find a seat for you."
                         " The room cannot accomodate more people as per COVID-19 norms of the company")
            elif len(occupied) == 1:
                dispatcher.utter_message(
                    text="Sorry we could not find result."
                         "This can be due to the seats is occupied by {} employee id".format(occupied[4]))
            elif len(not_sanitized)==1:
                dispatcher.utter_message(
                    text="Sorry we could not find a seat for you. "
                         "This can be due to seat of preference with seat id {} is not sanitized".format(0))
            elif occupied or not_sanitized:
                dispatcher.utter_message(
                    text="Sorry we could not find a seat for you."
                         " This can be due to {} seats are occupied & "
                         "{} seats not sanitized according to your preference".format(
                        len(occupied), len(not_sanitized)))
            else:
                dispatcher.utter_message(
                    text="Sorry we could not find a seat for you.")
        else:
            seat_num = data[0][0]
            cube_name = data[0][1]
            floor_num = data[0][2]
            time = tracker.get_slot("time")
            capacity = tracker.get_slot("capacity") + "capacity" if tracker.get_slot("capacity") else ""
            date_str = date_string(time)

            dispatcher.utter_message(text = "Hi Booking done for {0}"
                " Seating number- {1}"
                " Floor number- {2} {3} {4}".format(cube_name, seat_num, floor_num, date_str, capacity))

        return [AllSlotsReset()]


class ConditionalSlotting(object):
    def __init__(self, slots):
        self.form_slots = slots

    @staticmethod
    def create_filters_from_existing_set_slots(conditional_slots, current_slots, filters):
        """
        This function constructs filter using form-slots by checking if the slot is set in current session.
        """
        count=0
        for slot_name, entity in conditional_slots.items():
            if current_slots.get(slot_name):
                count+=1
                if slot_name in ['room_type', 'time', 'capacity']:
                    continue
                else:
                    filters.append((entity[0]['entity'], current_slots.get(slot_name))
                    )
        return filters, count

    @staticmethod
    def request_conditional_slots(form_slots, current_slots, count):
        """
        This function return next slot based on condition
        """
        # Check in conditional slots
        room_type = current_slots.get('room_type')
        for key, value in form_slots.items():
            if count <= len(form_slots) and not current_slots.get(key):

                if room_type=='cubicles' and key in['time']:

                    continue
                if room_type == 'recreation' and key in ['floor_num']:
                    continue
                else:
                    request_next_slot = key
                    return [SlotSet("requested_slot", request_next_slot)
                            ]

        return [SlotSet("requested_slot", None)]

    def get_next_requested_slot(self, current_slots, filters, table, current_intent,length_of_forms):
        """
        This function return next requested slot and sets the filter based on form-slot value
        """
        existing_filters, count = self.create_filters_from_existing_set_slots(self.form_slots, current_slots, filters)

        # Condition check if data is greater than threshold and apply conditional slot

        if current_intent not in ['deny']:
            request_slot = self.request_conditional_slots(self.form_slots, current_slots, count)
            return request_slot
        else:
            return [SlotSet("requested_slot", None),
                    SlotSet("table", table), SlotSet("filters", existing_filters)]


def date_string(date):
    date_str = ''
    if date and isinstance(date, dict):
        from_dt = date['from'][:16] if date['from'] else datetime.utcnow().strftime("%b %d, %Y")
        to_dt = date['to'][:16] if date['to'] else datetime.utcnow().strftime("%b %d, %Y")
        date_str = " from " + from_dt + " to " + to_dt

    return date_str
