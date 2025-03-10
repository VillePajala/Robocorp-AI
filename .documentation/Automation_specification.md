# Project Specification: VR Train Schedule Automation

## 1. Project Overview
**Project Name:** VR Train Schedule Automation  
**Description:**  
This project automates the process of checking the VR (Finnish Railways) website for today's train rides from Lappeenranta to Helsinki. The script will:
- Open the VR journey search page.
- Enter journey details (departure: Lappeenranta, arrival: Helsinki, date: today).
- Scrape the resulting schedule.
- Convert the schedule into an HTML format.
- Generate a PDF from the HTML.
- Save the PDF to the user's Desktop.

**Goal:**  
Demonstrate the speed and efficiency of building a business-relevant automation using AI-assisted coding with Cursor AI and Robocorp.

## 2. Functional Requirements
- **Browser Automation:**  
  - Open VR’s website.
  - Input journey details: "Lappeenranta" (departure), "Helsinki" (arrival), and current date.
  - Submit the search and wait for results.

- **Data Extraction:**  
  - Scrape the train schedule details such as departure time, arrival time, train number, and any additional schedule information.
  - Optionally filter or format the extracted data.

- **PDF Generation:**  
  - Format the extracted data into a clean HTML template.
  - Convert the HTML into a PDF file using a library like `pdfkit`.
  - Save the generated PDF file on the Desktop.

- **Error Handling & Logging:**  
  - Implement error handling to deal with dynamic website changes.
  - Log the automation steps for debugging purposes.

## 3. Technical Requirements
- **Programming Language:** Python
- **Libraries & Tools:**
  - **RPA.Browser.Playwright:** For browser automation.
  - **datetime:** For managing current date information.
  - **pdfkit:** To convert HTML to PDF.
  - *(Optional)* **BeautifulSoup:** For more granular HTML parsing if needed.
- **Development Environment:**  
  - Use Cursor AI with Robocorp’s integration.
  - Local execution via the Robocorp CLI (using `rcc run`).
- **Dependencies Configuration:**  
  - Define dependencies in `conda.yaml` (e.g., `rpaframework`, `pdfkit`, `playwright`).

## 4. Project Files Structure
- `tasks.py`  
  The main automation script.
- `robot.yaml`  
  Robocorp configuration file (defines tasks and settings).
- `conda.yaml`  
  Dependency file specifying required Python packages.

## 5. Non-Functional Requirements
- **Performance:**  
  The automation should complete within a few minutes.
- **Usability:**  
  Minimal user configuration; parameters like current date are auto-handled.
- **Maintainability:**  
  Code should be modular and well-documented to ease updates if the VR website changes.

## 6. Future Enhancements (Optional)
- Parameterize departure and arrival cities for broader use cases.
- Add scheduling features or notifications (e.g., via email) if no trains are found.
- Extend data extraction to include additional train details or alternative routes.
- Adapt the solution for cloud deployment using Robocorp Control Room.

## 7. Questions & Clarifications
1. **Website Details:**  
   - Do you have the current URL and CSS selectors for the VR journey search page? If not, we may need to use placeholders.
2. **Customization:**  
   - Would you like to include options for the user to change the departure and destination cities dynamically?
3. **PDF Formatting:**  
   - Do you have any specific formatting or branding requirements for the PDF output (fonts, headers, logos, etc.)?
4. **Error Handling:**  
   - Are there specific error messages or logging details you’d like to capture for troubleshooting?
5. **Deployment:**  
   - Is the initial focus solely on a local demo, or should the specification be prepared for a future transition to a cloud-based solution via Robocorp Control Room?

*Please review this specification and let me know if there are additional details or modifications you’d like to include.*
