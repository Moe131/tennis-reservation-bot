
# Reservation Bot

This bot automates court reservations on [ReserveMyCourt](https://reservemycourt.com/) by running a Python script on a set schedule using CRON on macOS.

## Prerequisites

- Python 3.x installed on your system.
- CRON setup to allow scheduled execution of the bot.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd reservation-bot
   ```

2. **Edit the Configuration File**:
   Update `config.py` with your reservation details:
   ```python
   USERNAME = 'email@gmail.com'           # Replace with your login email
   PASSWORD = 'password'                  # Replace with your password
   LOGIN_URL = 'https://reservemycourt.com/login'
   RESERVATION_DATE = "11/21/2024"        # Format: MM/DD/YYYY
   RESERVATION_LENGTH = "1 Hour 30 Minutes" # Reservation duration
   
   # Primary Reservation Time
   HOUR_TO_SELECT = "06"                  # Hour in 12-hour format (e.g., "06" for 6 PM)
   MINUTE_TO_SELECT = "00"                # Minutes ("00" or "30")
   PERIOD_TO_SELECT = "PM"                # AM or PM
   
   # Alternate Reservation Time
   ALTERNATE_HOUR_TO_SELECT = "06"        # Alternate hour in 12-hour format
   ALTERNATE_MINUTE_TO_SELECT = "30"      # Alternate minutes ("00" or "30")
   ALTERNATE_PERIOD_TO_SELECT = "PM"      # Alternate period (AM or PM)
   ```

## Setting Up CRON

1. **Grant CRON Full Disk Access**:
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Full Disk Access**.
   - Add `cron` by clicking the **+** button and navigating to `/usr/sbin/`.

2. **Schedule the Bot**:
   Open the CRON editor:
   ```bash
   crontab -e
   ```

3. **Add CRON Job**:
   Paste the following lines to schedule the bot:
   ```cron
   58 23 * * * /path/to/python3 /path/to/reserve.py
   ```
   - This schedules the bot to run at 11:58 every day and execute at 12:00 AM .

## Usage

Once the CRON job is set up, it will automatically run the reservation script at the specified times.

## Notes

- Ensure your credentials and reservation times are accurate in `config.py`.
- This bot requires Full Disk Access permissions to work with CRON on macOS.

---

**Disclaimer**: This bot is for personal use only. Ensure compliance with the website's terms and conditions before using this tool.
