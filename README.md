# Mail-Sender
User provide message, title of email, period of time after which e-mail is sent and lists of emails (recipients). It is something like mail-bot.



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

```console
Press 'git' and hit enter when you are ready. miazga$:git
```

```console
Give me subject of email and hit enter. miazga$:Test
```

```console
Give me your email (sender account) and hit enter. miazga$:test@test.com
```

```console
And now it's rough time for us... You need to trust me and give me your password and then hit enter. miazga$:passwd
```

```console
Do you want to add multiple accounts? (write y/n and hit enter). miazga$:y
```

```console
Give me your email for account number 1 and hit enter. miazga$:test2@test.com
Give me your password for account number 1 and hit enter. miazga$:passwd2
Would you like to add next account? (write y/n and hit enter). miazga$:n
```

```console
Do you want frequency between sending emails to be randomized? (write y/n and hit enter). miazga$:y
Give me min. number of seconds. miazga$:2
Give me max. number of seconds. miazga$:10
```

```console
Do you want frequency between sessions to be randomized? (write y/n and hit enter). miazga$:y
Give me min. number of seconds. miazga$:3
Give me max. number of seconds. miazga$:15
```

```console
Give me number of emails per session. miazga$:5
```

