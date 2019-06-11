import sys
import datetime
from datetime import timedelta
from datetime import date
import Speech_to_text
import Text_to_speech
from lunardate import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
keywords = ["today", "lunar", "yesterday", "tomorrow", "month", "year", "time", "hour", "capital", "country", "until"]

countries = {
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Bangladesh": "Dhaka",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Brazil": "Brasilia",
    "Brunei": "Bandar Seri Begawan",
    "Bulgaria": "Sofia",
    "Cambodia": "Phnom Penh",
    "Canada": "Ottawa",
    "Chile": "Santiago",
    "China": "Beijing",
    "Colombia": "Bogota",
    "Costa Rica": "San Jose",
    "Croatia": "Zagreb",
    "Cuba": "Havana",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "Ecuador": "Quito",
    "Egypt": "Cairo",
    "Ethiopia": "Addis Ababa",
    "Finland": "Helsinki",
    "France": "Paris",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Haiti": "Port-au-Prince",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Ireland": "Dublin",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Jamaica": "Kingston",
    "Japan": "Tokyo",
    "Kazakhstan": "Astana",
    "North Korea": "Pyongyang",
    "South Korea": "Seoul",
    "Laos": "Vientiane",
    "Malaysia": "Kuala Lumpur",
    "Mexico": "Mexico City",
    "Monaco": "Monaco",
    "Mozambique": "Maputo",
    "Myanmar": "Yangon",
    "Nepal": "Kathmandu",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "Pakistan": "Islamabad",
    "Panama": "Panama City",
    "Papua New Guinea": "Port Moresby",
    "Paraguay": "Asuncion",
    "Peru": "Lima",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Qatar": "Doha",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "Serbia": "Belgrade",
    "Singapore": "Singapore",
    "Slovakia": "Bratislava",
    "South Africa": "Pretoria",
    "Spain": "Madrid",
    "Sri Lanka": "Colombo",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "Uganda": "Kampala",
    "Ukraine": "Kyiv",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States of America": "Washington, D.C.",
    "Uruguay": "Montevideo",
    "Uzbekistan": "Tashkent",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Zimbabwe": "Harare"
}

events_solar = {
    "Christmas holiday": (24, 5),
    "New Year": (1, 1),
    "Valentine's day": (14, 2),
    "Halloween": (31, 10),
    "May Day": (1, 5),
    "Women's day": (8, 3),
    "Teacher's day": (20, 11),
    "Vietnamese Women's day": (20, 10),
    "Vietnam's Liberation day": (30, 4),
    "Vietnam's National Day": (2, 9)
}

events_lunar = {
    "Lunar New Year": (1, 1),
    "Hung Kings' Commemoration Day": (10, 3),
    "Moon Festival": (15, 8),
    "Shangsi Festival": (3,3),
    "Duanwu Festival": (5, 5),
}

answer = "No answer"
ask = ""
type = 0
class App(QWidget):

    global answer
    global ask
    def __init__(self):
        super().__init__()
        self.title = 'Man Minh Thao - 16020282'
        self.left = 500
        self.top = 100
        self.width = 440
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Title
        self.label = QLabel("<strong style='font-size:25px'>Ask and answer with voice</strong>", self)
        self.label.move(50, 20)

        self.category = QLabel("<strong style='font-size:15px'>Category:</strong>\n" +
                               "<ul>- Date and time (Solar and Lunar)\n</ul>" +
                               "<ul>- Holidays and countdown (Solar and Lunar)</ul>\n" +
                               "<ul>- Countries and its Capital</ul>", self)
        self.category.move(60, 60)

        button = QPushButton("Start record", self)
        button.move(190, 160)
        button.clicked.connect(self.onClick)

        self.question = QLabel("<font color='grey' style='font-size:17px'>Your answer goes here...</font>", self)
        self.question.move(60, 230)

        self.textbox = QLineEdit(self)
        self.textbox.move(60, 190)
        self.textbox.resize(280,40)

        self.buttontext = QPushButton("Run ", self)
        self.buttontext.move(340, 200)
        self.buttontext.clicked.connect(self.onClick2)

        self.again = QPushButton("Again?", self)
        self.again.move(190, 260)
        self.again.clicked.connect(self.onClick3)
        self.again.setVisible(0)

        self.show()

    @pyqtSlot()
    def onClick(self):
        asking = askWvoice()
        answer = script(asking)
        self.textbox.setText(asking)
        self.question.setText(answer)
        Text_to_speech.tts(answer)
        self.again.setVisible(1)
        Text_to_speech.tts("again?")

    def onClick2(self):
        ask = self.textbox.text()
        answer = script(ask)
        self.question.setText(answer)
        Text_to_speech.tts(answer)
        self.again.setVisible(1)
        Text_to_speech.tts("again?")

    def onClick3(self):
        self.textbox.setText("")
        self.question.setText("<font color='grey' style='font-size:17px'>Your answer goes here...</font>")
        self.again.setVisible(0)


def askWvoice():
    print("say something")
    ask = str(Speech_to_text.stt())
    print(ask)
    return ask


def script(ask_):
    print(ask_)
    data = ask_.split()
    keys = ""
    for i in keywords:
        for j in data:
            if i == j:
                keys = i
                break
    currtime = datetime.datetime.now()
    print(keys)
    answer = "No answer"
    def date_form(time):
        return time.strftime("%A") + ", " + time.strftime("%d") + " of " + time.strftime("%B") + ", " + time.strftime("%Y")

    if keys == 'today':
        time = currtime
        answer = "Today is " + date_form(time)
    elif keys == 'yesterday':
        time = currtime - timedelta(days=1)
        answer = "Yesterday is " + date_form(time)
    elif keys == 'tomorrow':
        time = currtime + timedelta(days=1)
        answer = "Tomorrow is " + date_form(time)
    elif keys == 'lunar':
        lunarday = datetime.datetime(LunarDate.today().year, LunarDate.today().month, LunarDate.today().day)
        answer = date_form(lunarday)
    elif keys == 'month':
        answer = "This month is " + currtime.strftime("%B")
    elif keys == 'year':
        answer = "This year is " + currtime.strftime("%Y")
    elif keys == 'time':
        answer = currtime.strftime("%X")
    elif keys == 'hour':
        answer = currtime.strftime("%H")
    elif keys == 'until':
        flag = 0
        # for i in data:
        for x,y in events_solar.items():
            if ask_.find(x) != -1:
                event = x
                print(x)
                flag = 1
                if y[1] <= currtime.month:
                    if y[0] <= currtime.day:
                        eventyear = currtime.year + 1
                else:
                    eventyear = currtime.year
                print("Year = " + str(eventyear))
                eventday = date(eventyear, y[1], y[0])
                today = date(currtime.year, currtime.month, currtime.day)
                distance = eventday - today
                answer = str(distance.days) + " days left before the next " + str(x)
                break
        for x,y in events_lunar.items():
            if ask_.find(x) != -1:
                event = x
                flag = 1
                if y[1] <= LunarDate.today().month:
                    if y[0] <= LunarDate.today().day:
                        eventyear = LunarDate.today().year + 1
                else:
                    eventyear = LunarDate.today().year
                eventday = LunarDate(eventyear, y[1], y[0])
                today = date(currtime.year, currtime.month, currtime.day)
                distance = eventday - today
                answer = str(distance.days) + " days left before the next " + str(x)
        if flag == 0:
            answer = "The event's name is not available"
    elif keys == 'capital' or keys == 'country':
        flag = 0
        for i in data:
            for x,y in countries.items():
                if i == x:
                    country = i
                    answer = "The capital of " + country + " is " + y
                    flag = 1
                    break
                if i == y:
                    capital = i
                    answer = capital + " is the capital of " + x
                    flag = 1
                    break
        if flag == 0:
            answer = "There is no Capital or Country has this name"
    else:
        for x,y in events_solar.items():
            if ask_.find(x) != -1:
                event = x
                flag = 1
                if y[1] <= currtime.month:
                    if y[0] <= currtime.day:
                        eventyear = currtime.year + 1
                else:
                    eventyear = currtime.year
                eventday = datetime.datetime(eventyear, y[1], y[0])
                answer = "The next " + str(x) + " is occurring in " + date_form(eventday)
                break
        for x,y in events_lunar.items():
            if ask_.find(x) != -1:
                event = x
                flag = 1
                if y[1] <= LunarDate.today().month:
                    if y[0] <= LunarDate.today().day:
                        eventyear = LunarDate.today().year + 1
                else:
                    eventyear = LunarDate.today().year
                eventday = LunarDate(eventyear, y[1], y[0]).toSolarDate()
                answer = "The next " + str(x) + " is occurring in " + date_form(eventday)
        if flag == 0:
            answer = "The event's name is not available"

    print(answer)
    return answer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
