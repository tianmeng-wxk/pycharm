*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
case01
    open browser    http://www.baidu.com    Chrome
    input text    id=kw    测试
    click element    id=su
    close browser