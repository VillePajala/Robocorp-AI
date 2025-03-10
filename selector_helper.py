from playwright.sync_api import sync_playwright
import time
import sys

print("\n=== VR Train Schedule Element Inspector ===\n")
print("This tool will help you identify selectors for elements on the VR website.")
print("Instructions:")
print("1. The browser will open with DevTools already activated")
print("2. Click on the element selector icon (🔍) in DevTools")
print("3. Click on any element on the page to see its selector")
print("4. Copy the selector from DevTools for use in your automation")
print("5. Press Ctrl+C in this terminal when you're done\n")

url = "https://www.vr.fi/en/departures-and-arrivals"
if len(sys.argv) > 1:
    url = sys.argv[1]

print(f"Opening {url}")
print("Please wait...\n")

with sync_playwright() as p:
    # Launch browser with DevTools open
    browser = p.chromium.launch(headless=False, devtools=True)
    context = browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()
    
    # Go to VR website
    page.goto(url)
    print("Browser opened. You can now inspect elements.")
    
    # Wait for page to fully load
    page.wait_for_load_state("networkidle")
    
    # Add helper to highlight elements when hovered
    page.evaluate("""() => {
        const style = document.createElement('style');
        style.innerHTML = `
            *:hover {
                outline: 2px solid red !important;
                background-color: rgba(255, 255, 0, 0.3) !important;
            }
        `;
        document.head.appendChild(style);
    }""")
    
    print("\nHelpful selectors on VR website:")
    print("- Cookie accept button: #CybotCookiebotDialogBodyButtonAccept")
    print("- From station field: #station-search-from input")
    print("- To station field: #station-search-to input")
    print("- Date picker: [data-testid='datepicker-input']")
    print("- Search button: .search-button")
    print("\nPress Ctrl+C to exit when you're done\n")
    
    try:
        # Keep the browser open until user exits
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClosing browser...")
    
    browser.close()

print("\nSelector helper closed. You can now use the selectors in your automation.") 