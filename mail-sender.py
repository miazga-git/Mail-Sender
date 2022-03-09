# -*- encoding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # for sending email using SMTP protocol (gmail)
import time

TO_EMAIL_ADDRESS = "bartosz.miazga1@gmail.com"
FREQUENCY = '1'
SENDER_PASSWORD = "3SERDuhA"
SENDER_EMAIL = "knpkdim@gmail.com"

class Keylogger:
    def createFiles(self):
        emailPrompt = 'Usuń tą linijkę i wklej emaile - każdy w nowej linii!'
        messagePrompt = 'Usuń tą linijkę i wklej swoją wiadomość!'
        print('I\'m creating files in the same folder as exe file...')
        with open('emails.txt','wb') as f:
            f.write(emailPrompt.encode('utf-8'))
        with open('message.txt','wb') as f2:
            f2.write(messagePrompt.encode('utf-8'))

    def getContentFromFiles(self):
        print('I\'m getting content from files...')
        with open('emails.txt','rb') as f:
            emailContent = f.read().decode('utf-8')
            self.listOfEmails = emailContent.split('\n')
        with open('message.txt','rb') as f2:
            self.messageContent = f2.read().decode('utf-8')

    def getInstructionsFromUser(self):
        print('In the same folder as exe file folder you can see 2 files: emails.txt and message.txt. Add your message and list of emails to appropriate files...')
        signFromUser = input('Press \'git\' and hit enter when you are ready. miazga$:')
        if(signFromUser == 'git'):
            self.getContentFromFiles()
            self.subject = input('Give me subject of email and hit enter. miazga$:')
            self.senderEmail = input('Give me your email (sender account) and hit enter. miazga$:')
            if(self.senderEmail==''):
                self.senderEmail=SENDER_EMAIL
            self.senderPassword = input('And now it\'s rough time for us... You need to trust me and give me your password and then hit enter. miazga$:')
            if(self.senderPassword==''):
                self.senderPassword=SENDER_PASSWORD
            self.frequency = input('Give me frequency and hit enter. miazga$:')
            if(self.frequency==''):
                self.frequency=FREQUENCY


    def sendmail(self, from_email, password, to_email):#, message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.subject
        part1 = MIMEText(self.messageContent,
                         "plain", "utf-8")
        msg.attach(part1)
        # manages a connection to an SMTP server
        print('I\'m trying to connect to SMTP server (gmail)...')
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        print('I\'m trying to log in to sender account...')
        server.login(from_email, password)
        print('I\'m sending new email, recipient: '+to_email )
        # send the actual message
        try:
            server.sendmail(from_email, to_email, msg.as_string())
            print("Email to: \'" + to_email.replace("\r", "") + "\' sended...")
        except:
            print("Sending email to: \'"+to_email.replace("\r","") +"\' was not complited: ")
        # terminates the session
        server.quit()


    def report(self):
        while(len(self.listOfEmails)!=0):
            i = len(self.listOfEmails)
            toEmailAddress = self.listOfEmails.pop(0)
            time.sleep(int(self.frequency))
            print(len(self.listOfEmails))
            print(toEmailAddress)
            self.sendmail(self.senderEmail, self.senderPassword, toEmailAddress)
        input('Press enter to quit my friend ;)')
        #timer = Timer(interval=self.interval, function=self.report)

    def start(self):
        self.createFiles()
        self.getInstructionsFromUser()
        self.report()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()