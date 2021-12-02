from models.event import *



event1 = Event("02.12.2021", "Tree Hugging", 100, "Glasgow", "Everyone is welcome!", True)
event2 = Event("03.12.2021", "Pre Xmas Party", 200, "Edinburgh", "Drinking before xmas starts", False)
events = [event1, event2]


def add_new_event(event):
    events.append(event)