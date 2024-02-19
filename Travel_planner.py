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


class MyApp(App):
    def build(self):
        # Create screen manager
        sm = ScreenManager()

        # Create screens
        profile_screen = ProfileScreen(name='profile')
        plan_trip_screen = PlanTripScreen(name='plan_trip')
        book_ride_screen = BookRideScreen(name='book_ride')
        settings_screen = SettingsScreen(name='settings')
        login_screen = LoginScreen(name='login')

        # Add screens to the screen manager
        sm.add_widget(profile_screen)
        sm.add_widget(plan_trip_screen)
        sm.add_widget(book_ride_screen)
        sm.add_widget(settings_screen)
        sm.add_widget(login_screen)

        # To initialize FlightBooking Instance
        self.flight_booking = FlightBooking(api_key='API_Key')
        # Set the login screen as the starting screen
        sm.current = 'login'
        return sm


class FlightBooking:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_flights(self, origin, destination, date):
        # This is to simulate calling an API to search for flights
        # Replace with actual API call to airlines e.g. skyscanner, kiwi.com, etc.
        params = {
            'Origin': origin,
            'Destination': destination,
            'Date': date,
            'api_key': self.api_key
        }
        response = requests.get('url', params=params)  # Replace 'url' with the actual API endpoint
        flights = response.json()
        return flights

    def sort_flights_by_price(self, flights):
        # Sorts flights according to price, layover, and time to get to the destination
        sorted_flights = sorted(flights, key=lambda x: (
        len(x.get('layovers', [])), x.get('price', 0), x.get('departure_time', '')))
        return sorted_flights


class LoginScreen(Screen):
    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Quick view menu
        quick_view_label = Label(text="Quick View Menu")
        layout.add_widget(quick_view_label)

        # Username and Password input fields for existing users
        self.existing_username_input = TextInput(hint_text='Enter your Username')
        self.existing_password_input = TextInput(hint_text='Password', password=True)
        layout.add_widget(self.existing_username_input)
        layout.add_widget(self.existing_password_input)

        # Login Button
        login_button = Button(text='Log In', on_press=self.login)
        layout.add_widget(login_button)

        # Separator
        layout.add_widget(Label(text='-------------'))

        # Create new account section
        self.new_username_input = TextInput(hint_text='Create a Username')
        self.new_password_input = TextInput(hint_text='Create a password', password=True)
        layout.add_widget(self.new_username_input)
        layout.add_widget(self.new_password_input)

        create_account_button = Button(text='Create Account', on_press=self.create_account)
        layout.add_widget(create_account_button)

        # Separator
        layout.add_widget(Label(text='---------------------'))

        # Login with social media buttons
        social_media_label = Label(text="Login with Social Media:")
        layout.add_widget(social_media_label)

        facebook_login_button = Button(text='Facebook', on_press=self.login)
        layout.add_widget(facebook_login_button)

        twitter_login_button = Button(text='Twitter', on_press=self.login)  # Corrected button text
        layout.add_widget(twitter_login_button)

        google_login_button = Button(text='Google', on_press=self.login)
        layout.add_widget(google_login_button)

        return layout

    def login(self, instance):
        # This simulates the login
        # Replace with actual login logic
        existing_username = self.existing_username_input.text
        existing_password = self.existing_password_input.text
        if existing_username == '' or existing_password == '':
            print("Enter both username and password")
            return

        # This checks if the username and password are correct and working
        if existing_username in self.users and self.users[existing_username] == existing_password:
            print("Login Successful")

            # Example usage of flight booking after login
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

    def create_account(self, instance):
        new_username = self.new_username_input.text
        new_password = self.new_password_input.text
        if new_username == '' or new_password == '':
            print("Enter username or password")
            return

        # This checks if the username already exists
        if new_username in self.users:
            print("Username already exists. Choose another one.")
        else:
            # Adds a new user to the users dictionary
            self.users[new_username] = new_password
            print("Account created successfully")

    def get_layout(self):
        return self.build()


# Dictionary to store user credentials
LoginScreen.users = {}

# Instantiate the MyApp class
if __name__ == "__main__":
    app = MyApp()
    app.run()