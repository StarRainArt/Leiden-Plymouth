import tkinter as tk
from tkinter import ttk
import random
import math

# Function to generate random user location
def generate_user_location():
    user_latitude = random.uniform(50, 60)  # Approx. Europe latitude range
    user_longitude = random.uniform(10, 20)  # Approx. Europe longitude range
    return user_latitude, user_longitude

# Function to generate random event data with location
def generate_event_data_with_location(user_location):
    event_data_with_location = {
        "Game Night": {
            "tags": ["gaming"],
            "location": (user_location[0] + random.uniform(-1, 1), user_location[1] + random.uniform(-1, 1))
        },
        "Football Match": {
            "tags": ["sports"],
            "location": (user_location[0] + random.uniform(-1, 1), user_location[1] + random.uniform(-1, 1))
        },
        "Concert": {
            "tags": ["music"],
            "location": (user_location[0] + random.uniform(-1, 1), user_location[1] + random.uniform(-1, 1))
        },
        "Book Club Meeting": {
            "tags": ["reading"],
            "location": (user_location[0] + random.uniform(-1, 1), user_location[1] + random.uniform(-1, 1))
        },
        "Fishing Trip": {
            "tags": ["fishing"],
            "location": (user_location[0] + random.uniform(-1, 1), user_location[1] + random.uniform(-1, 1))
        }
    }
    return event_data_with_location

# Function to calculate distance between two geographical points using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius_of_earth = 6371
    distance = radius_of_earth * c
    return distance

# Function to recommend events within a specified range of distance from the user
def recommend_events_within_distance(user_location, event_data_with_location, max_distance):
    user_latitude, user_longitude = user_location
    recommended_events = []

    for event_name, event_info in event_data_with_location.items():
        event_latitude, event_longitude = event_info["location"]
        distance = calculate_distance(user_latitude, user_longitude, event_latitude, event_longitude)
        if distance <= max_distance:
            recommended_events.append(event_name)

    return recommended_events

# Function to handle button click event
def recommend_events_click():
    # Generate user location
    user_location = generate_user_location()

    # Get selected distance range from dropdown menu
    distance = int(distance_combobox.get())

    # Generate event data
    event_data_with_location = generate_event_data_with_location(user_location)

    # Recommend events within the specified distance
    recommended_events = recommend_events_within_distance(user_location, event_data_with_location, distance)
    
    if recommended_events:
        result_label.config(text="Recommended events within {} km:".format(distance))
        events_text = "\n".join(recommended_events)
        events_label.config(text=events_text)
    else:
        result_label.config(text="No events found within {} km.".format(distance))
        events_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Event Recommender")

# Create dropdown menu for selecting distance range
distance_values = [5, 15, 25, 50, 100]
distance_combobox = ttk.Combobox(root, values=distance_values, state="readonly")
distance_combobox.current(0)  # Set default value
distance_combobox.pack(pady=5)

# Create button to recommend events
recommend_button = tk.Button(root, text="Recommend Events", command=recommend_events_click)
recommend_button.pack(pady=5)

# Create labels to display recommended events
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

events_label = tk.Label(root, text="")
events_label.pack()

# Run the GUI
root.mainloop()
