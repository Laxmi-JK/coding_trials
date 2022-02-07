import datetime
import wikipedia
import webbrowser
import os
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import driver as driver
import speech_recognition as sr
import pyttsx3
from keyboard import press
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


print('Loading your AI personal assistant - Eos')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Eos")
wishMe()


if __name__=='__main__':


    while True:
        speak("How may I be of service?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement \
                or "tata" in statement:
            speak('I shall see you later')
            print('I shall see you later')
            break

        if 'thank you' in statement:
            speak("You're welcome")
            print("You're welcome")
            time.sleep(1)
            speak("Is there anything else you would like to do?")
            statement = takeCommand().lower()
            if 'no' in statement:
                speak('Alright then, I shall see you later')
                print('Alright then, I shall see you later')
                break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement or 'what is your name' in statement:
            speak('I am Eos 1 point O your personal assistant. I am programmed to do minor tasks like'
                  'opening google, CLiC, Wikipedia, Youtube and stackoverflow ,predict time,'
                  'predict weather in different cities , get top headline news stories and and you can ask me computational or geographical questions too!!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Laxmi. I was the product of her first actual programming attempt")
            print("I was built by Laxmi. I was the product of her first actual programming attempt")

        elif "open stackoverflow" in statement or "open stack overflow" in statement \
                or "open stack over flow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")

        elif 'news' in statement or 'headlines' in statement:
            news = webbrowser.open_new_tab("https://www.thehindu.com/todays-paper/")
            speak('These are the latest headlines from the Hindu')
            time.sleep(6)


        elif 'ask' in statement or 'what is' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif 'open CLIC' in statement or 'open click' in statement or 'CLIC' in statement or 'open clic' in statement \
                or 'quick' in statement or 'open quick' in statement or 'click' in statement:
            chrome_driver = "C:\\Users\\USER\\python39\\Scripts\\chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver)
            driver.get('https://clic.bham.ac.uk/')
            speak('CLIC is now open. What would you like to do?')
            print('CLIC is now open. What would you like to do?')
            time.sleep(1)
            statement = takeCommand().lower()
            if 'concordance' in statement or 'khan' in statement or 'confidence' in statement \
                    or 'conference' in statement or 'khankho' in statement or 'codons' in statement \
                    or 'dance' in statement:
                CONCORDANCE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/legend/a'
                browser = driver
                button = browser.find_element(By.XPATH, CONCORDANCE_BUTTON_XPATH)
                button.click()
                time.sleep(1)
                speak('The concordance option is now open. What corpora are you searching for?')
                print('The concordance option is now open. What corpora are you searching for?')
                SEARCH_CORPORA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/ul/li/input'
                browser = driver
                button = browser.find_element(By.XPATH, SEARCH_CORPORA_BUTTON_XPATH)
                button.click()
                speak("The Corpora options are Dickens Novels, 19th Century Reference Corpus, Children's Literature, "
                      "Additional Requested Texts and African American Writers ")
                statement = takeCommand().lower()
                if 'Dickens Novels' in statement or 'Decans Novels' in statement \
                        or 'novels' in statement:
                    DNOV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[2]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DNOV_BUTTON_XPATH)
                    button.click()
                elif '19th Century Reference corpus' in statement:
                    NINETEENC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[3]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NINETEENC_BUTTON_XPATH)
                    button.click()
                elif "Children's Literature" in statement:
                    CHILIT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[4]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CHILIT_BUTTON_XPATH)
                    button.click()
                elif "Additional Requested Texts" in statement:
                    ARTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[5]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARTS_BUTTON_XPATH)
                    button.click()
                elif "African American Writers" in statement:
                    AAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[6]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAW_BUTTON_XPATH)
                    button.click()
                elif "Bleak House" in statement or "Bleak House" in statement:
                    BL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[8]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BL_BUTTON_XPATH)
                    button.click()
                elif "Barnaby Rudges" in statement:
                    BR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[9]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BR_BUTTON_XPATH)
                    button.click()
                elif "david copperfield" in statement:
                    DC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[10]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DC_BUTTON_XPATH)
                    button.click()
                elif "Dombey and son" in statement:
                    DAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[11]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DAS_BUTTON_XPATH)
                    button.click()
                elif "The mystery of edwin drood" in statement:
                    TMOED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[12]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TMOED_BUTTON_XPATH)
                    button.click()
                elif "great expectationS" in statement:
                    DE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[13]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DE_BUTTON_XPATH)
                    button.click()
                elif "hard times" in statement:
                    HT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[14]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HT_BUTTON_XPATH)
                    button.click()
                elif "little dorrit" in statement:
                    LD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[15]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LD_BUTTON_XPATH)
                    button.click()
                elif "martin chuzzlewit" in statement:
                    MC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[16]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MC_BUTTON_XPATH)
                    button.click()
                elif "nicholas nickleby" in statement:
                    NN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[17]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NN_BUTTON_XPATH)
                    button.click()
                elif "the old curiosity shop" in statement:
                    TLCS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[18]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TLCS_BUTTON_XPATH)
                    button.click()
                elif "our mutual friend" in statement:
                    OMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[19]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OMF_BUTTON_XPATH)
                    button.click()
                elif "oliver twist" in statement:
                    OT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[20]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OT_BUTTON_XPATH)
                    button.click()
                elif "pickwick papers" in statement:
                    PP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[21]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PP_BUTTON_XPATH)
                    button.click()
                elif "a tale of two cities" in statement:
                    ATOTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[22]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ATOTC_BUTTON_XPATH)
                    button.click()
                elif "agnes grey" in statement:
                    AG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[24]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AG_BUTTON_XPATH)
                    button.click()
                elif "the small house at Allington" in statement:
                    TSHAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[25]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSHAA_BUTTON_XPATH)
                    button.click()
                elif "antonina or the fall of rome" in statement:
                    AOTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[26]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AOTFOR_BUTTON_XPATH)
                    button.click()
                elif "armadale" in statement:
                    A_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[27]'
                    browser = driver
                    button = browser.find_element(By.XPATH, A_BUTTON_XPATH)
                    button.click()
                elif "the hound of the baskervilles" in statement:
                    THOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[28]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THOTB_BUTTON_XPATH)
                    button.click()
                elif "cranford" in statement:
                    C_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[29]'
                    browser = driver
                    button = browser.find_element(By.XPATH, C_BUTTON_XPATH)
                    button.click()
                elif "daniel deronda" in statement:
                    DD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[30]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DD_BUTTON_XPATH)
                    button.click()
                elif "the picture of dorian grey" in statement:
                    TPODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[31]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TPODG_BUTTON_XPATH)
                    button.click()
                elif "dracula" in statement:
                    D_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[32]'
                    browser = driver
                    button = browser.find_element(By.XPATH, D_BUTTON_XPATH)
                    button.click()
                elif "emma" in statement:
                    E_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[33]'
                    browser = driver
                    button = browser.find_element(By.XPATH, E_BUTTON_XPATH)
                    button.click()
                elif "frankenstein" in statement:
                    F_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[34]'
                    browser = driver
                    button = browser.find_element(By.XPATH, F_BUTTON_XPATH)
                    button.click()
                elif "jane eyre" in statement:
                    JE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[35]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JE_BUTTON_XPATH)
                    button.click()
                elif "the strange case of doctor Jekyll and mister hyde" in statement:
                    TSCODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[36]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSCODJAMH_BUTTON_XPATH)
                    button.click()
                elif "jude the obscure" in statement:
                    JTO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[37]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JTO_BUTTON_XPATH)
                    button.click()
                elif "lady audleys secret" in statement:
                    LAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[38]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAS_BUTTON_XPATH)
                    button.click()
                elif "mary barton" in statement:
                    MB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[39]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MB_BUTTON_XPATH)
                    button.click()
                elif "the mill on the floss" in statement:
                    TMOTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[40]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TMOTF_BUTTON_XPATH)
                    button.click()
                elif "the return of the native" in statement:
                    TROTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[41]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TROTN_BUTTON_XPATH)
                    button.click()
                elif "north and south" in statement:
                    NAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[42]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NAS_BUTTON_XPATH)
                    button.click()
                elif "persuasion" in statement:
                    P_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[43]'
                    browser = driver
                    button = browser.find_element(By.XPATH, P_BUTTON_XPATH)
                    button.click()
                elif "the last days of pompeii" in statement:
                    TLDOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[44]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TLDOP_BUTTON_XPATH)
                    button.click()
                elif "pride and prejudice" in statement:
                    PAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[45]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAP_BUTTON_XPATH)
                    button.click()
                elif "the professor" in statement:
                    TP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[46]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TP_BUTTON_XPATH)
                    button.click()
                elif "sybil or the two nations" in statement:
                    SOTTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[47]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SOTTN_BUTTON_XPATH)
                    button.click()
                elif "tess of the d'urbevilles" in statement:
                    TODU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[48]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TODU_BUTTON_XPATH)
                    button.click()
                elif "vanity fair" in statement:
                    VP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[49]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VP_BUTTON_XPATH)
                    button.click()
                elif "vivian grey" in statement:
                    VG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[50]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VG_BUTTON_XPATH)
                    button.click()
                elif "wuthering heights" in statement:
                    WH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[51]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WH_BUTTON_XPATH)
                    button.click()
                elif "the woman in white" in statement:
                    TWIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[52]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TWIW_BUTTON_XPATH)
                    button.click()
                elif "alice's adventures in wonderland" in statement:
                    AAIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[54]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAIW_BUTTON_XPATH)
                    button.click()
                elif "alone in london" in statement:
                    AIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[55]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AIL_BUTTON_XPATH)
                    button.click()
                elif "the story of the amulet " in statement:
                    TSOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[56]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSOTA_BUTTON_XPATH)
                    button.click()
                elif "black beauty" in statement:
                    BB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[57]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BB_BUTTON_XPATH)
                    button.click()
                elif "the brass bottle" in statement:
                    TBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[58]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBB_BUTTON_XPATH)
                    button.click()
                elif "the tale of benjamin bunny" in statement:
                    TTOBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[59]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOBB_BUTTON_XPATH)
                    button.click()
                elif "the settlers in canada" in statement:
                    TSIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[60]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSIC_BUTTON_XPATH)
                    button.click()
                elif "the  carved lions" in statement:
                    TCL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[61]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCL_BUTTON_XPATH)
                    button.click()
                elif "with clive in india" in statement:
                    WCII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[62]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WCII_BUTTON_XPATH)
                    button.click()
                elif "the coral island" in statement:
                    TCI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[63]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCI_BUTTON_XPATH)
                    button.click()
                elif "the crofton boys" in statement:
                    TCB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[64]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCB_BUTTON_XPATH)
                    button.click()
                elif "the cuckoo clock" in statement:
                    TCC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[65]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCC_BUTTON_XPATH)
                    button.click()
                elif "the daisy chain" in statement:
                    TDC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[66]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TDC_BUTTON_XPATH)
                    button.click()
                elif "the fifth form at saint dominics" in statement:
                    TFFASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[67]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TFFASD_BUTTON_XPATH)
                    button.click()
                elif "the dove in the eagles nest" in statement:
                    TDITEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[68]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TDITEN_BUTTON_XPATH)
                    button.click()
                elif "the book of dragons" in statement:
                    TBOD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[69]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBOD_BUTTON_XPATH)
                    button.click()
                elif "dream days" in statement:
                    DRD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[70]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DRD_BUTTON_XPATH)
                    button.click()
                elif "the little duke" in statement:
                    TLD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[71]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TLD_BUTTON_XPATH)
                    button.click()
                elif "eric" in statement:
                    ER_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[72]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ER_BUTTON_XPATH)
                    button.click()
                elif "feats on the fiord" in statement:
                    FOTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[73]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FOTF_BUTTON_XPATH)
                    button.click()
                elif "five children and it" in statement:
                    FCAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[74]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FCAI_BUTTON_XPATH)
                    button.click()
                elif "the tale of the flopsy bunnies" in statement:
                    TTOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[75]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOTFB_BUTTON_XPATH)
                    button.click()
                elif "the children of the new forest" in statement:
                    TCOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[76]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCOTNF_BUTTON_XPATH)
                    button.click()
                elif "a world of girls" in statement:
                    AWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[77]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AWOG_BUTTON_XPATH)
                    button.click()
                elif "through the looking glass" in statement:
                    TTLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[78]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTLG_BUTTON_XPATH)
                    button.click()
                elif "the golden age" in statement:
                    TGA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[79]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TGA_BUTTON_XPATH)
                    button.click()
                elif "holiday house" in statement:
                    HH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[80]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HH_BUTTON_XPATH)
                    button.click()
                elif "madam how and lady why" in statement:
                    MHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[81]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MHALW_BUTTON_XPATH)
                    button.click()
                elif "jackanapes" in statement:
                    J_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[82]'
                    browser = driver
                    button = browser.find_element(By.XPATH, J_BUTTON_XPATH)
                    button.click()
                elif "the tale of jemima puddle duck" in statement:
                    TTOJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[83]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOJP_BUTTON_XPATH)
                    button.click()
                elif "jessicas first prayer" in statement:
                    JFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[84]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JFP_BUTTON_XPATH)
                    button.click()
                elif "the jungle book" in statement:
                    TJB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[85]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TJB_BUTTON_XPATH)
                    button.click()
                elif "kidnapped" in statement:
                    K_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[86]'
                    browser = driver
                    button = browser.find_element(By.XPATH, K_BUTTON_XPATH)
                    button.click()
                elif "leila at home" in statement:
                    LAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[87]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAH_BUTTON_XPATH)
                    button.click()
                elif "masterman ready" in statement:
                    MR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[88]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MR_BUTTON_XPATH)
                    button.click()
                elif "little meg's children" in statement:
                    LMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[89]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LMC_BUTTON_XPATH)
                    button.click()
                elif "the tale of two bad mice" in statement:
                    TTOTBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[90]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOTBM_BUTTON_XPATH)
                    button.click()
                elif "moonfleet" in statement:
                    MF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[91]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MF_BUTTON_XPATH)
                    button.click()
                elif "mopsa the fairy" in statement:
                    MTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[92]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MTF_BUTTON_XPATH)
                    button.click()
                elif "the three mulla-mulgars" in statement:
                    TTMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[93]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTMM_BUTTON_XPATH)
                    button.click()
                elif "mrs. overtheways remembrances" in statement:
                    MOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[94]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MOR_BUTTON_XPATH)
                    button.click()
                elif "peter pan" in statement:
                    PEPA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[95]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PEPA_BUTTON_XPATH)
                    button.click()
                elif "the peasant and the prince" in statement:
                    TPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[96]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TPATP_BUTTON_XPATH)
                    button.click()
                elif "prince prigio" in statement:
                    PRPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[97]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PRPR_BUTTON_XPATH)
                    button.click()
                elif "the happy prince" in statement:
                    THP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[98]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THP_BUTTON_XPATH)
                    button.click()
                elif "the princess and the goblin" in statement:
                    TPATG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[99]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TPATG_BUTTON_XPATH)
                    button.click()
                elif "allan quatermain" in statement:
                    AQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[100]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AQ_BUTTON_XPATH)
                    button.click()
                elif "the tale of peter rabbit" in statement:
                    TTOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[101]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOPR_BUTTON_XPATH)
                    button.click()
                elif "the railway children" in statement:
                    TRC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[102]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TRC_BUTTON_XPATH)
                    button.click()
                elif "the heir of redclyffe" in statement:
                    THOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[103]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THOR_BUTTON_XPATH)
                    button.click()
                elif "the rival crusoes" in statement:
                    TRCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[104]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TRCR_BUTTON_XPATH)
                    button.click()
                elif "the rose and the ring" in statement:
                    TRATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[105]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TRATR_BUTTON_XPATH)
                    button.click()
                elif "the secret garden" in statement:
                    TSG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[106]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSG_BUTTON_XPATH)
                    button.click()
                elif "the story of the treasure seekers" in statement:
                    TSOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[107]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSOTTS_BUTTON_XPATH)
                    button.click()
                elif "the settlers at home" in statement:
                    TSAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[108]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSAH_BUTTON_XPATH)
                    button.click()
                elif "king solomons mines" in statement:
                    KSM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[109]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KSM_BUTTON_XPATH)
                    button.click()
                elif "the tale of squirrel nutkin" in statement:
                    TTOSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[110]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOSN_BUTTON_XPATH)
                    button.click()
                elif "stalky and co" in statement:
                    SAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[111]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAC_BUTTON_XPATH)
                    button.click()
                elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                        or "the black brothers" in statement:
                    TKOTGROTBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[112]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TKOTGROTBB_BUTTON_XPATH)
                    button.click()
                elif "the tapestry room" in statement:
                    TTR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[113]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTR_BUTTON_XPATH)
                    button.click()
                elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                    TSAOSTLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[114]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSAOSTLWTOGNS_BUTTON_XPATH)
                    button.click()
                elif "tom brown's schooldays" in statement:
                    TBS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[115]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBS_BUTTON_XPATH)
                    button.click()
                elif "treasure island" in statement:
                    TI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[116]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TI_BUTTON_XPATH)
                    button.click()
                elif "nine unlikely tales" in statement:
                    NUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[117]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NUT_BUTTON_XPATH)
                    button.click()
                elif "vise versa" in statement:
                    VV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[118]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VV_BUTTON_XPATH)
                    button.click()
                elif "adventures in wallypug land" in statement:
                    AIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[119]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AIW_BUTTON_XPATH)
                    button.click()
                elif "the water babies" in statement:
                    TWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[120]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TWB_BUTTON_XPATH)
                    button.click()
                elif "the wind in the willows" in statement:
                    TWITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[121]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TWITW_BUTTON_XPATH)
                    button.click()
                elif "at the back of the north wind" in statement:
                    ATBOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[122]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ATBOTNW_BUTTON_XPATH)
                    button.click()
                elif "winning his spurs" in statement:
                    WHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[123]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WHS_BUTTON_XPATH)
                    button.click()
                elif "wood magic" in statement:
                    WM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[124]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WM_BUTTON_XPATH)
                    button.click()
                elif "american notes for general circulation" in statement:
                    ANFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[126]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ANFGC_BUTTON_XPATH)
                    button.click()
                elif "the awakening and several short stories" in statement:
                    TAASSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[127]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAASSS_BUTTON_XPATH)
                    button.click()
                elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                        or "a ghost story of christmas" in statement:
                    ACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[128]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ACCAGSOC_BUTTON_XPATH)
                    button.click()
                elif "gullivers travels" in statement:
                    GT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[129]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GT_BUTTON_XPATH)
                    button.click()
                elif "heart of darkness" in statement:
                    HOD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[130]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HOD_BUTTON_XPATH)
                    button.click()
                elif "adventures of huckleberry finn" in statement:
                    AOHF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[131]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AOHF_BUTTON_XPATH)
                    button.click()
                elif "lady susan" in statement:
                    LS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[132]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LS_BUTTON_XPATH)
                    button.click()
                elif "what maisie knew" in statement:
                    WMK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[133]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WMK_BUTTON_XPATH)
                    button.click()
                elif "mansfield park" in statement:
                    MP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[134]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MP_BUTTON_XPATH)
                    button.click()
                elif "middlemarch" in statement:
                    M_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[135]'
                    browser = driver
                    button = browser.find_element(By.XPATH, M_BUTTON_XPATH)
                    button.click()
                elif "the moonstone" in statement:
                    TM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[136]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TM_BUTTON_XPATH)
                    button.click()
                elif "northanger abbey" in statement:
                    NA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[137]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NA_BUTTON_XPATH)
                    button.click()
                elif "pictures from italy" in statement:
                    PFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[138]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PFI_BUTTON_XPATH)
                    button.click()
                elif "portrait of a lady volume 1" in statement:
                    POALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[139]'
                    browser = driver
                    button = browser.find_element(By.XPATH, POALO_BUTTON_XPATH)
                    button.click()
                elif "portrait of a lady volume 2" in statement:
                    POALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[140]'
                    browser = driver
                    button = browser.find_element(By.XPATH, POALT_BUTTON_XPATH)
                    button.click()
                elif "a room with a view" in statement:
                    ARWAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[141]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARWAV_BUTTON_XPATH)
                    button.click()
                elif "sense and sensibility" in statement:
                    SAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[142]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAS_BUTTON_XPATH)
                    button.click()
                elif "shirley" in statement:
                    S_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[143]'
                    browser = driver
                    button = browser.find_element(By.XPATH, S_BUTTON_XPATH)
                    button.click()
                elif "the sign of four" in statement:
                    TSOF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[144]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSOF_BUTTON_XPATH)
                    button.click()
                elif "silas marner" in statement:
                    SM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[145]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SM_BUTTON_XPATH)
                    button.click()

                elif "the return of the soldier" in statement:
                    TROTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[147]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TROTS_BUTTON_XPATH)
                    button.click()
                elif "the tenant of wildfell hall" in statement:
                    TTOWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[148]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTOWH_BUTTON_XPATH)
                    button.click()
                elif "the jungle" in statement:
                    TJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[149]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TJ_BUTTON_XPATH)
                    button.click()
                elif "the time machine" in statement:
                    TTM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[150]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TTM_BUTTON_XPATH)
                    button.click()
                elif "twelve years a slave" in statement:
                    TYAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[151]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TYAS_BUTTON_XPATH)
                    button.click()
                elif "the uncommercial traveller" in statement:
                    TUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[152]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TUT_BUTTON_XPATH)
                    button.click()
                elif "vilette" in statement:
                    V_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[153]'
                    browser = driver
                    button = browser.find_element(By.XPATH, V_BUTTON_XPATH)
                    button.click()
                elif "the war of worlds" in statement:
                    TWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[154]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TWOW_BUTTON_XPATH)
                    button.click()
                elif "women in love" in statement:
                    WIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[155]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WIL_BUTTON_XPATH)
                    button.click()
                elif "the yellow wallpaper" in statement:
                    TYW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[156]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TYW_BUTTON_XPATH)
                    button.click()
                elif "the house behind the cedars" in statement:
                    THBTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[158]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THBTC_BUTTON_XPATH)
                    button.click()
                elif "the colonel's dream" in statement:
                    TCD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[159]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCD_BUTTON_XPATH)
                    button.click()
                elif "the autobiography of an ex-coloured man" in statement:
                    TAOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[160]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAOAEM_BUTTON_XPATH)
                    button.click()
                elif "imperium in imperio" in statement:
                    III_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[161]'
                    browser = driver
                    button = browser.find_element(By.XPATH, III_BUTTON_XPATH)
                    button.click()
                elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                        or "iola leroy" in statement:
                    ILOSU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[162]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ILOSU_BUTTON_XPATH)
                    button.click()
                elif "the marrow of tradition" in statement:
                    TMOT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[163]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TMOT_BUTTON_XPATH)
                    button.click()
                elif "the sport of the gods" in statement:
                    TSOTG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[164]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSOTG_BUTTON_XPATH)
                    button.click()
                elif "unfettered" in statement:
                    U_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[165]'
                    browser = driver
                    button = browser.find_element(By.XPATH, U_BUTTON_XPATH)
                    button.click()
                elif "agnes strickland" in statement:
                    AS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[167]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AS_BUTTON_XPATH)
                    button.click()
                elif "andrew lang" in statement:
                    AL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[168]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AL_BUTTON_XPATH)
                    button.click()
                elif "ann fraser tytler" in statement:
                    AFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[169]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AFT_BUTTON_XPATH)
                    button.click()
                elif "anna sewell" in statement:
                    ASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[170]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ASE_BUTTON_XPATH)
                    button.click()
                elif "anne bronte" in statement:
                    AB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[171]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AB_BUTTON_XPATH)
                    button.click()
                elif "anthony trollope" in statement:
                    ATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[172]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ATR_BUTTON_XPATH)
                    button.click()
                elif "arthur conan doyle" in statement:
                    ACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[173]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ACD_BUTTON_XPATH)
                    button.click()
                elif "baron edward bulwer lytton lytton" in statement:
                    BEBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[174]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BEBLL_BUTTON_XPATH)
                    button.click()
                elif "beatrix potter" in statement:
                    BP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[175]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BP_BUTTON_XPATH)
                    button.click()
                elif "bram stoker" in statement:
                    BS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[176]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BS_BUTTON_XPATH)
                    button.click()
                elif "captain frederick marryat" in statement:
                    CFM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[177]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CFM_BUTTON_XPATH)
                    button.click()
                elif "catherine sinclair" in statement:
                    CS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[178]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CS_BUTTON_XPATH)
                    button.click()
                elif "charles dickens" in statement:
                    CD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[179]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CD_BUTTON_XPATH)
                    button.click()
                elif "charles kinglsey" in statement:
                    CK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[180]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CK_BUTTON_XPATH)
                    button.click()
                elif "charles W. chestnutt" in statement:
                    CWC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[181]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CWC_BUTTON_XPATH)
                    button.click()
                elif "charlotte bronte" in statement:
                    CB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[182]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CB_BUTTON_XPATH)
                    button.click()
                elif "charlotte M. yonge" in statement:
                    CMY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[183]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CMY_BUTTON_XPATH)
                    button.click()
                elif "charlotte perkins gilman" in statement:
                    CPG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[184]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CPG_BUTTON_XPATH)
                    button.click()
                elif "D. H. lawrence" in statement:
                    DHL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[185]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DHL_BUTTON_XPATH)
                    button.click()
                elif "E. M. forster" in statement:
                    EMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[186]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EMF_BUTTON_XPATH)
                    button.click()
                elif "E. Nesbit" in statement:
                    EN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[187]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EN_BUTTON_XPATH)
                    button.click()
                elif "earl of beaconsfield benjamin disraeli" in statement:
                    EOBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[188]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EOBBD_BUTTON_XPATH)
                    button.click()
                elif "elizabeth cleghorn gaskell" in statement:
                    ECG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[189]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ECG_BUTTON_XPATH)
                    button.click()
                elif "emily bronte" in statement:
                    EB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[190]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EB_BUTTON_XPATH)
                    button.click()
                elif "F. anstey" in statement:
                    FA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[191]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FA_BUTTON_XPATH)
                    button.click()
                elif "frances E. W. harper" in statement:
                    FEWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[192]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FEWH_BUTTON_XPATH)
                    button.click()
                elif "francis hodgson burnett" in statement:
                    FHB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[193]'
                    browser = driver
                    browser.find_element(By.XPATH, FHB_BUTTON_XPATH)
                    button.click()
                elif "Frederic william farrar" in statement:
                    FWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[194]'
                    browser = driver
                    browser.find_element(By.XPATH, FWF_BUTTON_XPATH)
                    button.click()
                elif "G.A. Henty" in statement:
                    GAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[195]'
                    browser = driver
                    button = browser.find_element(By.XPATH,GAH_BUTTON_XPATH)
                    button.click()
                elif "G.E.Farrow" in statement:
                    GEF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[196]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GEF_BUTTON_XPATH)
                    button.click()
                elif "George Eliot" in statement:
                    GE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[197]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GE_BUTTON_XPATH)
                    button.click()
                elif "Geroge Macdonald" in statement:
                    GM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[198]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GM_BUTTON_XPATH)
                    button.click()
                elif "H. G Wells" in statement:
                    HGW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[199]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HGW_BUTTON_XPATH)
                    button.click()
                elif "H. Rider Haggard" in statement:
                    HRH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[200]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HRH_BUTTON_XPATH)
                    button.click()
                elif "Harriet Martineau" in statement:
                    HM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[201]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HM_BUTTON_XPATH)
                    button.click()
                elif "Henry James" in statement:
                    HJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[202]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HJ_BUTTON_XPATH)
                    button.click()
                elif "Hesba Stretton" in statement:
                    HS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[203]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HS_BUTTON_XPATH)
                    button.click()
                elif "J. Meade Falkner" in statement:
                    JMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[204]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JMF_BUTTON_XPATH)
                    button.click()
                elif "James M. Barrie" in statement:
                    JMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[205]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JMB_BUTTON_XPATH)
                    button.click()
                elif "James Weldon Johnson" in statement:
                    JWJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[206]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JWJ_BUTTON_XPATH)
                    button.click()
                elif "Jane Austen" in statement:
                    JA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[207]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JA_BUTTON_XPATH)
                    button.click()
                elif "Jean Ingelow" in statement:
                    JI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[208]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JI_BUTTON_XPATH)
                    button.click()
                elif "Jonathan Ruskin" in statement:
                    JR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[209]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JR_BUTTON_XPATH)
                    button.click()
                elif "Jonathan Swift" in statement:
                    JS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[210]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JS_BUTTON_XPATH)
                    button.click()
                elif "Joseph Conrad" in statement:
                    JC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[211]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JC_BUTTON_XPATH)
                    button.click()
                elif "Juliana Horatia Ewing" in statement:
                    JHE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[212]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JHE_BUTTON_XPATH)
                    button.click()
                elif "Kate Chopin" in statement:
                    KC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[213]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KC_BUTTON_XPATH)
                    button.click()
                elif "Kenneth Grahame" in statement:
                    KG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[214]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KG_BUTTON_XPATH)
                    button.click()
                elif "L.T. Meade" in statement:
                    LTM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[215]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LTM_BUTTON_XPATH)
                    button.click()
                elif "lewis carroll" in statement:
                    LC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[216]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LC_BUTTON_XPATH)
                    button.click()
                elif "M. E Braddon" in statement:
                    MEB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[217]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MEB_BUTTON_XPATH)
                    button.click()
                elif "mark twain" in statement:
                    MT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[218]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MT_BUTTON_XPATH)
                    button.click()
                elif "mary wollstonecraft shelley" in statement:
                    MWS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[219]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MWS_BUTTON_XPATH)
                    button.click()
                elif "Mrs. Molesworth" in statement:
                    MM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[220]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MM_BUTTON_XPATH)
                    button.click()
                elif "oscar wilde" in statement:
                    OW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[221]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OW_BUTTON_XPATH)
                    button.click()
                elif "paul laurence dunbar" in statement:
                    PLD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[222]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PLD_BUTTON_XPATH)
                    button.click()
                elif "R. M Ballantyne" in statement:
                    RMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[223]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RMB_BUTTON_XPATH)
                    button.click()
                elif "Rebecca West" in statement:
                    RW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[224]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RW_BUTTON_XPATH)
                    button.click()
                elif "Richard Jefferies" in statement:
                    RJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[225]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RJ_BUTTON_XPATH)
                    button.click()
                elif "Robert Louis Stevenson" in statement:
                    RLS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[226]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RLS_BUTTON_XPATH)
                    button.click()
                elif "rudyard kipling" in statement:
                    RK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[227]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RK_BUTTON_XPATH)
                    button.click()
                elif "S. R Crockett" in statement:
                    SRC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[228]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SRC_BUTTON_XPATH)
                    button.click()
                elif "solomon northrup" in statement:
                    SN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[229]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SN_BUTTON_XPATH)
                    button.click()
                elif "sutton E Griggs" in statement:
                    SEG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[230]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SEG_BUTTON_XPATH)
                    button.click()
                elif "talbot baines reed" in statement:
                    TBR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[231]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBR_BUTTON_XPATH)
                    button.click()
                elif "thomas hardy" in statement:
                    THA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[232]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THA_BUTTON_XPATH)
                    button.click()
                elif "thomas hughes" in statement:
                    TH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[233]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TH_BUTTON_XPATH)
                    button.click()
                elif "upton sinclair" in statement:
                    US_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[234]'
                    browser = driver
                    button = browser.find_element(By.XPATH, US_BUTTON_XPATH)
                    button.click()
                elif "walter de la mare" in statement:
                    WDLM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[235]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WDLM_BUTTON_XPATH)
                    button.click()
                elif "wilkie collins" in statement:
                    WC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[236]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WC_BUTTON_XPATH)
                    button.click()
                elif "william makepeace thackeray" in statement:
                    WMT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[1]/form/div[1]/div/ul/li[237]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WMT_BUTTON_XPATH)
                    button.click()
                else:
                    speak("The text was not found")
                    print("Text not found")
                    time.sleep(1)
                    speak("How else may I be of service?")
                    statement = takeCommand().lower()

                el = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/div/div/input')
                for option in el.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/a/span'):
                    option.click()
                speak("The subsets available are displayed. What type of text are you looking for?")
                print("The subsets available are displayed. What type of text are you looking for?")
                statement = takeCommand().lower()
                if 'all text' in statement:
                    el1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/a/span')
                    for option in el1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/div/ul/li[1]'):
                        option.click()
                if 'short suspensions' in statement:
                    el2 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/a/span')
                    for option in el2.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/div/ul/li[2]'):
                        option.click()
                if 'long suspensions' in statement:
                    el3 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/a/span')
                    for option in el3.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/div/ul/li[3]'):
                        option.click()
                if 'quotes' in statement:
                    el4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/a/span')
                    for option in el4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/div/ul/li[4]'):
                        option.click()
                if 'non quotes' in statement:
                    el5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/a/span')
                    for option in el5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[2]/div/ul/li[5]'):
                        option.click()

                speak('please type in your search terms')
                TEXTBOX_TERMS = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/input[1]')
                for option in TEXTBOX_TERMS.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/input[1]'):
                    option.click()
                time.sleep(5)

                speak("Are you looking for a whole phrase or any word?")
                statement = takeCommand().lower()
                if "whole phrase" in statement or 'phrase' in statement:
                    W_P = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[3]/label[1]/input')
                    for option in W_P.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[3]/label[1]/input'):
                        option.click()
                else:
                    A_W = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[3]/label[2]/input')
                    for option in A_W.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[3]/label[2]/input'):
                        option.click()
                press('enter')
                speak("Here are your results")
                speak("do you want to view the results as 'basic results', as 'full metadata', or as a 'distribution plot' ")
                statement = takeCommand().lower()
                if 'basic results' in statement or 'results' in statement:
                    B_R = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/label[5]/input')
                    for option in B_R.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/label[5]/input'):
                        option.click()
                if 'full metadata' in statement or 'metadata'in statement:
                    F_M = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/label[6]/input')
                    for option in F_M.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/label[6]/input'):
                        option.click()
                if 'distribution plot' in statement or 'plot' in statement:
                    D_P = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/label[7]/input')
                    for option in D_P.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/label[7]/input'):
                        option.click()

                speak("would you like to filter any rows?")
                statement = takeCommand().lower()
                if 'yes' in statement:
                    speak('please type in your filter terms')
                    F_R = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/input[2]')
                    for option in F_R.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/input[2]'):
                        option.click()
                    time.sleep(5)
                press('enter')

                speak("would like to you search in span?")
                statement = takeCommand().lower()
                speak("please adjust the slider to your requirements if you wish to search by span")
                time.sleep(2)
                press('enter')

                speak("would you like to search for types?")
                statement = takeCommand().lower()
                speak('please type in your search words if you wish to do so and hit enter')
                S_T = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[5]/ul/li/input')
                for option in S_T.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[1]/form/div[5]/ul/li/input'):
                    option.click()
                    time.sleep(5)
                speak('These are the results for the concordance search')

            if 'subsets' in statement or 'subset' in statement:
                SUBSETS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/legend/a'
                browser = driver
                button = browser.find_element(By.XPATH, SUBSETS_BUTTON_XPATH)
                button.click()
                speak('The subsets option is now open. What corpora are you searching for?')
                statement = takeCommand().lower()
                SEARCH2_CORPORA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/ul'
                browser = driver
                button = browser.find_element(By.XPATH, SEARCH2_CORPORA_BUTTON_XPATH)
                button.click()
                speak("The Corpora options are Dickens Novels, 19th Century Reference Corpus, Children's Literature, "
                      "Additional Requested Texts and African American Writers ")
                statement = takeCommand().lower()
                if 'Dickens Novels' in statement or 'Decans Novels' in statement \
                        or 'novels' in statement:
                    DINOV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[2]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DINOV_BUTTON_XPATH)
                    button.click()
                elif '19th Century Reference corpus' in statement:
                    NINETEENCN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[3]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NINETEENCN_BUTTON_XPATH)
                    button.click()
                elif "Children's Literature" in statement:
                    CHILLIT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[4]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CHILLIT_BUTTON_XPATH)
                    button.click()
                elif "Additional Requested Texts" in statement:
                    ARTSY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[5]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARTSY_BUTTON_XPATH)
                    button.click()
                elif "African American Writers" in statement:
                    AFAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[6]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AFAW_BUTTON_XPATH)
                    button.click()
                elif "Bleak House" in statement or "Bleak House" in statement:
                    BLO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[8]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BLO_BUTTON_XPATH)
                    button.click()
                elif "Barnaby Rudges" in statement:
                    BAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[9]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAR_BUTTON_XPATH)
                    button.click()
                elif "david copperfield" in statement:
                    DAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[10]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DAC_BUTTON_XPATH)
                    button.click()
                elif "Dombey and son" in statement:
                    DOAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[11]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DOAS_BUTTON_XPATH)
                    button.click()
                elif "The mystery of edwin drood" in statement:
                    THMOED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[12]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THMOED_BUTTON_XPATH)
                    button.click()
                elif "great expectationS" in statement:
                    DRE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[13]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DRE_BUTTON_XPATH)
                    button.click()
                elif "hard times" in statement:
                    HAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[14]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HAT_BUTTON_XPATH)
                    button.click()
                elif "little dorrit" in statement:
                    LID_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[15]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LID_BUTTON_XPATH)
                    button.click()
                elif "martin chuzzlewit" in statement:
                    MAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[16]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAC_BUTTON_XPATH)
                    button.click()
                elif "nicholas nickleby" in statement:
                    NIN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[17]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NIN_BUTTON_XPATH)
                    button.click()
                elif "the old curiosity shop" in statement:
                    TOCS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[18]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TOCS_BUTTON_XPATH)
                    button.click()
                elif "our mutual friend" in statement:
                    OUMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[19]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OUMF_BUTTON_XPATH)
                    button.click()
                elif "oliver twist" in statement:
                    OLT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[20]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OLT_BUTTON_XPATH)
                    button.click()
                elif "pickwick papers" in statement:
                    PIP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[21]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PIP_BUTTON_XPATH)
                    button.click()
                elif "a tale of two cities" in statement:
                    ATAOTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[22]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ATAOTC_BUTTON_XPATH)
                    button.click()
                elif "agnes grey" in statement:
                    AGG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[24]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AGG_BUTTON_XPATH)
                    button.click()
                elif "the small house at Allington" in statement:
                    THSHAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[25]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THSHAA_BUTTON_XPATH)
                    button.click()
                elif "antonina or the fall of rome" in statement:
                    ANOTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[26]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ANOTFOR_BUTTON_XPATH)
                    button.click()
                elif "armadale" in statement:
                    AR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[27]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AR_BUTTON_XPATH)
                    button.click()
                elif "the hound of the baskervilles" in statement:
                    THHOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[28]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THHOTB_BUTTON_XPATH)
                    button.click()
                elif "cranford" in statement:
                    CR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[29]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CR_BUTTON_XPATH)
                    button.click()
                elif "daniel deronda" in statement:
                    DAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[30]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DAD_BUTTON_XPATH)
                    button.click()
                elif "the picture of dorian grey" in statement:
                    THPODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[31]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THPODG_BUTTON_XPATH)
                    button.click()
                elif "dracula" in statement:
                    DR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[32]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DR_BUTTON_XPATH)
                    button.click()
                elif "emma" in statement:
                    EM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[33]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EM_BUTTON_XPATH)
                    button.click()
                elif "frankenstein" in statement:
                    FR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[34]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FR_BUTTON_XPATH)
                    button.click()
                elif "jane eyre" in statement:
                    JAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[35]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JAE_BUTTON_XPATH)
                    button.click()
                elif "the strange case of doctor Jekyll and mister hyde" in statement:
                    TASCODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[36]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASCODJAMH_BUTTON_XPATH)
                    button.click()
                elif "jude the obscure" in statement:
                    JATO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[37]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JATO_BUTTON_XPATH)
                    button.click()
                elif "lady audleys secret" in statement:
                    LAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[38]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAAS_BUTTON_XPATH)
                    button.click()
                elif "mary barton" in statement:
                    MBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[39]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MBA_BUTTON_XPATH)
                    button.click()
                elif "the mill on the floss" in statement:
                    TAMOTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[40]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAMOTF_BUTTON_XPATH)
                    button.click()
                elif "the return of the native" in statement:
                    TAROTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[41]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAROTN_BUTTON_XPATH)
                    button.click()
                elif "north and south" in statement:
                    NAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[42]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NAAS_BUTTON_XPATH)
                    button.click()
                elif "persuasion" in statement:
                    PA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[43]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PA_BUTTON_XPATH)
                    button.click()
                elif "the last days of pompeii" in statement:
                    TALDOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[44]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TALDOP_BUTTON_XPATH)
                    button.click()
                elif "pride and prejudice" in statement:
                    PAAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[45]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAAP_BUTTON_XPATH)
                    button.click()
                elif "the professor" in statement:
                    TAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[46]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAP_BUTTON_XPATH)
                    button.click()
                elif "sybil or the two nations" in statement:
                    SAOTTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[47]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAOTTN_BUTTON_XPATH)
                    button.click()
                elif "tess of the d'urbevilles" in statement:
                    TAODU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[48]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAODU_BUTTON_XPATH)
                    button.click()
                elif "vanity fair" in statement:
                    VAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[49]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VAP_BUTTON_XPATH)
                    button.click()
                elif "vivian grey" in statement:
                    VAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[50]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VAG_BUTTON_XPATH)
                    button.click()
                elif "wuthering heights" in statement:
                    WAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[51]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WAH_BUTTON_XPATH)
                    button.click()
                elif "the woman in white" in statement:
                    TAWIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[52]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAWIW_BUTTON_XPATH)
                    button.click()
                elif "alice's adventures in wonderland" in statement:
                    AAAIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[54]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAAIW_BUTTON_XPATH)
                    button.click()
                elif "alone in london" in statement:
                    AAIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[55]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAIL_BUTTON_XPATH)
                    button.click()
                elif "the story of the amulet " in statement:
                    TSAOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[56]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSAOTA_BUTTON_XPATH)
                    button.click()
                elif "black beauty" in statement:
                    BBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[57]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BBA_BUTTON_XPATH)
                    button.click()
                elif "the brass bottle" in statement:
                    TABB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[58]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABB_BUTTON_XPATH)
                    button.click()
                elif "the tale of benjamin bunny" in statement:
                    TATOBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[59]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOBB_BUTTON_XPATH)
                    button.click()
                elif "the settlers in canada" in statement:
                    TASIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[60]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASIC_BUTTON_XPATH)
                    button.click()
                elif "the  carved lions" in statement:
                    TACL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[61]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACL_BUTTON_XPATH)
                    button.click()
                elif "with clive in india" in statement:
                    WACII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[62]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WACII_BUTTON_XPATH)
                    button.click()
                elif "the coral island" in statement:
                    TACI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[63]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACI_BUTTON_XPATH)
                    button.click()
                elif "the crofton boys" in statement:
                    TACB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[64]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACB_BUTTON_XPATH)
                    button.click()
                elif "the cuckoo clock" in statement:
                    TACC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[65]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACC_BUTTON_XPATH)
                    button.click()
                elif "the daisy chain" in statement:
                    TADC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[66]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TADC_BUTTON_XPATH)
                    button.click()
                elif "the fifth form at saint dominics" in statement:
                    TAFFASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[67]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAFFASD_BUTTON_XPATH)
                    button.click()
                elif "the dove in the eagles nest" in statement:
                    TADITEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[68]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TADITEN_BUTTON_XPATH)
                    button.click()
                elif "the book of dragons" in statement:
                    TABOD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[69]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABOD_BUTTON_XPATH)
                    button.click()
                elif "dream days" in statement:
                    DARD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[70]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DARD_BUTTON_XPATH)
                    button.click()
                elif "the little duke" in statement:
                    TALD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[71]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TALD_BUTTON_XPATH)
                    button.click()
                elif "eric" in statement:
                    EAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[72]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EAR_BUTTON_XPATH)
                    button.click()
                elif "feats on the fiord" in statement:
                    FOATF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[73]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FOATF_BUTTON_XPATH)
                    button.click()
                elif "five children and it" in statement:
                    FACAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[74]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FACAI_BUTTON_XPATH)
                    button.click()
                elif "the tale of the flopsy bunnies" in statement:
                    TATOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[75]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOTFB_BUTTON_XPATH)
                    button.click()
                elif "the children of the new forest" in statement:
                    TACOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[76]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACOTNF_BUTTON_XPATH)
                    button.click()
                elif "a world of girls" in statement:
                    AAWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[77]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAWOG_BUTTON_XPATH)
                    button.click()
                elif "through the looking glass" in statement:
                    TATLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[78]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATLG_BUTTON_XPATH)
                    button.click()
                elif "the golden age" in statement:
                    TAGA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[79]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAGA_BUTTON_XPATH)
                    button.click()
                elif "holiday house" in statement:
                    HAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[80]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HAH_BUTTON_XPATH)
                    button.click()
                elif "madam how and lady why" in statement:
                    MAHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[81]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAHALW_BUTTON_XPATH)
                    button.click()
                elif "jackanapes" in statement:
                    JA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[82]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JA_BUTTON_XPATH)
                    button.click()
                elif "the tale of jemima puddle duck" in statement:
                    TATOJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[83]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOJP_BUTTON_XPATH)
                    button.click()
                elif "jessicas first prayer" in statement:
                    JAFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[84]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JAFP_BUTTON_XPATH)
                    button.click()
                elif "the jungle book" in statement:
                    TAJB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[85]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAJB_BUTTON_XPATH)
                    button.click()
                elif "kidnapped" in statement:
                    KA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[86]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KA_BUTTON_XPATH)
                    button.click()
                elif "leila at home" in statement:
                    LAAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[87]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAAH_BUTTON_XPATH)
                    button.click()
                elif "masterman ready" in statement:
                    MAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[88]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAR_BUTTON_XPATH)
                    button.click()
                elif "little meg's children" in statement:
                    LAMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[89]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAMC_BUTTON_XPATH)
                    button.click()
                elif "the tale of two bad mice" in statement:
                    TATOTBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[90]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOTBM_BUTTON_XPATH)
                    button.click()
                elif "moonfleet" in statement:
                    MAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[91]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAF_BUTTON_XPATH)
                    button.click()
                elif "mopsa the fairy" in statement:
                    MATF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[92]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MATF_BUTTON_XPATH)
                    button.click()
                elif "the three mulla-mulgars" in statement:
                    TATMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[93]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATMM_BUTTON_XPATH)
                    button.click()
                elif "mrs. overtheways remembrances" in statement:
                    MAOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[94]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAOR_BUTTON_XPATH)
                    button.click()
                elif "peter pan" in statement:
                    PAEPA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[95]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAEPA_BUTTON_XPATH)
                    button.click()
                elif "the peasant and the prince" in statement:
                    TAPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[96]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAPATP_BUTTON_XPATH)
                    button.click()
                elif "prince prigio" in statement:
                    PARPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[97]'
                    browser = driver
                    button =   browser.find_element(By.XPATH, PARPR_BUTTON_XPATH)
                    button.click()
                elif "the happy prince" in statement:
                    TAHP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[98]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAHP_BUTTON_XPATH)
                    button.click()
                elif "the princess and the goblin" in statement:
                    TPATA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[99]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TPATA_BUTTON_XPATH)
                    button.click()
                elif "allan quatermain" in statement:
                    AAQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[100]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAQ_BUTTON_XPATH)
                    button.click()
                elif "the tale of peter rabbit" in statement:
                    TATOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[101]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOPR_BUTTON_XPATH)
                    button.click()
                elif "the railway children" in statement:
                    TARC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[102]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TARC_BUTTON_XPATH)
                    button.click()
                elif "the heir of redclyffe" in statement:
                    TAHOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[103]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAHOR_BUTTON_XPATH)
                    button.click()
                elif "the rival crusoes" in statement:
                    TARCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[104]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TARCR_BUTTON_XPATH)
                    button.click()
                elif "the rose and the ring" in statement:
                    TARATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[105]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TARATR_BUTTON_XPATH)
                    button.click()
                elif "the secret garden" in statement:
                    TASG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[106]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASG_BUTTON_XPATH)
                    button.click()
                elif "the story of the treasure seekers" in statement:
                    TASOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[107]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASOTTS_BUTTON_XPATH)
                    button.click()
                elif "the settlers at home" in statement:
                    TASAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[108]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASAH_BUTTON_XPATH)
                    button.click()
                elif "king solomons mines" in statement:
                    KASM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[109]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KASM_BUTTON_XPATH)
                    button.click()
                elif "the tale of squirrel nutkin" in statement:
                    TATOSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[110]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOSN_BUTTON_XPATH)
                    button.click()
                elif "stalky and co" in statement:
                    SAAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[111]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAAC_BUTTON_XPATH)
                    button.click()
                elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                        or "the black brothers" in statement:
                    TAKOTGROTBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[112]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAKOTGROTBB_BUTTON_XPATH)
                    button.click()
                elif "the tapestry room" in statement:
                    TATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[113]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATR_BUTTON_XPATH)
                    button.click()
                elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                    TASAOSTLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[114]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASAOSTLWTOGNS_BUTTON_XPATH)
                    button.click()
                elif "tom brown's schooldays" in statement:
                    TABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[115]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABS_BUTTON_XPATH)
                    button.click()
                elif "treasure island" in statement:
                    TAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[116]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAI_BUTTON_XPATH)
                    button.click()
                elif "nine unlikely tales" in statement:
                    NAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[117]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NAUT_BUTTON_XPATH)
                    button.click()
                elif "vise versa" in statement:
                    VAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[118]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VAV_BUTTON_XPATH)
                    button.click()
                elif "adventures in wallypug land" in statement:
                    AAIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[119]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAIW_BUTTON_XPATH)
                    button.click()
                elif "the water babies" in statement:
                    TAWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[120]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAWB_BUTTON_XPATH)
                    button.click()
                elif "the wind in the willows" in statement:
                    TAWITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[121]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAWITW_BUTTON_XPATH)
                    button.click()
                elif "at the back of the north wind" in statement:
                    AATBOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[122]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AATBOTNW_BUTTON_XPATH)
                    button.click()
                elif "winning his spurs" in statement:
                    WAHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[123]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WAHS_BUTTON_XPATH)
                    button.click()
                elif "wood magic" in statement:
                    WAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[124]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WAM_BUTTON_XPATH)
                    button.click()
                elif "american notes for general circulation" in statement:
                    AANFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[126]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AANFGC_BUTTON_XPATH)
                    button.click()
                elif "the awakening and several short stories" in statement:
                    TAAASSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[127]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAAASSS_BUTTON_XPATH)
                    button.click()
                elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                        or "a ghost story of christmas" in statement:
                    AACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[128]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AACCAGSOC_BUTTON_XPATH)
                    button.click()
                elif "gullivers travels" in statement:
                    AGT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[129]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AGT_BUTTON_XPATH)
                    button.click()
                elif "heart of darkness" in statement:
                    HODA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[130]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HODA_BUTTON_XPATH)
                    button.click()
                elif "adventures of huckleberry finn" in statement:
                    AOHAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[131]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AOHAF_BUTTON_XPATH)
                    button.click()
                elif "lady susan" in statement:
                    LAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[132]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAS_BUTTON_XPATH)
                    button.click()
                elif "what maisie knew" in statement:
                    WMAK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[133]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WMAK_BUTTON_XPATH)
                    button.click()
                elif "mansfield park" in statement:
                    MAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[134]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAP_BUTTON_XPATH)
                    button.click()
                elif "middlemarch" in statement:
                    MA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[135]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MA_BUTTON_XPATH)
                    button.click()
                elif "the moonstone" in statement:
                    TAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[136]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAM_BUTTON_XPATH)
                    button.click()
                elif "northanger abbey" in statement:
                    NAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[137]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NAA_BUTTON_XPATH)
                    button.click()
                elif "pictures from italy" in statement:
                    PAFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[138]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAFI_BUTTON_XPATH)
                    button.click()
                elif "portrait of a lady volume 1" in statement:
                    PAOALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[139]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAOALO_BUTTON_XPATH)
                    button.click()
                elif "portrait of a lady volume 2" in statement:
                    PAOALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[140]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAOALT_BUTTON_XPATH)
                    button.click()
                elif "a room with a view" in statement:
                    ARAWAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[141]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARAWAV_BUTTON_XPATH)
                    button.click()
                elif "sense and sensibility" in statement:
                    SAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[142]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAAS_BUTTON_XPATH)
                    button.click()
                elif "shirley" in statement:
                    SA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[143]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SA_BUTTON_XPATH)
                    button.click()
                elif "the sign of four" in statement:
                    TSAOF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[144]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSAOF_BUTTON_XPATH)
                    button.click()
                elif "silas marner" in statement:
                    SAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[145]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAM_BUTTON_XPATH)
                    button.click()
                elif "the return of the soldier" in statement:
                    TAROTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[147]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAROTS_BUTTON_XPATH)
                    button.click()
                elif "the tenant of wildfell hall" in statement:
                    TATOWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[148]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOWH_BUTTON_XPATH)
                    button.click()
                elif "the jungle" in statement:
                    TAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[149]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAJ_BUTTON_XPATH)
                    button.click()
                elif "the time machine" in statement:
                    TATM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[150]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATM_BUTTON_XPATH)
                    button.click()
                elif "twelve years a slave" in statement:
                    TYAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[151]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TYAAS_BUTTON_XPATH)
                    button.click()
                elif "the uncommercial traveller" in statement:
                    TAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[152]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAUT_BUTTON_XPATH)
                    button.click()
                elif "vilette" in statement:
                    VA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[153]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VA_BUTTON_XPATH)
                    button.click()
                elif "the war of worlds" in statement:
                    TAWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[154]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAWOW_BUTTON_XPATH)
                    button.click()
                elif "women in love" in statement:
                    WIAL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[155]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WIAL_BUTTON_XPATH)
                    button.click()
                elif "the yellow wallpaper" in statement:
                    TAYW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[156]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAYW_BUTTON_XPATH)
                    button.click()
                elif "the house behind the cedars" in statement:
                    THABTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[158]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THABTC_BUTTON_XPATH)
                    button.click()
                elif "the colonel's dream" in statement:
                    TCAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[159]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCAD_BUTTON_XPATH)
                    button.click()
                elif "the autobiography of an ex-coloured man" in statement:
                    TAAOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[160]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAAOAEM_BUTTON_XPATH)
                    button.click()
                elif "imperium in imperio" in statement:
                    IIAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[161]'
                    browser = driver
                    button = browser.find_element(By.XPATH, IIAI_BUTTON_XPATH)
                    button.click()
                elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                        or "iola leroy" in statement:
                    ILOSAU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[162]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ILOSAU_BUTTON_XPATH)
                    button.click()
                elif "the marrow of tradition" in statement:
                    TMOAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[163]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TMOAT_BUTTON_XPATH)
                    button.click()
                elif "the sport of the gods" in statement:
                    TSOTAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[164]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSOTAG_BUTTON_XPATH)
                    button.click()
                elif "unfettered" in statement:
                    UA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[165]'
                    browser = driver
                    button = browser.find_element(By.XPATH, UA_BUTTON_XPATH)
                    button.click()
                elif "agnes strickland" in statement:
                    ASA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[167]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ASA_BUTTON_XPATH)
                    button.click()
                elif "andrew lang" in statement:
                    AAL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[168]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAL_BUTTON_XPATH)
                    button.click()
                elif "ann fraser tytler" in statement:
                    AAFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[169]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAFT_BUTTON_XPATH)
                    button.click()
                elif "anna sewell" in statement:
                    AASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[170]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AASE_BUTTON_XPATH)
                    button.click()
                elif "anne bronte" in statement:
                    AAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[171]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAB_BUTTON_XPATH)
                    button.click()
                elif "anthony trollope" in statement:
                    ATAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[172]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ATAR_BUTTON_XPATH)
                    button.click()
                elif "arthur conan doyle" in statement:
                    AACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[173]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AACD_BUTTON_XPATH)
                    button.click()
                elif "baron edward bulwer lytton lytton" in statement:
                    BAEBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[174]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAEBLL_BUTTON_XPATH)
                    button.click()
                elif "beatrix potter" in statement:
                    BAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[175]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAP_BUTTON_XPATH)
                    button.click()
                elif "bram stoker" in statement:
                    BAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[176]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAS_BUTTON_XPATH)
                    button.click()
                elif "captain frederick marryat" in statement:
                    CFAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[177]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CFAM_BUTTON_XPATH)
                    button.click()
                elif "catherine sinclair" in statement:
                    CAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[178]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAS_BUTTON_XPATH)
                    button.click()
                elif "charles dickens" in statement:
                    CAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[179]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAD_BUTTON_XPATH)
                    button.click()
                elif "charles kinglsey" in statement:
                    CAK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[180]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAK_BUTTON_XPATH)
                    button.click()
                elif "charles W. chestnutt" in statement:
                    CAWC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[181]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAWC_BUTTON_XPATH)
                    button.click()
                elif "charlotte bronte" in statement:
                    CAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[182]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAB_BUTTON_XPATH)
                    button.click()
                elif "charlotte M. yonge" in statement:
                    CMAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[183]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CMAY_BUTTON_XPATH)
                    button.click()
                elif "charlotte perkins gilman" in statement:
                    CPAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[184]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CPAG_BUTTON_XPATH)
                    button.click()
                elif "D. H. lawrence" in statement:
                    DHAL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[185]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DHAL_BUTTON_XPATH)
                    button.click()
                elif "E. M. forster" in statement:
                    EMAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[186]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EMAF_BUTTON_XPATH)
                    button.click()
                elif "E. Nesbit" in statement:
                    EAN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[187]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EAN_BUTTON_XPATH)
                    button.click()
                elif "earl of beaconsfield benjamin disraeli" in statement:
                    EAOBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[188]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EAOBBD_BUTTON_XPATH)
                    button.click()
                elif "elizabeth cleghorn gaskell" in statement:
                    EACG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[189]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EACG_BUTTON_XPATH)
                    button.click()
                elif "emily bronte" in statement:
                    EAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[190]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EAB_BUTTON_XPATH)
                    button.click()
                elif "F. anstey" in statement:
                    FAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[191]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FAA_BUTTON_XPATH)
                    button.click()
                elif "frances E. W. harper" in statement:
                    FAEWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[192]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FAEWH_BUTTON_XPATH)
                    button.click()
                elif "francis hodgson burnett" in statement:
                    FHAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[193]'
                    browser = driver
                    browser.find_element(By.XPATH, FHAB_BUTTON_XPATH)
                    button.click()
                elif "Frederic william farrar" in statement:
                    FAWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[194]'
                    browser = driver
                    browser.find_element(By.XPATH, FAWF_BUTTON_XPATH)
                    button.click()
                elif "G.A. Henty" in statement:
                    GAAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[195]'
                    browser = driver
                    button = browser.find_element(By.XPATH,GAAH_BUTTON_XPATH)
                    button.click()
                elif "G.E.Farrow" in statement:
                    GEAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[196]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GEAF_BUTTON_XPATH)
                    button.click()
                elif "George Eliot" in statement:
                    GAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[197]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GAE_BUTTON_XPATH)
                    button.click()
                elif "Geroge Macdonald" in statement:
                    AGM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[198]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AGM_BUTTON_XPATH)
                    button.click()
                elif "H. G Wells" in statement:
                    HGAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[199]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HGAW_BUTTON_XPATH)
                    button.click()
                elif "H. Rider Haggard" in statement:
                    HRAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[200]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HRAH_BUTTON_XPATH)
                    button.click()
                elif "Harriet Martineau" in statement:
                    HAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[201]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HAM_BUTTON_XPATH)
                    button.click()
                elif "Henry James" in statement:
                    HAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[202]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HAJ_BUTTON_XPATH)
                    button.click()
                elif "Hesba Stretton" in statement:
                    HAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[203]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HAS_BUTTON_XPATH)
                    button.click()
                elif "J. Meade Falkner" in statement:
                    JMAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[204]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JMAF_BUTTON_XPATH)
                    button.click()
                elif "James M. Barrie" in statement:
                    JMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[205]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JMB_BUTTON_XPATH)
                    button.click()
                elif "James Weldon Johnson" in statement:
                    JWAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[206]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JWAJ_BUTTON_XPATH)
                    button.click()
                elif "Jane Austen" in statement:
                    JAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[207]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JAA_BUTTON_XPATH)
                    button.click()
                elif "Jean Ingelow" in statement:
                    JAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[208]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JAI_BUTTON_XPATH)
                    button.click()
                elif "Jonathan Ruskin" in statement:
                    JRA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[209]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JRA_BUTTON_XPATH)
                    button.click()
                elif "Jonathan Swift" in statement:
                    JSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[210]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JSA_BUTTON_XPATH)
                    button.click()
                elif "Joseph Conrad" in statement:
                    JCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[211]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JCA_BUTTON_XPATH)
                    button.click()
                elif "Juliana Horatia Ewing" in statement:
                    JHAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[212]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JHAE_BUTTON_XPATH)
                    button.click()
                elif "Kate Chopin" in statement:
                    KCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[213]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KCA_BUTTON_XPATH)
                    button.click()
                elif "Kenneth Grahame" in statement:
                    KGA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[214]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KGA_BUTTON_XPATH)
                    button.click()
                elif "L.T. Meade" in statement:
                    LTMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[215]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LTMA_BUTTON_XPATH)
                    button.click()
                elif "lewis carroll" in statement:
                    LCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[216]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LCA_BUTTON_XPATH)
                    button.click()
                elif "M. E Braddon" in statement:
                    MEBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[217]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MEBA_BUTTON_XPATH)
                    button.click()
                elif "mark twain" in statement:
                    MTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[218]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MTA_BUTTON_XPATH)
                    button.click()
                elif "mary wollstonecraft shelley" in statement:
                    MWSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[219]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MWSA_BUTTON_XPATH)
                    button.click()
                elif "Mrs. Molesworth" in statement:
                    MMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[220]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MMA_BUTTON_XPATH)
                    button.click()
                elif "oscar wilde" in statement:
                    OWA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[221]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OWA_BUTTON_XPATH)
                    button.click()
                elif "paul laurence dunbar" in statement:
                    PLDA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[222]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PLDA_BUTTON_XPATH)
                    button.click()
                elif "R. M Ballantyne" in statement:
                    RAMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[223]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RAMB_BUTTON_XPATH)
                    button.click()
                elif "Rebecca West" in statement:
                    RAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[224]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RAW_BUTTON_XPATH)
                    button.click()
                elif "Richard Jefferies" in statement:
                    RJA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[225]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RJA_BUTTON_XPATH)
                    button.click()
                elif "Robert Louis Stevenson" in statement:
                    RLAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[226]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RLAS_BUTTON_XPATH)
                    button.click()
                elif "rudyard kipling" in statement:
                    RKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[227]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RKA_BUTTON_XPATH)
                    button.click()
                elif "S. R Crockett" in statement:
                    SRCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[228]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SRCA_BUTTON_XPATH)
                    button.click()
                elif "solomon northrup" in statement:
                    SNA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[229]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SNA_BUTTON_XPATH)
                    button.click()
                elif "sutton E Griggs" in statement:
                    SEGA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[230]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SEGA_BUTTON_XPATH)
                    button.click()
                elif "talbot baines reed" in statement:
                    TBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[231]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBAR_BUTTON_XPATH)
                    button.click()
                elif "thomas hardy" in statement:
                    TAHA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[232]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAHA_BUTTON_XPATH)
                    button.click()
                elif "thomas hughes" in statement:
                    THA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[233]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THA_BUTTON_XPATH)
                    button.click()
                elif "upton sinclair" in statement:
                    UAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[234]'
                    browser = driver
                    button = browser.find_element(By.XPATH, UAS_BUTTON_XPATH)
                    button.click()
                elif "walter de la mare" in statement:
                    WDLAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[235]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WDLAM_BUTTON_XPATH)
                    button.click()
                elif "wilkie collins" in statement:
                    WCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[236]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WCA_BUTTON_XPATH)
                    button.click()
                elif "william makepeace thackeray" in statement:
                    WMTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[2]/form/div[1]/div/ul/li[237]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WMTA_BUTTON_XPATH)
                    button.click()
                else:
                    speak("The text was not found")
                    print("Text not found")
                    time.sleep(1)
                    speak("How else may I be of service?")
                    statement = takeCommand().lower()

                sue = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/div/input')
                for option in sue.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/a/span'):
                    option.click()
                speak("The subsets available are displayed. What type of text are you looking for?")
                print("The subsets available are displayed. What type of text are you looking for?")
                statement = takeCommand().lower()
                if 'short suspensions' in statement or 'short' in statement:
                    sue1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[1]')
                    for option in sue1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[1]'):
                        option.click()
                if 'long suspensions' in statement or 'long' in statement:
                    sue3 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[2]')
                    for option in sue3.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[2]'):
                        option.click()
                if 'quotes' in statement or 'quote' in statement or 'hote' in statement:
                    sue4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[3]')
                    for option in sue4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[3]'):
                        option.click()
                if 'non quotes' in statement or 'non' in statement:
                    sue5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[4]')
                    for option in sue5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[2]/div/ul/li[4]'):
                        option.click()
                press('enter')
                speak("Here are your results")

                speak("do you want to view the results as 'basic results', as 'full metadata', or as a 'distribution plot' ")
                statement = takeCommand().lower()
                if 'basic results' in statement or 'results' in statement:
                    BA_R = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/label[4]/input')
                    for option in BA_R.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/label[4]/input'):
                        option.click()
                if 'full metadata' in statement or 'metadata'in statement:
                    FA_M = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/label[5]/input')
                    for option in FA_M.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/label[5]/input'):
                        option.click()
                if 'distribution plot' in statement or 'plot' in statement:
                    DA_P = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/label[6]/input')
                    for option in DA_P.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/label[6]/input'):
                        option.click()
                speak("would you like to filter any rows?")
                statement = takeCommand().lower()
                if 'yes' in statement:
                    speak('please type in your filter terms')
                    F_R = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/input[1]')
                    for option in F_R.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/input[1]'):
                        option.click()
                    time.sleep(5)
                    press('enter')

                speak("would you like to search in subset?")
                statement = takeCommand().lower()
                speak("please adjust the slider to your requirements if you wish to search by subset")
                time.sleep(5)
                press('enter')

                speak("would you like to search for types?")
                statement = takeCommand().lower()
                speak('please type in your search words if you wish to do so and press the enter key')
                SA_T = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[6]/ul/li/input')
                for option in SA_T.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[2]/form/div[6]/ul/li/input'):
                    option.click()
                    time.sleep(5)
                press('enter')
                speak('These are the results for the subset search')

            if 'clusters' in statement or 'cluster' in statement:
                CLUSTERS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/legend/a'
                browser = driver
                button = browser.find_element(By.XPATH, CLUSTERS_BUTTON_XPATH)
                button.click()
                speak('The clusters option is now open. What corpora are you searching for?')
                SEARCH3_CORPORA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/ul'
                browser = driver
                button = browser.find_element(By.XPATH, SEARCH3_CORPORA_BUTTON_XPATH)
                button.click()
                speak("The Corpora options are Dickens Novels, 19th Century Reference Corpus, Children's Literature, "
                      "Additional Requested Texts and African American Writers ")
                statement = takeCommand().lower()
                if 'Dickens Novels' in statement or 'Decans Novels' in statement \
                        or 'novels' in statement:
                    DBNOV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[2]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DBNOV_BUTTON_XPATH)
                    button.click()
                elif '19th Century Reference corpus' in statement:
                    NINETEENB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[3]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NINETEENB_BUTTON_XPATH)
                    button.click()
                elif "Children's Literature" in statement:
                    CBHILLIT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[4]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CBHILLIT_BUTTON_XPATH)
                    button.click()
                elif "Additional Requested Texts" in statement:
                    ARBTSY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[5]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARBTSY_BUTTON_XPATH)
                    button.click()
                elif "African American Writers" in statement:
                    AFBAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[6]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AFBAW_BUTTON_XPATH)
                    button.click()
                elif "Bleak House" in statement or "Bleak House" in statement:
                    BLOB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[8]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BLOB_BUTTON_XPATH)
                    button.click()
                elif "Barnaby Rudges" in statement:
                    BBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[9]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BBAR_BUTTON_XPATH)
                    button.click()
                elif "david copperfield" in statement:
                    DACB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[10]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DACB_BUTTON_XPATH)
                    button.click()
                elif "Dombey and son" in statement:
                    DOABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[11]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DOABS_BUTTON_XPATH)
                    button.click()
                elif "The mystery of edwin drood" in statement:
                    THMOBED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[12]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THMOBED_BUTTON_XPATH)
                    button.click()
                elif "great expectationS" in statement:
                    DREB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[13]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DREB_BUTTON_XPATH)
                    button.click()
                elif "hard times" in statement:
                    BHAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[14]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BHAT_BUTTON_XPATH)
                    button.click()
                elif "little dorrit" in statement:
                    BLID_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[15]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BLID_BUTTON_XPATH)
                    button.click()
                elif "martin chuzzlewit" in statement:
                    MACB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[16]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MACB_BUTTON_XPATH)
                    button.click()
                elif "nicholas nickleby" in statement:
                    NINB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[17]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NINB_BUTTON_XPATH)
                    button.click()
                elif "the old curiosity shop" in statement:
                    TOCBS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[18]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TOCBS_BUTTON_XPATH)
                    button.click()
                elif "our mutual friend" in statement:
                    BOUMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[19]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BOUMF_BUTTON_XPATH)
                    button.click()
                elif "oliver twist" in statement:
                    BOLT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[20]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BOLT_BUTTON_XPATH)
                    button.click()
                elif "pickwick papers" in statement:
                    PIPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[21]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PIPB_BUTTON_XPATH)
                    button.click()
                elif "a tale of two cities" in statement:
                    ATAOTCB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[22]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ATAOTCB_BUTTON_XPATH)
                    button.click()
                elif "agnes grey" in statement:
                    AGGB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[24]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AGGB_BUTTON_XPATH)
                    button.click()
                elif "the small house at Allington" in statement:
                    THSHAAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[25]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THSHAAB_BUTTON_XPATH)
                    button.click()
                elif "antonina or the fall of rome" in statement:
                    ANOBTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[26]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ANOBTFOR_BUTTON_XPATH)
                    button.click()
                elif "armadale" in statement:
                    ARB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[27]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARB_BUTTON_XPATH)
                    button.click()
                elif "the hound of the baskervilles" in statement:
                    BTHHOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[28]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BTHHOTB_BUTTON_XPATH)
                    button.click()
                elif "cranford" in statement:
                    CRB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[29]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CRB_BUTTON_XPATH)
                    button.click()
                elif "daniel deronda" in statement:
                    DBAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[30]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DBAD_BUTTON_XPATH)
                    button.click()
                elif "the picture of dorian grey" in statement:
                    THPBODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[31]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THPBODG_BUTTON_XPATH)
                    button.click()
                elif "dracula" in statement:
                    DRB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[32]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DRB_BUTTON_XPATH)
                    button.click()
                elif "emma" in statement:
                    BEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[33]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BEM_BUTTON_XPATH)
                    button.click()
                elif "frankenstein" in statement:
                    FRB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[34]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FRB_BUTTON_XPATH)
                    button.click()
                elif "jane eyre" in statement:
                    JAEB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[35]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JAEB_BUTTON_XPATH)
                    button.click()
                elif "the strange case of doctor Jekyll and mister hyde" in statement:
                    TASCBODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[36]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASCBODJAMH_BUTTON_XPATH)
                    button.click()
                elif "jude the obscure" in statement:
                    JATOB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[37]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JATOB_BUTTON_XPATH)
                    button.click()
                elif "lady audleys secret" in statement:
                    LAABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[38]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LAABS_BUTTON_XPATH)
                    button.click()
                elif "mary barton" in statement:
                    MBBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[39]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MBBA_BUTTON_XPATH)
                    button.click()
                elif "the mill on the floss" in statement:
                    TAMOBTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[40]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAMOBTF_BUTTON_XPATH)
                    button.click()
                elif "the return of the native" in statement:
                    TAROTBN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[41]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAROTBN_BUTTON_XPATH)
                    button.click()
                elif "north and south" in statement:
                    NAASB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[42]'
                    browser = driver
                    button = browser.find_element(By.XPATH, NAASB_BUTTON_XPATH)
                    button.click()
                elif "persuasion" in statement:
                    PAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[43]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAB_BUTTON_XPATH)
                    button.click()
                elif "the last days of pompeii" in statement:
                    TALDBOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[44]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TALDBOP_BUTTON_XPATH)
                    button.click()
                elif "pride and prejudice" in statement:
                    PBAAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[45]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PBAAP_BUTTON_XPATH)
                    button.click()
                elif "the professor" in statement:
                    TABP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[46]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABP_BUTTON_XPATH)
                    button.click()
                elif "sybil or the two nations" in statement:
                    SAOTBTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[47]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAOTBTN_BUTTON_XPATH)
                    button.click()
                elif "tess of the d'urbevilles" in statement:
                    TAODBU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[48]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAODBU_BUTTON_XPATH)
                    button.click()
                elif "vanity fair" in statement:
                    VAPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[49]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VAPB_BUTTON_XPATH)
                    button.click()
                elif "vivian grey" in statement:
                    VABG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[50]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VABG_BUTTON_XPATH)
                    button.click()
                elif "wuthering heights" in statement:
                    WBAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[51]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WBAH_BUTTON_XPATH)
                    button.click()
                elif "the woman in white" in statement:
                    TAWBIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[52]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAWBIW_BUTTON_XPATH)
                    button.click()
                elif "alice's adventures in wonderland" in statement:
                    AAAIBW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[54]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AAAIBW_BUTTON_XPATH)
                    button.click()
                elif "alone in london" in statement:
                    AABIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[55]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABIL_BUTTON_XPATH)
                    button.click()
                elif "the story of the amulet " in statement:
                    TSBAOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[56]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSBAOTA_BUTTON_XPATH)
                    button.click()
                elif "black beauty" in statement:
                    BBAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[57]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BBAB_BUTTON_XPATH)
                    button.click()
                elif "the brass bottle" in statement:
                    TABB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[58]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABB_BUTTON_XPATH)
                    button.click()
                elif "the tale of benjamin bunny" in statement:
                    TATOBBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[59]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOBBB_BUTTON_XPATH)
                    button.click()
                elif "the settlers in canada" in statement:
                    TASBIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[60]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASBIC_BUTTON_XPATH)
                    button.click()
                elif "the  carved lions" in statement:
                    TBACL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[61]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBACL_BUTTON_XPATH)
                    button.click()
                elif "with clive in india" in statement:
                    WABCII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[62]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WABCII_BUTTON_XPATH)
                    button.click()
                elif "the coral island" in statement:
                    TACBI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[63]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACBI_BUTTON_XPATH)
                    button.click()
                elif "the crofton boys" in statement:
                    TACBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[64]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACBB_BUTTON_XPATH)
                    button.click()
                elif "the cuckoo clock" in statement:
                    TACBC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[65]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TACBC_BUTTON_XPATH)
                    button.click()
                elif "the daisy chain" in statement:
                    TADCB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[66]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TADCB_BUTTON_XPATH)
                    button.click()
                elif "the fifth form at saint dominics" in statement:
                    TAFFBASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[67]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAFFBASD_BUTTON_XPATH)
                    button.click()
                elif "the dove in the eagles nest" in statement:
                    TADITBEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[68]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TADITBEN_BUTTON_XPATH)
                    button.click()
                elif "the book of dragons" in statement:
                    TABOBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[69]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABOBD_BUTTON_XPATH)
                    button.click()
                elif "dream days" in statement:
                    DARBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[70]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DARBD_BUTTON_XPATH)
                    button.click()
                elif "the little duke" in statement:
                    TALBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[71]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TALBD_BUTTON_XPATH)
                    button.click()
                elif "eric" in statement:
                    BEAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[72]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BEAR_BUTTON_XPATH)
                    button.click()
                elif "feats on the fiord" in statement:
                    FOABTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[73]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FOABTF_BUTTON_XPATH)
                    button.click()
                elif "five children and it" in statement:
                    FACBAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[74]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FACBAI_BUTTON_XPATH)
                    button.click()
                elif "the tale of the flopsy bunnies" in statement:
                    TBATOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[75]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBATOTFB_BUTTON_XPATH)
                    button.click()
                elif "the children of the new forest" in statement:
                    TABCOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[76]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABCOTNF_BUTTON_XPATH)
                    button.click()
                elif "a world of girls" in statement:
                    AABWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[77]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABWOG_BUTTON_XPATH)
                    button.click()
                elif "through the looking glass" in statement:
                    TABTLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[78]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABTLG_BUTTON_XPATH)
                    button.click()
                elif "the golden age" in statement:
                    TAGBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[79]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAGBA_BUTTON_XPATH)
                    button.click()
                elif "holiday house" in statement:
                    HBAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[80]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HBAH_BUTTON_XPATH)
                    button.click()
                elif "madam how and lady why" in statement:
                    MBAHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[81]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MBAHALW_BUTTON_XPATH)
                    button.click()
                elif "jackanapes" in statement:
                    JBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[82]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JBA_BUTTON_XPATH)
                    button.click()
                elif "the tale of jemima puddle duck" in statement:
                    TATOBJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[83]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOBJP_BUTTON_XPATH)
                    button.click()
                elif "jessicas first prayer" in statement:
                    JBAFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[84]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JBAFP_BUTTON_XPATH)
                    button.click()
                elif "the jungle book" in statement:
                    TAJBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[85]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAJBB_BUTTON_XPATH)
                    button.click()
                elif "kidnapped" in statement:
                    BKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[86]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BKA_BUTTON_XPATH)
                    button.click()
                elif "leila at home" in statement:
                    LABAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[87]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LABAH_BUTTON_XPATH)
                    button.click()
                elif "masterman ready" in statement:
                    MBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[88]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MBAR_BUTTON_XPATH)
                    button.click()
                elif "little meg's children" in statement:
                    LABMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[89]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LABMC_BUTTON_XPATH)
                    button.click()
                elif "the tale of two bad mice" in statement:
                    TATOTBBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[90]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOTBBM_BUTTON_XPATH)
                    button.click()
                elif "moonfleet" in statement:
                    MABF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[91]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MABF_BUTTON_XPATH)
                    button.click()
                elif "mopsa the fairy" in statement:
                    MABTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[92]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MABTF_BUTTON_XPATH)
                    button.click()
                elif "the three mulla-mulgars" in statement:
                    TATBMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[93]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATBMM_BUTTON_XPATH)
                    button.click()
                elif "mrs. overtheways remembrances" in statement:
                    MAORB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[94]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MAORB_BUTTON_XPATH)
                    button.click()
                elif "peter pan" in statement:
                    PAEPBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[95]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PAEPBA_BUTTON_XPATH)
                    button.click()
                elif "the peasant and the prince" in statement:
                    TABPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[96]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABPATP_BUTTON_XPATH)
                    button.click()
                elif "prince prigio" in statement:
                    PABRPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[97]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PABRPR_BUTTON_XPATH)
                    button.click()
                elif "the happy prince" in statement:
                    TABHP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[98]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABHP_BUTTON_XPATH)
                    button.click()
                elif "the princess and the goblin" in statement:
                    TPATGB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[99]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TPATGB_BUTTON_XPATH)
                    button.click()
                elif "allan quatermain" in statement:
                    AABQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[100]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABQ_BUTTON_XPATH)
                    button.click()
                elif "the tale of peter rabbit" in statement:
                    TBATOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[101]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBATOPR_BUTTON_XPATH)
                    button.click()
                elif "the railway children" in statement:
                    TARBC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[102]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TARBC_BUTTON_XPATH)
                    button.click()
                elif "the heir of redclyffe" in statement:
                    TAHOBR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[103]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAHOBR_BUTTON_XPATH)
                    button.click()
                elif "the rival crusoes" in statement:
                    TARBCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[104]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TARBCR_BUTTON_XPATH)
                    button.click()
                elif "the rose and the ring" in statement:
                    TBARATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[105]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBARATR_BUTTON_XPATH)
                    button.click()
                elif "the secret garden" in statement:
                    TASBG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[106]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASBG_BUTTON_XPATH)
                    button.click()
                elif "the story of the treasure seekers" in statement:
                    TBASOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[107]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBASOTTS_BUTTON_XPATH)
                    button.click()
                elif "the settlers at home" in statement:
                    TASABH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[108]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASABH_BUTTON_XPATH)
                    button.click()
                elif "king solomons mines" in statement:
                    KABSM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[109]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KABSM_BUTTON_XPATH)
                    button.click()
                elif "the tale of squirrel nutkin" in statement:
                    TATOBSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[110]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOBSN_BUTTON_XPATH)
                    button.click()
                elif "stalky and co" in statement:
                    SBAAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[111]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SBAAC_BUTTON_XPATH)
                    button.click()
                elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                        or "the black brothers" in statement:
                    TAKOTBGROTBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[112]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAKOTBGROTBB_BUTTON_XPATH)
                    button.click()
                elif "the tapestry room" in statement:
                    TABTR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[113]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABTR_BUTTON_XPATH)
                    button.click()
                elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                    TASAOSTBLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[114]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TASAOSTBLWTOGNS_BUTTON_XPATH)
                    button.click()
                elif "tom brown's schooldays" in statement:
                    TBABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[115]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBABS_BUTTON_XPATH)
                    button.click()
                elif "treasure island" in statement:
                    TAIB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[116]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAIB_BUTTON_XPATH)
                    button.click()
                elif "nine unlikely tales" in statement:
                    BNAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[117]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BNAUT_BUTTON_XPATH)
                    button.click()
                elif "vise versa" in statement:
                    VAVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[118]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VAVB_BUTTON_XPATH)
                    button.click()
                elif "adventures in wallypug land" in statement:
                    AABIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[119]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABIW_BUTTON_XPATH)
                    button.click()
                elif "the water babies" in statement:
                    TABWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[120]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABWB_BUTTON_XPATH)
                    button.click()
                elif "the wind in the willows" in statement:
                    TAWBITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[121]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAWBITW_BUTTON_XPATH)
                    button.click()
                elif "at the back of the north wind" in statement:
                    ABATBOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[122]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABATBOTNW_BUTTON_XPATH)
                    button.click()
                elif "winning his spurs" in statement:
                    WABHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[123]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WABHS_BUTTON_XPATH)
                    button.click()
                elif "wood magic" in statement:
                    WABM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[124]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WABM_BUTTON_XPATH)
                    button.click()
                elif "american notes for general circulation" in statement:
                    AABNFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[126]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABNFGC_BUTTON_XPATH)
                    button.click()
                elif "the awakening and several short stories" in statement:
                    TAAABSSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[127]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAAABSSS_BUTTON_XPATH)
                    button.click()
                elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                        or "a ghost story of christmas" in statement:
                    ABACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[128]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABACCAGSOC_BUTTON_XPATH)
                    button.click()
                elif "gullivers travels" in statement:
                    ABGT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[129]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABGT_BUTTON_XPATH)
                    button.click()
                elif "heart of darkness" in statement:
                    HODBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[130]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HODBA_BUTTON_XPATH)
                    button.click()
                elif "adventures of huckleberry finn" in statement:
                    AOHABF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[131]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AOHABF_BUTTON_XPATH)
                    button.click()
                elif "lady susan" in statement:
                    LABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[132]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LABS_BUTTON_XPATH)
                    button.click()
                elif "what maisie knew" in statement:
                    WMABK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[133]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WMABK_BUTTON_XPATH)
                    button.click()
                elif "mansfield park" in statement:
                    MBAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[134]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MBAP_BUTTON_XPATH)
                    button.click()
                elif "middlemarch" in statement:
                    BMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[135]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BMA_BUTTON_XPATH)
                    button.click()
                elif "the moonstone" in statement:
                    TBAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[136]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBAM_BUTTON_XPATH)
                    button.click()
                elif "northanger abbey" in statement:
                    BNAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[137]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BNAA_BUTTON_XPATH)
                    button.click()
                elif "pictures from italy" in statement:
                    BPAFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[138]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BPAFI_BUTTON_XPATH)
                    button.click()
                elif "portrait of a lady volume 1" in statement:
                    BPAOALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[139]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BPAOALO_BUTTON_XPATH)
                    button.click()
                elif "portrait of a lady volume 2" in statement:
                    BPAOALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[140]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BPAOALT_BUTTON_XPATH)
                    button.click()
                elif "a room with a view" in statement:
                    ARBAWAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[141]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ARBAWAV_BUTTON_XPATH)
                    button.click()
                elif "sense and sensibility" in statement:
                    SAABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[142]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SAABS_BUTTON_XPATH)
                    button.click()
                elif "shirley" in statement:
                    BSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[143]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BSA_BUTTON_XPATH)
                    button.click()
                elif "the sign of four" in statement:
                    TSAOBF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[144]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSAOBF_BUTTON_XPATH)
                    button.click()
                elif "silas marner" in statement:
                    SABM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[145]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SABM_BUTTON_XPATH)
                    button.click()
                elif "the return of the soldier" in statement:
                    TAROBTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[147]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAROBTS_BUTTON_XPATH)
                    button.click()
                elif "the tenant of wildfell hall" in statement:
                    TATOBWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[148]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TATOBWH_BUTTON_XPATH)
                    button.click()
                elif "the jungle" in statement:
                    BTAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[149]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BTAJ_BUTTON_XPATH)
                    button.click()
                elif "the time machine" in statement:
                    TBATM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[150]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBATM_BUTTON_XPATH)
                    button.click()
                elif "twelve years a slave" in statement:
                    BTYAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[151]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BTYAAS_BUTTON_XPATH)
                    button.click()
                elif "the uncommercial traveller" in statement:
                    BTAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[152]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BTAUT_BUTTON_XPATH)
                    button.click()
                elif "vilette" in statement:
                    VBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[153]'
                    browser = driver
                    button = browser.find_element(By.XPATH, VBA_BUTTON_XPATH)
                    button.click()
                elif "the war of worlds" in statement:
                    TBAWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[154]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBAWOW_BUTTON_XPATH)
                    button.click()
                elif "women in love" in statement:
                    WIABL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[155]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WIABL_BUTTON_XPATH)
                    button.click()
                elif "the yellow wallpaper" in statement:
                    TBAYW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[156]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBAYW_BUTTON_XPATH)
                    button.click()
                elif "the house behind the cedars" in statement:
                    THABBTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[158]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THABBTC_BUTTON_XPATH)
                    button.click()
                elif "the colonel's dream" in statement:
                    TCBAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[159]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TCBAD_BUTTON_XPATH)
                    button.click()
                elif "the autobiography of an ex-coloured man" in statement:
                    TAABOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[160]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TAABOAEM_BUTTON_XPATH)
                    button.click()
                elif "imperium in imperio" in statement:
                    IBIAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[161]'
                    browser = driver
                    button = browser.find_element(By.XPATH, IBIAI_BUTTON_XPATH)
                    button.click()
                elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                        or "iola leroy" in statement:
                    ILOSBAU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[162]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ILOSBAU_BUTTON_XPATH)
                    button.click()
                elif "the marrow of tradition" in statement:
                    TMOBAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[163]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TMOBAT_BUTTON_XPATH)
                    button.click()
                elif "the sport of the gods" in statement:
                    TSOBTAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[164]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TSOBTAG_BUTTON_XPATH)
                    button.click()
                elif "unfettered" in statement:
                    BUA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[165]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BUA_BUTTON_XPATH)
                    button.click()
                elif "agnes strickland" in statement:
                    ABSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[167]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABSA_BUTTON_XPATH)
                    button.click()
                elif "andrew lang" in statement:
                    AABL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[168]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABL_BUTTON_XPATH)
                    button.click()
                elif "ann fraser tytler" in statement:
                    AABFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[169]'
                    browser = driver
                    button = browser.find_element(By.XPATH, AABFT_BUTTON_XPATH)
                    button.click()
                elif "anna sewell" in statement:
                    ABASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[170]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABASE_BUTTON_XPATH)
                    button.click()
                elif "anne bronte" in statement:
                    ABAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[171]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABAB_BUTTON_XPATH)
                    button.click()
                elif "anthony trollope" in statement:
                    ABTAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[172]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABTAR_BUTTON_XPATH)
                    button.click()
                elif "arthur conan doyle" in statement:
                    BAACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[173]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAACD_BUTTON_XPATH)
                    button.click()
                elif "baron edward bulwer lytton lytton" in statement:
                    BAEBBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[174]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAEBBLL_BUTTON_XPATH)
                    button.click()
                elif "beatrix potter" in statement:
                    BAPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[175]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BAPB_BUTTON_XPATH)
                    button.click()
                elif "bram stoker" in statement:
                    BBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[176]'
                    browser = driver
                    button = browser.find_element(By.XPATH, BBAS_BUTTON_XPATH)
                    button.click()
                elif "captain frederick marryat" in statement:
                    CFBAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[177]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CFBAM_BUTTON_XPATH)
                    button.click()
                elif "catherine sinclair" in statement:
                    CASB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[178]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CASB_BUTTON_XPATH)
                    button.click()
                elif "charles dickens" in statement:
                    CADB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[179]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CADB_BUTTON_XPATH)
                    button.click()
                elif "charles kinglsey" in statement:
                    CAKB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[180]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAKB_BUTTON_XPATH)
                    button.click()
                elif "charles W. chestnutt" in statement:
                    CAWBC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[181]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CAWBC_BUTTON_XPATH)
                    button.click()
                elif "charlotte bronte" in statement:
                    CBAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[182]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CBAB_BUTTON_XPATH)
                    button.click()
                elif "charlotte M. yonge" in statement:
                    CMABY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[183]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CMABY_BUTTON_XPATH)
                    button.click()
                elif "charlotte perkins gilman" in statement:
                    CBPAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[184]'
                    browser = driver
                    button = browser.find_element(By.XPATH, CBPAG_BUTTON_XPATH)
                    button.click()
                elif "D. H. lawrence" in statement:
                    DHABL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[185]'
                    browser = driver
                    button = browser.find_element(By.XPATH, DHABL_BUTTON_XPATH)
                    button.click()
                elif "E. M. forster" in statement:
                    EMBAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[186]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EMBAF_BUTTON_XPATH)
                    button.click()
                elif "E. Nesbit" in statement:
                    EBAN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[187]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EBAN_BUTTON_XPATH)
                    button.click()
                elif "earl of beaconsfield benjamin disraeli" in statement:
                    EAOBBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[188]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EAOBBBD_BUTTON_XPATH)
                    button.click()
                elif "elizabeth cleghorn gaskell" in statement:
                    EBACG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[189]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EBACG_BUTTON_XPATH)
                    button.click()
                elif "emily bronte" in statement:
                    EABB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[190]'
                    browser = driver
                    button = browser.find_element(By.XPATH, EABB_BUTTON_XPATH)
                    button.click()
                elif "F. anstey" in statement:
                    FABA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[191]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FABA_BUTTON_XPATH)
                    button.click()
                elif "frances E. W. harper" in statement:
                    FAEBWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[192]'
                    browser = driver
                    button = browser.find_element(By.XPATH, FAEBWH_BUTTON_XPATH)
                    button.click()
                elif "francis hodgson burnett" in statement:
                    FHABB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[193]'
                    browser = driver
                    browser.find_element(By.XPATH, FHABB_BUTTON_XPATH)
                    button.click()
                elif "Frederic william farrar" in statement:
                    FABWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[194]'
                    browser = driver
                    browser.find_element(By.XPATH, FABWF_BUTTON_XPATH)
                    button.click()
                elif "G.A. Henty" in statement:
                    GAABH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[195]'
                    browser = driver
                    button = browser.find_element(By.XPATH,GAABH_BUTTON_XPATH)
                    button.click()
                elif "G.E.Farrow" in statement:
                    GEBAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[196]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GEBAF_BUTTON_XPATH)
                    button.click()
                elif "George Eliot" in statement:
                    GBAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[197]'
                    browser = driver
                    button = browser.find_element(By.XPATH, GBAE_BUTTON_XPATH)
                    button.click()
                elif "Geroge Macdonald" in statement:
                    ABGM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[198]'
                    browser = driver
                    button = browser.find_element(By.XPATH, ABGM_BUTTON_XPATH)
                    button.click()
                elif "H. G Wells" in statement:
                    HBGAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[199]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HBGAW_BUTTON_XPATH)
                    button.click()
                elif "H. Rider Haggard" in statement:
                    HRBAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[200]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HRBAH_BUTTON_XPATH)
                    button.click()
                elif "Harriet Martineau" in statement:
                    HABM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[201]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HABM_BUTTON_XPATH)
                    button.click()
                elif "Henry James" in statement:
                    HABJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[202]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HABJ_BUTTON_XPATH)
                    button.click()
                elif "Hesba Stretton" in statement:
                    HBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[203]'
                    browser = driver
                    button = browser.find_element(By.XPATH, HBAS_BUTTON_XPATH)
                    button.click()
                elif "J. Meade Falkner" in statement:
                    JMBAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[204]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JMBAF_BUTTON_XPATH)
                    button.click()
                elif "James M. Barrie" in statement:
                    JMBB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[205]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JMBB_BUTTON_XPATH)
                    button.click()
                elif "James Weldon Johnson" in statement:
                    JWBAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[206]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JWBAJ_BUTTON_XPATH)
                    button.click()
                elif "Jane Austen" in statement:
                    JBAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[207]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JBAA_BUTTON_XPATH)
                    button.click()
                elif "Jean Ingelow" in statement:
                    JABI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[208]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JABI_BUTTON_XPATH)
                    button.click()
                elif "Jonathan Ruskin" in statement:
                    JBRA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[209]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JBRA_BUTTON_XPATH)
                    button.click()
                elif "Jonathan Swift" in statement:
                    JSAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[210]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JSAB_BUTTON_XPATH)
                    button.click()
                elif "Joseph Conrad" in statement:
                    JCBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[211]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JCBA_BUTTON_XPATH)
                    button.click()
                elif "Juliana Horatia Ewing" in statement:
                    JHABE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[212]'
                    browser = driver
                    button = browser.find_element(By.XPATH, JHABE_BUTTON_XPATH)
                    button.click()
                elif "Kate Chopin" in statement:
                    KCBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[213]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KCBA_BUTTON_XPATH)
                    button.click()
                elif "Kenneth Grahame" in statement:
                    KGBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[214]'
                    browser = driver
                    button = browser.find_element(By.XPATH, KGBA_BUTTON_XPATH)
                    button.click()
                elif "L.T. Meade" in statement:
                    LTBMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[215]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LTBMA_BUTTON_XPATH)
                    button.click()
                elif "lewis carroll" in statement:
                    LCAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[216]'
                    browser = driver
                    button = browser.find_element(By.XPATH, LCAB_BUTTON_XPATH)
                    button.click()
                elif "M. E Braddon" in statement:
                    MEBBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[217]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MEBBA_BUTTON_XPATH)
                    button.click()
                elif "mark twain" in statement:
                    MTBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[218]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MTBA_BUTTON_XPATH)
                    button.click()
                elif "mary wollstonecraft shelley" in statement:
                    MWBSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[219]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MWBSA_BUTTON_XPATH)
                    button.click()
                elif "Mrs. Molesworth" in statement:
                    MMBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[220]'
                    browser = driver
                    button = browser.find_element(By.XPATH, MMBA_BUTTON_XPATH)
                    button.click()
                elif "oscar wilde" in statement:
                    OBWA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[221]'
                    browser = driver
                    button = browser.find_element(By.XPATH, OBWA_BUTTON_XPATH)
                    button.click()
                elif "paul laurence dunbar" in statement:
                    PLBDA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[222]'
                    browser = driver
                    button = browser.find_element(By.XPATH, PLBDA_BUTTON_XPATH)
                    button.click()
                elif "R. M Ballantyne" in statement:
                    RABMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[223]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RABMB_BUTTON_XPATH)
                    button.click()
                elif "Rebecca West" in statement:
                    RBAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[224]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RBAW_BUTTON_XPATH)
                    button.click()
                elif "Richard Jefferies" in statement:
                    RJBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[225]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RJBA_BUTTON_XPATH)
                    button.click()
                elif "Robert Louis Stevenson" in statement:
                    RLBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[226]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RLBAS_BUTTON_XPATH)
                    button.click()
                elif "rudyard kipling" in statement:
                    RBKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[227]'
                    browser = driver
                    button = browser.find_element(By.XPATH, RBKA_BUTTON_XPATH)
                    button.click()
                elif "S. R Crockett" in statement:
                    SRBCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[228]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SRBCA_BUTTON_XPATH)
                    button.click()
                elif "solomon northrup" in statement:
                    SNBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[229]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SNBA_BUTTON_XPATH)
                    button.click()
                elif "sutton E Griggs" in statement:
                    SEGBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[230]'
                    browser = driver
                    button = browser.find_element(By.XPATH, SEGBA_BUTTON_XPATH)
                    button.click()
                elif "talbot baines reed" in statement:
                    TBARB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[231]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TBARB_BUTTON_XPATH)
                    button.click()
                elif "thomas hardy" in statement:
                    TABHA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[232]'
                    browser = driver
                    button = browser.find_element(By.XPATH, TABHA_BUTTON_XPATH)
                    button.click()
                elif "thomas hughes" in statement:
                    THAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[233]'
                    browser = driver
                    button = browser.find_element(By.XPATH, THAB_BUTTON_XPATH)
                    button.click()
                elif "upton sinclair" in statement:
                    UBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[234]'
                    browser = driver
                    button = browser.find_element(By.XPATH, UBAS_BUTTON_XPATH)
                    button.click()
                elif "walter de la mare" in statement:
                    WBDLAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[235]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WBDLAM_BUTTON_XPATH)
                    button.click()
                elif "wilkie collins" in statement:
                    WCBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[236]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WCBA_BUTTON_XPATH)
                    button.click()
                elif "william makepeace thackeray" in statement:
                    WMTBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[3]/form/div[1]/div/ul/li[237]'
                    browser = driver
                    button = browser.find_element(By.XPATH, WMTBA_BUTTON_XPATH)
                    button.click()
                else:
                    speak("The text was not found")
                    print("Text not found")
                    time.sleep(1)
                    speak("How else may I be of service?")
                    statement = takeCommand().lower()

                boo = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/div/input')
                for option in boo.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/a/span'):
                    option.click()
                speak("The subsets available are displayed. What type of text are you looking for?")
                print("The subsets available are displayed. What type of text are you looking for?")
                statement = takeCommand().lower()
                if 'all text' in statement:
                    boo1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[1]')
                    for option in boo1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[1]'):
                        option.click()
                if 'short suspensions' in statement or 'short' in statement:
                    boo2 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[2]')
                    for option in boo2.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[2]'):
                        option.click()
                if 'long suspensions' in statement or 'long' in statement:
                    boo3 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[3]')
                    for option in boo3.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[3]'):
                        option.click()
                if 'quotes' in statement:
                    boo4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[4]')
                    for option in boo4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[4]'):
                        option.click()
                if 'non quotes' in statement or 'non' in statement:
                    boo5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[5]')
                    for option in boo5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[2]/div/ul/li[5]'):
                        option.click()
                speak("which ngram would you like to choose?")
                g0 = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/div/input')
                for option in g0.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/a/span'):
                    option.click()
                speak("please select the n-gram you want")
                g0 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/div/input')
                for option in g0.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/div/input'):
                    option.click()
                statement = takeCommand().lower()
                if '1 gram' in statement or 'one' in statement:
                    g1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[1]')
                    for option in g1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[1]'):
                        option.click()
                if '2 gram' in statement or 'two' in statement:
                    g2 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[2]')
                    for option in g2.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[2]'):
                        option.click()
                if '3 gram' in statement or 'three' in statement:
                    g3 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[3]')
                    for option in g3.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[3]'):
                        option.click()
                if '4 gram' in statement or 'four' in statement:
                    g4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[4]')
                    for option in g4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[4]'):
                        option.click()
                if '5 gram' in statement or 'five' in statement:
                    g5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[5]')
                    for option in g5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[5]'):
                        option.click()
                if '6 gram' in statement or 'six' in statement:
                    g6 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[6]')
                    for option in g6.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[6]'):
                        option.click()
                if '7 gram' in statement or 'seven' in statement:
                    g7 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[7]')
                    for option in g7.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[3]/form/div[3]/div/ul/li[7]'):
                        option.click()
                press('enter')
                speak("Here are your results")
                speak("would you like to filter any rows?")
                statement = takeCommand().lower()
                if 'yes' in statement:
                    speak('please type in your filter terms')
                    FB_R = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[3]/form/input[1]')
                    for option in FB_R.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[3]/form/input[1]'):
                        option.click()
                    time.sleep(5)
                press('enter')
                speak('These are the results for the cluster search')

        if 'keyword' in statement:
            KEYWORDS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/legend/a'
            browser = driver
            button = browser.find_element(By.XPATH, KEYWORDS_BUTTON_XPATH)
            button.click()
            speak('The keywords option is now open. What corpora are you searching for?')
            SEARCH4_CORPORA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/ul/li/input'
            browser = driver
            button = browser.find_element(By.XPATH, SEARCH4_CORPORA_BUTTON_XPATH)
            button.click()
            speak("The Target corpus options are Dickens Novels, 19th Century Reference Corpus, Children's Literature,"
                  "Additional Requested Texts and African American Writers ")
            statement = takeCommand().lower()
            if  'novels' in statement:
                DYNOY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[2]'
                browser = driver
                button = browser.find_element(By.XPATH, DYNOY_BUTTON_XPATH)
                button.click()
                # or 'Additional Requested Texts' in statement or 'African American Writers' in statement:
            elif '19th Century Reference corpus' in statement:
                NINETEENY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[3]'
                browser = driver
                button = browser.find_element(By.XPATH, NINETEENY_BUTTON_XPATH)
                button.click()
            elif "Children's Literature" in statement:
                CYHILLIT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[4]'
                browser = driver
                button = browser.find_element(By.XPATH, CYHILLIT_BUTTON_XPATH)
                button.click()
            elif "Additional Requested Texts" in statement:
                ARYTSY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[5]'
                browser = driver
                button = browser.find_element(By.XPATH, ARYTSY_BUTTON_XPATH)
                button.click()
            elif "African American Writers" in statement:
                AFYAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[6]'
                browser = driver
                button = browser.find_element(By.XPATH, AFYAW_BUTTON_XPATH)
                button.click()
            elif "Bleak House" in statement or "Bleak House" in statement:
                YLOB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[8]'
                browser = driver
                button = browser.find_element(By.XPATH, YLOB_BUTTON_XPATH)
                button.click()
            elif "Barnaby Rudges" in statement:
                YBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[9]'
                browser = driver
                button = browser.find_element(By.XPATH, YBAR_BUTTON_XPATH)
                button.click()
            elif "david copperfield" in statement:
                DACY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[10]'
                browser = driver
                button = browser.find_element(By.XPATH, DACY_BUTTON_XPATH)
                button.click()
            elif "Dombey and son" in statement:
                DOAYS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[11]'
                browser = driver
                button = browser.find_element(By.XPATH, DOAYS_BUTTON_XPATH)
                button.click()
            elif "The mystery of edwin drood" in statement:
                THMOYED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[12]'
                browser = driver
                button = browser.find_element(By.XPATH, THMOYED_BUTTON_XPATH)
                button.click()
            elif "great expectationS" in statement:
                DREY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[13]'
                browser = driver
                button = browser.find_element(By.XPATH, DREY_BUTTON_XPATH)
                button.click()
            elif "hard times" in statement:
                YHAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[14]'
                browser = driver
                button = browser.find_element(By.XPATH, YHAT_BUTTON_XPATH)
                button.click()
            elif "little dorrit" in statement:
                YLID_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[15]'
                browser = driver
                button = browser.find_element(By.XPATH, YLID_BUTTON_XPATH)
                button.click()
            elif "martin chuzzlewit" in statement:
                MACY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[16]'
                browser = driver
                button = browser.find_element(By.XPATH, MACY_BUTTON_XPATH)
                button.click()
            elif "nicholas nickleby" in statement:
                NINY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[17]'
                browser = driver
                button = browser.find_element(By.XPATH, NINY_BUTTON_XPATH)
                button.click()
            elif "the old curiosity shop" in statement:
                TOCYS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[18]'
                browser = driver
                button = browser.find_element(By.XPATH, TOCYS_BUTTON_XPATH)
                button.click()
            elif "our mutual friend" in statement:
                YOUMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[19]'
                browser = driver
                button = browser.find_element(By.XPATH, YOUMF_BUTTON_XPATH)
                button.click()
            elif "oliver twist" in statement:
                YOLT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[20]'
                browser = driver
                button = browser.find_element(By.XPATH, YOLT_BUTTON_XPATH)
                button.click()
            elif "pickwick papers" in statement:
                PIPY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[21]'
                browser = driver
                button = browser.find_element(By.XPATH, PIPY_BUTTON_XPATH)
                button.click()
            elif "a tale of two cities" in statement:
                ATAOTCY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[22]'
                browser = driver
                button = browser.find_element(By.XPATH, ATAOTCY_BUTTON_XPATH)
                button.click()
            elif "agnes grey" in statement:
                AGGY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[24]'
                browser = driver
                button = browser.find_element(By.XPATH, AGGY_BUTTON_XPATH)
                button.click()
            elif "the small house at Allington" in statement:
                THSHAAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[25]'
                browser = driver
                button = browser.find_element(By.XPATH, THSHAAY_BUTTON_XPATH)
                button.click()
            elif "antonina or the fall of rome" in statement:
                ANOYTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[26]'
                browser = driver
                button = browser.find_element(By.XPATH, ANOYTFOR_BUTTON_XPATH)
                button.click()
            elif "armadale" in statement:
                ARY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[27]'
                browser = driver
                button = browser.find_element(By.XPATH, ARY_BUTTON_XPATH)
                button.click()
            elif "the hound of the baskervilles" in statement:
                YTHHOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[28]'
                browser = driver
                button = browser.find_element(By.XPATH, YTHHOTB_BUTTON_XPATH)
                button.click()
            elif "cranford" in statement:
                CRY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[29]'
                browser = driver
                button = browser.find_element(By.XPATH, CRY_BUTTON_XPATH)
                button.click()
            elif "daniel deronda" in statement:
                DYAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[30]'
                browser = driver
                button = browser.find_element(By.XPATH, DYAD_BUTTON_XPATH)
                button.click()
            elif "the picture of dorian grey" in statement:
                THPYODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[31]'
                browser = driver
                button = browser.find_element(By.XPATH, THPYODG_BUTTON_XPATH)
                button.click()
            elif "dracula" in statement:
                DRY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[32]'
                browser = driver
                button = browser.find_element(By.XPATH, DRY_BUTTON_XPATH)
                button.click()
            elif "emma" in statement:
                YEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[33]'
                browser = driver
                button = browser.find_element(By.XPATH, YEM_BUTTON_XPATH)
                button.click()
            elif "frankenstein" in statement:
                FRY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[34]'
                browser = driver
                button = browser.find_element(By.XPATH, FRY_BUTTON_XPATH)
                button.click()
            elif "jane eyre" in statement:
                JAEY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[35]'
                browser = driver
                button = browser.find_element(By.XPATH, JAEY_BUTTON_XPATH)
                button.click()
            elif "the strange case of doctor Jekyll and mister hyde" in statement:
                TASCYODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[36]'
                browser = driver
                button = browser.find_element(By.XPATH, TASCYODJAMH_BUTTON_XPATH)
                button.click()
            elif "jude the obscure" in statement:
                JATOY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[37]'
                browser = driver
                button = browser.find_element(By.XPATH, JATOY_BUTTON_XPATH)
                button.click()
            elif "lady audleys secret" in statement:
                LAAYS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[38]'
                browser = driver
                button = browser.find_element(By.XPATH, LAAYS_BUTTON_XPATH)
                button.click()
            elif "mary barton" in statement:
                MYBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[39]'
                browser = driver
                button = browser.find_element(By.XPATH, MYBA_BUTTON_XPATH)
                button.click()
            elif "the mill on the floss" in statement:
                TAMOYTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[40]'
                browser = driver
                button = browser.find_element(By.XPATH, TAMOYTF_BUTTON_XPATH)
                button.click()
            elif "the return of the native" in statement:
                TAROTYN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[41]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROTYN_BUTTON_XPATH)
                button.click()
            elif "north and south" in statement:
                NAASY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[42]'
                browser = driver
                button = browser.find_element(By.XPATH, NAASY_BUTTON_XPATH)
                button.click()
            elif "persuasion" in statement:
                PAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[43]'
                browser = driver
                button = browser.find_element(By.XPATH, PAY_BUTTON_XPATH)
                button.click()
            elif "the last days of pompeii" in statement:
                TALDYOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[44]'
                browser = driver
                button = browser.find_element(By.XPATH, TALDYOP_BUTTON_XPATH)
                button.click()
            elif "pride and prejudice" in statement:
                PYAAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[45]'
                browser = driver
                button = browser.find_element(By.XPATH, PYAAP_BUTTON_XPATH)
                button.click()
            elif "the professor" in statement:
                TAYP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[46]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYP_BUTTON_XPATH)
                button.click()
            elif "sybil or the two nations" in statement:
                SAOTYTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[47]'
                browser = driver
                button = browser.find_element(By.XPATH, SAOTYTN_BUTTON_XPATH)
                button.click()
            elif "tess of the d'urbevilles" in statement:
                TAODYU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[48]'
                browser = driver
                button = browser.find_element(By.XPATH, TAODYU_BUTTON_XPATH)
                button.click()
            elif "vanity fair" in statement:
                YAPY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[49]'
                browser = driver
                button = browser.find_element(By.XPATH, YAPY_BUTTON_XPATH)
                button.click()
            elif "vivian grey" in statement:
                YAYG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[50]'
                browser = driver
                button = browser.find_element(By.XPATH, YAYG_BUTTON_XPATH)
                button.click()
            elif "wuthering heights" in statement:
                WYAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[51]'
                browser = driver
                button = browser.find_element(By.XPATH, WYAH_BUTTON_XPATH)
                button.click()
            elif "the woman in white" in statement:
                TAWYIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[52]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWYIW_BUTTON_XPATH)
                button.click()
            elif "alice's adventures in wonderland" in statement:
                AAAIYW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[54]'
                browser = driver
                button = browser.find_element(By.XPATH, AAAIYW_BUTTON_XPATH)
                button.click()
            elif "alone in london" in statement:
                AAYIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[55]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYIL_BUTTON_XPATH)
                button.click()
            elif "the story of the amulet " in statement:
                TSYAOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[56]'
                browser = driver
                button = browser.find_element(By.XPATH, TSYAOTA_BUTTON_XPATH)
                button.click()
            elif "black beauty" in statement:
                YBAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[57]'
                browser = driver
                button = browser.find_element(By.XPATH, YBAB_BUTTON_XPATH)
                button.click()
            elif "the brass bottle" in statement:
                TABY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[58]'
                browser = driver
                button = browser.find_element(By.XPATH, TABY_BUTTON_XPATH)
                button.click()
            elif "the tale of benjamin bunny" in statement:
                TATOBBY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[59]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOBBY_BUTTON_XPATH)
                button.click()
            elif "the settlers in canada" in statement:
                TASYIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[60]'
                browser = driver
                button = browser.find_element(By.XPATH, TASYIC_BUTTON_XPATH)
                button.click()
            elif "the  carved lions" in statement:
                TYACL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[61]'
                browser = driver
                button = browser.find_element(By.XPATH, TYACL_BUTTON_XPATH)
                button.click()
            elif "with clive in india" in statement:
                WAYCII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[62]'
                browser = driver
                button = browser.find_element(By.XPATH, WAYCII_BUTTON_XPATH)
                button.click()
            elif "the coral island" in statement:
                TACYI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[63]'
                browser = driver
                button = browser.find_element(By.XPATH, TACYI_BUTTON_XPATH)
                button.click()
            elif "the crofton boys" in statement:
                TACYB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[64]'
                browser = driver
                button = browser.find_element(By.XPATH, TACYB_BUTTON_XPATH)
                button.click()
            elif "the cuckoo clock" in statement:
                TACYC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[65]'
                browser = driver
                button = browser.find_element(By.XPATH, TACYC_BUTTON_XPATH)
                button.click()
            elif "the daisy chain" in statement:
                TADCY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[66]'
                browser = driver
                button = browser.find_element(By.XPATH, TADCY_BUTTON_XPATH)
                button.click()
            elif "the fifth form at saint dominics" in statement:
                TAFFYASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[67]'
                browser = driver
                button = browser.find_element(By.XPATH, TAFFYASD_BUTTON_XPATH)
                button.click()
            elif "the dove in the eagles nest" in statement:
                TADITYEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[68]'
                browser = driver
                button = browser.find_element(By.XPATH, TADITYEN_BUTTON_XPATH)
                button.click()
            elif "the book of dragons" in statement:
                TAYOBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[69]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYOBD_BUTTON_XPATH)
                button.click()
            elif "dream days" in statement:
                DARYD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[70]'
                browser = driver
                button = browser.find_element(By.XPATH, DARYD_BUTTON_XPATH)
                button.click()
            elif "the little duke" in statement:
                TALYD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[71]'
                browser = driver
                button = browser.find_element(By.XPATH, TALYD_BUTTON_XPATH)
                button.click()
            elif "eric" in statement:
                YEAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[72]'
                browser = driver
                button = browser.find_element(By.XPATH, YEAR_BUTTON_XPATH)
                button.click()
            elif "feats on the fiord" in statement:
                FOAYTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[73]'
                browser = driver
                button = browser.find_element(By.XPATH, FOAYTF_BUTTON_XPATH)
                button.click()
            elif "five children and it" in statement:
                FACYAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[74]'
                browser = driver
                button = browser.find_element(By.XPATH, FACYAI_BUTTON_XPATH)
                button.click()
            elif "the tale of the flopsy bunnies" in statement:
                TYATOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[75]'
                browser = driver
                button = browser.find_element(By.XPATH, TYATOTFB_BUTTON_XPATH)
                button.click()
            elif "the children of the new forest" in statement:
                TAYCOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[76]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYCOTNF_BUTTON_XPATH)
                button.click()
            elif "a world of girls" in statement:
                AAYWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[77]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYWOG_BUTTON_XPATH)
                button.click()
            elif "through the looking glass" in statement:
                TAYTLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[78]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYTLG_BUTTON_XPATH)
                button.click()
            elif "the golden age" in statement:
                TAGYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[79]'
                browser = driver
                button = browser.find_element(By.XPATH, TAGYA_BUTTON_XPATH)
                button.click()
            elif "holiday house" in statement:
                HYAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[80]'
                browser = driver
                button = browser.find_element(By.XPATH, HYAH_BUTTON_XPATH)
                button.click()
            elif "madam how and lady why" in statement:
                MBAYHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[81]'
                browser = driver
                button = browser.find_element(By.XPATH, MBAYHALW_BUTTON_XPATH)
                button.click()
            elif "jackanapes" in statement:
                JYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[82]'
                browser = driver
                button = browser.find_element(By.XPATH, JYA_BUTTON_XPATH)
                button.click()
            elif "the tale of jemima puddle duck" in statement:
                TATOYJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[83]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOYJP_BUTTON_XPATH)
                button.click()
            elif "jessicas first prayer" in statement:
                JYAFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[84]'
                browser = driver
                button = browser.find_element(By.XPATH, JYAFP_BUTTON_XPATH)
                button.click()
            elif "the jungle book" in statement:
                TAJYB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[85]'
                browser = driver
                button = browser.find_element(By.XPATH, TAJYB_BUTTON_XPATH)
                button.click()
            elif "kidnapped" in statement:
                YKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[86]'
                browser = driver
                button = browser.find_element(By.XPATH, YKA_BUTTON_XPATH)
                button.click()
            elif "leila at home" in statement:
                LAYAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[87]'
                browser = driver
                button = browser.find_element(By.XPATH, LAYAH_BUTTON_XPATH)
                button.click()
            elif "masterman ready" in statement:
                MYAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[88]'
                browser = driver
                button = browser.find_element(By.XPATH, MYAR_BUTTON_XPATH)
                button.click()
            elif "little meg's children" in statement:
                LAYMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[89]'
                browser = driver
                button = browser.find_element(By.XPATH, LAYMC_BUTTON_XPATH)
                button.click()
            elif "the tale of two bad mice" in statement:
                TATOTYBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[90]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOTYBM_BUTTON_XPATH)
                button.click()
            elif "moonfleet" in statement:
                MAYF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[91]'
                browser = driver
                button = browser.find_element(By.XPATH, MAYF_BUTTON_XPATH)
                button.click()
            elif "mopsa the fairy" in statement:
                MAYTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[92]'
                browser = driver
                button = browser.find_element(By.XPATH, MAYTF_BUTTON_XPATH)
                button.click()
            elif "the three mulla-mulgars" in statement:
                TATYMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[93]'
                browser = driver
                button = browser.find_element(By.XPATH, TATYMM_BUTTON_XPATH)
                button.click()
            elif "mrs. overtheways remembrances" in statement:
                MAORY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[94]'
                browser = driver
                button = browser.find_element(By.XPATH, MAORY_BUTTON_XPATH)
                button.click()
            elif "peter pan" in statement:
                PAEPYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[95]'
                browser = driver
                button = browser.find_element(By.XPATH, PAEPYA_BUTTON_XPATH)
                button.click()
            elif "the peasant and the prince" in statement:
                TAYPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[96]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYPATP_BUTTON_XPATH)
                button.click()
            elif "prince prigio" in statement:
                PAYRPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[97]'
                browser = driver
                button = browser.find_element(By.XPATH, PAYRPR_BUTTON_XPATH)
                button.click()
            elif "the happy prince" in statement:
                TAYHP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[98]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYHP_BUTTON_XPATH)
                button.click()
            elif "the princess and the goblin" in statement:
                TPYATG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[99]'
                browser = driver
                button = browser.find_element(By.XPATH, TPYATG_BUTTON_XPATH)
                button.click()
            elif "allan quatermain" in statement:
                AAYQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[100]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYQ_BUTTON_XPATH)
                button.click()
            elif "the tale of peter rabbit" in statement:
                TYATOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[101]'
                browser = driver
                button = browser.find_element(By.XPATH, TYATOPR_BUTTON_XPATH)
                button.click()
            elif "the railway children" in statement:
                TARYC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[102]'
                browser = driver
                button = browser.find_element(By.XPATH, TARYC_BUTTON_XPATH)
                button.click()
            elif "the heir of redclyffe" in statement:
                TAHOYR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[103]'
                browser = driver
                button = browser.find_element(By.XPATH, TAHOYR_BUTTON_XPATH)
                button.click()
            elif "the rival crusoes" in statement:
                TARYCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[104]'
                browser = driver
                button = browser.find_element(By.XPATH, TARYCR_BUTTON_XPATH)
                button.click()
            elif "the rose and the ring" in statement:
                TYARATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[105]'
                browser = driver
                button = browser.find_element(By.XPATH, TYARATR_BUTTON_XPATH)
                button.click()
            elif "the secret garden" in statement:
                TASYG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[106]'
                browser = driver
                button = browser.find_element(By.XPATH, TASYG_BUTTON_XPATH)
                button.click()
            elif "the story of the treasure seekers" in statement:
                TYASOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[107]'
                browser = driver
                button = browser.find_element(By.XPATH, TYASOTTS_BUTTON_XPATH)
                button.click()
            elif "the settlers at home" in statement:
                TASAYH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[108]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAYH_BUTTON_XPATH)
                button.click()
            elif "king solomons mines" in statement:
                KAYSM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[109]'
                browser = driver
                button = browser.find_element(By.XPATH, KAYSM_BUTTON_XPATH)
                button.click()
            elif "the tale of squirrel nutkin" in statement:
                TATOYSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[110]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOYSN_BUTTON_XPATH)
                button.click()
            elif "stalky and co" in statement:
                SYAAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[111]'
                browser = driver
                button = browser.find_element(By.XPATH, SYAAC_BUTTON_XPATH)
                button.click()
            elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                    or "the black brothers" in statement:
                TAKOTYGROTYB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[112]'
                browser = driver
                button = browser.find_element(By.XPATH, TAKOTYGROTYB_BUTTON_XPATH)
                button.click()
            elif "the tapestry room" in statement:
                TAYTR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[113]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYTR_BUTTON_XPATH)
                button.click()
            elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                TASAOSTYLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[114]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAOSTYLWTOGNS_BUTTON_XPATH)
                button.click()
            elif "tom brown's schooldays" in statement:
                TYABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[115]'
                browser = driver
                button = browser.find_element(By.XPATH, TYABS_BUTTON_XPATH)
                button.click()
            elif "treasure island" in statement:
                TAIY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[116]'
                browser = driver
                button = browser.find_element(By.XPATH, TAIY_BUTTON_XPATH)
                button.click()
            elif "nine unlikely tales" in statement:
                YNAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[117]'
                browser = driver
                button = browser.find_element(By.XPATH, YNAUT_BUTTON_XPATH)
                button.click()
            elif "vise versa" in statement:
                YAYY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[118]'
                browser = driver
                button = browser.find_element(By.XPATH, YAYY_BUTTON_XPATH)
                button.click()
            elif "adventures in wallypug land" in statement:
                AAYIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[119]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYIW_BUTTON_XPATH)
                button.click()
            elif "the water babies" in statement:
                TAYWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[120]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYWB_BUTTON_XPATH)
                button.click()
            elif "the wind in the willows" in statement:
                TAWYITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[121]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWYITW_BUTTON_XPATH)
                button.click()
            elif "at the back of the north wind" in statement:
                ABATYOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[122]'
                browser = driver
                button = browser.find_element(By.XPATH, ABATYOTNW_BUTTON_XPATH)
                button.click()
            elif "winning his spurs" in statement:
                WAYHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[123]'
                browser = driver
                button = browser.find_element(By.XPATH, WAYHS_BUTTON_XPATH)
                button.click()
            elif "wood magic" in statement:
                WAYM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[124]'
                browser = driver
                button = browser.find_element(By.XPATH, WAYM_BUTTON_XPATH)
                button.click()
            elif "american notes for general circulation" in statement:
                AAYNFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[126]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYNFGC_BUTTON_XPATH)
                button.click()
            elif "the awakening and several short stories" in statement:
                TAAAYSSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[127]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAAYSSS_BUTTON_XPATH)
                button.click()
            elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                    or "a ghost story of christmas" in statement:
                AYACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[128]'
                browser = driver
                button = browser.find_element(By.XPATH, AYACCAGSOC_BUTTON_XPATH)
                button.click()
            elif "gullivers travels" in statement:
                AYGT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[129]'
                browser = driver
                button = browser.find_element(By.XPATH, AYGT_BUTTON_XPATH)
                button.click()
            elif "heart of darkness" in statement:
                HODYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[130]'
                browser = driver
                button = browser.find_element(By.XPATH, HODYA_BUTTON_XPATH)
                button.click()
            elif "adventures of huckleberry finn" in statement:
                AOHAYF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[131]'
                browser = driver
                button = browser.find_element(By.XPATH, AOHAYF_BUTTON_XPATH)
                button.click()
            elif "lady susan" in statement:
                LAYS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[132]'
                browser = driver
                button = browser.find_element(By.XPATH, LAYS_BUTTON_XPATH)
                button.click()
            elif "what maisie knew" in statement:
                WMAYK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[133]'
                browser = driver
                button = browser.find_element(By.XPATH, WMAYK_BUTTON_XPATH)
                button.click()
            elif "mansfield park" in statement:
                MYAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[134]'
                browser = driver
                button = browser.find_element(By.XPATH, MYAP_BUTTON_XPATH)
                button.click()
            elif "middlemarch" in statement:
                YMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[135]'
                browser = driver
                button = browser.find_element(By.XPATH, YMA_BUTTON_XPATH)
                button.click()
            elif "the moonstone" in statement:
                TYAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[136]'
                browser = driver
                button = browser.find_element(By.XPATH, TYAM_BUTTON_XPATH)
                button.click()
            elif "northanger abbey" in statement:
                YNAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[137]'
                browser = driver
                button = browser.find_element(By.XPATH, YNAA_BUTTON_XPATH)
                button.click()
            elif "pictures from italy" in statement:
                YPAFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[138]'
                browser = driver
                button = browser.find_element(By.XPATH, YPAFI_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 1" in statement:
                YPAOALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[139]'
                browser = driver
                button = browser.find_element(By.XPATH, YPAOALO_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 2" in statement:
                YPAOALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[140]'
                browser = driver
                button = browser.find_element(By.XPATH, YPAOALT_BUTTON_XPATH)
                button.click()
            elif "a room with a view" in statement:
                ARYAWAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[141]'
                browser = driver
                button = browser.find_element(By.XPATH, ARYAWAY_BUTTON_XPATH)
                button.click()
            elif "sense and sensibility" in statement:
                SAAYS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[142]'
                browser = driver
                button = browser.find_element(By.XPATH, SAAYS_BUTTON_XPATH)
                button.click()
            elif "shirley" in statement:
                YSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[143]'
                browser = driver
                button = browser.find_element(By.XPATH, YSA_BUTTON_XPATH)
                button.click()
            elif "the sign of four" in statement:
                TSAOYF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[144]'
                browser = driver
                button = browser.find_element(By.XPATH, TSAOYF_BUTTON_XPATH)
                button.click()
            elif "silas marner" in statement:
                SAYM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[145]'
                browser = driver
                button = browser.find_element(By.XPATH, SAYM_BUTTON_XPATH)
                button.click()
            elif "the return of the soldier" in statement:
                TAROYTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[147]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROYTS_BUTTON_XPATH)
                button.click()
            elif "the tenant of wildfell hall" in statement:
                TATOYWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[148]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOYWH_BUTTON_XPATH)
                button.click()
            elif "the jungle" in statement:
                YTAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[149]'
                browser = driver
                button = browser.find_element(By.XPATH, YTAJ_BUTTON_XPATH)
                button.click()
            elif "the time machine" in statement:
                TYATM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[150]'
                browser = driver
                button = browser.find_element(By.XPATH, TYATM_BUTTON_XPATH)
                button.click()
            elif "twelve years a slave" in statement:
                YTYAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[151]'
                browser = driver
                button = browser.find_element(By.XPATH, YTYAAS_BUTTON_XPATH)
                button.click()
            elif "the uncommercial traveller" in statement:
                YTAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[152]'
                browser = driver
                button = browser.find_element(By.XPATH, YTAUT_BUTTON_XPATH)
                button.click()
            elif "vilette" in statement:
                YYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[153]'
                browser = driver
                button = browser.find_element(By.XPATH, YYA_BUTTON_XPATH)
                button.click()
            elif "the war of worlds" in statement:
                TYAWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[154]'
                browser = driver
                button = browser.find_element(By.XPATH, TYAWOW_BUTTON_XPATH)
                button.click()
            elif "women in love" in statement:
                WIAYL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[155]'
                browser = driver
                button = browser.find_element(By.XPATH, WIAYL_BUTTON_XPATH)
                button.click()
            elif "the yellow wallpaper" in statement:
                TYAYW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[156]'
                browser = driver
                button = browser.find_element(By.XPATH, TYAYW_BUTTON_XPATH)
                button.click()
            elif "the house behind the cedars" in statement:
                THAYBTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[158]'
                browser = driver
                button = browser.find_element(By.XPATH, THAYBTC_BUTTON_XPATH)
                button.click()
            elif "the colonel's dream" in statement:
                TCYAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[159]'
                browser = driver
                button = browser.find_element(By.XPATH, TCYAD_BUTTON_XPATH)
                button.click()
            elif "the autobiography of an ex-coloured man" in statement:
                TAAYOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[160]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAYOAEM_BUTTON_XPATH)
                button.click()
            elif "imperium in imperio" in statement:
                IYIAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[161]'
                browser = driver
                button = browser.find_element(By.XPATH, IYIAI_BUTTON_XPATH)
                button.click()
            elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                    or "iola leroy" in statement:
                ILOSYAU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[162]'
                browser = driver
                button = browser.find_element(By.XPATH, ILOSYAU_BUTTON_XPATH)
                button.click()
            elif "the marrow of tradition" in statement:
                TMOYAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[163]'
                browser = driver
                button = browser.find_element(By.XPATH, TMOYAT_BUTTON_XPATH)
                button.click()
            elif "the sport of the gods" in statement:
                TSOYTAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[164]'
                browser = driver
                button = browser.find_element(By.XPATH, TSOYTAG_BUTTON_XPATH)
                button.click()
            elif "unfettered" in statement:
                YUA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[165]'
                browser = driver
                button = browser.find_element(By.XPATH, YUA_BUTTON_XPATH)
                button.click()
            elif "agnes strickland" in statement:
                AYSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[167]'
                browser = driver
                button = browser.find_element(By.XPATH, AYSA_BUTTON_XPATH)
                button.click()
            elif "andrew lang" in statement:
                AAYL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[168]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYL_BUTTON_XPATH)
                button.click()
            elif "ann fraser tytler" in statement:
                AAYFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[169]'
                browser = driver
                button = browser.find_element(By.XPATH, AAYFT_BUTTON_XPATH)
                button.click()
            elif "anna sewell" in statement:
                AYASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[170]'
                browser = driver
                button = browser.find_element(By.XPATH, AYASE_BUTTON_XPATH)
                button.click()
            elif "anne bronte" in statement:
                AYAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[171]'
                browser = driver
                button = browser.find_element(By.XPATH, AYAB_BUTTON_XPATH)
                button.click()
            elif "anthony trollope" in statement:
                AYTAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[172]'
                browser = driver
                button = browser.find_element(By.XPATH, AYTAR_BUTTON_XPATH)
                button.click()
            elif "arthur conan doyle" in statement:
                YAACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[173]'
                browser = driver
                button = browser.find_element(By.XPATH, YAACD_BUTTON_XPATH)
                button.click()
            elif "baron edward bulwer lytton lytton" in statement:
                YAEBBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[174]'
                browser = driver
                button = browser.find_element(By.XPATH, YAEBBLL_BUTTON_XPATH)
                button.click()
            elif "beatrix potter" in statement:
                YAPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[175]'
                browser = driver
                button = browser.find_element(By.XPATH, YAPB_BUTTON_XPATH)
                button.click()
            elif "bram stoker" in statement:
                YBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[176]'
                browser = driver
                button = browser.find_element(By.XPATH, YBAS_BUTTON_XPATH)
                button.click()
            elif "captain frederick marryat" in statement:
                CFYAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[177]'
                browser = driver
                button = browser.find_element(By.XPATH, CFYAM_BUTTON_XPATH)
                button.click()
            elif "catherine sinclair" in statement:
                CASY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[178]'
                browser = driver
                button = browser.find_element(By.XPATH, CASY_BUTTON_XPATH)
                button.click()
            elif "charles dickens" in statement:
                CADY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[179]'
                browser = driver
                button = browser.find_element(By.XPATH, CADY_BUTTON_XPATH)
                button.click()
            elif "charles kinglsey" in statement:
                CAKY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[180]'
                browser = driver
                button = browser.find_element(By.XPATH, CAKY_BUTTON_XPATH)
                button.click()
            elif "charles W. chestnutt" in statement:
                CAWYC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[181]'
                browser = driver
                button = browser.find_element(By.XPATH, CAWYC_BUTTON_XPATH)
                button.click()
            elif "charlotte bronte" in statement:
                CYAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[182]'
                browser = driver
                button = browser.find_element(By.XPATH, CYAB_BUTTON_XPATH)
                button.click()
            elif "charlotte M. yonge" in statement:
                CMAYY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[183]'
                browser = driver
                button = browser.find_element(By.XPATH, CMAYY_BUTTON_XPATH)
                button.click()
            elif "charlotte perkins gilman" in statement:
                CYPAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[184]'
                browser = driver
                button = browser.find_element(By.XPATH, CYPAG_BUTTON_XPATH)
                button.click()
            elif "D. H. lawrence" in statement:
                DHAYL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[185]'
                browser = driver
                button = browser.find_element(By.XPATH, DHAYL_BUTTON_XPATH)
                button.click()
            elif "E. M. forster" in statement:
                EMYAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[186]'
                browser = driver
                button = browser.find_element(By.XPATH, EMYAF_BUTTON_XPATH)
                button.click()
            elif "E. Nesbit" in statement:
                EYAN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[187]'
                browser = driver
                button = browser.find_element(By.XPATH, EYAN_BUTTON_XPATH)
                button.click()
            elif "earl of beaconsfield benjamin disraeli" in statement:
                EAOYBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[188]'
                browser = driver
                button = browser.find_element(By.XPATH, EAOYBBD_BUTTON_XPATH)
                button.click()
            elif "elizabeth cleghorn gaskell" in statement:
                EYACG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[189]'
                browser = driver
                button = browser.find_element(By.XPATH, EYACG_BUTTON_XPATH)
                button.click()
            elif "emily bronte" in statement:
                EAYB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[190]'
                browser = driver
                button = browser.find_element(By.XPATH, EAYB_BUTTON_XPATH)
                button.click()
            elif "F. anstey" in statement:
                FAYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[191]'
                browser = driver
                button = browser.find_element(By.XPATH, FAYA_BUTTON_XPATH)
                button.click()
            elif "frances E. W. harper" in statement:
                FAEYWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[192]'
                browser = driver
                button = browser.find_element(By.XPATH, FAEYWH_BUTTON_XPATH)
                button.click()
            elif "francis hodgson burnett" in statement:
                FHAYB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[193]'
                browser = driver
                browser.find_element(By.XPATH, FHAYB_BUTTON_XPATH)
                button.click()
            elif "Frederic william farrar" in statement:
                FAYWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[194]'
                browser = driver
                browser.find_element(By.XPATH, FAYWF_BUTTON_XPATH)
                button.click()
            elif "G.A. Henty" in statement:
                GAAYH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[195]'
                browser = driver
                button = browser.find_element(By.XPATH,GAAYH_BUTTON_XPATH)
                button.click()
            elif "G.E.Farrow" in statement:
                GEYAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[196]'
                browser = driver
                button = browser.find_element(By.XPATH, GEYAF_BUTTON_XPATH)
                button.click()
            elif "George Eliot" in statement:
                GYAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[197]'
                browser = driver
                button = browser.find_element(By.XPATH, GYAE_BUTTON_XPATH)
                button.click()
            elif "Geroge Macdonald" in statement:
                AYGM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[198]'
                browser = driver
                button = browser.find_element(By.XPATH, AYGM_BUTTON_XPATH)
                button.click()
            elif "H. G Wells" in statement:
                HYGAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[199]'
                browser = driver
                button = browser.find_element(By.XPATH, HYGAW_BUTTON_XPATH)
                button.click()
            elif "H. Rider Haggard" in statement:
                HRYAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[200]'
                browser = driver
                button = browser.find_element(By.XPATH, HRYAH_BUTTON_XPATH)
                button.click()
            elif "Harriet Martineau" in statement:
                HAYM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[201]'
                browser = driver
                button = browser.find_element(By.XPATH, HAYM_BUTTON_XPATH)
                button.click()
            elif "Henry James" in statement:
                HAYJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[202]'
                browser = driver
                button = browser.find_element(By.XPATH, HAYJ_BUTTON_XPATH)
                button.click()
            elif "Hesba Stretton" in statement:
                HYAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[203]'
                browser = driver
                button = browser.find_element(By.XPATH, HYAS_BUTTON_XPATH)
                button.click()
            elif "J. Meade Falkner" in statement:
                JMYAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[204]'
                browser = driver
                button = browser.find_element(By.XPATH, JMYAF_BUTTON_XPATH)
                button.click()
            elif "James M. Barrie" in statement:
                JMYB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[205]'
                browser = driver
                button = browser.find_element(By.XPATH, JMYB_BUTTON_XPATH)
                button.click()
            elif "James Weldon Johnson" in statement:
                JWYAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[206]'
                browser = driver
                button = browser.find_element(By.XPATH, JWYAJ_BUTTON_XPATH)
                button.click()
            elif "Jane Austen" in statement:
                JYAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[207]'
                browser = driver
                button = browser.find_element(By.XPATH, JYAA_BUTTON_XPATH)
                button.click()
            elif "Jean Ingelow" in statement:
                JAYI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[208]'
                browser = driver
                button = browser.find_element(By.XPATH, JAYI_BUTTON_XPATH)
                button.click()
            elif "Jonathan Ruskin" in statement:
                JYRA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[209]'
                browser = driver
                button = browser.find_element(By.XPATH, JYRA_BUTTON_XPATH)
                button.click()
            elif "Jonathan Swift" in statement:
                JSAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[210]'
                browser = driver
                button = browser.find_element(By.XPATH, JSAY_BUTTON_XPATH)
                button.click()
            elif "Joseph Conrad" in statement:
                JCYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[211]'
                browser = driver
                button = browser.find_element(By.XPATH, JCYA_BUTTON_XPATH)
                button.click()
            elif "Juliana Horatia Ewing" in statement:
                JHAYE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[212]'
                browser = driver
                button = browser.find_element(By.XPATH, JHAYE_BUTTON_XPATH)
                button.click()
            elif "Kate Chopin" in statement:
                KCYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[213]'
                browser = driver
                button = browser.find_element(By.XPATH, KCYA_BUTTON_XPATH)
                button.click()
            elif "Kenneth Grahame" in statement:
                KGYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[214]'
                browser = driver
                button = browser.find_element(By.XPATH, KGYA_BUTTON_XPATH)
                button.click()
            elif "L.T. Meade" in statement:
                LTYMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[215]'
                browser = driver
                button = browser.find_element(By.XPATH, LTYMA_BUTTON_XPATH)
                button.click()
            elif "lewis carroll" in statement:
                LCAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[216]'
                browser = driver
                button = browser.find_element(By.XPATH, LCAY_BUTTON_XPATH)
                button.click()
            elif "M. E Braddon" in statement:
                MEYBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[217]'
                browser = driver
                button = browser.find_element(By.XPATH, MEYBA_BUTTON_XPATH)
                button.click()
            elif "mark twain" in statement:
                MTYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[218]'
                browser = driver
                button = browser.find_element(By.XPATH, MTYA_BUTTON_XPATH)
                button.click()
            elif "mary wollstonecraft shelley" in statement:
                MWYSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[219]'
                browser = driver
                button = browser.find_element(By.XPATH, MWYSA_BUTTON_XPATH)
                button.click()
            elif "Mrs. Molesworth" in statement:
                MMYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[220]'
                browser = driver
                button = browser.find_element(By.XPATH, MMYA_BUTTON_XPATH)
                button.click()
            elif "oscar wilde" in statement:
                OYWA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[221]'
                browser = driver
                button = browser.find_element(By.XPATH, OYWA_BUTTON_XPATH)
                button.click()
            elif "paul laurence dunbar" in statement:
                PLYDA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[222]'
                browser = driver
                button = browser.find_element(By.XPATH, PLYDA_BUTTON_XPATH)
                button.click()
            elif "R. M Ballantyne" in statement:
                RAYMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[223]'
                browser = driver
                button = browser.find_element(By.XPATH, RAYMB_BUTTON_XPATH)
                button.click()
            elif "Rebecca West" in statement:
                RYAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[224]'
                browser = driver
                button = browser.find_element(By.XPATH, RYAW_BUTTON_XPATH)
                button.click()
            elif "Richard Jefferies" in statement:
                RJYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[225]'
                browser = driver
                button = browser.find_element(By.XPATH, RJYA_BUTTON_XPATH)
                button.click()
            elif "Robert Louis Stevenson" in statement:
                RLYAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[226]'
                browser = driver
                button = browser.find_element(By.XPATH, RLYAS_BUTTON_XPATH)
                button.click()
            elif "rudyard kipling" in statement:
                RYKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[227]'
                browser = driver
                button = browser.find_element(By.XPATH, RYKA_BUTTON_XPATH)
                button.click()
            elif "S. R Crockett" in statement:
                SRYCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[228]'
                browser = driver
                button = browser.find_element(By.XPATH, SRYCA_BUTTON_XPATH)
                button.click()
            elif "solomon northrup" in statement:
                SNYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[229]'
                browser = driver
                button = browser.find_element(By.XPATH, SNYA_BUTTON_XPATH)
                button.click()
            elif "sutton E Griggs" in statement:
                SEGYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[230]'
                browser = driver
                button = browser.find_element(By.XPATH, SEGYA_BUTTON_XPATH)
                button.click()
            elif "talbot baines reed" in statement:
                TYARB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[231]'
                browser = driver
                button = browser.find_element(By.XPATH, TYARB_BUTTON_XPATH)
                button.click()
            elif "thomas hardy" in statement:
                TAYHA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[232]'
                browser = driver
                button = browser.find_element(By.XPATH, TAYHA_BUTTON_XPATH)
                button.click()
            elif "thomas hughes" in statement:
                THAY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[233]'
                browser = driver
                button = browser.find_element(By.XPATH, THAY_BUTTON_XPATH)
                button.click()
            elif "upton sinclair" in statement:
                UYAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[234]'
                browser = driver
                button = browser.find_element(By.XPATH, UYAS_BUTTON_XPATH)
                button.click()
            elif "walter de la mare" in statement:
                WYDLAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[235]'
                browser = driver
                button = browser.find_element(By.XPATH, WYDLAM_BUTTON_XPATH)
                button.click()
            elif "wilkie collins" in statement:
                WCYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[236]'
                browser = driver
                button = browser.find_element(By.XPATH, WCYA_BUTTON_XPATH)
                button.click()
            elif "william makepeace thackeray" in statement:
                WMTYA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[1]/div/ul/li[237]'
                browser = driver
                button = browser.find_element(By.XPATH, WMTYA_BUTTON_XPATH)
                button.click()
            else:
                speak("The text was not found")
                print("Text not found")
                time.sleep(1)
                speak("How else may I be of service?")
                statement = takeCommand().lower()

            gre = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/div/input')
            for option in gre.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/a/span'):
                option.click()
            speak("The subsets available are displayed. What option are you looking for?")
            print("The subsets available are displayed. What option are you looking for?")
            statement = takeCommand().lower()
            if 'all text' in statement:
                gre1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[1]')
                for option in gre1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[1]'):
                    option.click()
            if 'short suspensions' in statement or 'short' in statement:
                gre2 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[2]')
                for option in gre2.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[2]'):
                    option.click()
            if 'long suspensions' in statement or 'long' in statement:
                gre3 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[3]')
                for option in gre3.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[3]'):
                    option.click()
            if 'quotes' in statement:
                gre4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[4]')
                for option in gre4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[4]'):
                    option.click()
            if 'non quotes' in statement or 'non' in statement:
                gre5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[5]')
                for option in gre5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[2]/div/ul/li[5]'):
                    option.click()

            speak("which ngram would you like to choose?")
            gr0 = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/div/input')
            for option in gr0.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/a/span'):
                option.click()
            statement = takeCommand().lower()
            if '1 gram' in statement or 'one' in statement:
                gr1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[1]')
                for option in gr1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[1]'):
                    option.click()
            if '2 gram' in statement or 'two' in statement:
                gr2 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[2]')
                for option in gr2.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[2]'):
                    option.click()
            if '3 gram' in statement or 'three' in statement:
                gr3 = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[3]')
                for option in gr3.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[3]'):
                    option.click()
            if '4 gram' in statement or 'four' in statement:
                gr4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[4]')
                for option in gr4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[4]'):
                    option.click()
            if '5 gram' in statement or 'five' in statement:
                gr5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[5]')
                for option in gr5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[5]'):
                    option.click()
            if '6 gram' in statement or 'six' in statement:
                gr6 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[6]')
                for option in gr6.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[6]'):
                    option.click()
            if '7 gram' in statement or 'seven' in statement:
                gr7 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[7]')
                for option in gr7.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[3]/div/ul/li[7]'):
                    option.click()
            SEARCH41_CORPORA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/ul/li/input'
            browser = driver
            button = browser.find_element(By.XPATH, SEARCH41_CORPORA_BUTTON_XPATH)
            button.click()
            speak("The reference corpus options are Dickens Novels, 19th Century Reference Corpus, Children's Literature, "
                  "Additional Requested Texts and African American Writers ")
            statement = takeCommand().lower()
            if 'Dickens Novels' in statement or 'Decans Novels' in statement \
                    or 'novels' in statement:
                DZNOZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[2]'
                browser = driver
                button = browser.find_element(By.XPATH, DZNOZ_BUTTON_XPATH)
                button.click()
                # or 'Additional Requested Texts' in statement or 'African American Writers' in statement:
            elif '19th Century Reference corpus' in statement:
                NINETEENZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[3]'
                browser = driver
                button = browser.find_element(By.XPATH, NINETEENZ_BUTTON_XPATH)
                button.click()
            elif "Children's Literature" in statement:
                CZHILLIT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[4]'
                browser = driver
                button = browser.find_element(By.XPATH, CZHILLIT_BUTTON_XPATH)
                button.click()
            elif "Additional Requested Texts" in statement:
                ARZTSZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[5]'
                browser = driver
                button = browser.find_element(By.XPATH, ARZTSZ_BUTTON_XPATH)
                button.click()
            elif "African American Writers" in statement:
                AFZAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[6]'
                browser = driver
                button = browser.find_element(By.XPATH, AFZAW_BUTTON_XPATH)
                button.click()
            elif "Bleak House" in statement or "Bleak House" in statement:
                ZLOB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[8]'
                browser = driver
                button = browser.find_element(By.XPATH, ZLOB_BUTTON_XPATH)
                button.click()
            elif "Barnaby Rudges" in statement:
                ZBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[9]'
                browser = driver
                button = browser.find_element(By.XPATH, ZBAR_BUTTON_XPATH)
                button.click()
            elif "david copperfield" in statement:
                DACZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[10]'
                browser = driver
                button = browser.find_element(By.XPATH, DACZ_BUTTON_XPATH)
                button.click()
            elif "Dombey and son" in statement:
                DOAZS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[11]'
                browser = driver
                button = browser.find_element(By.XPATH, DOAZS_BUTTON_XPATH)
                button.click()
            elif "The mystery of edwin drood" in statement:
                THMOZED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[12]'
                browser = driver
                button = browser.find_element(By.XPATH, THMOZED_BUTTON_XPATH)
                button.click()
            elif "great expectationS" in statement:
                DREZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[13]'
                browser = driver
                button = browser.find_element(By.XPATH, DREZ_BUTTON_XPATH)
                button.click()
            elif "hard times" in statement:
                ZHAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[14]'
                browser = driver
                button = browser.find_element(By.XPATH, ZHAT_BUTTON_XPATH)
                button.click()
            elif "little dorrit" in statement:
                ZLID_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[15]'
                browser = driver
                button = browser.find_element(By.XPATH, ZLID_BUTTON_XPATH)
                button.click()
            elif "martin chuzzlewit" in statement:
                MACZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[16]'
                browser = driver
                button = browser.find_element(By.XPATH, MACZ_BUTTON_XPATH)
                button.click()
            elif "nicholas nickleby" in statement:
                NINZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[17]'
                browser = driver
                button = browser.find_element(By.XPATH, NINZ_BUTTON_XPATH)
                button.click()
            elif "the old curiosity shop" in statement:
                TOCZS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[18]'
                browser = driver
                button = browser.find_element(By.XPATH, TOCZS_BUTTON_XPATH)
                button.click()
            elif "our mutual friend" in statement:
                ZOUMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[19]'
                browser = driver
                button = browser.find_element(By.XPATH, ZOUMF_BUTTON_XPATH)
                button.click()
            elif "oliver twist" in statement:
                ZOLT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[20]'
                browser = driver
                button = browser.find_element(By.XPATH, ZOLT_BUTTON_XPATH)
                button.click()
            elif "pickwick papers" in statement:
                PIPZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[21]'
                browser = driver
                button = browser.find_element(By.XPATH, PIPZ_BUTTON_XPATH)
                button.click()
            elif "a tale of two cities" in statement:
                ATAOTCZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[22]'
                browser = driver
                button = browser.find_element(By.XPATH, ATAOTCZ_BUTTON_XPATH)
                button.click()
            elif "agnes grey" in statement:
                AGGZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[24]'
                browser = driver
                button = browser.find_element(By.XPATH, AGGZ_BUTTON_XPATH)
                button.click()
            elif "the small house at Allington" in statement:
                THSHAAZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[25]'
                browser = driver
                button = browser.find_element(By.XPATH, THSHAAZ_BUTTON_XPATH)
                button.click()
            elif "antonina or the fall of rome" in statement:
                ANOZTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[26]'
                browser = driver
                button = browser.find_element(By.XPATH, ANOZTFOR_BUTTON_XPATH)
                button.click()
            elif "armadale" in statement:
                ARZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[27]'
                browser = driver
                button = browser.find_element(By.XPATH, ARZ_BUTTON_XPATH)
                button.click()
            elif "the hound of the baskervilles" in statement:
                ZTHHOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[28]'
                browser = driver
                button = browser.find_element(By.XPATH, ZTHHOTB_BUTTON_XPATH)
                button.click()
            elif "cranford" in statement:
                CRZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[29]'
                browser = driver
                button = browser.find_element(By.XPATH, CRZ_BUTTON_XPATH)
                button.click()
            elif "daniel deronda" in statement:
                DZAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[30]'
                browser = driver
                button = browser.find_element(By.XPATH, DZAD_BUTTON_XPATH)
                button.click()
            elif "the picture of dorian grey" in statement:
                THPZODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[31]'
                browser = driver
                button = browser.find_element(By.XPATH, THPZODG_BUTTON_XPATH)
                button.click()
            elif "dracula" in statement:
                DRZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[32]'
                browser = driver
                button = browser.find_element(By.XPATH, DRZ_BUTTON_XPATH)
                button.click()
            elif "emma" in statement:
                ZEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[33]'
                browser = driver
                button = browser.find_element(By.XPATH, ZEM_BUTTON_XPATH)
                button.click()
            elif "frankenstein" in statement:
                FRZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[34]'
                browser = driver
                button = browser.find_element(By.XPATH, FRZ_BUTTON_XPATH)
                button.click()
            elif "jane eyre" in statement:
                JAEZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[35]'
                browser = driver
                button = browser.find_element(By.XPATH, JAEZ_BUTTON_XPATH)
                button.click()
            elif "the strange case of doctor Jekyll and mister hyde" in statement:
                TASCZODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[36]'
                browser = driver
                button = browser.find_element(By.XPATH, TASCZODJAMH_BUTTON_XPATH)
                button.click()
            elif "jude the obscure" in statement:
                JATOZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[37]'
                browser = driver
                button = browser.find_element(By.XPATH, JATOZ_BUTTON_XPATH)
                button.click()
            elif "lady audleys secret" in statement:
                LAAZS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[38]'
                browser = driver
                button = browser.find_element(By.XPATH, LAAZS_BUTTON_XPATH)
                button.click()
            elif "mary barton" in statement:
                MZBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[39]'
                browser = driver
                button = browser.find_element(By.XPATH, MZBA_BUTTON_XPATH)
                button.click()
            elif "the mill on the floss" in statement:
                TAMOZTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[40]'
                browser = driver
                button = browser.find_element(By.XPATH, TAMOZTF_BUTTON_XPATH)
                button.click()
            elif "the return of the native" in statement:
                TAROTZN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[41]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROTZN_BUTTON_XPATH)
                button.click()
            elif "north and south" in statement:
                NAASZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[42]'
                browser = driver
                button = browser.find_element(By.XPATH, NAASZ_BUTTON_XPATH)
                button.click()
            elif "persuasion" in statement:
                PAZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[43]'
                browser = driver
                button = browser.find_element(By.XPATH, PAZ_BUTTON_XPATH)
                button.click()
            elif "the last days of pompeii" in statement:
                TALDZOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[44]'
                browser = driver
                button = browser.find_element(By.XPATH, TALDZOP_BUTTON_XPATH)
                button.click()
            elif "pride and prejudice" in statement:
                PZAAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[45]'
                browser = driver
                button = browser.find_element(By.XPATH, PZAAP_BUTTON_XPATH)
                button.click()
            elif "the professor" in statement:
                TAZP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[46]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZP_BUTTON_XPATH)
                button.click()
            elif "sybil or the two nations" in statement:
                SAOTZTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[47]'
                browser = driver
                button = browser.find_element(By.XPATH, SAOTZTN_BUTTON_XPATH)
                button.click()
            elif "tess of the d'urbevilles" in statement:
                TAODZU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[48]'
                browser = driver
                button = browser.find_element(By.XPATH, TAODZU_BUTTON_XPATH)
                button.click()
            elif "vanity fair" in statement:
                ZAPZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[49]'
                browser = driver
                button = browser.find_element(By.XPATH, ZAPZ_BUTTON_XPATH)
                button.click()
            elif "vivian grey" in statement:
                ZAZG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[50]'
                browser = driver
                button = browser.find_element(By.XPATH, ZAZG_BUTTON_XPATH)
                button.click()
            elif "wuthering heights" in statement:
                WZAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[51]'
                browser = driver
                button = browser.find_element(By.XPATH, WZAH_BUTTON_XPATH)
                button.click()
            elif "the woman in white" in statement:
                TAWZIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[52]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWZIW_BUTTON_XPATH)
                button.click()
            elif "alice's adventures in wonderland" in statement:
                AAAIZW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[54]'
                browser = driver
                button = browser.find_element(By.XPATH, AAAIZW_BUTTON_XPATH)
                button.click()
            elif "alone in london" in statement:
                AAZIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[55]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZIL_BUTTON_XPATH)
                button.click()
            elif "the story of the amulet " in statement:
                TSZAOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[56]'
                browser = driver
                button = browser.find_element(By.XPATH, TSZAOTA_BUTTON_XPATH)
                button.click()
            elif "black beauty" in statement:
                ZBAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[57]'
                browser = driver
                button = browser.find_element(By.XPATH, ZBAB_BUTTON_XPATH)
                button.click()
            elif "the brass bottle" in statement:
                TABZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[58]'
                browser = driver
                button = browser.find_element(By.XPATH, TABZ_BUTTON_XPATH)
                button.click()
            elif "the tale of benjamin bunny" in statement:
                TATOBBZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[59]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOBBZ_BUTTON_XPATH)
                button.click()
            elif "the settlers in canada" in statement:
                TASZIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[60]'
                browser = driver
                button = browser.find_element(By.XPATH, TASZIC_BUTTON_XPATH)
                button.click()
            elif "the  carved lions" in statement:
                TZACL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[61]'
                browser = driver
                button = browser.find_element(By.XPATH, TZACL_BUTTON_XPATH)
                button.click()
            elif "with clive in india" in statement:
                WAZCII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[62]'
                browser = driver
                button = browser.find_element(By.XPATH, WAZCII_BUTTON_XPATH)
                button.click()
            elif "the coral island" in statement:
                TACZI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[63]'
                browser = driver
                button = browser.find_element(By.XPATH, TACZI_BUTTON_XPATH)
                button.click()
            elif "the crofton boys" in statement:
                TACZB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[64]'
                browser = driver
                button = browser.find_element(By.XPATH, TACZB_BUTTON_XPATH)
                button.click()
            elif "the cuckoo clock" in statement:
                TACZC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[65]'
                browser = driver
                button = browser.find_element(By.XPATH, TACZC_BUTTON_XPATH)
                button.click()
            elif "the daisy chain" in statement:
                TADCZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[66]'
                browser = driver
                button = browser.find_element(By.XPATH, TADCZ_BUTTON_XPATH)
                button.click()
            elif "the fifth form at saint dominics" in statement:
                TAFFZASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[67]'
                browser = driver
                button = browser.find_element(By.XPATH, TAFFZASD_BUTTON_XPATH)
                button.click()
            elif "the dove in the eagles nest" in statement:
                TADITZEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[68]'
                browser = driver
                button = browser.find_element(By.XPATH, TADITZEN_BUTTON_XPATH)
                button.click()
            elif "the book of dragons" in statement:
                TAZOBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[69]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZOBD_BUTTON_XPATH)
                button.click()
            elif "dream days" in statement:
                DARZD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[70]'
                browser = driver
                button = browser.find_element(By.XPATH, DARZD_BUTTON_XPATH)
                button.click()
            elif "the little duke" in statement:
                TALZD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[71]'
                browser = driver
                button = browser.find_element(By.XPATH, TALZD_BUTTON_XPATH)
                button.click()
            elif "eric" in statement:
                ZEAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[72]'
                browser = driver
                button = browser.find_element(By.XPATH, ZEAR_BUTTON_XPATH)
                button.click()
            elif "feats on the fiord" in statement:
                FOAZTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[73]'
                browser = driver
                button = browser.find_element(By.XPATH, FOAZTF_BUTTON_XPATH)
                button.click()
            elif "five children and it" in statement:
                FACZAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[74]'
                browser = driver
                button = browser.find_element(By.XPATH, FACZAI_BUTTON_XPATH)
                button.click()
            elif "the tale of the flopsy bunnies" in statement:
                TZATOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[75]'
                browser = driver
                button = browser.find_element(By.XPATH, TZATOTFB_BUTTON_XPATH)
                button.click()
            elif "the children of the new forest" in statement:
                TAZCOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[76]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZCOTNF_BUTTON_XPATH)
                button.click()
            elif "a world of girls" in statement:
                AAZWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[77]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZWOG_BUTTON_XPATH)
                button.click()
            elif "through the looking glass" in statement:
                TAZTLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[78]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZTLG_BUTTON_XPATH)
                button.click()
            elif "the golden age" in statement:
                TAGZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[79]'
                browser = driver
                button = browser.find_element(By.XPATH, TAGZA_BUTTON_XPATH)
                button.click()
            elif "holiday house" in statement:
                HZAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[80]'
                browser = driver
                button = browser.find_element(By.XPATH, HZAH_BUTTON_XPATH)
                button.click()
            elif "madam how and lady why" in statement:
                MBAZHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[81]'
                browser = driver
                button = browser.find_element(By.XPATH, MBAZHALW_BUTTON_XPATH)
                button.click()
            elif "jackanapes" in statement:
                JZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[82]'
                browser = driver
                button = browser.find_element(By.XPATH, JZA_BUTTON_XPATH)
                button.click()
            elif "the tale of jemima puddle duck" in statement:
                TATOZJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[83]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOZJP_BUTTON_XPATH)
                button.click()
            elif "jessicas first prayer" in statement:
                JZAFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[84]'
                browser = driver
                button = browser.find_element(By.XPATH, JZAFP_BUTTON_XPATH)
                button.click()
            elif "the jungle book" in statement:
                TAJZB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[85]'
                browser = driver
                button = browser.find_element(By.XPATH, TAJZB_BUTTON_XPATH)
                button.click()
            elif "kidnapped" in statement:
                ZKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[86]'
                browser = driver
                button = browser.find_element(By.XPATH, ZKA_BUTTON_XPATH)
                button.click()
            elif "leila at home" in statement:
                LAZAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[87]'
                browser = driver
                button = browser.find_element(By.XPATH, LAZAH_BUTTON_XPATH)
                button.click()
            elif "masterman ready" in statement:
                MZAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[88]'
                browser = driver
                button = browser.find_element(By.XPATH, MZAR_BUTTON_XPATH)
                button.click()
            elif "little meg's children" in statement:
                LAZMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[89]'
                browser = driver
                button = browser.find_element(By.XPATH, LAZMC_BUTTON_XPATH)
                button.click()
            elif "the tale of two bad mice" in statement:
                TATOTZBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[90]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOTZBM_BUTTON_XPATH)
                button.click()
            elif "moonfleet" in statement:
                MAZF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[91]'
                browser = driver
                button = browser.find_element(By.XPATH, MAZF_BUTTON_XPATH)
                button.click()
            elif "mopsa the fairy" in statement:
                MAZTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[92]'
                browser = driver
                button = browser.find_element(By.XPATH, MAZTF_BUTTON_XPATH)
                button.click()
            elif "the three mulla-mulgars" in statement:
                TATZMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[93]'
                browser = driver
                button = browser.find_element(By.XPATH, TATZMM_BUTTON_XPATH)
                button.click()
            elif "mrs. overtheways remembrances" in statement:
                MAORZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[94]'
                browser = driver
                button = browser.find_element(By.XPATH, MAORZ_BUTTON_XPATH)
                button.click()
            elif "peter pan" in statement:
                PAEPZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[95]'
                browser = driver
                button = browser.find_element(By.XPATH, PAEPZA_BUTTON_XPATH)
                button.click()
            elif "the peasant and the prince" in statement:
                TAZPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[96]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZPATP_BUTTON_XPATH)
                button.click()
            elif "prince prigio" in statement:
                PAZRPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[97]'
                browser = driver
                button = browser.find_element(By.XPATH, PAZRPR_BUTTON_XPATH)
                button.click()
            elif "the happy prince" in statement:
                TAZHP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[98]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZHP_BUTTON_XPATH)
                button.click()
            elif "the princess in goblin" in statement:
                TPZATC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[99]'
                browser = driver
                button = browser.find_element(By.XPATH, TPZATC_BUTTON_XPATH)
                button.click()
            elif "allan quatermain" in statement:
                AAZQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[100]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZQ_BUTTON_XPATH)
                button.click()
            elif "the tale of peter rabbit" in statement:
                TZATOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[101]'
                browser = driver
                button = browser.find_element(By.XPATH, TZATOPR_BUTTON_XPATH)
                button.click()
            elif "the railway children" in statement:
                TARZC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[102]'
                browser = driver
                button = browser.find_element(By.XPATH, TARZC_BUTTON_XPATH)
                button.click()
            elif "the heir of redclyffe" in statement:
                TAHOZR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[103]'
                browser = driver
                button = browser.find_element(By.XPATH, TAHOZR_BUTTON_XPATH)
                button.click()
            elif "the rival crusoes" in statement:
                TARZCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[104]'
                browser = driver
                button = browser.find_element(By.XPATH, TARZCR_BUTTON_XPATH)
                button.click()
            elif "the rose and the ring" in statement:
                TZARATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[105]'
                browser = driver
                button = browser.find_element(By.XPATH, TZARATR_BUTTON_XPATH)
                button.click()
            elif "the secret garden" in statement:
                TASZG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[106]'
                browser = driver
                button = browser.find_element(By.XPATH, TASZG_BUTTON_XPATH)
                button.click()
            elif "the story of the treasure seekers" in statement:
                TZASOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[107]'
                browser = driver
                button = browser.find_element(By.XPATH, TZASOTTS_BUTTON_XPATH)
                button.click()
            elif "the settlers at home" in statement:
                TASAZH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[108]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAZH_BUTTON_XPATH)
                button.click()
            elif "king solomons mines" in statement:
                KAZSM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[109]'
                browser = driver
                button = browser.find_element(By.XPATH, KAZSM_BUTTON_XPATH)
                button.click()
            elif "the tale of squirrel nutkin" in statement:
                TATOZSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[110]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOZSN_BUTTON_XPATH)
                button.click()
            elif "stalky and co" in statement:
                SZAAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[111]'
                browser = driver
                button = browser.find_element(By.XPATH, SZAAC_BUTTON_XPATH)
                button.click()
            elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                    or "the black brothers" in statement:
                TAKOTZGROTZB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[112]'
                browser = driver
                button = browser.find_element(By.XPATH, TAKOTZGROTZB_BUTTON_XPATH)
                button.click()
            elif "the tapestry room" in statement:
                TAZTR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[113]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZTR_BUTTON_XPATH)
                button.click()
            elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                TASAOSTZLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[114]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAOSTZLWTOGNS_BUTTON_XPATH)
                button.click()
            elif "tom brown's schooldays" in statement:
                TZABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[115]'
                browser = driver
                button = browser.find_element(By.XPATH, TZABS_BUTTON_XPATH)
                button.click()
            elif "treasure island" in statement:
                TAIZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[116]'
                browser = driver
                button = browser.find_element(By.XPATH, TAIZ_BUTTON_XPATH)
                button.click()
            elif "nine unlikely tales" in statement:
                ZNAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[117]'
                browser = driver
                button = browser.find_element(By.XPATH, ZNAUT_BUTTON_XPATH)
                button.click()
            elif "vise versa" in statement:
                ZAZZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[118]'
                browser = driver
                button = browser.find_element(By.XPATH, ZAZZ_BUTTON_XPATH)
                button.click()
            elif "adventures in wallypug land" in statement:
                AAZIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[119]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZIW_BUTTON_XPATH)
                button.click()
            elif "the water babies" in statement:
                TAZWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[120]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZWB_BUTTON_XPATH)
                button.click()
            elif "the wind in the willows" in statement:
                TAWZITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[121]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWZITW_BUTTON_XPATH)
                button.click()
            elif "at the back of the north wind" in statement:
                ABATZOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[122]'
                browser = driver
                button = browser.find_element(By.XPATH, ABATZOTNW_BUTTON_XPATH)
                button.click()
            elif "winning his spurs" in statement:
                WAZHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[123]'
                browser = driver
                button = browser.find_element(By.XPATH, WAZHS_BUTTON_XPATH)
                button.click()
            elif "wood magic" in statement:
                WAZM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[124]'
                browser = driver
                button = browser.find_element(By.XPATH, WAZM_BUTTON_XPATH)
                button.click()
            elif "american notes for general circulation" in statement:
                AAZNFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[126]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZNFGC_BUTTON_XPATH)
                button.click()
            elif "the awakening and several short stories" in statement:
                TAAAZSSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[127]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAAZSSS_BUTTON_XPATH)
                button.click()
            elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                    or "a ghost story of christmas" in statement:
                AZACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[128]'
                browser = driver
                button = browser.find_element(By.XPATH, AZACCAGSOC_BUTTON_XPATH)
                button.click()
            elif "gullivers travels" in statement:
                AZGT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[129]'
                browser = driver
                button = browser.find_element(By.XPATH, AZGT_BUTTON_XPATH)
                button.click()
            elif "heart of darkness" in statement:
                HODZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[130]'
                browser = driver
                button = browser.find_element(By.XPATH, HODZA_BUTTON_XPATH)
                button.click()
            elif "adventures of huckleberry finn" in statement:
                AOHAZF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[131]'
                browser = driver
                button = browser.find_element(By.XPATH, AOHAZF_BUTTON_XPATH)
                button.click()
            elif "lady susan" in statement:
                LAZS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[132]'
                browser = driver
                button = browser.find_element(By.XPATH, LAZS_BUTTON_XPATH)
                button.click()
            elif "what maisie knew" in statement:
                WMAZK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[133]'
                browser = driver
                button = browser.find_element(By.XPATH, WMAZK_BUTTON_XPATH)
                button.click()
            elif "mansfield park" in statement:
                MZAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[134]'
                browser = driver
                button = browser.find_element(By.XPATH, MZAP_BUTTON_XPATH)
                button.click()
            elif "middlemarch" in statement:
                ZMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[135]'
                browser = driver
                button = browser.find_element(By.XPATH, ZMA_BUTTON_XPATH)
                button.click()
            elif "the moonstone" in statement:
                TZAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[136]'
                browser = driver
                button = browser.find_element(By.XPATH, TZAM_BUTTON_XPATH)
                button.click()
            elif "northanger abbey" in statement:
                ZNAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[137]'
                browser = driver
                button = browser.find_element(By.XPATH, ZNAA_BUTTON_XPATH)
                button.click()
            elif "pictures from italy" in statement:
                ZPAFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[138]'
                browser = driver
                button = browser.find_element(By.XPATH, ZPAFI_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 1" in statement:
                ZPAOALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[139]'
                browser = driver
                button = browser.find_element(By.XPATH, ZPAOALO_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 2" in statement:
                ZPAOALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[140]'
                browser = driver
                button = browser.find_element(By.XPATH, ZPAOALT_BUTTON_XPATH)
                button.click()
            elif "a room with a view" in statement:
                ARZAWAZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[141]'
                browser = driver
                button = browser.find_element(By.XPATH, ARZAWAZ_BUTTON_XPATH)
                button.click()
            elif "sense and sensibility" in statement:
                SAAZS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[142]'
                browser = driver
                button = browser.find_element(By.XPATH, SAAZS_BUTTON_XPATH)
                button.click()
            elif "shirley" in statement:
                ZSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[143]'
                browser = driver
                button = browser.find_element(By.XPATH, ZSA_BUTTON_XPATH)
                button.click()
            elif "the sign of four" in statement:
                TSAOZF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[144]'
                browser = driver
                button = browser.find_element(By.XPATH, TSAOZF_BUTTON_XPATH)
                button.click()
            elif "silas marner" in statement:
                SAZM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[145]'
                browser = driver
                button = browser.find_element(By.XPATH, SAZM_BUTTON_XPATH)
                button.click()
            elif "the return of the soldier" in statement:
                TAROZTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[147]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROZTS_BUTTON_XPATH)
                button.click()
            elif "the tenant of wildfell hall" in statement:
                TATOZWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[148]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOZWH_BUTTON_XPATH)
                button.click()
            elif "the jungle" in statement:
                ZTAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[149]'
                browser = driver
                button = browser.find_element(By.XPATH, ZTAJ_BUTTON_XPATH)
                button.click()
            elif "the time machine" in statement:
                TZATM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[150]'
                browser = driver
                button = browser.find_element(By.XPATH, TZATM_BUTTON_XPATH)
                button.click()
            elif "twelve years a slave" in statement:
                ZTZAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[151]'
                browser = driver
                button = browser.find_element(By.XPATH, ZTZAAS_BUTTON_XPATH)
                button.click()
            elif "the uncommercial traveller" in statement:
                ZTAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[152]'
                browser = driver
                button = browser.find_element(By.XPATH, ZTAUT_BUTTON_XPATH)
                button.click()
            elif "vilette" in statement:
                ZZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[153]'
                browser = driver
                button = browser.find_element(By.XPATH, ZZA_BUTTON_XPATH)
                button.click()
            elif "the war of worlds" in statement:
                TZAWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[154]'
                browser = driver
                button = browser.find_element(By.XPATH, TZAWOW_BUTTON_XPATH)
                button.click()
            elif "women in love" in statement:
                WIAZL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[155]'
                browser = driver
                button = browser.find_element(By.XPATH, WIAZL_BUTTON_XPATH)
                button.click()
            elif "the yellow wallpaper" in statement:
                TZAZW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[156]'
                browser = driver
                button = browser.find_element(By.XPATH, TZAZW_BUTTON_XPATH)
                button.click()
            elif "the house behind the cedars" in statement:
                THAZBTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[158]'
                browser = driver
                button = browser.find_element(By.XPATH, THAZBTC_BUTTON_XPATH)
                button.click()
            elif "the colonel's dream" in statement:
                TCZAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[159]'
                browser = driver
                button = browser.find_element(By.XPATH, TCZAD_BUTTON_XPATH)
                button.click()
            elif "the autobiography of an ex-coloured man" in statement:
                TAAZOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[160]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAZOAEM_BUTTON_XPATH)
                button.click()
            elif "imperium in imperio" in statement:
                IZIAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[161]'
                browser = driver
                button = browser.find_element(By.XPATH, IZIAI_BUTTON_XPATH)
                button.click()
            elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                    or "iola leroy" in statement:
                ILOSZAU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[162]'
                browser = driver
                button = browser.find_element(By.XPATH, ILOSZAU_BUTTON_XPATH)
                button.click()
            elif "the marrow of tradition" in statement:
                TMOZAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[163]'
                browser = driver
                button = browser.find_element(By.XPATH, TMOZAT_BUTTON_XPATH)
                button.click()
            elif "the sport of the gods" in statement:
                TSOZTAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[164]'
                browser = driver
                button = browser.find_element(By.XPATH, TSOZTAG_BUTTON_XPATH)
                button.click()
            elif "unfettered" in statement:
                ZUA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[165]'
                browser = driver
                button = browser.find_element(By.XPATH, ZUA_BUTTON_XPATH)
                button.click()
            elif "agnes strickland" in statement:
                AZSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[167]'
                browser = driver
                button = browser.find_element(By.XPATH, AZSA_BUTTON_XPATH)
                button.click()
            elif "andrew lang" in statement:
                AAZL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[168]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZL_BUTTON_XPATH)
                button.click()
            elif "ann fraser tytler" in statement:
                AAZFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[169]'
                browser = driver
                button = browser.find_element(By.XPATH, AAZFT_BUTTON_XPATH)
                button.click()
            elif "anna sewell" in statement:
                AZASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[170]'
                browser = driver
                button = browser.find_element(By.XPATH, AZASE_BUTTON_XPATH)
                button.click()
            elif "anne bronte" in statement:
                AZAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[171]'
                browser = driver
                button = browser.find_element(By.XPATH, AZAB_BUTTON_XPATH)
                button.click()
            elif "anthony trollope" in statement:
                AZTAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[172]'
                browser = driver
                button = browser.find_element(By.XPATH, AZTAR_BUTTON_XPATH)
                button.click()
            elif "arthur conan doyle" in statement:
                ZAACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[173]'
                browser = driver
                button = browser.find_element(By.XPATH, ZAACD_BUTTON_XPATH)
                button.click()
            elif "baron edward bulwer lytton lytton" in statement:
                ZAEBBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[174]'
                browser = driver
                button = browser.find_element(By.XPATH, ZAEBBLL_BUTTON_XPATH)
                button.click()
            elif "beatrix potter" in statement:
                ZAPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[175]'
                browser = driver
                button = browser.find_element(By.XPATH, ZAPB_BUTTON_XPATH)
                button.click()
            elif "bram stoker" in statement:
                ZBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[176]'
                browser = driver
                button = browser.find_element(By.XPATH, ZBAS_BUTTON_XPATH)
                button.click()
            elif "captain frederick marryat" in statement:
                CFZAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[177]'
                browser = driver
                button = browser.find_element(By.XPATH, CFZAM_BUTTON_XPATH)
                button.click()
            elif "catherine sinclair" in statement:
                CASZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[178]'
                browser = driver
                button = browser.find_element(By.XPATH, CASZ_BUTTON_XPATH)
                button.click()
            elif "charles dickens" in statement:
                CADZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[179]'
                browser = driver
                button = browser.find_element(By.XPATH, CADZ_BUTTON_XPATH)
                button.click()
            elif "charles kinglsey" in statement:
                CAKZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[180]'
                browser = driver
                button = browser.find_element(By.XPATH, CAKZ_BUTTON_XPATH)
                button.click()
            elif "charles W. chestnutt" in statement:
                CAWZC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[181]'
                browser = driver
                button = browser.find_element(By.XPATH, CAWZC_BUTTON_XPATH)
                button.click()
            elif "charlotte bronte" in statement:
                CZAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[182]'
                browser = driver
                button = browser.find_element(By.XPATH, CZAB_BUTTON_XPATH)
                button.click()
            elif "charlotte M. yonge" in statement:
                CMAZZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[183]'
                browser = driver
                button = browser.find_element(By.XPATH, CMAZZ_BUTTON_XPATH)
                button.click()
            elif "charlotte perkins gilman" in statement:
                CZPAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[184]'
                browser = driver
                button = browser.find_element(By.XPATH, CZPAG_BUTTON_XPATH)
                button.click()
            elif "D. H. lawrence" in statement:
                DHAZL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[185]'
                browser = driver
                button = browser.find_element(By.XPATH, DHAZL_BUTTON_XPATH)
                button.click()
            elif "E. M. forster" in statement:
                EMZAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[186]'
                browser = driver
                button = browser.find_element(By.XPATH, EMZAF_BUTTON_XPATH)
                button.click()
            elif "E. Nesbit" in statement:
                EZAN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[187]'
                browser = driver
                button = browser.find_element(By.XPATH, EZAN_BUTTON_XPATH)
                button.click()
            elif "earl of beaconsfield benjamin disraeli" in statement:
                EAOZBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[188]'
                browser = driver
                button = browser.find_element(By.XPATH, EAOZBBD_BUTTON_XPATH)
                button.click()
            elif "elizabeth cleghorn gaskell" in statement:
                EZACG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[189]'
                browser = driver
                button = browser.find_element(By.XPATH, EZACG_BUTTON_XPATH)
                button.click()
            elif "emily bronte" in statement:
                EAZB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[190]'
                browser = driver
                button = browser.find_element(By.XPATH, EAZB_BUTTON_XPATH)
                button.click()
            elif "F. anstey" in statement:
                FAZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[191]'
                browser = driver
                button = browser.find_element(By.XPATH, FAZA_BUTTON_XPATH)
                button.click()
            elif "frances E. W. harper" in statement:
                FAEZWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[192]'
                browser = driver
                button = browser.find_element(By.XPATH, FAEZWH_BUTTON_XPATH)
                button.click()
            elif "francis hodgson burnett" in statement:
                FHAZB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[193]'
                browser = driver
                browser.find_element(By.XPATH, FHAZB_BUTTON_XPATH)
                button.click()
            elif "Frederic william farrar" in statement:
                FAZWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[194]'
                browser = driver
                browser.find_element(By.XPATH, FAZWF_BUTTON_XPATH)
                button.click()
            elif "G.A. Henty" in statement:
                GAAZH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[195]'
                browser = driver
                button = browser.find_element(By.XPATH,GAAZH_BUTTON_XPATH)
                button.click()
            elif "G.E.Farrow" in statement:
                GEZAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[196]'
                browser = driver
                button = browser.find_element(By.XPATH, GEZAF_BUTTON_XPATH)
                button.click()
            elif "George Eliot" in statement:
                GZAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[197]'
                browser = driver
                button = browser.find_element(By.XPATH, GZAE_BUTTON_XPATH)
                button.click()
            elif "Geroge Macdonald" in statement:
                AZGM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[198]'
                browser = driver
                button = browser.find_element(By.XPATH, AZGM_BUTTON_XPATH)
                button.click()
            elif "H. G Wells" in statement:
                HZGAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[199]'
                browser = driver
                button = browser.find_element(By.XPATH, HZGAW_BUTTON_XPATH)
                button.click()
            elif "H. Rider Haggard" in statement:
                HRZAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[200]'
                browser = driver
                button = browser.find_element(By.XPATH, HRZAH_BUTTON_XPATH)
                button.click()
            elif "Harriet Martineau" in statement:
                HAZM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[201]'
                browser = driver
                button = browser.find_element(By.XPATH, HAZM_BUTTON_XPATH)
                button.click()
            elif "Henry James" in statement:
                HAZJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[202]'
                browser = driver
                button = browser.find_element(By.XPATH, HAZJ_BUTTON_XPATH)
                button.click()
            elif "Hesba Stretton" in statement:
                HZAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[203]'
                browser = driver
                button = browser.find_element(By.XPATH, HZAS_BUTTON_XPATH)
                button.click()
            elif "J. Meade Falkner" in statement:
                JMZAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[204]'
                browser = driver
                button = browser.find_element(By.XPATH, JMZAF_BUTTON_XPATH)
                button.click()
            elif "James M. Barrie" in statement:
                JMZB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[205]'
                browser = driver
                button = browser.find_element(By.XPATH, JMZB_BUTTON_XPATH)
                button.click()
            elif "James Weldon Johnson" in statement:
                JWZAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[206]'
                browser = driver
                button = browser.find_element(By.XPATH, JWZAJ_BUTTON_XPATH)
                button.click()
            elif "Jane Austen" in statement:
                JZAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[207]'
                browser = driver
                button = browser.find_element(By.XPATH, JZAA_BUTTON_XPATH)
                button.click()
            elif "Jean Ingelow" in statement:
                JAZI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[208]'
                browser = driver
                button = browser.find_element(By.XPATH, JAZI_BUTTON_XPATH)
                button.click()
            elif "Jonathan Ruskin" in statement:
                JZRA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[209]'
                browser = driver
                button = browser.find_element(By.XPATH, JZRA_BUTTON_XPATH)
                button.click()
            elif "Jonathan Swift" in statement:
                JSAZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[210]'
                browser = driver
                button = browser.find_element(By.XPATH, JSAZ_BUTTON_XPATH)
                button.click()
            elif "Joseph Conrad" in statement:
                JCZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[211]'
                browser = driver
                button = browser.find_element(By.XPATH, JCZA_BUTTON_XPATH)
                button.click()
            elif "Juliana Horatia Ewing" in statement:
                JHAZE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[212]'
                browser = driver
                button = browser.find_element(By.XPATH, JHAZE_BUTTON_XPATH)
                button.click()
            elif "Kate Chopin" in statement:
                KCZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[213]'
                browser = driver
                button = browser.find_element(By.XPATH, KCZA_BUTTON_XPATH)
                button.click()
            elif "Kenneth Grahame" in statement:
                KGZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[214]'
                browser = driver
                button = browser.find_element(By.XPATH, KGZA_BUTTON_XPATH)
                button.click()
            elif "L.T. Meade" in statement:
                LTZMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[215]'
                browser = driver
                button = browser.find_element(By.XPATH, LTZMA_BUTTON_XPATH)
                button.click()
            elif "lewis carroll" in statement:
                LCAZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[216]'
                browser = driver
                button = browser.find_element(By.XPATH, LCAZ_BUTTON_XPATH)
                button.click()
            elif "M. E Braddon" in statement:
                MEZBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[217]'
                browser = driver
                button = browser.find_element(By.XPATH, MEZBA_BUTTON_XPATH)
                button.click()
            elif "mark twain" in statement:
                MTZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[218]'
                browser = driver
                button = browser.find_element(By.XPATH, MTZA_BUTTON_XPATH)
                button.click()
            elif "mary wollstonecraft shelley" in statement:
                MWZSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[219]'
                browser = driver
                button = browser.find_element(By.XPATH, MWZSA_BUTTON_XPATH)
                button.click()
            elif "Mrs. Molesworth" in statement:
                MMZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[220]'
                browser = driver
                button = browser.find_element(By.XPATH, MMZA_BUTTON_XPATH)
                button.click()
            elif "oscar wilde" in statement:
                OZWA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[221]'
                browser = driver
                button = browser.find_element(By.XPATH, OZWA_BUTTON_XPATH)
                button.click()
            elif "paul laurence dunbar" in statement:
                PLZDA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[222]'
                browser = driver
                button = browser.find_element(By.XPATH, PLZDA_BUTTON_XPATH)
                button.click()
            elif "R. M Ballantyne" in statement:
                RAZMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[223]'
                browser = driver
                button = browser.find_element(By.XPATH, RAZMB_BUTTON_XPATH)
                button.click()
            elif "Rebecca West" in statement:
                RZAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[224]'
                browser = driver
                button = browser.find_element(By.XPATH, RZAW_BUTTON_XPATH)
                button.click()
            elif "Richard Jefferies" in statement:
                RJZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[225]'
                browser = driver
                button = browser.find_element(By.XPATH, RJZA_BUTTON_XPATH)
                button.click()
            elif "Robert Louis Stevenson" in statement:
                RLZAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[226]'
                browser = driver
                button = browser.find_element(By.XPATH, RLZAS_BUTTON_XPATH)
                button.click()
            elif "rudyard kipling" in statement:
                RZKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[227]'
                browser = driver
                button = browser.find_element(By.XPATH, RZKA_BUTTON_XPATH)
                button.click()
            elif "S. R Crockett" in statement:
                SRZCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[228]'
                browser = driver
                button = browser.find_element(By.XPATH, SRZCA_BUTTON_XPATH)
                button.click()
            elif "solomon northrup" in statement:
                SNZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[229]'
                browser = driver
                button = browser.find_element(By.XPATH, SNZA_BUTTON_XPATH)
                button.click()
            elif "sutton E Griggs" in statement:
                SEGZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[230]'
                browser = driver
                button = browser.find_element(By.XPATH, SEGZA_BUTTON_XPATH)
                button.click()
            elif "talbot baines reed" in statement:
                TZARB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[231]'
                browser = driver
                button = browser.find_element(By.XPATH, TZARB_BUTTON_XPATH)
                button.click()
            elif "thomas hardy" in statement:
                TAZHA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[232]'
                browser = driver
                button = browser.find_element(By.XPATH, TAZHA_BUTTON_XPATH)
                button.click()
            elif "thomas hughes" in statement:
                THAZ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[233]'
                browser = driver
                button = browser.find_element(By.XPATH, THAZ_BUTTON_XPATH)
                button.click()
            elif "upton sinclair" in statement:
                UZAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[234]'
                browser = driver
                button = browser.find_element(By.XPATH, UZAS_BUTTON_XPATH)
                button.click()
            elif "walter de la mare" in statement:
                WZDLAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[235]'
                browser = driver
                button = browser.find_element(By.XPATH, WZDLAM_BUTTON_XPATH)
                button.click()
            elif "wilkie collins" in statement:
                WCZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[236]'
                browser = driver
                button = browser.find_element(By.XPATH, WCZA_BUTTON_XPATH)
                button.click()
            elif "william makepeace thackeray" in statement:
                WMTZA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/div[4]/div/ul/li[237]'
                browser = driver
                button = browser.find_element(By.XPATH, WMTZA_BUTTON_XPATH)
                button.click()
            else:
                speak("The text was not found")
                print("Text not found")
                time.sleep(1)
                speak("How else may I be of service?")
                statement = takeCommand().lower()

            grea = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/div/input')
            for option in grea.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/a/span'):
                option.click()
            speak("The subsets available are displayed. What option are you looking for?")
            print("The subsets available are displayed. What option are you looking for?")
            statement = takeCommand().lower()
            if 'all text' in statement:
                grea1 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[1]')
                for option in grea1.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[1]'):
                    option.click()
            if 'short suspensions' in statement or 'short' in statement:
                grea2 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[2]')
                for option in grea2.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[2]'):
                    option.click()
            if 'long suspensions' in statement or 'long' in statement:
                grea3 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[3]')
                for option in grea3.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[3]'):
                    option.click()
            if 'quotes' in statement:
                grea4 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[4]')
                for option in grea4.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[4]'):
                    option.click()
            if 'non quotes' in statement or 'non' in statement:
                grea5 = driver.find_element(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[5]')
                for option in grea5.find_elements(By.XPATH,'//*[@id="control-bar"]/div/fieldset[4]/form/div[5]/div/ul/li[5]'):
                    option.click()
            speak("Here are your results")
            speak("would you like to swap target and reference corpus?")
            statement = takeCommand().lower()
            if 'yes' in statement:
                SWTAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[4]/form/p/a'
                browser = driver
                button = browser.find_element(By.XPATH, SWTAR_BUTTON_XPATH)
                button.click()
                speak("Here are your results")
            speak("would you like to change the p-value cut off?")
            statement = takeCommand().lower()
            if 'yes' in statement:
                PCO_V = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/div/input')
                for option in PCO_V.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/a/span'):
                    option.click()
                speak("what value do you want to choose?")
                if "zero point zero five" in statement:
                    ZPZF = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[1]')
                    for option in ZPZF.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[1]'):
                        option.click()
                if "zero point zero one" in statement:
                    ZPZO = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[2]')
                    for option in ZPZO.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[2]'):
                        option.click()
                if "zero point zero zero one" in statement:
                    ZPZZO = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[3]')
                    for option in ZPZZO.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[3]'):
                        option.click()
            else:
                ZPZZZO = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[4]')
                for option in ZPZZZO.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/div[6]/div/ul/li[4]'):
                    option.click()
            speak("Here are your results")

            speak("would you like to filter any rows?")
            statement = takeCommand().lower()
            if 'yes' in statement:
                speak('please type in your filter terms')
                FXB_R = driver.find_element(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/input[1]')
                for option in FXB_R.find_elements(By.XPATH, '//*[@id="control-bar"]/div/fieldset[4]/form/input[1]'):
                    option.click()
                time.sleep(5)
            press('enter')
            speak('These are the results for the keywords search')


    if 'counts' in statement or 'count' in statement:
            COUNTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/legend/a'
            browser = driver
            button = browser.find_element(By.XPATH, COUNTS_BUTTON_XPATH)
            button.click()
            speak('The counts option is now open. What corpora are you searching for?')
            SEARCH5_CORPORA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div/ul/li/input'
            browser = driver
            button = browser.find_element(By.XPATH, SEARCH5_CORPORA_BUTTON_XPATH)
            button.click()
            speak("The Corpora options are Dickens Novels, 19th Century Reference Corpus, Children's Literature, "
                  "Additional Requested Texts and African American Writers ")
            statement = takeCommand().lower()
            if 'Dickens Novels' in statement or 'Decans Novels' in statement \
                    or 'novels' in statement:
                DVNOV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[2]'
                browser = driver
                button = browser.find_element(By.XPATH, DVNOV_BUTTON_XPATH)
                button.click()
                # or 'Additional Requested Texts' in statement or 'African American Writers' in statement:
            elif '19th Century Reference corpus' in statement:
                NINETEENV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[3]'
                browser = driver
                button = browser.find_element(By.XPATH, NINETEENV_BUTTON_XPATH)
                button.click()
            elif "Children's Literature" in statement:
                CVHILLIT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[4]'
                browser = driver
                button = browser.find_element(By.XPATH, CVHILLIT_BUTTON_XPATH)
                button.click()
            elif "Additional Requested Texts" in statement:
                ARVTSY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[5]'
                browser = driver
                button = browser.find_element(By.XPATH, ARVTSY_BUTTON_XPATH)
                button.click()
            elif "African American Writers" in statement:
                AFVAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[6]'
                browser = driver
                button = browser.find_element(By.XPATH, AFVAW_BUTTON_XPATH)
                button.click()
            elif "Bleak House" in statement or "Bleak House" in statement:
                VLOB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[8]'
                browser = driver
                button = browser.find_element(By.XPATH, VLOB_BUTTON_XPATH)
                button.click()
            elif "Barnaby Rudges" in statement:
                VBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[9]'
                browser = driver
                button = browser.find_element(By.XPATH, VBAR_BUTTON_XPATH)
                button.click()
            elif "david copperfield" in statement:
                DACV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[10]'
                browser = driver
                button = browser.find_element(By.XPATH, DACV_BUTTON_XPATH)
                button.click()
            elif "Dombey and son" in statement:
                DOAVS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[11]'
                browser = driver
                button = browser.find_element(By.XPATH, DOAVS_BUTTON_XPATH)
                button.click()
            elif "The mystery of edwin drood" in statement:
                THMOVED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[12]'
                browser = driver
                button = browser.find_element(By.XPATH, THMOVED_BUTTON_XPATH)
                button.click()
            elif "great expectationS" in statement:
                DREV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[13]'
                browser = driver
                button = browser.find_element(By.XPATH, DREV_BUTTON_XPATH)
                button.click()
            elif "hard times" in statement:
                VHAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[14]'
                browser = driver
                button = browser.find_element(By.XPATH, VHAT_BUTTON_XPATH)
                button.click()
            elif "little dorrit" in statement:
                VLID_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[15]'
                browser = driver
                button = browser.find_element(By.XPATH, VLID_BUTTON_XPATH)
                button.click()
            elif "martin chuzzlewit" in statement:
                MACV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[16]'
                browser = driver
                button = browser.find_element(By.XPATH, MACV_BUTTON_XPATH)
                button.click()
            elif "nicholas nickleby" in statement:
                NINV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[17]'
                browser = driver
                button = browser.find_element(By.XPATH, NINV_BUTTON_XPATH)
                button.click()
            elif "the old curiosity shop" in statement:
                TOCVS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[18]'
                browser = driver
                button = browser.find_element(By.XPATH, TOCVS_BUTTON_XPATH)
                button.click()
            elif "our mutual friend" in statement:
                VOUMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[19]'
                browser = driver
                button = browser.find_element(By.XPATH, VOUMF_BUTTON_XPATH)
                button.click()
            elif "oliver twist" in statement:
                VOLT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[20]'
                browser = driver
                button = browser.find_element(By.XPATH, VOLT_BUTTON_XPATH)
                button.click()
            elif "pickwick papers" in statement:
                PIPV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[21]'
                browser = driver
                button = browser.find_element(By.XPATH, PIPV_BUTTON_XPATH)
                button.click()
            elif "a tale of two cities" in statement:
                ATAOTCV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[22]'
                browser = driver
                button = browser.find_element(By.XPATH, ATAOTCV_BUTTON_XPATH)
                button.click()
            elif "agnes grey" in statement:
                AGGV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[24]'
                browser = driver
                button = browser.find_element(By.XPATH, AGGV_BUTTON_XPATH)
                button.click()
            elif "the small house at Allington" in statement:
                THSHAAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[25]'
                browser = driver
                button = browser.find_element(By.XPATH, THSHAAV_BUTTON_XPATH)
                button.click()
            elif "antonina or the fall of rome" in statement:
                ANOVTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[26]'
                browser = driver
                button = browser.find_element(By.XPATH, ANOVTFOR_BUTTON_XPATH)
                button.click()
            elif "armadale" in statement:
                ARV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[27]'
                browser = driver
                button = browser.find_element(By.XPATH, ARV_BUTTON_XPATH)
                button.click()
            elif "the hound of the baskervilles" in statement:
                VTHHOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[28]'
                browser = driver
                button = browser.find_element(By.XPATH, VTHHOTB_BUTTON_XPATH)
                button.click()
            elif "cranford" in statement:
                CRV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[29]'
                browser = driver
                button = browser.find_element(By.XPATH, CRV_BUTTON_XPATH)
                button.click()
            elif "daniel deronda" in statement:
                DVAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[30]'
                browser = driver
                button = browser.find_element(By.XPATH, DVAD_BUTTON_XPATH)
                button.click()
            elif "the picture of dorian grey" in statement:
                THPVODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[31]'
                browser = driver
                button = browser.find_element(By.XPATH, THPVODG_BUTTON_XPATH)
                button.click()
            elif "dracula" in statement:
                DRV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[32]'
                browser = driver
                button = browser.find_element(By.XPATH, DRV_BUTTON_XPATH)
                button.click()
            elif "emma" in statement:
                VEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[33]'
                browser = driver
                button = browser.find_element(By.XPATH, VEM_BUTTON_XPATH)
                button.click()
            elif "frankenstein" in statement:
                FRV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[34]'
                browser = driver
                button = browser.find_element(By.XPATH, FRV_BUTTON_XPATH)
                button.click()
            elif "jane eyre" in statement:
                JAEV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[35]'
                browser = driver
                button = browser.find_element(By.XPATH, JAEV_BUTTON_XPATH)
                button.click()
            elif "the strange case of doctor Jekyll and mister hyde" in statement:
                TASCVODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[36]'
                browser = driver
                button = browser.find_element(By.XPATH, TASCVODJAMH_BUTTON_XPATH)
                button.click()
            elif "jude the obscure" in statement:
                JATOV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[37]'
                browser = driver
                button = browser.find_element(By.XPATH, JATOV_BUTTON_XPATH)
                button.click()
            elif "lady audleys secret" in statement:
                LAAVS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[38]'
                browser = driver
                button = browser.find_element(By.XPATH, LAAVS_BUTTON_XPATH)
                button.click()
            elif "mary barton" in statement:
                MVBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[39]'
                browser = driver
                button = browser.find_element(By.XPATH, MVBA_BUTTON_XPATH)
                button.click()
            elif "the mill on the floss" in statement:
                TAMOVTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[40]'
                browser = driver
                button = browser.find_element(By.XPATH, TAMOVTF_BUTTON_XPATH)
                button.click()
            elif "the return of the native" in statement:
                TAROTVN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[41]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROTVN_BUTTON_XPATH)
                button.click()
            elif "north and south" in statement:
                NAASV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[42]'
                browser = driver
                button = browser.find_element(By.XPATH, NAASV_BUTTON_XPATH)
                button.click()
            elif "persuasion" in statement:
                PAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[43]'
                browser = driver
                button = browser.find_element(By.XPATH, PAV_BUTTON_XPATH)
                button.click()
            elif "the last days of pompeii" in statement:
                TALDVOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[44]'
                browser = driver
                button = browser.find_element(By.XPATH, TALDVOP_BUTTON_XPATH)
                button.click()
            elif "pride and prejudice" in statement:
                PVAAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[45]'
                browser = driver
                button = browser.find_element(By.XPATH, PVAAP_BUTTON_XPATH)
                button.click()
            elif "the professor" in statement:
                TAVP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[46]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVP_BUTTON_XPATH)
                button.click()
            elif "sybil or the two nations" in statement:
                SAOTVTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[47]'
                browser = driver
                button = browser.find_element(By.XPATH, SAOTVTN_BUTTON_XPATH)
                button.click()
            elif "tess of the d'urbevilles" in statement:
                TAODVU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[48]'
                browser = driver
                button = browser.find_element(By.XPATH, TAODVU_BUTTON_XPATH)
                button.click()
            elif "vanity fair" in statement:
                VAPV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[49]'
                browser = driver
                button = browser.find_element(By.XPATH, VAPV_BUTTON_XPATH)
                button.click()
            elif "vivian grey" in statement:
                VAVG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[50]'
                browser = driver
                button = browser.find_element(By.XPATH, VAVG_BUTTON_XPATH)
                button.click()
            elif "wuthering heights" in statement:
                WVAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[51]'
                browser = driver
                button = browser.find_element(By.XPATH, WVAH_BUTTON_XPATH)
                button.click()
            elif "the woman in white" in statement:
                TAWVIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[52]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWVIW_BUTTON_XPATH)
                button.click()
            elif "alice's adventures in wonderland" in statement:
                AAAIVW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[54]'
                browser = driver
                button = browser.find_element(By.XPATH, AAAIVW_BUTTON_XPATH)
                button.click()
            elif "alone in london" in statement:
                AAVIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[55]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVIL_BUTTON_XPATH)
                button.click()
            elif "the story of the amulet " in statement:
                TSVAOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[56]'
                browser = driver
                button = browser.find_element(By.XPATH, TSVAOTA_BUTTON_XPATH)
                button.click()
            elif "black beauty" in statement:
                VBAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[57]'
                browser = driver
                button = browser.find_element(By.XPATH, VBAB_BUTTON_XPATH)
                button.click()
            elif "the brass bottle" in statement:
                TABV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[58]'
                browser = driver
                button = browser.find_element(By.XPATH, TABV_BUTTON_XPATH)
                button.click()
            elif "the tale of benjamin bunny" in statement:
                TATOBBV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[59]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOBBV_BUTTON_XPATH)
                button.click()
            elif "the settlers in canada" in statement:
                TASVIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[60]'
                browser = driver
                button = browser.find_element(By.XPATH, TASVIC_BUTTON_XPATH)
                button.click()
            elif "the  carved lions" in statement:
                TVACL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[61]'
                browser = driver
                button = browser.find_element(By.XPATH, TVACL_BUTTON_XPATH)
                button.click()
            elif "with clive in india" in statement:
                WAVCII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[62]'
                browser = driver
                button = browser.find_element(By.XPATH, WAVCII_BUTTON_XPATH)
                button.click()
            elif "the coral island" in statement:
                TACVI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[63]'
                browser = driver
                button = browser.find_element(By.XPATH, TACVI_BUTTON_XPATH)
                button.click()
            elif "the crofton boys" in statement:
                TACVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[64]'
                browser = driver
                button = browser.find_element(By.XPATH, TACVB_BUTTON_XPATH)
                button.click()
            elif "the cuckoo clock" in statement:
                TACVC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[65]'
                browser = driver
                button = browser.find_element(By.XPATH, TACVC_BUTTON_XPATH)
                button.click()
            elif "the daisy chain" in statement:
                TADCV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[66]'
                browser = driver
                button = browser.find_element(By.XPATH, TADCV_BUTTON_XPATH)
                button.click()
            elif "the fifth form at saint dominics" in statement:
                TAFFVASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[67]'
                browser = driver
                button = browser.find_element(By.XPATH, TAFFVASD_BUTTON_XPATH)
                button.click()
            elif "the dove in the eagles nest" in statement:
                TADITVEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[68]'
                browser = driver
                button = browser.find_element(By.XPATH, TADITVEN_BUTTON_XPATH)
                button.click()
            elif "the book of dragons" in statement:
                TAVOBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[69]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVOBD_BUTTON_XPATH)
                button.click()
            elif "dream days" in statement:
                DARVD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[70]'
                browser = driver
                button = browser.find_element(By.XPATH, DARVD_BUTTON_XPATH)
                button.click()
            elif "the little duke" in statement:
                TALVD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[71]'
                browser = driver
                button = browser.find_element(By.XPATH, TALVD_BUTTON_XPATH)
                button.click()
            elif "eric" in statement:
                VEAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[72]'
                browser = driver
                button = browser.find_element(By.XPATH, VEAR_BUTTON_XPATH)
                button.click()
            elif "feats on the fiord" in statement:
                FOAVTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[73]'
                browser = driver
                button = browser.find_element(By.XPATH, FOAVTF_BUTTON_XPATH)
                button.click()
            elif "five children and it" in statement:
                FACVAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[74]'
                browser = driver
                button = browser.find_element(By.XPATH, FACVAI_BUTTON_XPATH)
                button.click()
            elif "the tale of the flopsy bunnies" in statement:
                TVATOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[75]'
                browser = driver
                button = browser.find_element(By.XPATH, TVATOTFB_BUTTON_XPATH)
                button.click()
            elif "the children of the new forest" in statement:
                TAVCOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[76]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVCOTNF_BUTTON_XPATH)
                button.click()
            elif "a world of girls" in statement:
                AAVWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[77]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVWOG_BUTTON_XPATH)
                button.click()
            elif "through the looking glass" in statement:
                TAVTLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[78]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVTLG_BUTTON_XPATH)
                button.click()
            elif "the golden age" in statement:
                TAGVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[79]'
                browser = driver
                button = browser.find_element(By.XPATH, TAGVA_BUTTON_XPATH)
                button.click()
            elif "holiday house" in statement:
                HVAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[80]'
                browser = driver
                button = browser.find_element(By.XPATH, HVAH_BUTTON_XPATH)
                button.click()
            elif "madam how and lady why" in statement:
                MBAVHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[81]'
                browser = driver
                button = browser.find_element(By.XPATH, MBAVHALW_BUTTON_XPATH)
                button.click()
            elif "jackanapes" in statement:
                JVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[82]'
                browser = driver
                button = browser.find_element(By.XPATH, JVA_BUTTON_XPATH)
                button.click()
            elif "the tale of jemima puddle duck" in statement:
                TATOVJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[83]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOVJP_BUTTON_XPATH)
                button.click()
            elif "jessicas first prayer" in statement:
                JVAFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[84]'
                browser = driver
                button = browser.find_element(By.XPATH, JVAFP_BUTTON_XPATH)
                button.click()
            elif "the jungle book" in statement:
                TAJVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[85]'
                browser = driver
                button = browser.find_element(By.XPATH, TAJVB_BUTTON_XPATH)
                button.click()
            elif "kidnapped" in statement:
                VKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[86]'
                browser = driver
                button = browser.find_element(By.XPATH, VKA_BUTTON_XPATH)
                button.click()
            elif "leila at home" in statement:
                LAVAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[87]'
                browser = driver
                button = browser.find_element(By.XPATH, LAVAH_BUTTON_XPATH)
                button.click()
            elif "masterman ready" in statement:
                MVAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[88]'
                browser = driver
                button = browser.find_element(By.XPATH, MVAR_BUTTON_XPATH)
                button.click()
            elif "little meg's children" in statement:
                LAVMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[89]'
                browser = driver
                button = browser.find_element(By.XPATH, LAVMC_BUTTON_XPATH)
                button.click()
            elif "the tale of two bad mice" in statement:
                TATOTVBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[90]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOTVBM_BUTTON_XPATH)
                button.click()
            elif "moonfleet" in statement:
                MAVF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[91]'
                browser = driver
                button = browser.find_element(By.XPATH, MAVF_BUTTON_XPATH)
                button.click()
            elif "mopsa the fairy" in statement:
                MAVTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[92]'
                browser = driver
                button = browser.find_element(By.XPATH, MAVTF_BUTTON_XPATH)
                button.click()
            elif "the three mulla-mulgars" in statement:
                TATVMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[93]'
                browser = driver
                button = browser.find_element(By.XPATH, TATVMM_BUTTON_XPATH)
                button.click()
            elif "mrs. overtheways remembrances" in statement:
                MAORV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[94]'
                browser = driver
                button = browser.find_element(By.XPATH, MAORV_BUTTON_XPATH)
                button.click()
            elif "peter pan" in statement:
                PAEPVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[95]'
                browser = driver
                button = browser.find_element(By.XPATH, PAEPVA_BUTTON_XPATH)
                button.click()
            elif "the peasant and the prince" in statement:
                TAVPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[96]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVPATP_BUTTON_XPATH)
                button.click()
            elif "prince prigio" in statement:
                PAVRPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[97]'
                browser = driver
                button = browser.find_element(By.XPATH, PAVRPR_BUTTON_XPATH)
                button.click()
            elif "the happy prince" in statement:
                TAVHP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[98]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVHP_BUTTON_XPATH)
                button.click()
            elif "the princess and the goblin" in statement:
                TPVATG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[99]'
                browser = driver
                button = browser.find_element(By.XPATH, TPVATG_BUTTON_XPATH)
                button.click()
            elif "allan quatermain" in statement:
                AAVQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[100]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVQ_BUTTON_XPATH)
                button.click()
            elif "the tale of peter rabbit" in statement:
                TVATOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[101]'
                browser = driver
                button = browser.find_element(By.XPATH, TVATOPR_BUTTON_XPATH)
                button.click()
            elif "the railway children" in statement:
                TARVC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[102]'
                browser = driver
                button = browser.find_element(By.XPATH, TARVC_BUTTON_XPATH)
                button.click()
            elif "the heir of redclyffe" in statement:
                TAHOVR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[103]'
                browser = driver
                button = browser.find_element(By.XPATH, TAHOVR_BUTTON_XPATH)
                button.click()
            elif "the rival crusoes" in statement:
                TARVCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[104]'
                browser = driver
                button = browser.find_element(By.XPATH, TARVCR_BUTTON_XPATH)
                button.click()
            elif "the rose and the ring" in statement:
                TVARATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[105]'
                browser = driver
                button = browser.find_element(By.XPATH, TVARATR_BUTTON_XPATH)
                button.click()
            elif "the secret garden" in statement:
                TASVG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[106]'
                browser = driver
                button = browser.find_element(By.XPATH, TASVG_BUTTON_XPATH)
                button.click()
            elif "the story of the treasure seekers" in statement:
                TVASOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[107]'
                browser = driver
                button = browser.find_element(By.XPATH, TVASOTTS_BUTTON_XPATH)
                button.click()
            elif "the settlers at home" in statement:
                TASAVH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[108]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAVH_BUTTON_XPATH)
                button.click()
            elif "king solomons mines" in statement:
                KAVSM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[109]'
                browser = driver
                button = browser.find_element(By.XPATH, KAVSM_BUTTON_XPATH)
                button.click()
            elif "the tale of squirrel nutkin" in statement:
                TATOVSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[110]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOVSN_BUTTON_XPATH)
                button.click()
            elif "stalky and co" in statement:
                SVAAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[111]'
                browser = driver
                button = browser.find_element(By.XPATH, SVAAC_BUTTON_XPATH)
                button.click()
            elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                    or "the black brothers" in statement:
                TAKOTVGROTVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[112]'
                browser = driver
                button = browser.find_element(By.XPATH, TAKOTVGROTVB_BUTTON_XPATH)
                button.click()
            elif "the tapestry room" in statement:
                TAVTR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[113]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVTR_BUTTON_XPATH)
                button.click()
            elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                TASAOSTVLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[114]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAOSTVLWTOGNS_BUTTON_XPATH)
                button.click()
            elif "tom brown's schooldays" in statement:
                TVABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[115]'
                browser = driver
                button = browser.find_element(By.XPATH, TVABS_BUTTON_XPATH)
                button.click()
            elif "treasure island" in statement:
                TAIV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[116]'
                browser = driver
                button = browser.find_element(By.XPATH, TAIV_BUTTON_XPATH)
                button.click()
            elif "nine unlikely tales" in statement:
                VNAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[117]'
                browser = driver
                button = browser.find_element(By.XPATH, VNAUT_BUTTON_XPATH)
                button.click()
            elif "vise versa" in statement:
                VAVV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[118]'
                browser = driver
                button = browser.find_element(By.XPATH, VAVV_BUTTON_XPATH)
                button.click()
            elif "adventures in wallypug land" in statement:
                AAVIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[119]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVIW_BUTTON_XPATH)
                button.click()
            elif "the water babies" in statement:
                TAVWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[120]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVWB_BUTTON_XPATH)
                button.click()
            elif "the wind in the willows" in statement:
                TAWVITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[121]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWVITW_BUTTON_XPATH)
                button.click()
            elif "at the back of the north wind" in statement:
                ABATVOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[122]'
                browser = driver
                button = browser.find_element(By.XPATH, ABATVOTNW_BUTTON_XPATH)
                button.click()
            elif "winning his spurs" in statement:
                WAVHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[123]'
                browser = driver
                button = browser.find_element(By.XPATH, WAVHS_BUTTON_XPATH)
                button.click()
            elif "wood magic" in statement:
                WAVM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[124]'
                browser = driver
                button = browser.find_element(By.XPATH, WAVM_BUTTON_XPATH)
                button.click()
            elif "american notes for general circulation" in statement:
                AAVNFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[126]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVNFGC_BUTTON_XPATH)
                button.click()
            elif "the awakening and several short stories" in statement:
                TAAAVSSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[127]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAAVSSS_BUTTON_XPATH)
                button.click()
            elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                    or "a ghost story of christmas" in statement:
                AVACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[128]'
                browser = driver
                button = browser.find_element(By.XPATH, AVACCAGSOC_BUTTON_XPATH)
                button.click()
            elif "gullivers travels" in statement:
                AVGT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[129]'
                browser = driver
                button = browser.find_element(By.XPATH, AVGT_BUTTON_XPATH)
                button.click()
            elif "heart of darkness" in statement:
                HODVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[130]'
                browser = driver
                button = browser.find_element(By.XPATH, HODVA_BUTTON_XPATH)
                button.click()
            elif "adventures of huckleberry finn" in statement:
                AOHAVF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[131]'
                browser = driver
                button = browser.find_element(By.XPATH, AOHAVF_BUTTON_XPATH)
                button.click()
            elif "lady susan" in statement:
                LAVS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[132]'
                browser = driver
                button = browser.find_element(By.XPATH, LAVS_BUTTON_XPATH)
                button.click()
            elif "what maisie knew" in statement:
                WMAVK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[133]'
                browser = driver
                button = browser.find_element(By.XPATH, WMAVK_BUTTON_XPATH)
                button.click()
            elif "mansfield park" in statement:
                MVAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[134]'
                browser = driver
                button = browser.find_element(By.XPATH, MVAP_BUTTON_XPATH)
                button.click()
            elif "middlemarch" in statement:
                VMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[135]'
                browser = driver
                button = browser.find_element(By.XPATH, VMA_BUTTON_XPATH)
                button.click()
            elif "the moonstone" in statement:
                TVAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[136]'
                browser = driver
                button = browser.find_element(By.XPATH, TVAM_BUTTON_XPATH)
                button.click()
            elif "northanger abbey" in statement:
                VNAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[137]'
                browser = driver
                button = browser.find_element(By.XPATH, VNAA_BUTTON_XPATH)
                button.click()
            elif "pictures from italy" in statement:
                VPAFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[138]'
                browser = driver
                button = browser.find_element(By.XPATH, VPAFI_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 1" in statement:
                VPAOALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[139]'
                browser = driver
                button = browser.find_element(By.XPATH, VPAOALO_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 2" in statement:
                VPAOALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[140]'
                browser = driver
                button = browser.find_element(By.XPATH, VPAOALT_BUTTON_XPATH)
                button.click()
            elif "a room with a view" in statement:
                ARVAWAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[141]'
                browser = driver
                button = browser.find_element(By.XPATH, ARVAWAV_BUTTON_XPATH)
                button.click()
            elif "sense and sensibility" in statement:
                SAAVS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[142]'
                browser = driver
                button = browser.find_element(By.XPATH, SAAVS_BUTTON_XPATH)
                button.click()
            elif "shirley" in statement:
                VSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[143]'
                browser = driver
                button = browser.find_element(By.XPATH, VSA_BUTTON_XPATH)
                button.click()
            elif "the sign of four" in statement:
                TSAOVF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[144]'
                browser = driver
                button = browser.find_element(By.XPATH, TSAOVF_BUTTON_XPATH)
                button.click()
            elif "silas marner" in statement:
                SAVM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[145]'
                browser = driver
                button = browser.find_element(By.XPATH, SAVM_BUTTON_XPATH)
                button.click()
            elif "the return of the soldier" in statement:
                TAROVTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[147]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROVTS_BUTTON_XPATH)
                button.click()
            elif "the tenant of wildfell hall" in statement:
                TATOVWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[148]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOVWH_BUTTON_XPATH)
                button.click()
            elif "the jungle" in statement:
                VTAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[149]'
                browser = driver
                button = browser.find_element(By.XPATH, VTAJ_BUTTON_XPATH)
                button.click()
            elif "the time machine" in statement:
                TVATM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[150]'
                browser = driver
                button = browser.find_element(By.XPATH, TVATM_BUTTON_XPATH)
                button.click()
            elif "twelve years a slave" in statement:
                VTYAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[151]'
                browser = driver
                button = browser.find_element(By.XPATH, VTYAAS_BUTTON_XPATH)
                button.click()
            elif "the uncommercial traveller" in statement:
                VTAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[152]'
                browser = driver
                button = browser.find_element(By.XPATH, VTAUT_BUTTON_XPATH)
                button.click()
            elif "vilette" in statement:
                VVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[153]'
                browser = driver
                button = browser.find_element(By.XPATH, VVA_BUTTON_XPATH)
                button.click()
            elif "the war of worlds" in statement:
                TVAWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[154]'
                browser = driver
                button = browser.find_element(By.XPATH, TVAWOW_BUTTON_XPATH)
                button.click()
            elif "women in love" in statement:
                WIAVL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[155]'
                browser = driver
                button = browser.find_element(By.XPATH, WIAVL_BUTTON_XPATH)
                button.click()
            elif "the yellow wallpaper" in statement:
                TVAYW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[156]'
                browser = driver
                button = browser.find_element(By.XPATH, TVAYW_BUTTON_XPATH)
                button.click()
            elif "the house behind the cedars" in statement:
                THAVBTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[158]'
                browser = driver
                button = browser.find_element(By.XPATH, THAVBTC_BUTTON_XPATH)
                button.click()
            elif "the colonel's dream" in statement:
                TCVAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[159]'
                browser = driver
                button = browser.find_element(By.XPATH, TCVAD_BUTTON_XPATH)
                button.click()
            elif "the autobiography of an ex-coloured man" in statement:
                TAAVOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[160]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAVOAEM_BUTTON_XPATH)
                button.click()
            elif "imperium in imperio" in statement:
                IVIAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[161]'
                browser = driver
                button = browser.find_element(By.XPATH, IVIAI_BUTTON_XPATH)
                button.click()
            elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                    or "iola leroy" in statement:
                ILOSVAU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[162]'
                browser = driver
                button = browser.find_element(By.XPATH, ILOSVAU_BUTTON_XPATH)
                button.click()
            elif "the marrow of tradition" in statement:
                TMOVAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[163]'
                browser = driver
                button = browser.find_element(By.XPATH, TMOVAT_BUTTON_XPATH)
                button.click()
            elif "the sport of the gods" in statement:
                TSOVTAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[164]'
                browser = driver
                button = browser.find_element(By.XPATH, TSOVTAG_BUTTON_XPATH)
                button.click()
            elif "unfettered" in statement:
                VUA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[165]'
                browser = driver
                button = browser.find_element(By.XPATH, VUA_BUTTON_XPATH)
                button.click()
            elif "agnes strickland" in statement:
                AVSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[167]'
                browser = driver
                button = browser.find_element(By.XPATH, AVSA_BUTTON_XPATH)
                button.click()
            elif "andrew lang" in statement:
                AAVL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[168]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVL_BUTTON_XPATH)
                button.click()
            elif "ann fraser tytler" in statement:
                AAVFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[169]'
                browser = driver
                button = browser.find_element(By.XPATH, AAVFT_BUTTON_XPATH)
                button.click()
            elif "anna sewell" in statement:
                AVASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[170]'
                browser = driver
                button = browser.find_element(By.XPATH, AVASE_BUTTON_XPATH)
                button.click()
            elif "anne bronte" in statement:
                AVAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[171]'
                browser = driver
                button = browser.find_element(By.XPATH, AVAB_BUTTON_XPATH)
                button.click()
            elif "anthony trollope" in statement:
                AVTAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[172]'
                browser = driver
                button = browser.find_element(By.XPATH, AVTAR_BUTTON_XPATH)
                button.click()
            elif "arthur conan doyle" in statement:
                VAACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[173]'
                browser = driver
                button = browser.find_element(By.XPATH, VAACD_BUTTON_XPATH)
                button.click()
            elif "baron edward bulwer lytton lytton" in statement:
                VAEBBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[174]'
                browser = driver
                button = browser.find_element(By.XPATH, VAEBBLL_BUTTON_XPATH)
                button.click()
            elif "beatrix potter" in statement:
                VAPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[175]'
                browser = driver
                button = browser.find_element(By.XPATH, VAPB_BUTTON_XPATH)
                button.click()
            elif "bram stoker" in statement:
                VBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[176]'
                browser = driver
                button = browser.find_element(By.XPATH, VBAS_BUTTON_XPATH)
                button.click()
            elif "captain frederick marryat" in statement:
                CFVAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[177]'
                browser = driver
                button = browser.find_element(By.XPATH, CFVAM_BUTTON_XPATH)
                button.click()
            elif "catherine sinclair" in statement:
                CASV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[178]'
                browser = driver
                button = browser.find_element(By.XPATH, CASV_BUTTON_XPATH)
                button.click()
            elif "charles dickens" in statement:
                CADV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[179]'
                browser = driver
                button = browser.find_element(By.XPATH, CADV_BUTTON_XPATH)
                button.click()
            elif "charles kinglsey" in statement:
                CAKV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[180]'
                browser = driver
                button = browser.find_element(By.XPATH, CAKV_BUTTON_XPATH)
                button.click()
            elif "charles W. chestnutt" in statement:
                CAWVC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[181]'
                browser = driver
                button = browser.find_element(By.XPATH, CAWVC_BUTTON_XPATH)
                button.click()
            elif "charlotte bronte" in statement:
                CVAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[182]'
                browser = driver
                button = browser.find_element(By.XPATH, CVAB_BUTTON_XPATH)
                button.click()
            elif "charlotte M. yonge" in statement:
                CMAVY_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[183]'
                browser = driver
                button = browser.find_element(By.XPATH, CMAVY_BUTTON_XPATH)
                button.click()
            elif "charlotte perkins gilman" in statement:
                CVPAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[184]'
                browser = driver
                button = browser.find_element(By.XPATH, CVPAG_BUTTON_XPATH)
                button.click()
            elif "D. H. lawrence" in statement:
                DHAVL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[185]'
                browser = driver
                button = browser.find_element(By.XPATH, DHAVL_BUTTON_XPATH)
                button.click()
            elif "E. M. forster" in statement:
                EMVAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[186]'
                browser = driver
                button = browser.find_element(By.XPATH, EMVAF_BUTTON_XPATH)
                button.click()
            elif "E. Nesbit" in statement:
                EVAN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[187]'
                browser = driver
                button = browser.find_element(By.XPATH, EVAN_BUTTON_XPATH)
                button.click()
            elif "earl of beaconsfield benjamin disraeli" in statement:
                EAOVBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[188]'
                browser = driver
                button = browser.find_element(By.XPATH, EAOVBBD_BUTTON_XPATH)
                button.click()
            elif "elizabeth cleghorn gaskell" in statement:
                EVACG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[189]'
                browser = driver
                button = browser.find_element(By.XPATH, EVACG_BUTTON_XPATH)
                button.click()
            elif "emily bronte" in statement:
                EAVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[190]'
                browser = driver
                button = browser.find_element(By.XPATH, EAVB_BUTTON_XPATH)
                button.click()
            elif "F. anstey" in statement:
                FAVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[191]'
                browser = driver
                button = browser.find_element(By.XPATH, FAVA_BUTTON_XPATH)
                button.click()
            elif "frances E. W. harper" in statement:
                FAEVWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[192]'
                browser = driver
                button = browser.find_element(By.XPATH, FAEVWH_BUTTON_XPATH)
                button.click()
            elif "francis hodgson burnett" in statement:
                FHAVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[193]'
                browser = driver
                browser.find_element(By.XPATH, FHAVB_BUTTON_XPATH)
                button.click()
            elif "Frederic william farrar" in statement:
                FAVWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[194]'
                browser = driver
                browser.find_element(By.XPATH, FAVWF_BUTTON_XPATH)
                button.click()
            elif "G.A. Henty" in statement:
                GAAVH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[195]'
                browser = driver
                button = browser.find_element(By.XPATH,GAAVH_BUTTON_XPATH)
                button.click()
            elif "G.E.Farrow" in statement:
                GEVAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[196]'
                browser = driver
                button = browser.find_element(By.XPATH, GEVAF_BUTTON_XPATH)
                button.click()
            elif "George Eliot" in statement:
                GVAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[197]'
                browser = driver
                button = browser.find_element(By.XPATH, GVAE_BUTTON_XPATH)
                button.click()
            elif "Geroge Macdonald" in statement:
                AVGM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[198]'
                browser = driver
                button = browser.find_element(By.XPATH, AVGM_BUTTON_XPATH)
                button.click()
            elif "H. G Wells" in statement:
                HVGAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[199]'
                browser = driver
                button = browser.find_element(By.XPATH, HVGAW_BUTTON_XPATH)
                button.click()
            elif "H. Rider Haggard" in statement:
                HRVAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[200]'
                browser = driver
                button = browser.find_element(By.XPATH, HRVAH_BUTTON_XPATH)
                button.click()
            elif "Harriet Martineau" in statement:
                HAVM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[201]'
                browser = driver
                button = browser.find_element(By.XPATH, HAVM_BUTTON_XPATH)
                button.click()
            elif "Henry James" in statement:
                HAVJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[202]'
                browser = driver
                button = browser.find_element(By.XPATH, HAVJ_BUTTON_XPATH)
                button.click()
            elif "Hesba Stretton" in statement:
                HVAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[203]'
                browser = driver
                button = browser.find_element(By.XPATH, HVAS_BUTTON_XPATH)
                button.click()
            elif "J. Meade Falkner" in statement:
                JMVAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[204]'
                browser = driver
                button = browser.find_element(By.XPATH, JMVAF_BUTTON_XPATH)
                button.click()
            elif "James M. Barrie" in statement:
                JMVB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[205]'
                browser = driver
                button = browser.find_element(By.XPATH, JMVB_BUTTON_XPATH)
                button.click()
            elif "James Weldon Johnson" in statement:
                JWVAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[206]'
                browser = driver
                button = browser.find_element(By.XPATH, JWVAJ_BUTTON_XPATH)
                button.click()
            elif "Jane Austen" in statement:
                JVAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[207]'
                browser = driver
                button = browser.find_element(By.XPATH, JVAA_BUTTON_XPATH)
                button.click()
            elif "Jean Ingelow" in statement:
                JAVI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[208]'
                browser = driver
                button = browser.find_element(By.XPATH, JAVI_BUTTON_XPATH)
                button.click()
            elif "Jonathan Ruskin" in statement:
                JVRA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[209]'
                browser = driver
                button = browser.find_element(By.XPATH, JVRA_BUTTON_XPATH)
                button.click()
            elif "Jonathan Swift" in statement:
                JSAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[210]'
                browser = driver
                button = browser.find_element(By.XPATH, JSAV_BUTTON_XPATH)
                button.click()
            elif "Joseph Conrad" in statement:
                JCVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[211]'
                browser = driver
                button = browser.find_element(By.XPATH, JCVA_BUTTON_XPATH)
                button.click()
            elif "Juliana Horatia Ewing" in statement:
                JHAVE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[212]'
                browser = driver
                button = browser.find_element(By.XPATH, JHAVE_BUTTON_XPATH)
                button.click()
            elif "Kate Chopin" in statement:
                KCVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[213]'
                browser = driver
                button = browser.find_element(By.XPATH, KCVA_BUTTON_XPATH)
                button.click()
            elif "Kenneth Grahame" in statement:
                KGVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[214]'
                browser = driver
                button = browser.find_element(By.XPATH, KGVA_BUTTON_XPATH)
                button.click()
            elif "L.T. Meade" in statement:
                LTVMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[215]'
                browser = driver
                button = browser.find_element(By.XPATH, LTVMA_BUTTON_XPATH)
                button.click()
            elif "lewis carroll" in statement:
                LCAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[216]'
                browser = driver
                button = browser.find_element(By.XPATH, LCAV_BUTTON_XPATH)
                button.click()
            elif "M. E Braddon" in statement:
                MEVBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[217]'
                browser = driver
                button = browser.find_element(By.XPATH, MEVBA_BUTTON_XPATH)
                button.click()
            elif "mark twain" in statement:
                MTVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[218]'
                browser = driver
                button = browser.find_element(By.XPATH, MTVA_BUTTON_XPATH)
                button.click()
            elif "mary wollstonecraft shelley" in statement:
                MWVSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[219]'
                browser = driver
                button = browser.find_element(By.XPATH, MWVSA_BUTTON_XPATH)
                button.click()
            elif "Mrs. Molesworth" in statement:
                MMVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[220]'
                browser = driver
                button = browser.find_element(By.XPATH, MMVA_BUTTON_XPATH)
                button.click()
            elif "oscar wilde" in statement:
                OVWA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[221]'
                browser = driver
                button = browser.find_element(By.XPATH, OVWA_BUTTON_XPATH)
                button.click()
            elif "paul laurence dunbar" in statement:
                PLVDA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[222]'
                browser = driver
                button = browser.find_element(By.XPATH, PLVDA_BUTTON_XPATH)
                button.click()
            elif "R. M Ballantyne" in statement:
                RAVMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[223]'
                browser = driver
                button = browser.find_element(By.XPATH, RAVMB_BUTTON_XPATH)
                button.click()
            elif "Rebecca West" in statement:
                RVAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[224]'
                browser = driver
                button = browser.find_element(By.XPATH, RVAW_BUTTON_XPATH)
                button.click()
            elif "Richard Jefferies" in statement:
                RJVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[225]'
                browser = driver
                button = browser.find_element(By.XPATH, RJVA_BUTTON_XPATH)
                button.click()
            elif "Robert Louis Stevenson" in statement:
                RLVAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[226]'
                browser = driver
                button = browser.find_element(By.XPATH, RLVAS_BUTTON_XPATH)
                button.click()
            elif "rudyard kipling" in statement:
                RVKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[227]'
                browser = driver
                button = browser.find_element(By.XPATH, RVKA_BUTTON_XPATH)
                button.click()
            elif "S. R Crockett" in statement:
                SRVCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[228]'
                browser = driver
                button = browser.find_element(By.XPATH, SRVCA_BUTTON_XPATH)
                button.click()
            elif "solomon northrup" in statement:
                SNVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[229]'
                browser = driver
                button = browser.find_element(By.XPATH, SNVA_BUTTON_XPATH)
                button.click()
            elif "sutton E Griggs" in statement:
                SEGVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[230]'
                browser = driver
                button = browser.find_element(By.XPATH, SEGVA_BUTTON_XPATH)
                button.click()
            elif "talbot baines reed" in statement:
                TVARB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[231]'
                browser = driver
                button = browser.find_element(By.XPATH, TVARB_BUTTON_XPATH)
                button.click()
            elif "thomas hardy" in statement:
                TAVHA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[232]'
                browser = driver
                button = browser.find_element(By.XPATH, TAVHA_BUTTON_XPATH)
                button.click()
            elif "thomas hughes" in statement:
                THAV_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[233]'
                browser = driver
                button = browser.find_element(By.XPATH, THAV_BUTTON_XPATH)
                button.click()
            elif "upton sinclair" in statement:
                UVAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[234]'
                browser = driver
                button = browser.find_element(By.XPATH, UVAS_BUTTON_XPATH)
                button.click()
            elif "walter de la mare" in statement:
                WVDLAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[235]'
                browser = driver
                button = browser.find_element(By.XPATH, WVDLAM_BUTTON_XPATH)
                button.click()
            elif "wilkie collins" in statement:
                WCVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[236]'
                browser = driver
                button = browser.find_element(By.XPATH, WCVA_BUTTON_XPATH)
                button.click()
            elif "william makepeace thackeray" in statement:
                WMTVA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[5]/form/div[1]/div/ul/li[237]'
                browser = driver
                button = browser.find_element(By.XPATH, WMTVA_BUTTON_XPATH)
                button.click()
            else:
                speak("The text was not found")
                print("Text not found")
                time.sleep(1)
                speak("How else may I be of service?")
                statement = takeCommand().lower()
            speak("These are the results of the counts search")

    if 'texts' in statement or 'text' in statement:
            TEXTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/legend/a'
            browser = driver
            button = browser.find_element(By.XPATH, TEXTS_BUTTON_XPATH)
            button.click()
            speak('The texts option is now open. What book are you searching for?')
            statement = takeCommand().lower()
            SEARCH6_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/div/input'
            browser = driver
            button = browser.find_element(By.XPATH, SEARCH6_BUTTON_XPATH)
            button.click()
            speak("The books are from Dickens Novels, 19th Century Reference Corpus, Children's Literature, "
                  "AddiCorpora optionstional Requested Texts and African American Writers ")
            statement = takeCommand().lower
            if "Bleak House" in statement or "Bleak House" in statement:
                XLOB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[2]'
                browser = driver
                button = browser.find_element(By.XPATH, XLOB_BUTTON_XPATH)
                button.click()
            elif "Barnaby Rudges" in statement:
                XBAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[3]'
                browser = driver
                button = browser.find_element(By.XPATH, XBAR_BUTTON_XPATH)
                button.click()
            elif "david copperfield" in statement:
                DACX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[4]'
                browser = driver
                button = browser.find_element(By.XPATH, DACX_BUTTON_XPATH)
                button.click()
            elif "Dombey and son" in statement:
                DOAXS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[5]'
                browser = driver
                button = browser.find_element(By.XPATH, DOAXS_BUTTON_XPATH)
                button.click()
            elif "The mystery of edwin drood" in statement:
                THMOXED_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[6]'
                browser = driver
                button = browser.find_element(By.XPATH, THMOXED_BUTTON_XPATH)
                button.click()
            elif "great expectationS" in statement:
                DREX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[7]'
                browser = driver
                button = browser.find_element(By.XPATH, DREX_BUTTON_XPATH)
                button.click()
            elif "hard times" in statement:
                XHAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[8]'
                browser = driver
                button = browser.find_element(By.XPATH, XHAT_BUTTON_XPATH)
                button.click()
            elif "little dorrit" in statement:
                XLID_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[9]'
                browser = driver
                button = browser.find_element(By.XPATH, XLID_BUTTON_XPATH)
                button.click()
            elif "martin chuzzlewit" in statement:
                MACX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[10]'
                browser = driver
                button = browser.find_element(By.XPATH, MACX_BUTTON_XPATH)
                button.click()
            elif "nicholas nickleby" in statement:
                NINX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[11]'
                browser = driver
                button = browser.find_element(By.XPATH, NINX_BUTTON_XPATH)
                button.click()
            elif "the old curiosity shop" in statement:
                TOCXS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[12]'
                browser = driver
                button = browser.find_element(By.XPATH, TOCXS_BUTTON_XPATH)
                button.click()
            elif "our mutual friend" in statement:
                XOUMF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[13]'
                browser = driver
                button = browser.find_element(By.XPATH, XOUMF_BUTTON_XPATH)
                button.click()
            elif "oliver twist" in statement:
                XOLT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[14]'
                browser = driver
                button = browser.find_element(By.XPATH, XOLT_BUTTON_XPATH)
                button.click()
            elif "pickwick papers" in statement:
                PIPX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[15]'
                browser = driver
                button = browser.find_element(By.XPATH, PIPX_BUTTON_XPATH)
                button.click()
            elif "a tale of two cities" in statement:
                ATAOTCX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[16]'
                browser = driver
                button = browser.find_element(By.XPATH, ATAOTCX_BUTTON_XPATH)
                button.click()
            elif "agnes grey" in statement:
                AGGX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[18]'
                browser = driver
                button = browser.find_element(By.XPATH, AGGX_BUTTON_XPATH)
                button.click()
            elif "the small house at Allington" in statement:
                THSHAAX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[19]'
                browser = driver
                button = browser.find_element(By.XPATH, THSHAAX_BUTTON_XPATH)
                button.click()
            elif "antonina or the fall of rome" in statement:
                ANOXTFOR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[20]'
                browser = driver
                button = browser.find_element(By.XPATH, ANOXTFOR_BUTTON_XPATH)
                button.click()
            elif "armadale" in statement:
                ARX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[21]'
                browser = driver
                button = browser.find_element(By.XPATH, ARX_BUTTON_XPATH)
                button.click()
            elif "the hound of the baskervilles" in statement:
                XTHHOTB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[22]'
                browser = driver
                button = browser.find_element(By.XPATH, XTHHOTB_BUTTON_XPATH)
                button.click()
            elif "cranford" in statement:
                CRX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[23]'
                browser = driver
                button = browser.find_element(By.XPATH, CRX_BUTTON_XPATH)
                button.click()
            elif "daniel deronda" in statement:
                DXAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[24]'
                browser = driver
                button = browser.find_element(By.XPATH, DXAD_BUTTON_XPATH)
                button.click()
            elif "the picture of dorian grey" in statement:
                THPXODG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[25]'
                browser = driver
                button = browser.find_element(By.XPATH, THPXODG_BUTTON_XPATH)
                button.click()
            elif "dracula" in statement:
                DRX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[26]'
                browser = driver
                button = browser.find_element(By.XPATH, DRX_BUTTON_XPATH)
                button.click()
            elif "emma" in statement:
                XEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[27]'
                browser = driver
                button = browser.find_element(By.XPATH, XEM_BUTTON_XPATH)
                button.click()
            elif "frankenstein" in statement:
                FRX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[28]'
                browser = driver
                button = browser.find_element(By.XPATH, FRX_BUTTON_XPATH)
                button.click()
            elif "jane eyre" in statement:
                JAEX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[29]'
                browser = driver
                button = browser.find_element(By.XPATH, JAEX_BUTTON_XPATH)
                button.click()
            elif "the strange case of doctor Jekyll and mister hyde" in statement:
                TASCXODJAMH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[30]'
                browser = driver
                button = browser.find_element(By.XPATH, TASCXODJAMH_BUTTON_XPATH)
                button.click()
            elif "jude the obscure" in statement:
                JATOX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[31]'
                browser = driver
                button = browser.find_element(By.XPATH, JATOX_BUTTON_XPATH)
                button.click()
            elif "lady audleys secret" in statement:
                LAAXS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[32]'
                browser = driver
                button = browser.find_element(By.XPATH, LAAXS_BUTTON_XPATH)
                button.click()
            elif "mary barton" in statement:
                MXBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[33]'
                browser = driver
                button = browser.find_element(By.XPATH, MXBA_BUTTON_XPATH)
                button.click()
            elif "the mill on the floss" in statement:
                TAMOXTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[34]'
                browser = driver
                button = browser.find_element(By.XPATH, TAMOXTF_BUTTON_XPATH)
                button.click()
            elif "the return of the native" in statement:
                TAROTXN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[35]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROTXN_BUTTON_XPATH)
                button.click()
            elif "north and south" in statement:
                NAASX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[36]'
                browser = driver
                button = browser.find_element(By.XPATH, NAASX_BUTTON_XPATH)
                button.click()
            elif "persuasion" in statement:
                PAX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[37]'
                browser = driver
                button = browser.find_element(By.XPATH, PAX_BUTTON_XPATH)
                button.click()
            elif "the last days of pompeii" in statement:
                TALDXOP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[38]'
                browser = driver
                button = browser.find_element(By.XPATH, TALDXOP_BUTTON_XPATH)
                button.click()
            elif "pride and prejudice" in statement:
                PXAAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[39]'
                browser = driver
                button = browser.find_element(By.XPATH, PXAAP_BUTTON_XPATH)
                button.click()
            elif "the professor" in statement:
                TAXP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[40]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXP_BUTTON_XPATH)
                button.click()
            elif "sybil or the two nations" in statement:
                SAOTXTN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[41]'
                browser = driver
                button = browser.find_element(By.XPATH, SAOTXTN_BUTTON_XPATH)
                button.click()
            elif "tess of the d'urbevilles" in statement:
                TAODXU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[42]'
                browser = driver
                button = browser.find_element(By.XPATH, TAODXU_BUTTON_XPATH)
                button.click()
            elif "vanity fair" in statement:
                XAPX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[43]'
                browser = driver
                button = browser.find_element(By.XPATH, XAPX_BUTTON_XPATH)
                button.click()
            elif "vivian grey" in statement:
                XAXG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[44]'
                browser = driver
                button = browser.find_element(By.XPATH, XAXG_BUTTON_XPATH)
                button.click()
            elif "wuthering heights" in statement:
                WXAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[45]'
                browser = driver
                button = browser.find_element(By.XPATH, WXAH_BUTTON_XPATH)
                button.click()
            elif "the woman in white" in statement:
                TAWXIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[46]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWXIW_BUTTON_XPATH)
                button.click()
            elif "alice's adventures in wonderland" in statement:
                AAAIXW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[48]'
                browser = driver
                button = browser.find_element(By.XPATH, AAAIXW_BUTTON_XPATH)
                button.click()
            elif "alone in london" in statement:
                AAXIL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[49]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXIL_BUTTON_XPATH)
                button.click()
            elif "the story of the amulet " in statement:
                TSXAOTA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[50]'
                browser = driver
                button = browser.find_element(By.XPATH, TSXAOTA_BUTTON_XPATH)
                button.click()
            elif "black beauty" in statement:
                XBAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[51]'
                browser = driver
                button = browser.find_element(By.XPATH, XBAB_BUTTON_XPATH)
                button.click()
            elif "the brass bottle" in statement:
                TABX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[52]'
                browser = driver
                button = browser.find_element(By.XPATH, TABX_BUTTON_XPATH)
                button.click()
            elif "the tale of benjamin bunny" in statement:
                TATOBBX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[53]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOBBX_BUTTON_XPATH)
                button.click()
            elif "the settlers in canada" in statement:
                TASXIC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[54]'
                browser = driver
                button = browser.find_element(By.XPATH, TASXIC_BUTTON_XPATH)
                button.click()
            elif "the  carved lions" in statement:
                TXACL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[55]'
                browser = driver
                button = browser.find_element(By.XPATH, TXACL_BUTTON_XPATH)
                button.click()
            elif "with clive in india" in statement:
                WAXCII_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[56]'
                browser = driver
                button = browser.find_element(By.XPATH, WAXCII_BUTTON_XPATH)
                button.click()
            elif "the coral island" in statement:
                TACXI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[57]'
                browser = driver
                button = browser.find_element(By.XPATH, TACXI_BUTTON_XPATH)
                button.click()
            elif "the crofton boys" in statement:
                TACXB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[58]'
                browser = driver
                button = browser.find_element(By.XPATH, TACXB_BUTTON_XPATH)
                button.click()
            elif "the cuckoo clock" in statement:
                TACXC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[59]'
                browser = driver
                button = browser.find_element(By.XPATH, TACXC_BUTTON_XPATH)
                button.click()
            elif "the daisy chain" in statement:
                TADCX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[60]'
                browser = driver
                button = browser.find_element(By.XPATH, TADCX_BUTTON_XPATH)
                button.click()
            elif "the fifth form at saint dominics" in statement:
                TAFFXASD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[61]'
                browser = driver
                button = browser.find_element(By.XPATH, TAFFXASD_BUTTON_XPATH)
                button.click()
            elif "the dove in the eagles nest" in statement:
                TADITXEN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[62]'
                browser = driver
                button = browser.find_element(By.XPATH, TADITXEN_BUTTON_XPATH)
                button.click()
            elif "the book of dragons" in statement:
                TAXOBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[63]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXOBD_BUTTON_XPATH)
                button.click()
            elif "dream days" in statement:
                DARXD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[64]'
                browser = driver
                button = browser.find_element(By.XPATH, DARXD_BUTTON_XPATH)
                button.click()
            elif "the little duke" in statement:
                TALXD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[65]'
                browser = driver
                button = browser.find_element(By.XPATH, TALXD_BUTTON_XPATH)
                button.click()
            elif "eric" in statement:
                XEAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[66]'
                browser = driver
                button = browser.find_element(By.XPATH, XEAR_BUTTON_XPATH)
                button.click()
            elif "feats on the fiord" in statement:
                FOAXTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[67]'
                browser = driver
                button = browser.find_element(By.XPATH, FOAXTF_BUTTON_XPATH)
                button.click()
            elif "five children and it" in statement:
                FACXAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[68]'
                browser = driver
                button = browser.find_element(By.XPATH, FACXAI_BUTTON_XPATH)
                button.click()
            elif "the tale of the flopsy bunnies" in statement:
                TXATOTFB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[69]'
                browser = driver
                button = browser.find_element(By.XPATH, TXATOTFB_BUTTON_XPATH)
                button.click()
            elif "the children of the new forest" in statement:
                TAXCOTNF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[70]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXCOTNF_BUTTON_XPATH)
                button.click()
            elif "a world of girls" in statement:
                AAXWOG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[71]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXWOG_BUTTON_XPATH)
                button.click()
            elif "through the looking glass" in statement:
                TAXTLG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[72]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXTLG_BUTTON_XPATH)
                button.click()
            elif "the golden age" in statement:
                TAGXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[73]'
                browser = driver
                button = browser.find_element(By.XPATH, TAGXA_BUTTON_XPATH)
                button.click()
            elif "holiday house" in statement:
                HXAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[74]'
                browser = driver
                button = browser.find_element(By.XPATH, HXAH_BUTTON_XPATH)
                button.click()
            elif "madam how and lady why" in statement:
                MBAXHALW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[75]'
                browser = driver
                button = browser.find_element(By.XPATH, MBAXHALW_BUTTON_XPATH)
                button.click()
            elif "jackanapes" in statement:
                JXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[76]'
                browser = driver
                button = browser.find_element(By.XPATH, JXA_BUTTON_XPATH)
                button.click()
            elif "the tale of jemima puddle duck" in statement:
                TATOXJP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[77]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOXJP_BUTTON_XPATH)
                button.click()
            elif "jessicas first prayer" in statement:
                JXAFP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[78]'
                browser = driver
                button = browser.find_element(By.XPATH, JXAFP_BUTTON_XPATH)
                button.click()
            elif "the jungle book" in statement:
                TAJXB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[79]'
                browser = driver
                button = browser.find_element(By.XPATH, TAJXB_BUTTON_XPATH)
                button.click()
            elif "kidnapped" in statement:
                XKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[80]'
                browser = driver
                button = browser.find_element(By.XPATH, XKA_BUTTON_XPATH)
                button.click()
            elif "leila at home" in statement:
                LAXAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[81]'
                browser = driver
                button = browser.find_element(By.XPATH, LAXAH_BUTTON_XPATH)
                button.click()
            elif "masterman ready" in statement:
                MXAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[82]'
                browser = driver
                button = browser.find_element(By.XPATH, MXAR_BUTTON_XPATH)
                button.click()
            elif "little meg's children" in statement:
                LAXMC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[83]'
                browser = driver
                button = browser.find_element(By.XPATH, LAXMC_BUTTON_XPATH)
                button.click()
            elif "the tale of two bad mice" in statement:
                TATOTXBM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[84]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOTXBM_BUTTON_XPATH)
                button.click()
            elif "moonfleet" in statement:
                MAXF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[85]'
                browser = driver
                button = browser.find_element(By.XPATH, MAXF_BUTTON_XPATH)
                button.click()
            elif "mopsa the fairy" in statement:
                MAXTF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[86]'
                browser = driver
                button = browser.find_element(By.XPATH, MAXTF_BUTTON_XPATH)
                button.click()
            elif "the three mulla-mulgars" in statement:
                TATXMM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[87]'
                browser = driver
                button = browser.find_element(By.XPATH, TATXMM_BUTTON_XPATH)
                button.click()
            elif "mrs. overtheways remembrances" in statement:
                MAORX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[88]'
                browser = driver
                button = browser.find_element(By.XPATH, MAORX_BUTTON_XPATH)
                button.click()
            elif "peter pan" in statement:
                PAEPXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[89]'
                browser = driver
                button = browser.find_element(By.XPATH, PAEPXA_BUTTON_XPATH)
                button.click()
            elif "the peasant and the prince" in statement:
                TAXPATP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[90]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXPATP_BUTTON_XPATH)
                button.click()
            elif "prince prigio" in statement:
                PAXRPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[91]'
                browser = driver
                button = browser.find_element(By.XPATH, PAXRPR_BUTTON_XPATH)
                button.click()
            elif "the happy prince" in statement:
                TAXHP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[92]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXHP_BUTTON_XPATH)
                button.click()
            elif "the princess and the goblin" in statement:
                THPX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[93]'
                browser = driver
                button = browser.find_element(By.XPATH, THPX_BUTTON_XPATH)
                button.click()
            elif "allan quatermain" in statement:
                AAXQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[94]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXQ_BUTTON_XPATH)
                button.click()
            elif "the tale of peter rabbit" in statement:
                TXATOPR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[95]'
                browser = driver
                button = browser.find_element(By.XPATH, TXATOPR_BUTTON_XPATH)
                button.click()
            elif "the railway children" in statement:
                TARXC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[96]'
                browser = driver
                button = browser.find_element(By.XPATH, TARXC_BUTTON_XPATH)
                button.click()
            elif "the heir of redclyffe" in statement:
                TAHOXR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[97]'
                browser = driver
                button = browser.find_element(By.XPATH, TAHOXR_BUTTON_XPATH)
                button.click()
            elif "the rival crusoes" in statement:
                TARXCR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[98]'
                browser = driver
                button = browser.find_element(By.XPATH, TARXCR_BUTTON_XPATH)
                button.click()
            elif "the rose and the ring" in statement:
                TXARATR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[99]'
                browser = driver
                button = browser.find_element(By.XPATH, TXARATR_BUTTON_XPATH)
                button.click()
            elif "the secret garden" in statement:
                TASXG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[100]'
                browser = driver
                button = browser.find_element(By.XPATH, TASXG_BUTTON_XPATH)
                button.click()
            elif "the story of the treasure seekers" in statement:
                TXASOTTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[101]'
                browser = driver
                button = browser.find_element(By.XPATH, TXASOTTS_BUTTON_XPATH)
                button.click()
            elif "the settlers at home" in statement:
                TASAXH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[102]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAXH_BUTTON_XPATH)
                button.click()
            elif "king solomons mines" in statement:
                KAXSM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[103]'
                browser = driver
                button = browser.find_element(By.XPATH, KAXSM_BUTTON_XPATH)
                button.click()
            elif "the tale of squirrel nutkin" in statement:
                TATOXSN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[104]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOXSN_BUTTON_XPATH)
                button.click()
            elif "stalky and co" in statement:
                SXAAC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[105]'
                browser = driver
                button = browser.find_element(By.XPATH, SXAAC_BUTTON_XPATH)
                button.click()
            elif "the king of the golden river or the black brothers" in statement or "the king of the golden river" in statement \
                    or "the black brothers" in statement:
                TAKOTXGROTXB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[106]'
                browser = driver
                button = browser.find_element(By.XPATH, TAKOTXGROTXB_BUTTON_XPATH)
                button.click()
            elif "the tapestry room" in statement:
                TAXTR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[107]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXTR_BUTTON_XPATH)
                button.click()
            elif "the surprising adventures of sir toady lion with those of general napolean smith" in statement:
                TASAOSTXLWTOGNS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[108]'
                browser = driver
                button = browser.find_element(By.XPATH, TASAOSTXLWTOGNS_BUTTON_XPATH)
                button.click()
            elif "tom brown's schooldays" in statement:
                TXABS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[109]'
                browser = driver
                button = browser.find_element(By.XPATH, TXABS_BUTTON_XPATH)
                button.click()
            elif "treasure island" in statement:
                TAIX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[110]'
                browser = driver
                button = browser.find_element(By.XPATH, TAIX_BUTTON_XPATH)
                button.click()
            elif "nine unlikely tales" in statement:
                XNAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[111]'
                browser = driver
                button = browser.find_element(By.XPATH, XNAUT_BUTTON_XPATH)
                button.click()
            elif "vise versa" in statement:
                XAXX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[112]'
                browser = driver
                button = browser.find_element(By.XPATH, XAXX_BUTTON_XPATH)
                button.click()
            elif "adventures in wallypug land" in statement:
                AAXIW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[113]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXIW_BUTTON_XPATH)
                button.click()
            elif "the water babies" in statement:
                TAXWB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[114]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXWB_BUTTON_XPATH)
                button.click()
            elif "the wind in the willows" in statement:
                TAWXITW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[115]'
                browser = driver
                button = browser.find_element(By.XPATH, TAWXITW_BUTTON_XPATH)
                button.click()
            elif "at the back of the north wind" in statement:
                ABATXOTNW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[116]'
                browser = driver
                button = browser.find_element(By.XPATH, ABATXOTNW_BUTTON_XPATH)
                button.click()
            elif "winning his spurs" in statement:
                WAXHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[117]'
                browser = driver
                button = browser.find_element(By.XPATH, WAXHS_BUTTON_XPATH)
                button.click()
            elif "wood magic" in statement:
                WAXM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[118]'
                browser = driver
                button = browser.find_element(By.XPATH, WAXM_BUTTON_XPATH)
                button.click()
            elif "american notes for general circulation" in statement:
                AAXNFGC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[120]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXNFGC_BUTTON_XPATH)
                button.click()
            elif "the awakening and several short stories" in statement:
                TAAAXSSS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[121]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAAXSSS_BUTTON_XPATH)
                button.click()
            elif "a christmas carol a ghost story of christmas" in statement or "a christmas carol" in statement \
                    or "a ghost story of christmas" in statement:
                AXACCAGSOC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[122]'
                browser = driver
                button = browser.find_element(By.XPATH, AXACCAGSOC_BUTTON_XPATH)
                button.click()
            elif "gullivers travels" in statement:
                AXGT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[123]'
                browser = driver
                button = browser.find_element(By.XPATH, AXGT_BUTTON_XPATH)
                button.click()
            elif "heart of darkness" in statement:
                HODXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[124]'
                browser = driver
                button = browser.find_element(By.XPATH, HODXA_BUTTON_XPATH)
                button.click()
            elif "adventures of huckleberry finn" in statement:
                AOHAXF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[125]'
                browser = driver
                button = browser.find_element(By.XPATH, AOHAXF_BUTTON_XPATH)
                button.click()
            elif "lady susan" in statement:
                LAXS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[126]'
                browser = driver
                button = browser.find_element(By.XPATH, LAXS_BUTTON_XPATH)
                button.click()
            elif "what maisie knew" in statement:
                WMAXK_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[127]'
                browser = driver
                button = browser.find_element(By.XPATH, WMAXK_BUTTON_XPATH)
                button.click()
            elif "mansfield park" in statement:
                MXAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[128]'
                browser = driver
                button = browser.find_element(By.XPATH, MXAP_BUTTON_XPATH)
                button.click()
            elif "middlemarch" in statement:
                XMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[129]'
                browser = driver
                button = browser.find_element(By.XPATH, XMA_BUTTON_XPATH)
                button.click()
            elif "the moonstone" in statement:
                TXAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[130]'
                browser = driver
                button = browser.find_element(By.XPATH, TXAM_BUTTON_XPATH)
                button.click()
            elif "northanger abbey" in statement:
                XNAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[131]'
                browser = driver
                button = browser.find_element(By.XPATH, XNAA_BUTTON_XPATH)
                button.click()
            elif "pictures from italy" in statement:
                XPAFI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[132]'
                browser = driver
                button = browser.find_element(By.XPATH, XPAFI_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 1" in statement:
                XPAOALO_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[133]'
                browser = driver
                button = browser.find_element(By.XPATH, XPAOALO_BUTTON_XPATH)
                button.click()
            elif "portrait of a lady volume 2" in statement:
                XPAOALT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[134]'
                browser = driver
                button = browser.find_element(By.XPATH, XPAOALT_BUTTON_XPATH)
                button.click()
            elif "a room with a view" in statement:
                ARXAWAX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[135]'
                browser = driver
                button = browser.find_element(By.XPATH, ARXAWAX_BUTTON_XPATH)
                button.click()
            elif "sense and sensibility" in statement:
                SAAXS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[136]'
                browser = driver
                button = browser.find_element(By.XPATH, SAAXS_BUTTON_XPATH)
                button.click()
            elif "shirley" in statement:
                XSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[137]'
                browser = driver
                button = browser.find_element(By.XPATH, XSA_BUTTON_XPATH)
                button.click()
            elif "the sign of four" in statement:
                TSAOXF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[138]'
                browser = driver
                button = browser.find_element(By.XPATH, TSAOXF_BUTTON_XPATH)
                button.click()
            elif "silas marner" in statement:
                SAXM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[139]'
                browser = driver
                button = browser.find_element(By.XPATH, SAXM_BUTTON_XPATH)
                button.click()
            elif "the return of the soldier" in statement:
                TAROXTS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[141]'
                browser = driver
                button = browser.find_element(By.XPATH, TAROXTS_BUTTON_XPATH)
                button.click()
            elif "the tenant of wildfell hall" in statement:
                TATOXWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[142]'
                browser = driver
                button = browser.find_element(By.XPATH, TATOXWH_BUTTON_XPATH)
                button.click()
            elif "the jungle" in statement:
                XTAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[143]'
                browser = driver
                button = browser.find_element(By.XPATH, XTAJ_BUTTON_XPATH)
                button.click()
            elif "the time machine" in statement:
                TXATM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[144]'
                browser = driver
                button = browser.find_element(By.XPATH, TXATM_BUTTON_XPATH)
                button.click()
            elif "twelve years a slave" in statement:
                XTXAAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[145]'
                browser = driver
                button = browser.find_element(By.XPATH, XTXAAS_BUTTON_XPATH)
                button.click()
            elif "the uncommercial traveller" in statement:
                XTAUT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[146]'
                browser = driver
                button = browser.find_element(By.XPATH, XTAUT_BUTTON_XPATH)
                button.click()
            elif "vilette" in statement:
                XXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[147]'
                browser = driver
                button = browser.find_element(By.XPATH, XXA_BUTTON_XPATH)
                button.click()
            elif "the war of worlds" in statement:
                TXAWOW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[148]'
                browser = driver
                button = browser.find_element(By.XPATH, TXAWOW_BUTTON_XPATH)
                button.click()
            elif "women in love" in statement:
                WIAXL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[149]'
                browser = driver
                button = browser.find_element(By.XPATH, WIAXL_BUTTON_XPATH)
                button.click()
            elif "the yellow wallpaper" in statement:
                TXAXW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[150]'
                browser = driver
                button = browser.find_element(By.XPATH, TXAXW_BUTTON_XPATH)
                button.click()
            elif "the house behind the cedars" in statement:
                THAXBTC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[152]'
                browser = driver
                button = browser.find_element(By.XPATH, THAXBTC_BUTTON_XPATH)
                button.click()
            elif "the colonel's dream" in statement:
                TCXAD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[153]'
                browser = driver
                button = browser.find_element(By.XPATH, TCXAD_BUTTON_XPATH)
                button.click()
            elif "the autobiography of an ex-coloured man" in statement:
                TAAXOAEM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[154]]'
                browser = driver
                button = browser.find_element(By.XPATH, TAAXOAEM_BUTTON_XPATH)
                button.click()
            elif "imperium in imperio" in statement:
                IXIAI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[155]'
                browser = driver
                button = browser.find_element(By.XPATH, IXIAI_BUTTON_XPATH)
                button.click()
            elif "iola leroy or shadows uplifted" in statement or "shadows uplifted" in statement \
                    or "iola leroy" in statement:
                ILOSXAU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[156]'
                browser = driver
                button = browser.find_element(By.XPATH, ILOSXAU_BUTTON_XPATH)
                button.click()
            elif "the marrow of tradition" in statement:
                TMOXAT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[157]'
                browser = driver
                button = browser.find_element(By.XPATH, TMOXAT_BUTTON_XPATH)
                button.click()
            elif "the sport of the gods" in statement:
                TSOXTAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[158]'
                browser = driver
                button = browser.find_element(By.XPATH, TSOXTAG_BUTTON_XPATH)
                button.click()
            elif "unfettered" in statement:
                XUA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[159]'
                browser = driver
                button = browser.find_element(By.XPATH, XUA_BUTTON_XPATH)
                button.click()
            elif "agnes strickland" in statement:
                AXSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[161]'
                browser = driver
                button = browser.find_element(By.XPATH, AXSA_BUTTON_XPATH)
                button.click()
            elif "andrew lang" in statement:
                AAXL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[162]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXL_BUTTON_XPATH)
                button.click()
            elif "ann fraser tytler" in statement:
                AAXFT_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[163]'
                browser = driver
                button = browser.find_element(By.XPATH, AAXFT_BUTTON_XPATH)
                button.click()
            elif "anna sewell" in statement:
                AXASE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[164]'
                browser = driver
                button = browser.find_element(By.XPATH, AXASE_BUTTON_XPATH)
                button.click()
            elif "anne bronte" in statement:
                AXAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[165]'
                browser = driver
                button = browser.find_element(By.XPATH, AXAB_BUTTON_XPATH)
                button.click()
            elif "anthony trollope" in statement:
                AXTAR_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[166]'
                browser = driver
                button = browser.find_element(By.XPATH, AXTAR_BUTTON_XPATH)
                button.click()
            elif "arthur conan doyle" in statement:
                XAACD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[167]'
                browser = driver
                button = browser.find_element(By.XPATH, XAACD_BUTTON_XPATH)
                button.click()
            elif "baron edward bulwer lytton lytton" in statement:
                XAEBBLL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[168]'
                browser = driver
                button = browser.find_element(By.XPATH, XAEBBLL_BUTTON_XPATH)
                button.click()
            elif "beatrix potter" in statement:
                XAPB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[169]'
                browser = driver
                button = browser.find_element(By.XPATH, XAPB_BUTTON_XPATH)
                button.click()
            elif "bram stoker" in statement:
                XBAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[170]'
                browser = driver
                button = browser.find_element(By.XPATH, XBAS_BUTTON_XPATH)
                button.click()
            elif "captain frederick marryat" in statement:
                CFXAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[171]'
                browser = driver
                button = browser.find_element(By.XPATH, CFXAM_BUTTON_XPATH)
                button.click()
            elif "catherine sinclair" in statement:
                CASX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[172]'
                browser = driver
                button = browser.find_element(By.XPATH, CASX_BUTTON_XPATH)
                button.click()
            elif "charles dickens" in statement:
                CADX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[173]'
                browser = driver
                button = browser.find_element(By.XPATH, CADX_BUTTON_XPATH)
                button.click()
            elif "charles kinglsey" in statement:
                CAKX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[174]'
                browser = driver
                button = browser.find_element(By.XPATH, CAKX_BUTTON_XPATH)
                button.click()
            elif "charles W. chestnutt" in statement:
                CAWXC_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[175]'
                browser = driver
                button = browser.find_element(By.XPATH, CAWXC_BUTTON_XPATH)
                button.click()
            elif "charlotte bronte" in statement:
                CXAB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[176]'
                browser = driver
                button = browser.find_element(By.XPATH, CXAB_BUTTON_XPATH)
                button.click()
            elif "charlotte M. yonge" in statement:
                CMAXX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[177]'
                browser = driver
                button = browser.find_element(By.XPATH, CMAXX_BUTTON_XPATH)
                button.click()
            elif "charlotte perkins gilman" in statement:
                CXPAG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[178]'
                browser = driver
                button = browser.find_element(By.XPATH, CXPAG_BUTTON_XPATH)
                button.click()
            elif "D. H. lawrence" in statement:
                DHAXL_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[179]'
                browser = driver
                button = browser.find_element(By.XPATH, DHAXL_BUTTON_XPATH)
                button.click()
            elif "E. M. forster" in statement:
                EMXAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[180]'
                browser = driver
                button = browser.find_element(By.XPATH, EMXAF_BUTTON_XPATH)
                button.click()
            elif "E. Nesbit" in statement:
                EXAN_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[181]'
                browser = driver
                button = browser.find_element(By.XPATH, EXAN_BUTTON_XPATH)
                button.click()
            elif "earl of beaconsfield benjamin disraeli" in statement:
                EAOXBBD_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[182]'
                browser = driver
                button = browser.find_element(By.XPATH, EAOXBBD_BUTTON_XPATH)
                button.click()
            elif "eliXabeth cleghorn gaskell" in statement:
                EXACG_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[183]'
                browser = driver
                button = browser.find_element(By.XPATH, EXACG_BUTTON_XPATH)
                button.click()
            elif "emily bronte" in statement:
                EAXB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[184]'
                browser = driver
                button = browser.find_element(By.XPATH, EAXB_BUTTON_XPATH)
                button.click()
            elif "F. anstey" in statement:
                FAXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[185]'
                browser = driver
                button = browser.find_element(By.XPATH, FAXA_BUTTON_XPATH)
                button.click()
            elif "frances E. W. harper" in statement:
                FAEXWH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[186]'
                browser = driver
                button = browser.find_element(By.XPATH, FAEXWH_BUTTON_XPATH)
                button.click()
            elif "francis hodgson burnett" in statement:
                FHAXB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[187]'
                browser = driver
                browser.find_element(By.XPATH, FHAXB_BUTTON_XPATH)
                button.click()
            elif "Frederic william farrar" in statement:
                FAXWF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[188]'
                browser = driver
                browser.find_element(By.XPATH, FAXWF_BUTTON_XPATH)
                button.click()
            elif "G.A. Henty" in statement:
                GAAXH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[189]'
                browser = driver
                button = browser.find_element(By.XPATH,GAAXH_BUTTON_XPATH)
                button.click()
            elif "G.E.Farrow" in statement:
                GEXAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[190]'
                browser = driver
                button = browser.find_element(By.XPATH, GEXAF_BUTTON_XPATH)
                button.click()
            elif "George Eliot" in statement:
                GXAE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[191]'
                browser = driver
                button = browser.find_element(By.XPATH, GXAE_BUTTON_XPATH)
                button.click()
            elif "Geroge Macdonald" in statement:
                AXGM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[192]'
                browser = driver
                button = browser.find_element(By.XPATH, AXGM_BUTTON_XPATH)
                button.click()
            elif "H. G Wells" in statement:
                HXGAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[193]'
                browser = driver
                button = browser.find_element(By.XPATH, HXGAW_BUTTON_XPATH)
                button.click()
            elif "H. Rider Haggard" in statement:
                HRXAH_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[194]'
                browser = driver
                button = browser.find_element(By.XPATH, HRXAH_BUTTON_XPATH)
                button.click()
            elif "Harriet Martineau" in statement:
                HAXM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[195]'
                browser = driver
                button = browser.find_element(By.XPATH, HAXM_BUTTON_XPATH)
                button.click()
            elif "Henry James" in statement:
                HAXJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[196]'
                browser = driver
                button = browser.find_element(By.XPATH, HAXJ_BUTTON_XPATH)
                button.click()
            elif "Hesba Stretton" in statement:
                HXAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[197]'
                browser = driver
                button = browser.find_element(By.XPATH, HXAS_BUTTON_XPATH)
                button.click()
            elif "J. Meade Falkner" in statement:
                JMXAF_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[198]'
                browser = driver
                button = browser.find_element(By.XPATH, JMXAF_BUTTON_XPATH)
                button.click()
            elif "James M. Barrie" in statement:
                JMXB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[199]'
                browser = driver
                button = browser.find_element(By.XPATH, JMXB_BUTTON_XPATH)
                button.click()
            elif "James Weldon Johnson" in statement:
                JWXAJ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[200]'
                browser = driver
                button = browser.find_element(By.XPATH, JWXAJ_BUTTON_XPATH)
                button.click()
            elif "Jane Austen" in statement:
                JXAA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[201]'
                browser = driver
                button = browser.find_element(By.XPATH, JXAA_BUTTON_XPATH)
                button.click()
            elif "Jean Ingelow" in statement:
                JAXI_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[202]'
                browser = driver
                button = browser.find_element(By.XPATH, JAXI_BUTTON_XPATH)
                button.click()
            elif "Jonathan Ruskin" in statement:
                JXRA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[203]'
                browser = driver
                button = browser.find_element(By.XPATH, JXRA_BUTTON_XPATH)
                button.click()
            elif "Jonathan Swift" in statement:
                JSAX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[204]'
                browser = driver
                button = browser.find_element(By.XPATH, JSAX_BUTTON_XPATH)
                button.click()
            elif "Joseph Conrad" in statement:
                JCXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[205]'
                browser = driver
                button = browser.find_element(By.XPATH, JCXA_BUTTON_XPATH)
                button.click()
            elif "Juliana Horatia Ewing" in statement:
                JHAXE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[206]'
                browser = driver
                button = browser.find_element(By.XPATH, JHAXE_BUTTON_XPATH)
                button.click()
            elif "Kate Chopin" in statement:
                KCXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[207]'
                browser = driver
                button = browser.find_element(By.XPATH, KCXA_BUTTON_XPATH)
                button.click()
            elif "Kenneth Grahame" in statement:
                KGXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[208]'
                browser = driver
                button = browser.find_element(By.XPATH, KGXA_BUTTON_XPATH)
                button.click()
            elif "L.T. Meade" in statement:
                LTXMA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[209]'
                browser = driver
                button = browser.find_element(By.XPATH, LTXMA_BUTTON_XPATH)
                button.click()
            elif "lewis carroll" in statement:
                LCAX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[210]'
                browser = driver
                button = browser.find_element(By.XPATH, LCAX_BUTTON_XPATH)
                button.click()
            elif "M. E Braddon" in statement:
                MEXBA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[211]'
                browser = driver
                button = browser.find_element(By.XPATH, MEXBA_BUTTON_XPATH)
                button.click()
            elif "mark twain" in statement:
                MTXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[212]'
                browser = driver
                button = browser.find_element(By.XPATH, MTXA_BUTTON_XPATH)
                button.click()
            elif "mary wollstonecraft shelley" in statement:
                MWXSA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[213]'
                browser = driver
                button = browser.find_element(By.XPATH, MWXSA_BUTTON_XPATH)
                button.click()
            elif "Mrs. Molesworth" in statement:
                MMXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[214]'
                browser = driver
                button = browser.find_element(By.XPATH, MMXA_BUTTON_XPATH)
                button.click()
            elif "oscar wilde" in statement:
                OXWA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[215]'
                browser = driver
                button = browser.find_element(By.XPATH, OXWA_BUTTON_XPATH)
                button.click()
            elif "paul laurence dunbar" in statement:
                PLXDA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[216]'
                browser = driver
                button = browser.find_element(By.XPATH, PLXDA_BUTTON_XPATH)
                button.click()
            elif "R. M Ballantyne" in statement:
                RAXMB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[217]'
                browser = driver
                button = browser.find_element(By.XPATH, RAXMB_BUTTON_XPATH)
                button.click()
            elif "Rebecca West" in statement:
                RXAW_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[218]'
                browser = driver
                button = browser.find_element(By.XPATH, RXAW_BUTTON_XPATH)
                button.click()
            elif "Richard Jefferies" in statement:
                RJXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[219]'
                browser = driver
                button = browser.find_element(By.XPATH, RJXA_BUTTON_XPATH)
                button.click()
            elif "Robert Louis Stevenson" in statement:
                RLXAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[220]'
                browser = driver
                button = browser.find_element(By.XPATH, RLXAS_BUTTON_XPATH)
                button.click()
            elif "rudyard kipling" in statement:
                RXKA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[221]'
                browser = driver
                button = browser.find_element(By.XPATH, RXKA_BUTTON_XPATH)
                button.click()
            elif "S. R Crockett" in statement:
                SRXCA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[222]'
                browser = driver
                button = browser.find_element(By.XPATH, SRXCA_BUTTON_XPATH)
                button.click()
            elif "solomon northrup" in statement:
                SNXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[223]'
                browser = driver
                button = browser.find_element(By.XPATH, SNXA_BUTTON_XPATH)
                button.click()
            elif "sutton E Griggs" in statement:
                SEGXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[224]'
                browser = driver
                button = browser.find_element(By.XPATH, SEGXA_BUTTON_XPATH)
                button.click()
            elif "talbot baines reed" in statement:
                TXARB_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[225]'
                browser = driver
                button = browser.find_element(By.XPATH, TXARB_BUTTON_XPATH)
                button.click()
            elif "thomas hardy" in statement:
                TAXHA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[226]'
                browser = driver
                button = browser.find_element(By.XPATH, TAXHA_BUTTON_XPATH)
                button.click()
            elif "thomas hughes" in statement:
                THAX_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[227]'
                browser = driver
                button = browser.find_element(By.XPATH, THAX_BUTTON_XPATH)
                button.click()
            elif "upton sinclair" in statement:
                UXAS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[228]'
                browser = driver
                button = browser.find_element(By.XPATH, UXAS_BUTTON_XPATH)
                button.click()
            elif "walter de la mare" in statement:
                WXDLAM_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[229]'
                browser = driver
                button = browser.find_element(By.XPATH, WXDLAM_BUTTON_XPATH)
                button.click()
            elif "wilkie collins" in statement:
                WCXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[230]'
                browser = driver
                button = browser.find_element(By.XPATH, WCXA_BUTTON_XPATH)
                button.click()
            elif "william makepeace thackeray" in statement:
                WMTXA_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[1]/div/ul/li[231]'
                browser = driver
                button = browser.find_element(By.XPATH, WMTXA_BUTTON_XPATH)
                button.click()
            else:
                speak("The text was not found")
                print("Text not found")
                time.sleep(1)
                speak("How else may I be of service?")
                statement = takeCommand().lower()
            speak("would you like to choose a specific chapter?")
            CHAP_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/div[2]/div/div/input'
            browser = driver
            button = browser.find_element(By.XPATH, CHAP_BUTTON_XPATH)
            button.click()
            speak("Please scroll and select the chapter you want to read")

            speak("do you want to highlight any subsets? That is, do you want to highlight any sentences, quotes"
                  "short suspensions, long suspensions or embedded quotes?")
            statement = takeCommand().lower()
            if 'yes' in statement:
                speak("which subsets do you wish to choose?")
                statement = takeCommand().lower()
                if 'sentences' in statement:
                    SE_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/label[3]/input'
                    browser = driver
                    button = browser.find_element(By.XPATH, SE_BUTTON_XPATH)
                    button.click()
                if 'quotes' in statement:
                    QU_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/label[4]/input'
                    browser = driver
                    button = browser.find_element(By.XPATH, QU_BUTTON_XPATH)
                    button.click()
                if 'short suspensions' in statement:
                    SHS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/label[5]/input'
                    browser = driver
                    button = browser.find_element(By.XPATH, SHS_BUTTON_XPATH)
                    button.click()
                if 'long suspensions' in statement:
                    LOS_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/label[6]/input'
                    browser = driver
                    button = browser.find_element(By.XPATH, LOS_BUTTON_XPATH)
                    button.click()
                if 'embedded quotes' in statement:
                    EQ_BUTTON_XPATH = '//*[@id="control-bar"]/div/fieldset[6]/form/label[7]/input'
                    browser = driver
                    button = browser.find_element(By.XPATH, EQ_BUTTON_XPATH)
                    button.click()
                speak("here are the results")
            else:
                speak("here are the results")


time.sleep(3)