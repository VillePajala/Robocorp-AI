*** Settings ***
Documentation     A robot that gets the current week number and saves it to a file.
Library          RPA.Browser
Library          DateTime
Library          RPA.FileSystem

*** Tasks ***
Get Week Number
    Open Available Browser    https://www.timeanddate.com/date/
    ${current_week}=    Get Current Week Number
    Create File With Week Number    ${current_week}
    [Teardown]    Close All Browsers

*** Keywords ***
Get Current Week Number
    ${date}=    Get Current Date
    ${week}=    Convert Date    ${date}    result_format=%V
    [Return]    ${week}

Create File With Week Number
    [Arguments]    ${week_number}
    Create File    ${CURDIR}${/}week_number.txt    Current Week Number: ${week_number} 