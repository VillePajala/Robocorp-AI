# VR Train Schedule Automation Guide

This guide explains how to use the tools in this project to identify selectors on the VR website and run the automation with those selectors.

## Step 1: Find Selectors

First, you need to find the correct selectors for the elements you want to interact with. There are two tools to help with this:

### Element Inspector Tool

1. Double-click on `run_selector_helper.bat` or run `python selector_helper.py`
2. A browser will open with DevTools activated
3. Click on the element selector icon (🔍) in DevTools
4. Click on any element to see its selector
5. Write down the selectors you find for later use
6. Press Ctrl+C in the terminal to close the browser when done

### Interactive Automation Tool

1. Double-click on `run_interactive.bat` or run `python interactive_automation.py`
2. A browser will open and navigate to the VR website
3. Follow the on-screen menu to test different actions
4. You can click elements, type text, and see if your selectors work
5. Choose "Quit" from the menu when you're done

## Step 2: Run the Automation with Your Selectors

Once you've found the correct selectors, you can run the automation with them:

### Option 1: Run with Command-Line Arguments

1. Double-click on `run_automation.bat` or run `python run_with_selectors.py`
2. This will update the selectors.py file with default selectors and ask if you want to run the automation
3. Type 'y' to run or 'n' to update the selectors first

To specify custom selectors, use command-line arguments:

```
run_automation.bat --cookie-button="#myCookieButton" --from-field="#myFromField"
```

Available arguments:
- `--cookie-button`: Selector for the cookie accept button
- `--from-field`: Selector for the FROM station field
- `--to-field`: Selector for the TO station field
- `--date-picker`: Selector for the date picker field
- `--search-button`: Selector for the search button
- `--from-station`: FROM station name (default: Lappeenranta)
- `--to-station`: TO station name (default: Helsinki)

### Option 2: Edit selectors.py Directly

1. Open `selectors.py` in a text editor
2. Replace the selectors with the ones you found
3. Save the file
4. Run `rcc.exe run` to start the automation

## Tips for Finding Good Selectors

1. **ID Selectors** are most reliable: `#element-id`
2. **Data Attributes** are also good: `[data-testid="test-id"]`
3. **Class Selectors** work if unique: `.unique-class-name`
4. **Combination Selectors** may be needed: `div.container > button.search`

## Troubleshooting

- If the automation doesn't find an element, try using a different selector type
- Make sure your selectors are unique on the page
- Some elements may only appear after other actions, so timing is important
- If needed, you can add waits between steps by editing the tasks.py file 