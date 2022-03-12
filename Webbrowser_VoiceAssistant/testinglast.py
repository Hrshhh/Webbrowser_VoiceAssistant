import sys
import mss
import mss.tools
from PyQt5.QtGui import *
from datetime import datetime
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import smtplib
import webbrowser

class voiceassist(QWidget):
    def __init__(self):
        super(voiceassist,self).__init__()
        self.setGeometry(100, 60, 650, 500)
  
        # creating a label to display a name
        #label = QLabel(self)
        #label.setStyleSheet("background-image : url(voiceicon.png);background-repeat : no-repeat;background-position : center;")
        #label.resize(320,400)

        chhBtn = QPushButton(self)
        chhBtn.setIcon(QIcon('voiceicon.png'))
        chhBtn.clicked.connect(self.ch)

        # creating text box to display text
        text1 = QTextEdit(self)
        text1.move(320,30)
        text1.resize(310, 450)
        
        
       
    def ch(self):
        engine = pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        print(voices[0].id)
        engine.setProperty('voice',voices[0].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-40)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        def wishMe():
            hour=int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak('Good Morning!')
            elif hour>=12 and hour<18:
                speak("Good Afternoon!")
            else:
                speak('Good Evevning')
            speak('I am Your Voice Assistant, please tell me how may I help You!')
        def takeCommand(): #it takes microphone input from the user and return string output
            r=sr.Recognizer()
            with sr.Microphone() as source: # use the default microphone as the audio source
                print("Listening....")
                r.pause_threshold=0.5
                audio=r.listen(source) # listen for the first phrase and extract it into audio data
            try:
                print("Recognising...")
                query=r.recognize_google(audio, language='en-in')
                print(f"User Said: {query}\n")
            except Exception as e:
                print(e)
                print("I can't Listen Please Say That Again.....")
                return "None"
            return query
        def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login('shaikhruhullah@gmail.com', '********')
            server.sendmail('ruhullah@gmail.com',to, content)
            server.close()
        if __name__=='__main__':
            wishMe()
            while True:
            #if 1:
                query = takeCommand().lower() #Logic for executing task
                if 'wikipedia' in query:
                    speak('Searching Wikipedia....')
                    query=query.replace("wikipedia","")
                    result=wikipedia.summary(query,sentences=5)
                    speak("According to Wikipedia")
                    print(result)
                    speak(result)
         
                elif 'youtube' in query:
                    urll = 'https://www.youtube.com/'
                    chrome = webbrowser.Chrome(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    chrome.open(urll)
                elif 'google' in query:
                    webbrowser.open("google.com")
                elif 'rizvi' in query:
                    webbrowser.open("https://eng.rizvi.edu.in/")
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                    speak(f"Sir, the time is {strTime}")
                    print(strTime)
                elif 'date' in query:
                    strDate=datetime.date.today()
                    print(strDate.day,strDate.month,strDate.year)
                    speak("today date is {strDate}")
                    print(strDate)
                #elif 'open notepad' in query:
                    #codePath = "‪C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
                    #os.startfile(codePath)
                #elif 'play music' in query:
                    #music_dir = '‪C:\\Users\\KhanFaiz\\Music'
                    #songs = os.listdir(music_dir)
                    #print(songs) 
                   # os.startfile(os.path.join(music_dir, songs[0]))
                elif 'send email' in query:
                    try:
                        print('What conversation you want to say Please tell me?')
                        speak("What conversation you want to say Please tell me?")
                        content = takeCommand()
                        to="ruhullah@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")
                        print("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend. I am not able to send this email")
                elif "college name" in query:
                        speak('Rizvi college of engineering')
                        print('Rizvi college of engineering')
                elif "band ho ja" in query:
                        sys.exit(0)
                elif 'your name' in query:
                        speak('Voice Assistant')
                        print("Voice Assistant")
                elif 'how are you' in query:
                        speak("I am fine. What about yourself?")
                        print("I am fine. What about yourself?")

class Webbrowser(QMainWindow):
	def __init__(self):
		super(Webbrowser,self).__init__()

		# for web browser
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()
		self.browser.urlChanged.connect(self.updateUrl)
		# adding navigation bar
		tools1 = QToolBar()
		self.addToolBar(tools1)
		# Creating Buttons 

		# Back button 
		backBtn = QAction('Back',self)
		backBtn.setIcon(QIcon('back.jpg'))
		backBtn.triggered.connect(self.browser.back)
		tools1.addAction(backBtn)

		# forward button
		forwardBtn = QAction('Forward',self)
		forwardBtn.setIcon(QIcon('forward.jpg'))
		forwardBtn.triggered.connect(self.browser.forward)
		tools1.addAction(forwardBtn)

		# Reload button 
		reloadBtn = QAction('Reload',self)
		reloadBtn.setIcon(QIcon('refresh - Copy.jpg'))
		reloadBtn.triggered.connect(self.browser.reload)
		tools1.addAction(reloadBtn)

		# Home Button 
		homeBtn = QAction('Home',self)
		homeBtn.setIcon(QIcon('home.jpg'))
		homeBtn.triggered.connect(self.home)
		tools1.addAction(homeBtn)

		# Search engine 
		self.searchBar = QLineEdit(self)
		self.searchBar.setFont(QFont("Italian",18))
		self.searchBar.returnPressed.connect(self.loadUrl)
		tools1.addWidget(self.searchBar)

		# Screenshot Button 
		ssBtn = QAction('Screenshot',self)
		ssBtn.setIcon(QIcon('screenshot - Copy.jpg'))
		ssBtn.triggered.connect(self.takescreenshot)
		tools1.addAction(ssBtn)

		# voice button
		asstBtn = QAction('Assistance',self)
		asstBtn.setIcon(QIcon('voiceicon - Copy.png'))
		asstBtn.triggered.connect(self.newwindow)
		tools1.addAction(asstBtn)

	def newwindow(self, checked):
		self.w = voiceassist()
		self.w.show()

    



	# function for home button 
	def home(self):
		self.browser.setUrl(QUrl('http://google.com'))


	# function for loading the Url
	def loadUrl(self):
		url = self.searchBar.text()
		self.browser.setUrl(QUrl(url))


	# function for updating the Url
	def updateUrl(self, url):
		self.searchBar.setText(url.toString())


	# function for Screenshot 
	def takescreenshot(self):
		with mss.mss() as sct:
			filename = sct.shot(mon=-1, output=f"{datetime.datetime.now():%Y-%m-%d %H-%M-%S}.png")
			QMessageBox.about(self, "Successful", "Screenshot taken Successfully")

	
MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Rizvi Webbrowser')
window = Webbrowser()
MyApp.exec_()





	

