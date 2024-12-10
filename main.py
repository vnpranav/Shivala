import streamlit as st 
from streamlit_folium import folium_static
import folium
from streamlit_scroll_navigation import scroll_navbar
from streamlit_calendar import calendar
import datetime
from events import calendar_events
import os


st.set_page_config(page_title="Shiv Shankar Mandir", page_icon="🕉️", layout="wide")

anchor_ids = ["About", "Events", "Location"]
anchor_icons = ["info-circle", "tag", "map"]

st.subheader("Narmadeshwar Shiv Shankar Mandir")
scroll_navbar(
   anchor_ids=anchor_ids,
   key="navbar",
   anchor_icons=anchor_icons,
   orientation="horizontal"
)

def planner():
   st.subheader(
   "Event Calendar📆"
   )

   mode = st.selectbox(
      "Calendar Mode:",
      (
         "daygrid",
         "timegrid",
         "timeline",
         "list",
         "multimonth",
      ),
   )

   events = calendar_events


   calendar_options = {
      "editable": "false",
      "navLinks": "false",
      "resources": None,
      "selectable": "false",
      "contentHeight" : "auto"
   }

   today_date = datetime.date.today().strftime("%Y-%m-%d")

   if mode == "daygrid":
      calendar_options = {
         **calendar_options,
         "headerToolbar": {
               "left": "today prev,next",
               "center": "title",
               "right": "dayGridDay,dayGridWeek,dayGridMonth",
         },
         "initialDate": today_date,
         "initialView": "dayGridMonth",
      }
   elif mode == "timegrid":
      calendar_options = {
         **calendar_options,
         "initialView": "timeGridWeek",
      }
   elif mode == "timeline":
      calendar_options = {
         **calendar_options,
         "headerToolbar": {
               "left": "today prev,next",
               "center": "title",
               "right": "timelineDay,timelineWeek,timelineMonth",
         },
         "initialDate": today_date,
         "initialView": "timelineMonth",
      }
   elif mode == "list":
      calendar_options = {
         **calendar_options,
         "initialDate": today_date,
         "initialView": "listMonth",
      }
   elif mode == "multimonth":
      calendar_options = {
         **calendar_options,
         "initialView": "multiMonthYear",
         }

   state = calendar(
      events=st.session_state.get("events", events),
      options=calendar_options,
      custom_css="""
      .fc-event-past {
         opacity: 0.8;
      }
      .fc-event-time {
         font-style: italic;
      }
      .fc-event-title {
         font-weight: 700;
      }
      .fc-toolbar-title {
         font-size: 2rem;
      }
      """,
      key=mode,
   )

   if state.get("eventsSet") is not None:
      st.session_state["events"] = state["eventsSet"]

def location():
   col1, col2 = st.columns(2)

   loc = folium.Map((-20.400956632353818, 57.59489778964128), zoom_start=30)
   folium.Marker((-20.400956632353818, 57.59489778964128), popup="Shiv Shankar Mandir", tooltip="Shiv Shankar Mandir").add_to(loc)

   with col1:
      st.subheader("Marie Jeanie, Joomadhar Lane, Rose Belle")
      st.markdown("Opening hour: ")
      st.markdown("Closing hour: ")
      st.markdown("Contact : 627-xxxx")
      st.warning("Opening and closing times may vary during festivals")

   with col2: 
      folium_static(loc)

def dummy():
   st.write("content" * 50)

sections = {
   "About" : dummy,
   "Events" : planner,
   "Location" : location,
}

for anchor_id in anchor_ids:
   st.subheader(anchor_id,anchor=anchor_id)
   sections[anchor_id]()
   st.divider()





