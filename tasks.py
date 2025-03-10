"""Robot Framework task to get the current week number."""
from robocorp.tasks import task
from RPA.Browser import Browser
from datetime import datetime
import os

@task
def get_week_number():
    """Get current week number and save it to a file."""
    browser = Browser()
    
    try:
        # Open browser and navigate to a date website
        browser.open_available_browser("https://www.timeanddate.com/date/")
        
        # Get current week number
        current_week = datetime.now().isocalendar()[1]
        
        # Create the file path on desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "week_number.txt")
        
        # Save week number to file
        with open(file_path, "w") as f:
            f.write(f"Current Week Number: {current_week}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise
    finally:
        browser.close_all_browsers() 