from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from twilio.rest import Client

ps5Availability = ""
accountSID = "ACb7a914aad0b52df7181d08e7f3434228"
authToken = "b9baa1e155ac75958721e899156c9482"
twilioCli = Client(accountSID, authToken)
myTwilioNumber = "+16183283103"
myCellPhone = "+16049992505"

def checkForPlayStation():
    os.environ['MOZ_HEADLESS'] = '1'
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", firefox_profile=profile)
    driver.get("https://www.ebgames.ca/PS5/Games/877522/playstation-5")
    try:
        assert "PlayStation 5" in driver.title
    except AssertionError:
        print("EBGames did not load!")
    try:
        assert "Out of Stock" not in driver.page_source
        print("The PS5 is in stock at EB Games!!!! Order here: https://www.ebgames.ca/PS5/Games/877522/playstation-5")
        ps5Availability.append("The PS5 is in stock at EB Games!!!! Order here: https://www.ebgames.ca/PS5/Games/877522/playstation-5")

    except AssertionError:
        print("Not in stock at EB games...")

    driver.get("https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185")
    try:
        assert "PlayStation 5" in driver.title
    except AssertionError:
        print("BestBuy did not load!")
    try:
        assert "PlayStation 5 consoles sold out quickly" not in driver.page_source
        print("The Standard edition PS5 is in stock at Best Buy!!!! Order here: https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185")
        ps5Availability.append("The Standard edition PS5 is in stock at Best Buy!!!! Order here: https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185")
    except AssertionError:
        print("Standard edition not in stock at Best Buy...")

    driver.get("https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184")
    try:
        assert "PlayStation 5" in driver.title
    except AssertionError:
        print("BestBuy did not load!")
    try:
        assert "PlayStation 5 consoles sold out quickly" not in driver.page_source
        print("The Digital edition PS5 is in stock at Best Buy!!!! Order here: https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184")
        ps5Availability.append("The Digital edition PS5 is in stock at Best Buy!!!! Order here: https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184")
    except AssertionError:
         print("Digital edition not in stock at Best Buy...")

    driver.get("https://www.walmart.ca/en/video-games/playstation-5/ps5-consoles/N-9857")
    try:
        assert "PS5" in driver.title
    except AssertionError:
        print("WalMart did not load!")
    try:
        assert "out of stock" not in driver.page_source
        print("The PS5 is in stock at WalMart!!!! Order here: https://www.walmart.ca/en/video-games/playstation-5/ps5-consoles/N-9857")
        ps5Availability.append("The PS5 is in stock at WalMart!!!! Order here: https://www.walmart.ca/en/video-games/playstation-5/ps5-consoles/N-9857")
    except AssertionError:
        print("Not in stock at WalMart...")

    driver.get("https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G?ref_=ast_sto_dp")
    try:
        assert "PlayStation 5" in driver.title
    except AssertionError:
        print("Amazon did not load!")
    try:
        assert "Currently unavailable." not in driver.page_source
        print("The Standard edition PS5 is in stock at Amazon!!!! Order here: https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G?ref_=ast_sto_dp")
        ps5Availability.append("The Standard edition PS5 is in stock at Amazon!!!! Order here: https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G?ref_=ast_sto_dp")
    except AssertionError:
        print("Standard edition not in stock at Amazon...")

    driver.get("https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H?ref_=ast_sto_dp")
    try:
        assert "PlayStation 5" in driver.title
    except AssertionError:
        print("Amazon did not load!")
    try:
        assert "Currently unavailable." not in driver.page_source
        print("The Digital edition PS5 is in stock at Amazon!!!! Order here: https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H?ref_=ast_sto_dp")
        ps5Availability.append("The Digital edition PS5 is in stock at Amazon!!!! Order here: https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H?ref_=ast_sto_dp")
    except AssertionError:
        print("Digital edition not in stock at Amazon...")

    driver.get("https://www.thesource.ca/en-ca/p/108090499")
    try:
        assert "Good news: we’ve got more tech you’ll love." not in driver.page_source
        print("The PS5 is in stock at The Source!!!! Order here: https://www.thesource.ca/en-ca/p/108090499")
        ps5Availability.append("The PS5 is in stock at The Source!!!! Order here: https://www.thesource.ca/en-ca/p/108090499")
    except AssertionError:
        print("PS5 not in stock at The Source...")

    driver.get("https://www1.shoppersdrugmart.ca/en/food-and-electronics/playstation5")
    try:
        assert "PlayStation 5" in driver.title
    except AssertionError:
        print("Shoppers Drug Mart did not load!")
    try:
        assert "Out of stock" not in driver.page_source
        print("The PS5 is in stock at Shoppers Drug Mart!!!! Order here: https://www1.shoppersdrugmart.ca/en/food-and-electronics/playstation5")
        ps5Availability.append("The PS5 is in stock at Shoppers Drug Mart!!!! Order here: https://www1.shoppersdrugmart.ca/en/food-and-electronics/playstation5")
    except AssertionError:
        print("PS5 not in stock at Shoppers Drug Mart...")
        driver.close()
checkForPlayStation()

if ps5Availability != "":
    message = twilioCli.messages.create(body=ps5Availability, from_=myTwilioNumber, to=myCellPhone)
