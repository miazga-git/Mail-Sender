# -*- encoding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # for sending email using SMTP protocol (gmail)
import time
import os
import time
import datetime
from random import seed, randrange



FREQUENCY = '1'
SENDER_PASSWORD = ""
SENDER_EMAIL = ""
NUMBER_OF_EMAILS_PER_SESSION = '100'
FREQUENCY_BETWEEN_SESSIONS = '10'


#wyrzucić greetings i happy endings
#wyrzucić zbędne printy

class Mailsender:
    def greetings(self):
        greetingText = ['*' ,'*', '*', 'H', 'e', 'l', 'l', 'o', '*', '*', '*']
        i = 0
        while (len(greetingText) >=i+1):
            print(greetingText[i], end= ' ')
            i = i + 1
            time.sleep(0.4)
        print('\n')

    def createFiles(self):
        emailPrompt = 'Usuń tą linijkę i wklej emaile - każdy w nowej linii!'
        #flowersForJulii = "Kwiaty na dzień kobiet: \n \U0001F33C \U0001F490 \U0001F339"
        messagePrompt = 'Usuń tą linijkę i wklej swoją wiadomość!'
        #messageWishes = 'Julii, chciałbym Ci życzyć wszystkiego najlepszego z okazji wczorajszego dnia kobiet!\nMiałem plan złożyć Ci życzenia w ten quality sposób już wczoraj, jednak nie zdążyłem skończyć kodu. \nMam nadzieję, że wybaczysz spóźnienie i docenisz życzonka w tej oryginalnej formie :*'
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
            print("Your message below:")
            print(self.messageContent)

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
            self.multipleAccounts = input('Do you want to add multiple accounts? (write y/n and hit enter). miazga$:')
            if(self.multipleAccounts == 'y'):
                self.getOtherAccountsFromUser()

            self.is_frequency_email_random = input('Do you want frequency between sending emails to be randomized? (write y/n and hit enter). miazga$:')
            if(self.is_frequency_email_random == 'y'):
                self.frequency_email_random_bottom = input('Give me min. number of seconds. miazga$:')
                self.frequency_email_random_ceiling = input('Give me max. number of seconds. miazga$:')
            else:
                self.frequency_email = input('Give me frequency and hit enter. miazga$:')
                if(self.frequency_email==''):
                    self.frequency_email=FREQUENCY

            self.is_frequency_between_sessions_random = input('Do you want frequency between sessions to be randomized? (write y/n and hit enter). miazga$:')
            if (self.is_frequency_between_sessions_random == 'y'):
                self.frequency_between_sessions_bottom = input('Give me min. number of seconds. miazga$:')
                self.frequency_between_sessions_ceiling = input('Give me max. number of seconds. miazga$:')
            else:
                self.frequency_between_sessions = input('Give me frequency and hit enter. miazga$:')
                if (self.frequency_between_sessions == ''):
                    self.frequency_between_sessions = FREQUENCY_BETWEEN_SESSIONS

            self.numberOfEmailsPerSession = input('Give me number of emails per session. miazga$:')
            if(self.numberOfEmailsPerSession==''):
                self.numberOfEmailsPerSession=NUMBER_OF_EMAILS_PER_SESSION

    def getOtherAccountsFromUser(self):
        i = 0
        self.listOfAccounts = []
        self.listOfPasswords = []
        while 1 != 0:
            i=i+1
            self.senderEmail2 = input('Give me your email for account number '+str(i)+ ' and hit enter. miazga$:')
            self.senderPassword2 = input('Give me your password for account number '+str(i)+ ' and hit enter. miazga$:')
            self.endOfEmails = input('Would you like to add next account? (write y/n and hit enter). miazga$:')
            self.listOfAccounts.append((self.senderEmail2))
            self.listOfPasswords.append(self.senderPassword2)
            if (self.endOfEmails == 'n'):
                break

   # def getOtherAccounts(self):
   #     print(self.listOfAccounts)
    #    print(self.listOfPasswords)

    def controlFlowOfSessions(self):
        self.seconds_start_program = time.time()
        print("Program started")
        while(len(self.listOfEmails) != 0):
            if(self.multipleAccounts == 'y'):
                self.startingEmailSession(self.senderEmail,self.senderPassword)
                i = 0
                while(len(self.listOfAccounts) > i):
                    print(self.listOfEmails)
                    if(len(self.listOfEmails) != 0):
                        self.startingEmailSession(self.listOfAccounts[i], self.listOfPasswords[i])
                    i = i + 1
            elif(self.multipleAccounts == 'n'):
                if(len(self.listOfEmails) != 0):
                    self.startingEmailSession(self.senderEmail,self.senderPassword)

    def startingEmailSession(self, from_email, password):
        print('I\'m sleeping before connecting to SMTP server (gmail)... zzz...')

        if (self.is_frequency_between_sessions_random == 'y'):
            self.frequency_between_sessions = randrange(int(self.frequency_between_sessions_bottom), int(self.frequency_between_sessions_ceiling),1)
            print('frequency_between_sessions: ' + str(self.frequency_between_sessions))
        time.sleep(int(self.frequency_between_sessions))
        # manages a connection to an SMTP server
        print('I\'m trying to connect to SMTP server (gmail)...')
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        print('I\'m trying to log in to sender account...')
        print(from_email)
        print(password)
        server.login(from_email, password)
        self.sendmail(server, from_email)
        # terminates the session
        server.quit()


    def sendmail(self, server,from_email):#, message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.subject
        part1 = MIMEText(self.messageContent,
                         "plain", "utf-8")
        msg.attach(part1)
        iterations = 0
        seconds_start_session = time.time()
        while (len(self.listOfEmails) != 0 and iterations != int(self.numberOfEmailsPerSession)):
            i = len(self.listOfEmails)
            #print("server email: "+str(server.gel))
            toEmailAddress = self.listOfEmails.pop(0)
            if(self.is_frequency_email_random == 'y'):
                self.frequency_email = randrange(int(self.frequency_email_random_bottom),int(self.frequency_email_random_ceiling),1)
                print('frequency_email: '+str(self.frequency_email))
            time.sleep(int(self.frequency_email)) # uspienie miedzy mailami
            print('I\'m sending new email, recipient: '+ toEmailAddress)
            # send the actual message
            try:
                server.sendmail(from_email, toEmailAddress, msg.as_string())
                print(" =========== Email to: \'" + toEmailAddress.replace("\r", "") + "\' sended... ===========" )
            except:
                print(" =========== Sending email to: \'"+toEmailAddress.replace("\r","") +"\' was not complited... =========== ")
            seconds_end = time.time()
            seconds_int = int(seconds_end - seconds_start_session)
            m, s = divmod(seconds_int, 60)
            h, m = divmod(m, 60)
            seconds_int_total = int(seconds_end - self.seconds_start_program)
            m2, s2 = divmod(seconds_int_total, 60)
            h2, m2 = divmod(m2, 60)
            print("Time of working per this session :" + str(h) + ' hours ' + str(m) + ' minutes ' + str(s) + 'seconds')
            print("Program has been working for :" + str(h2) + ' hours ' + str(m2) + ' minutes ' + str(s2) + 'seconds')
            iterations = iterations + 1
            print("Iterations: " +str(iterations))
            print("NumberOfEmailsPerSession: "+str(int(self.numberOfEmailsPerSession)))


    def cleaning(self):
        os.remove("message.txt")
        os.remove("emails.txt")
        input('Press enter to quit my friend ;)')

    def happyEnding(self):
        endingText = ['*' ,'*', '*', 'G', 'o', 'o', 'd', 'b', 'y', 'e', ' ', 'J', 'u', 'l', 'i', '*', '*', '*']
        i = 0
        while (len(endingText) >=i+1):
            print(endingText[i], end= ' ')
            i = i + 1
            time.sleep(0.4)

    def start(self):
        self.greetings()
        self.createFiles()
        self.getInstructionsFromUser()
        self.controlFlowOfSessions()
        self.sendmail(self.senderEmail, self.senderPassword)
        self.cleaning()
        self.happyEnding()

if __name__ == "__main__":
    mailsender = Mailsender()
    mailsender.start()