# Mail-Sender
User provide message, title of email, period of time after which e-mail is sent and lists of emails (recipients). It is something like mail-bot. I've made this script for my friend from psychologic studies to help her automate her work - sending emails with behavioral surveys.

## Libraries needed

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # for sending email using SMTP protocol (gmail)
import os
import time
from random import randrange
```

## Parameters in Code

```python
FREQUENCY = 'frequency_between_sending_email'
SENDER_PASSWORD = "password_of_sender_email"
SENDER_EMAIL = "sender_email"
NUMBER_OF_EMAILS_PER_SESSION = 'number_of_emails_per_session'
FREQUENCY_BETWEEN_SESSIONS = 'frequency_between_sessions'
```

Upper parameters are default settings, but during startup process <b>mail-sender</b> asks if user want to change this settings.


## Startup process and options

### List of emails and message content
```console
Press 'git' and hit enter when you are ready. miazga$:git
```

- After starting script in the same folder as exe file folder user can see 2 files: emails.txt and message.txt. In emails.txt user should add emails list (emails starting from new line). In text.txt user should add message to be sent.

### Subject of the message
```console
Give me subject of email and hit enter. miazga$:Test
```

### Sender account credentials 
```console
Give me your email (sender account) and hit enter. miazga$:test@test.com
```

```console
And now it's rough time for us... You need to trust me and give me your password and then hit enter. miazga$:passwd
```

### Multiple sender accounts options
```console
Do you want to add multiple accounts? (write y/n and hit enter). miazga$:y
```

```console
Give me your email for account number 1 and hit enter. miazga$:test2@test.com
Give me your password for account number 1 and hit enter. miazga$:passwd2
Would you like to add next account? (write y/n and hit enter). miazga$:n
```

- user can add more than one sender email. Script give a possibility to send emails from multiple accounts. If one account is blocked, then other accounts will be sending emails. User can add as much sender accounts as user wants.

### Frequency between email sending

```console
Do you want frequency between sending emails to be randomized? (write y/n and hit enter). miazga$:y
Give me min. number of seconds. miazga$:2
Give me max. number of seconds. miazga$:10
```

- script can wait some amount of seccounds between sending emails. This functionality has been made to make sending emails more similar to human actions.

### Frequency between sessions
```console
Do you want frequency between sessions to be randomized? (write y/n and hit enter). miazga$:y
Give me min. number of seconds. miazga$:3
Give me max. number of seconds. miazga$:15
```

- script changes session from one account to another, and script can wait some amount of seccounds during changing session. If only one account is added, script also changes session - it makes logout and login operation for the same account in loop.

### Emails per session
```console
Give me number of emails per session. miazga$:5
```

## Runtime example

![image](https://user-images.githubusercontent.com/82395921/219880062-4b33bc0c-844f-4916-b23b-b6b66c177c2c.png)

## Warnings
- script has gmail smtp settings hardcoded, but gmail disabled 'less secure devices' option. There is need to change smtp setting in code.<br>
- case, when one of the sender accounts would be blocked has never been tested

