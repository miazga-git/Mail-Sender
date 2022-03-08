# -*- encoding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # for sending email using SMTP protocol (gmail)

# Timer is to make a method runs after an `interval` amount of time
from threading import Timer


TO_EMAIL_ADDRESS = "bartosz.miazga1@gmail.com"


#pobieranie maili i wysylanie kolejno wiadomosci do kolejnych odbiorców
#spowolnic wysylanie maili
#dodac komunikaty
#obslugiwac wyjątki - rzucony wyjatek - podaj maila, na którym utknęło

class Keylogger:
    def createFiles(self):
        emailPrompt = 'Usuń tą linijkę i wklej emaile - każdy w nowej linii!'
        messagePrompt = 'Usuń tą linijkę i wklej swoją wiadomość!'
        with open('emails.txt','wb') as f:
            f.write(emailPrompt.encode('utf-8'))
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
            self.subject = input('Give me subject of email and hit enter:')
            self.senderEmail = input('Give me your email (sender account) and hit enter:')
            self.senderPassword = input('And now it\'s rough time for us... You need to trust me and give me your password and then hit enter:')
            self.frequency = input('Give me frequency and hit enter:')
            print('Frequency: '+self.frequency)


    def sendmail(self, from_email, password, to_email):#, message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.subject
        part1 = MIMEText(self.messageContent,
                         "plain", "utf-8")
        msg.attach(part1)
        # manages a connection to an SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(from_email, password)
        # send the actual message
        server.sendmail(from_email, to_email, msg.as_string())
        # terminates the session
        server.quit()

    def report(self):
        self.sendmail(self.senderEmail, self.senderPassword, TO_EMAIL_ADDRESS)
        #timer = Timer(interval=self.interval, function=self.report)

    def start(self):
        self.createFiles()
        self.getInstructionsFromUser()
        self.report()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()