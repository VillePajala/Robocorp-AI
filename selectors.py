"""
VR Train Schedule Selectors Configuration

This file contains all selectors used by the automation script.
Update these selectors if the website changes without modifying the main script.
"""

# Main page selectors
COOKIE_ACCEPT_BUTTON = "#CybotCookiebotDialogBodyButtonAccept"
FROM_FIELD = "#station-search-from input"
TO_FIELD = "#station-search-to input"
DATE_PICKER = "[data-testid='datepicker-input']"
SEARCH_BUTTON = ".search-button"

# Search results selectors
TRAIN_CARD = ".search-results .journey-card"
DEPARTURE_TIME = ".departure-time"
ARRIVAL_TIME = ".arrival-time"
TRAIN_NUMBER = ".train-number"
DURATION = ".journey-duration"
PRICE = ".price-from"

# Define additional selectors as needed 