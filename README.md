# VR Train Schedule RPA Robot

A Robocorp RPA robot that:
1. Opens the VR (Finnish Railways) website
2. Enters journey details (Departure: Lappeenranta, Arrival: Helsinki, Date: Today)
3. Scrapes the resulting train schedule
4. Converts the schedule into an HTML report 
5. Generates a PDF from the HTML
6. Saves the PDF to the user's Desktop

## Project Structure

- `conda.yaml`: Environment configuration for Robocorp (includes necessary dependencies)
- `robot.yaml`: Robot configuration file
- `tasks.py`: Python script containing the main automation logic

## Requirements

- Python 3.9.13
- Robocorp RCC
- pdfkit (requires wkhtmltopdf to be installed - see setup notes)

## Setup Notes

This robot requires wkhtmltopdf to be installed on your system for PDF generation. 
You can download it from: https://wkhtmltopdf.org/downloads.html

## How to Run

1. Install Robocorp RCC (Robot Command Center) if not already installed
2. Run the following command in the project directory:
```
rcc run
```

## Output

The robot creates a PDF file on your Desktop named `VR_Train_Schedule_DD_MM_YYYY.pdf` containing the train schedule from Lappeenranta to Helsinki for the current day.

If PDF generation fails (due to missing wkhtmltopdf), an HTML file will be saved instead. 