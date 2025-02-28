# config.py 

USERNAME = "example@gmail.com"
PASSWORD = "password"
LOGIN_URL = "https://reservemycourt.com/login"
RESERVATION_DATE = "03/03/2025"  # Format: MM/DD/YYYY
RESERVATION_LENGTH = "1 Hour 30 Minutes"  # Duration for reservation, e.g. "1 Hour 30 Minutes" or "1 Hour"


# Primary Reservation Time
HOUR_TO_SELECT = "10"                  # Hour in 12-hour format (e.g., "06" for 6 PM)
MINUTE_TO_SELECT = "00"                # Minutes ("00" or "30")
PERIOD_TO_SELECT = "AM"                # AM or PM

# Alternate Reservation Time
ALTERNATE_HOUR_TO_SELECT = "10"        # Alternate hour in 12-hour format
ALTERNATE_MINUTE_TO_SELECT = "30"      # Alternate minutes ("00" or "30")
ALTERNATE_PERIOD_TO_SELECT = "AM"      # Alternate period (AM or PM)


# Do not remove the quotation marks "".