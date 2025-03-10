# VR Train Schedule Selector Helper

This repository contains tools to help you interact with the VR website and find element selectors without writing code. You can use these tools to identify the right selectors for your automation.

## Available Tools

### 1. Element Inspector Tool (selector_helper.py)

This tool opens a browser with DevTools activated so you can easily inspect elements and find their selectors.

```
python selector_helper.py
```

Features:
- Browser opens with DevTools already activated
- Elements are highlighted in red when you hover over them
- Common VR website selectors are listed in the console
- Browser stays open until you press Ctrl+C

### 2. Interactive Automation Tool (interactive_automation.py)

This tool lets you test selectors by actually clicking and interacting with elements on the page.

```
python interactive_automation.py
```

Features:
- Menu-driven interface for testing different actions
- Click elements using selectors you provide
- Type text into input fields
- Take screenshots at any point
- Wait for specific amounts of time
- Navigate to different URLs

## Common Elements on VR Website

Here are some common elements you might need to interact with:

1. Cookie consent button: `#CybotCookiebotDialogBodyButtonAccept`
2. From station field: `#station-search-from input`
3. To station field: `#station-search-to input`
4. Date selection field: `[data-testid="datepicker-input"]` 
5. Search button: `.search-button`

## Step-by-Step Guide

1. First, use the Element Inspector (selector_helper.py) to identify the selectors you need
2. Then, test the selectors using the Interactive Automation tool (interactive_automation.py)
3. Once you're confident in your selectors, you can incorporate them into your RPA script

## Troubleshooting

- If you don't see elements highlighted, try clicking on the element selector tool in DevTools first
- If an element isn't found, try waiting a few seconds for the page to fully load
- Use different selector types if one isn't working (try ID, class, or attribute selectors)
- For dynamic elements, you may need to wait or use more specific selectors

## Requirements

These tools require:
- Python 3.9 or higher
- Playwright package
- Browser installations (Chrome/Chromium, Firefox, and WebKit)

To install the requirements:
```
pip install playwright
python -m playwright install
``` 