*** Settings ***
Documentation     A robot that gets VR train schedules from Lappeenranta to Helsinki
...               and generates a PDF report.
Library           tasks.py

*** Tasks ***
VR Train Schedule
    vr_train_schedule 