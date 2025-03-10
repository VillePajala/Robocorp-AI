"""
Robot Framework task to scrape VR train schedules from Lappeenranta to Helsinki
and generate a PDF report.
"""
from robot.api.deco import keyword
import traceback
import sys

print("Starting VR Train Schedule script...")
print("\n\n*** RUNNING IN AUTO-CAPTURE MODE - NO USER INPUT NEEDED ***\n")
print("If you need to inspect elements, the script will pause at key points.\n")
print("When paused, you can use the Playwright Inspector to select elements.\n\n")

from RPA.Browser import Browser
from datetime import datetime
import os
import pdfkit
import time
from bs4 import BeautifulSoup
import jinja2
import subprocess
# Import selectors
from selectors import *

# Configure jinja2 environment
TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

# Create screenshots directory if it doesn't exist
SCREENSHOTS_DIR = os.path.join(TEMPLATE_DIR, "screenshots")
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)
    print(f"Created screenshots directory: {SCREENSHOTS_DIR}")
else:
    print(f"Screenshots directory already exists: {SCREENSHOTS_DIR}")

# Get a timestamp for this run
RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
print(f"Run timestamp: {RUN_TIMESTAMP}")

# Create a session directory for this run
SESSION_DIR = os.path.join(SCREENSHOTS_DIR, f"session_{RUN_TIMESTAMP}")
if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)
    print(f"Created session directory: {SESSION_DIR}")

# Global variable to track if an error occurred
error_occurred = False

# Enable debug mode for element selection
ENABLE_INSPECTOR = True

@keyword
def vr_train_schedule():
    """Scrape train schedules from VR website and generate a PDF report."""
    global error_occurred
    error_occurred = False
    
    print("\n\n")
    print("*"*80)
    print("AUTOMATION STARTING - AUTO CAPTURE MODE")
    print("The browser will open and screenshots will be saved at each step")
    print("*"*80)
    print("\n\n")
    
    browser = Browser()
    
    try:
        # Keep track of the step number
        step = 1
        
        # Get today's date
        today = datetime.now().strftime("%d.%m.%Y")
        print(f"Today's date: {today}")
        
        # Open browser and navigate to VR website
        browser.open_browser("https://www.vr.fi/en/departures-and-arrivals")
        browser.maximize_browser_window()
        time.sleep(3)  # Give page time to load
        
        # Capture screenshot and HTML
        capture_state(browser, f"{step:02d}_initial_page")
        step += 1
        
        print("Looking for cookie consent dialog...")
        try:
            # Use the selector from selectors.py
            if browser.is_element_visible(COOKIE_ACCEPT_BUTTON):
                print(f"Found cookie consent button: {COOKIE_ACCEPT_BUTTON}")
                browser.click_element(COOKIE_ACCEPT_BUTTON)
                print("Accepted cookies")
                time.sleep(2)
                
                # Capture state after accepting cookies
                capture_state(browser, f"{step:02d}_after_cookies")
                step += 1
            else:
                print("No cookie consent dialog found")
        except Exception as e:
            print(f"Error handling cookies: {e}")
        
        # Try to fill in the From field
        print("Looking for From station field...")
        try:
            # Use the selector from selectors.py
            if browser.is_element_visible(FROM_FIELD):
                print(f"Found From station field: {FROM_FIELD}")
                browser.click_element(FROM_FIELD)
                browser.input_text(FROM_FIELD, FROM_STATION)
                print(f"Entered departure station: {FROM_STATION}")
                time.sleep(2)
                
                # Capture state after entering departure station
                capture_state(browser, f"{step:02d}_after_from_station")
                step += 1
            else:
                print("From station field not found")
        except Exception as e:
            print(f"Error with From station field: {e}")
            
        # Try to fill in the To field
        print("Looking for To station field...")
        try:
            # Use the selector from selectors.py
            if browser.is_element_visible(TO_FIELD):
                print(f"Found To station field: {TO_FIELD}")
                browser.click_element(TO_FIELD)
                browser.input_text(TO_FIELD, TO_STATION)
                print(f"Entered destination station: {TO_STATION}")
                time.sleep(2)
                
                # Capture state after entering destination station
                capture_state(browser, f"{step:02d}_after_to_station")
                step += 1
            else:
                print("To station field not found")
        except Exception as e:
            print(f"Error with To station field: {e}")
        
        # Try to select today's date
        print("Looking for date picker...")
        try:
            # Use the selector from selectors.py
            if browser.is_element_visible(DATE_PICKER):
                print(f"Found date picker: {DATE_PICKER}")
                browser.click_element(DATE_PICKER)
                browser.input_text(DATE_PICKER, today)
                print(f"Selected date: {today}")
                time.sleep(2)
                
                # Capture state after selecting date
                capture_state(browser, f"{step:02d}_after_date_selection")
                step += 1
            else:
                print("Date picker not found")
        except Exception as e:
            print(f"Error with date selection: {e}")
        
        # Click the search button
        print("Looking for search button...")
        try:
            # Use the selector from selectors.py
            if browser.is_element_visible(SEARCH_BUTTON):
                print(f"Found search button: {SEARCH_BUTTON}")
                browser.click_element(SEARCH_BUTTON)
                print("Clicked search button")
                time.sleep(5)  # Give time for results to load
                
                # Capture state after searching
                capture_state(browser, f"{step:02d}_search_results")
                step += 1
            else:
                print("Search button not found")
        except Exception as e:
            print(f"Error with search button: {e}")
        
        # Enable Playwright Inspector when needed
        if ENABLE_INSPECTOR:
            print("\n*** PAUSING FOR ELEMENT INSPECTION ***")
            print("A new window with Playwright Inspector should open.")
            print("You can now click on elements to see their selectors.")
            print("Look at the console output to see the selectors.")
            print("Press Enter in this console when you're ready to continue...")
            
            # Launch Playwright Inspector in a separate process
            try:
                # This works only with Playwright-based automation
                # We're using a subprocess call since RPA.Browser might not expose this directly
                subprocess.Popen("playwright open https://www.vr.fi/en/departures-and-arrivals --inspector", shell=True)
                input("Press Enter to continue when you're finished inspecting elements...")
            except Exception as e:
                print(f"Could not launch Playwright Inspector: {e}")
                print("Continue with regular automation...")
        
        # After all attempts, save the final page state
        capture_state(browser, f"{step:02d}_final_state")
        
        # Print the location where all screenshots and HTML were saved
        print("\n\n")
        print("*"*80)
        print(f"AUTOMATION COMPLETED - All captures saved to: {SESSION_DIR}")
        print("Review the screenshots and HTML files to understand the page structure")
        print("*"*80)
        print("\n\n")
        
    except Exception as e:
        error_occurred = True
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()
        
        # Capture the error state
        try:
            capture_state(browser, "error_state")
        except:
            pass
            
        print("\n\n*** BROWSER KEPT OPEN FOR DEBUGGING - Close it manually when done ***\n\n")
        # Sleep to keep the browser open for inspection
        time.sleep(300)  # Keep the browser open for 5 minutes for debugging
        raise
    finally:
        # Only close the browser if no error occurred
        if not error_occurred:
            print("Closing browser as execution completed successfully.")
            browser.close_all_browsers()
        else:
            print("Browser left open due to errors.")

def capture_state(browser, step_name):
    """Capture the current state of the browser including screenshot and HTML."""
    try:
        # Take a screenshot
        screenshot_path = os.path.join(SESSION_DIR, f"{step_name}.png")
        browser.capture_page_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        
        # Save the page HTML
        try:
            html = browser.get_source()
            html_path = os.path.join(SESSION_DIR, f"{step_name}.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"HTML saved to: {html_path}")
        except Exception as e:
            print(f"Could not capture HTML: {e}")
            
        # Save page title and URL
        try:
            title = browser.get_title()
            url = browser.get_location()
            info_path = os.path.join(SESSION_DIR, f"{step_name}_info.txt")
            with open(info_path, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\nURL: {url}\n")
        except Exception as e:
            print(f"Could not capture page info: {e}")
    except Exception as e:
        print(f"Error capturing state: {e}")

def extract_train_data(html_content):
    """Extract train schedule data from the HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    schedules = []
    
    print("Analyzing HTML structure for train data...")
    
    # Try multiple possible selectors for train rows based on VR site structure
    possible_row_selectors = [
        '.journey-card',
        '.journey-option',
        '.connection-option',
        '.train-option',
        'div[data-testid*="journey"]',
        'div[data-testid*="connection"]'
    ]
    
    train_rows = []
    for selector in possible_row_selectors:
        train_rows = soup.select(selector)
        if train_rows:
            print(f"Found {len(train_rows)} train rows with selector: {selector}")
            break
    
    # If no rows found with class selectors, try to find time patterns
    if not train_rows:
        print("No train rows found with standard selectors, trying time pattern approach...")
        import re
        time_pattern = re.compile(r'(\d{1,2}:\d{2})')
        
        # Look for elements that might contain departure/arrival times
        time_containers = soup.find_all(['div', 'span', 'p'], string=time_pattern)
        
        if time_containers:
            print(f"Found {len(time_containers)} elements with time patterns")
            
            # Group times in pairs (departure/arrival)
            times = []
            for container in time_containers:
                match = time_pattern.search(container.text)
                if match:
                    times.append(match.group(1))
            
            # If we have times, create simple schedule entries
            if len(times) >= 2:
                for i in range(0, len(times) - 1, 2):
                    schedules.append({
                        'departure_time': times[i],
                        'arrival_time': times[i+1] if i+1 < len(times) else "Unknown",
                        'train_number': "Not found",
                        'duration': "Not calculated"
                    })
    else:
        # Process found train rows
        for i, row in enumerate(train_rows):
            try:
                print(f"Processing train row {i+1}")
                
                # Try to extract train information using multiple selectors
                departure_time = extract_with_selectors(row, [
                    '.departure-time', 
                    '.depart-time',
                    '[data-testid*="departure-time"]',
                    'time.departure',
                    'span[data-testid*="departure"]'
                ])
                
                arrival_time = extract_with_selectors(row, [
                    '.arrival-time', 
                    '.arrive-time',
                    '[data-testid*="arrival-time"]',
                    'time.arrival',
                    'span[data-testid*="arrival"]'
                ])
                
                train_number = extract_with_selectors(row, [
                    '.train-number', 
                    '.train-type',
                    '[data-testid*="train-number"]',
                    '[data-testid*="train-type"]',
                    'span.train'
                ])
                
                duration = extract_with_selectors(row, [
                    '.duration', 
                    '.travel-time',
                    '[data-testid*="duration"]',
                    'span.time'
                ])
                
                if departure_time or arrival_time:
                    schedules.append({
                        'departure_time': departure_time or 'Unknown',
                        'arrival_time': arrival_time or 'Unknown',
                        'train_number': train_number or 'Unknown',
                        'duration': duration or 'Unknown'
                    })
                    print(f"Added train: {departure_time} -> {arrival_time}, Train: {train_number}, Duration: {duration}")
            except Exception as e:
                print(f"Error extracting data from row {i+1}: {e}")
    
    print(f"Total schedules extracted: {len(schedules)}")
    return schedules

def extract_with_selectors(element, selectors):
    """Try multiple selectors to extract text from an element."""
    for selector in selectors:
        try:
            found = element.select_one(selector)
            if found:
                return found.text.strip()
        except:
            pass
    return None

def generate_pdf_report(train_schedules, date):
    """Generate a PDF report from the train schedule data."""
    # Create HTML template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VR Train Schedule: Lappeenranta to Helsinki</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #0000A0; }
            table { border-collapse: collapse; width: 100%; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #0000A0; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>VR Train Schedule: Lappeenranta to Helsinki</h1>
        <p>Date: {{ date }}</p>
        
        {% if schedules %}
        <table>
            <tr>
                <th>Departure Time</th>
                <th>Arrival Time</th>
                <th>Train Number</th>
                <th>Duration</th>
            </tr>
            {% for schedule in schedules %}
            <tr>
                <td>{{ schedule.departure_time }}</td>
                <td>{{ schedule.arrival_time }}</td>
                <td>{{ schedule.train_number }}</td>
                <td>{{ schedule.duration }}</td>
            </tr>
            {% endfor %}
        </table>
        {% else %}
        <p>No train schedules found for the selected date.</p>
        {% endif %}
    </body>
    </html>
    """
    
    # Render template with data
    template = jinja2.Template(html_template)
    html_content = template.render(schedules=train_schedules, date=date)
    
    # Get desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Save HTML file temporarily
    html_file_path = os.path.join(desktop_path, "vr_schedule_temp.html")
    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Convert HTML to PDF
    pdf_file_path = os.path.join(desktop_path, f"VR_Train_Schedule_{date.replace('.', '_')}.pdf")
    
    try:
        # Try to use pdfkit to convert HTML to PDF
        pdfkit.from_file(html_file_path, pdf_file_path)
    except Exception as e:
        print(f"Error generating PDF with pdfkit: {e}")
        print("Keeping HTML file as output instead.")
        # If PDF generation fails, rename HTML file as the final output
        os.rename(html_file_path, html_file_path.replace("_temp", ""))
        return
    
    # Remove temporary HTML file if PDF was successfully created
    if os.path.exists(html_file_path):
        os.remove(html_file_path)

if __name__ == "__main__":
    vr_train_schedule() 