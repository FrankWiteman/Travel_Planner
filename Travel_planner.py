import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class ProfileScreen(Screen):
    def build(self):
        return Label(text="Profile Screen")
    
class PlanTripScreen(Screen):
    def build(self):
        return Label(text="Plan a Trip")
    
class BookRideScreen(Screen):
    def build(self):
        return Label(text="Book a ride")
    
class SettingsScreen(Screen):
    def build(self):
        return Label(text="Settings")
    
class FlightBooking:
    def __init__(self, api_key):
        self.api_key=api_key
        
    
    def search_flights(self, origin, destination, date):
        #This is to simulate calling an API to search for flights
        # Replace with actual API call to airlines e.g. skyscanner, kiwi.com e.t.c.
        
        params = {
            'Origin': origin,
            'Destination': destination,
            'Date': date,
            'api_key':self.api_key
        }
    
        response = requests.get(url)
        flights = response.json()
        return flights
    
    def sort_flights_by_price(self, flights):  
        
class LoginScreen(Screen):
    def build(self):
        layout= BoxLayout(orientation='vertical', spacing=10)        
        
        
        #Quick view menu
        quick_view_label = Label(text="Quick View Menu")
        layout.add_widget(quick_view_label)
        
        
        #Username and Password input fields for existing users
        
        self.existing_username_input = TextInput(hint_text='Enter your Username')
        self.existing_password_input = TextInput(hint_text='Password', password=True)
        layout.add_widget(self.existing_username_input)
        layout.add_widget(self.existing_password_input)
        
        #Login Button
        login_button = Button(text='Log In', on_press=self.login)
        layout.add_widget(login_button)
        
        # Separator
        layout.add_widget(Label(text='-------------'))
        
        #Login with social media buttons
        social_media_label= Label(text="Login with Social Media:")
        layout.add_widget(social_media_label)
        
        facebook_login_button = Button(text='Facebook', on_press=self.login)
        layout.add_widget(facebook_login_button)
        
        twitter_login_button = Button(text='X', on_press=self.login)
        layout.add_widget(twitter_login_button)
        
        google_login_button = Button(text='Google', on_press=self.login)
        layout.add_widget(google_login_button)
        
        
        return layout
    
    def login(self, instance):
        #This simulates the login
        #Replace with actual login logic
    

App().run()