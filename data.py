import pandas as pd

calendar_events = [
    {
        "title": "Event 1",
        "color": "#FF6C6C",
        "start": "2023-07-03",
        "end": "2023-07-05",
        "resourceId": "b",
    },
    {
        "title": "Event 2",
        "color": "#FFBD45",
        "start": "2023-07-01",
        "end": "2023-07-10",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "color": "#FF4B4B",
        "start": "2023-07-20",
        "end": "2023-07-20",
        "resourceId": "c",
    },
    {
        "title": "Event 4",
        "color": "#FF6C6C",
        "start": "2023-07-23",
        "end": "2023-07-25",
        "resourceId": "d",
    },
    {
        "title": "Event 5",
        "color": "#FFBD45",
        "start": "2023-07-29",
        "end": "2023-07-30",
        "resourceId": "e",
    },
    {
        "title": "Event 6",
        "color": "#FF4B4B",
        "start": "2023-07-28",
        "end": "2023-07-20",
        "resourceId": "f",
    },
    {
        "title": "Event 7",
        "color": "#FF4B4B",
        "start": "2023-07-01T08:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 8",
        "color": "#3D9DF3",
        "start": "2023-07-01T07:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 9",
        "color": "#3DD56D",
        "start": "2023-07-02T10:40:00",
        "end": "2023-07-02T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 10",
        "color": "#FF4B4B",
        "start": "2023-07-15T08:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 11",
        "color": "#3DD56D",
        "start": "2023-07-15T07:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "e",
    },
    {
        "title": "Event 12",
        "color": "#3D9DF3",
        "start": "2023-07-21T10:40:00",
        "end": "2023-07-21T12:30:00",
        "resourceId": "f",
    },
    {
        "title": "Event 13",
        "color": "#FF4B4B",
        "start": "2023-07-17T08:30:00",
        "end": "2023-07-17T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 14",
        "color": "#3D9DF3",
        "start": "2023-07-17T09:30:00",
        "end": "2023-07-17T11:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 15",
        "color": "#3DD56D",
        "start": "2023-07-17T10:30:00",
        "end": "2023-07-17T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 16",
        "color": "#FF6C6C",
        "start": "2023-07-17T13:30:00",
        "end": "2023-07-17T14:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 17",
        "color": "#FFBD45",
        "start": "2023-07-17T15:30:00",
        "end": "2023-07-17T16:30:00",
        "resourceId": "e",
    },
]

# st.markdown("## API reference")
# st.help(calendar)

names = []
position = []
contact = []
dict = {'Name' : names, "Position" : position, "Contact" : contact}

df = pd.DataFrame(dict)