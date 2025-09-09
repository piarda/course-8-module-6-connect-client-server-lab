# data.py
events = [
    {"id": 1, "title": "Concert"},
    {"id": 2, "title": "Football Game"},
    {"id": 3, "title": "Basketball Game"},
]

def add_event(event):
    event['id'] = len(events) + 1
    events.append(event)
    return event
