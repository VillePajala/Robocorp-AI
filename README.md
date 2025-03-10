# Week Number RPA Robot

A simple Robocorp RPA robot that:
1. Opens a browser and navigates to https://www.timeanddate.com/date/
2. Gets the current week number
3. Saves the week number to a text file

## Project Structure

- `conda.yaml`: Environment configuration for Robocorp
- `robot.yaml`: Robot configuration file
- `tasks.robot`: Robot Framework file containing the main task
- `tasks.py`: Python script for additional automation tasks

## Requirements

- Python 3.9.13
- Robocorp RCC

## How to Run

1. Install Robocorp RCC (Robot Command Center)
2. Run the following command in the project directory:
```
rcc run
```

## Output

The robot creates a file named `week_number.txt` containing the current week number. 