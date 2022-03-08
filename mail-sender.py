# -*- encoding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # for sending email using SMTP protocol (gmail)

# Timer is to make a method runs after an `interval` amount of time
from threading import Timer

SEND_REPORT_EVERY = 20  # in seconds, 60 means 1 minute and so on
FROM_EMAIL_ADDRESS = "knpkdim@gmail.com"
TO_EMAIL_ADDRESS = "bartosz.miazga1@gmail.com"
EMAIL_PASSWORD = "3SERDuhA"



class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the mesage
        self.message = MIMEText(u'Szanowni Państwo \nw imieniu zespołu badawczego działajacym przy Instytucie Psychologii Akademii\nPedagogiki Specjalnej w Warszawie życzliwie prosimy Państwa o pomoc w\nznalezieniu uczestników do badania, które obecnie prowadzimy pod \nkierownictwem naukowym dr Ewy Odachowskiej. Jego celem jest poznanie emocji i\nopinii związanych z pandemią SARS-CoV-2 oraz zdalnym nauczaniem i ich\nwplywem na ogólne funkcjonowanie psychospołeczne rodziców oraz ich dzieci.\n\nDo udzialu w badaniu zapraszamy rodziców dzieci w wieku wczesnoszkolnym z\ndoświadczeniem nauczania zdalnego (obecnych uczniow klas 2-4 szkoły\npodstawowej).  Wypełnienie ankiety potrwa ok. 20 -  30 minut.\n\nLink do kwestionariusza: https://badania.aps.edu.pl/index.php/983755?lang=pl',
                                "plain","utf-8")

    def createFiles(self):
        emailPrompt = 'Usuń tą linijkę i wklej emaile - każdy w nowej linii!'
        messagePrompt = 'Usuń tą linijkę i wklej swoją wiadomość!'
        with open('emails.txt','wb') as f:
            f.write(emailPrompt.encode('utf-8'))
        testMessage = "śćąźęąóbartosz"
        with open('message.txt','wb') as f2:
            f2.write(messagePrompt.encode('utf-8'))

    def getContentFromFiles(self):
        with open('emails.txt','rb') as f:
            emailContent = f.read().decode('utf-8')
            print(emailContent)
        with open('message.txt','rb') as f2:
            self.messageContent = f2.read().decode('utf-8')
            print(self.messageContent)

    def getInstructionsFromUser(self):
        signFromUser = input('Press \'git\' and hit enter when you are ready')
        if(signFromUser == 'git'):
            self.getContentFromFiles()
            #self.sendmail()
            print('jestem')

    def sendmail(self, from_email, password, to_email):#, message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = u'テストメール'
        part1 = MIMEText(u'Szanowni Państwo \nw imieniu zespołu badawczego działajacym przy Instytucie Psychologii Akademii\nPedagogiki Specjalnej w Warszawie życzliwie prosimy Państwa o pomoc w\nznalezieniu uczestników do badania, które obecnie prowadzimy pod \nkierownictwem naukowym dr Ewy Odachowskiej. Jego celem jest poznanie emocji i\nopinii związanych z pandemią SARS-CoV-2 oraz zdalnym nauczaniem i ich\nwplywem na ogólne funkcjonowanie psychospołeczne rodziców oraz ich dzieci.\n\nDo udzialu w badaniu zapraszamy rodziców dzieci w wieku wczesnoszkolnym z\ndoświadczeniem nauczania zdalnego (obecnych uczniow klas 2-4 szkoły\npodstawowej).  Wypełnienie ankiety potrwa ok. 20 -  30 minut.\n\nLink do kwestionariusza: https://badania.aps.edu.pl/index.php/983755?lang=pl',
                         "plain", "utf-8")
        part2 = MIMEText(self.messageContent,
                         "plain", "utf-8")
        msg.attach(part2)
        # manages a connection to an SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(from_email, password)
        # send the actual message
        server.sendmail(from_email, to_email, msg.as_string()) #- wazna linijka
        # terminates the session
        server.quit()

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """

        self.sendmail(FROM_EMAIL_ADDRESS, EMAIL_PASSWORD, TO_EMAIL_ADDRESS)#, self.message.encode('utf-8','ignore')
        #timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        #timer.daemon = True
        # start the timer
        #timer.start()

    def start(self):
        # start reporting the keylogs
        self.createFiles()
        self.getInstructionsFromUser()
        #self.getContentFromFiles()
        self.report()


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()