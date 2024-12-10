import folium.map
import streamlit as st 
from streamlit_folium import st_folium
import folium
from streamlit_scroll_navigation import scroll_navbar
from streamlit_calendar import calendar
from streamlit_carousel import carousel
import datetime
from data import calendar_events, df
import os

def main():
   st.set_page_config(page_title="Shiv Shankar Mandir", page_icon="🕉️", layout="centered")

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

      st.subheader("Past Events")

      test_items = [
      dict(
         title="Slide 1",
         text="A tree in the savannah",
         img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
      ),
      dict(
         title="Slide 2",
         text="A wooden bridge in a forest in Autumn",
         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
      ),
      dict(
         title="Slide 3",
         text="A distant mountain chain preceded by a sea",
         img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
      ),
   ]

      carousel(items=test_items)

   def location():
      col1, col2 = st.columns(2)

      loc = folium.Map((-20.400956632353818, 57.59489778964128), zoom_start=30)
      folium.map.Marker((-20.400956632353818, 57.59489778964128)).add_to(loc)

      with col1:
         st.subheader("Marie Jeanie, Joomadhar Lane, Rose Belle")
         st.markdown("Opening hour: ")
         st.markdown("Closing hour: ")
         st.markdown("Contact : 627-xxxx")
         st.markdown("Email : ")
         st.warning("Opening and closing times may vary during festivals")

      with col2: 
         st_folium(loc)

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

   st.subheader("Resource Persons")
   st.table(df)




if __name__ == "__main__":
   main()



