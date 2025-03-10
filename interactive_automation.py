from playwright.sync_api import sync_playwright
import time
import os
from datetime import datetime

def take_screenshot(page, name):
    """Take a screenshot and save it to the screenshots directory"""
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{screenshots_dir}/{timestamp}_{name}.png"
    page.screenshot(path=filename)
    print(f"Screenshot saved: {filename}")
    return filename

def main():
    """Interactive automation for VR train schedule"""
    print("\n=== Interactive VR Train Schedule Automation ===\n")
    print("This tool lets you interactively test selectors and actions on the VR website.")
    print("You will be prompted for selectors and can see the results of your actions.\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        
        # Start navigation
        print("Opening VR website...")
        page.goto("https://www.vr.fi/en/departures-and-arrivals")
        page.wait_for_load_state("networkidle")
        take_screenshot(page, "initial_page")
        
        # Interactive loop
        while True:
            print("\n=== ACTIONS ===")
            print("1. Click element")
            print("2. Type text into element")
            print("3. Take screenshot")
            print("4. Wait (seconds)")
            print("5. Go to URL")
            print("6. Quit")
            
            choice = input("\nEnter action number (1-6): ")
            
            if choice == "1":
                selector = input("Enter element selector to click (e.g. #button-id, .class-name): ")
                try:
                    page.click(selector)
                    print(f"Clicked element: {selector}")
                    take_screenshot(page, f"after_click_{selector.replace('#', '').replace('.', '').replace(' ', '_')}")
                except Exception as e:
                    print(f"Error clicking element: {e}")
            
            elif choice == "2":
                selector = input("Enter element selector to type into: ")
                text = input("Enter text to type: ")
                try:
                    page.fill(selector, text)
                    print(f"Typed '{text}' into {selector}")
                    take_screenshot(page, f"after_type_{selector.replace('#', '').replace('.', '').replace(' ', '_')}")
                except Exception as e:
                    print(f"Error typing into element: {e}")
            
            elif choice == "3":
                name = input("Enter name for screenshot: ")
                take_screenshot(page, name)
            
            elif choice == "4":
                seconds = input("Enter seconds to wait: ")
                try:
                    time.sleep(int(seconds))
                    print(f"Waited {seconds} seconds")
                except ValueError:
                    print("Please enter a valid number")
            
            elif choice == "5":
                url = input("Enter URL to navigate to: ")
                page.goto(url)
                page.wait_for_load_state("networkidle")
                print(f"Navigated to: {url}")
                take_screenshot(page, "new_page")
            
            elif choice == "6":
                print("Quitting...")
                break
            
            else:
                print("Invalid choice. Please enter a number from 1-6.")
        
        browser.close()

if __name__ == "__main__":
    main() 