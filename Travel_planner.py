import requests
import webbrowser
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('main.kv')

class ProfileScreen(Screen):
    pass

class PlanTripScreen(Screen):
    pass

class BookRideScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class FlightBooking:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_flights(self, origin, destination, date):
        # Simulate calling an API to search for flights
        # Replace 'url' with the actual API endpoint
        params = {
            'Origin': origin,
            'Destination': destination,
            'Date': date,
            'api_key': self.api_key
        }
        response = requests.get('url', params=params)
        flights = response.json()
        return flights

    def sort_flights_by_price(self, flights):
        # Sort flights according to price, layover, and time to get to the destination
        sorted_flights = sorted(flights, key=lambda x: (len(x.get('layovers', [])), x.get('price', 0), x.get('departure_time', '')))
        return sorted_flights

class LoginScreen(Screen):
    users = {}

    def open_external_signup(self, social_media):
        # Define the URLs for each social media signup page
        social_media_urls = {
            'Facebook': 'https://www.facebook.com/signup',
            'Twitter': 'https://twitter.com/signup',
            'Google': 'https://accounts.google.com/signup'
        }

        # Check if the selected social media is in the dictionary
        if social_media in social_media_urls:
            # Open the URL in the web browser
            webbrowser.open(social_media_urls[social_media])
        else:
            print(f"Signup for {social_media} is not available.")

    def login(self):
        existing_username = self.ids.existing_username_input.text
        existing_password = self.ids.existing_password_input.text
        if existing_username == '' or existing_password == '':
            print("Enter both username and password")
            return

        if existing_username in self.users and self.users[existing_username] == existing_password:
            print("Login Successful")
            origin = 'LAS'
            destination = 'MIA'
            date = '2024-03-01'
            flights = app.flight_booking.search_flights(origin, destination, date)
            sorted_flights = app.flight_booking.sort_flights_by_price(flights)
            for flight in sorted_flights:
                print(f"Flight from {flight['origin']} to {flight['destination']} "
                      f"on {flight['date']} for ${flight['price']}")
        else:
            print("Invalid username or password. Please try again.")

    def create_account(self):
        new_username = self.ids.new_username_input.text
        new_password = self.ids.new_password_input.text
        if new_username == '' or new_password == '':
            print("Enter username or password")
            return

        if new_username in self.users:
            print("Username already exists. Choose another one.")
        else:
            self.users[new_username] = new_password
            print("Account created successfully")

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(PlanTripScreen(name='plan_trip'))
        sm.add_widget(BookRideScreen(name='book_ride'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(LoginScreen(name='login'))

        self.flight_booking = FlightBooking(api_key='API_Key')
        sm.current = 'login'
        return sm

if __name__ == '__main__':
    app = MyApp()
    app.run()
