*** Settings ***
Library    ../resources/CustomerKeywords.py

*** Test Cases ***
Validate Customer Login Token
    Customer Login    12345678
    Should Be Equal    ${TOKEN_STATUS}    SUCCESS
    Log    Token received: ${TOKEN}