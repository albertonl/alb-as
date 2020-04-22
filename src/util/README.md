# Authentication setup

To complete the application setup, you will need to follow these instructions. Please create an empty file and name it `auth.py`. Now, copy and paste the following contents into the file:

```python
# Aules authentication
username = ""
password = ""

# Email sender authentication
gmail_user = ""
gmail_password = ""

# Email receiver information
gmail_to = ""
```

- **Aules authentication**
	- `username` represents your username (NIA if you are a student).
	- `password` represents your Aules password. We **won't be able to access your password nor any of your accounts**. However, keep this file private or use some encryption method as to prevent other people from knowing it. Nevertheless, the password given as input to the emailer script **must be decrypted and in plain text**.
- **Email sender authentication**
	- `gmail_user` represents the email address of the sender (e.g. `mygmailaccount@gmail.com`). Take note that this application **only works with Gmail** (at least to what it comes to the sender), as we use their SMTP server to send the emails.
	- `gmail_password` represents the password of the sender's Gmail account. Again, the password given to the emailer script must be decrypted and in plain text.
- **Email receiver information**
	- `gmail_to` is the receiver's email account. Usually, this might be your personal account where you want to receive your data. This account can be of any provider, as long as it is a real email account. **Please do not spam random or unknown accounts, as they would be able to get access to your Aules data!**

Now add your own values as in the following example:

```python
# Aules authentication
username = "12345678"
password = "catsRcute"

# Email sender authentication
gmail_user = "example1@gmail.com"
password = "qwerty1234"

# Email receiver information
gmail_to = "mypersonalaccount@gmail.com"
```
