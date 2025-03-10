"""
VR Train Schedule Automation Command-Line Tool

This tool allows you to run the VR Train Schedule automation with your own selectors.
"""

import os
import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description='Run VR Train Schedule automation with custom selectors')
    
    parser.add_argument('--cookie-button', default='#CybotCookiebotDialogBodyButtonAccept',
                      help='Selector for the cookie accept button')
    
    parser.add_argument('--from-field', default='#station-search-from input',
                      help='Selector for the FROM station field')
    
    parser.add_argument('--to-field', default='#station-search-to input',
                      help='Selector for the TO station field')
    
    parser.add_argument('--date-picker', default='[data-testid="datepicker-input"]',
                      help='Selector for the date picker field')
    
    parser.add_argument('--search-button', default='.search-button',
                      help='Selector for the search button')
    
    parser.add_argument('--from-station', default='Lappeenranta',
                      help='FROM station name (default: Lappeenranta)')
    
    parser.add_argument('--to-station', default='Helsinki',
                      help='TO station name (default: Helsinki)')
    
    return parser.parse_args()

def update_selectors_file(args):
    """Update the selectors.py file with the provided selectors"""
    with open('selectors.py', 'w') as f:
        f.write('"""\nVR Train Schedule Selectors Configuration\n\n')
        f.write('This file contains all selectors used by the automation script.\n')
        f.write('Update these selectors if the website changes without modifying the main script.\n"""\n\n')
        
        f.write(f'# Main page selectors\n')
        f.write(f'COOKIE_ACCEPT_BUTTON = "{args.cookie_button}"\n')
        f.write(f'FROM_FIELD = "{args.from_field}"\n')
        f.write(f'TO_FIELD = "{args.to_field}"\n')
        f.write(f'DATE_PICKER = "{args.date_picker}"\n')
        f.write(f'SEARCH_BUTTON = "{args.search_button}"\n\n')
        
        f.write(f'# Station names\n')
        f.write(f'FROM_STATION = "{args.from_station}"\n')
        f.write(f'TO_STATION = "{args.to_station}"\n\n')
        
        f.write(f'# Search results selectors\n')
        f.write(f'TRAIN_CARD = ".search-results .journey-card"\n')
        f.write(f'DEPARTURE_TIME = ".departure-time"\n')
        f.write(f'ARRIVAL_TIME = ".arrival-time"\n')
        f.write(f'TRAIN_NUMBER = ".train-number"\n')
        f.write(f'DURATION = ".journey-duration"\n')
        f.write(f'PRICE = ".price-from"\n')
    
    print(f"Updated selectors.py with custom selectors")

def main():
    print("\n=== VR Train Schedule Automation Runner ===\n")
    
    # Parse command line arguments
    args = parse_args()
    
    # Update the selectors.py file
    update_selectors_file(args)
    
    # Ask the user if they want to run the automation
    print("\nSelectors have been updated. Ready to run the automation.")
    answer = input("Run the automation now? (y/n): ")
    
    if answer.lower() == 'y':
        print("\nRunning the automation. This may take a few minutes...")
        # Run the automation
        subprocess.run(["rcc.exe", "run"], check=True)
        print("\nAutomation completed!")
    else:
        print("\nAutomation not started. You can run it later with: rcc.exe run")

if __name__ == "__main__":
    main() 