
# 📧 Email Unsubscriber Bot

A Python script that automates unsubscribing from unwanted emails by:

1. Connecting to your Gmail account
2. Parsing emails to find "unsubscribe" links
3. Automatically clicking those links to unsubscribe

---

## 🚀 Features

- Securely connect to Gmail using IMAP and OAuth2
- Parse emails to extract unsubscribe links
- Automate the unsubscription process using Selenium
- Log unsubscribed links for review

---

## 🛠️ Requirements

- Python 3.7+
- Gmail account with IMAP access enabled
- Google Cloud project with Gmail API and OAuth2 credentials
- Installed Python packages:
  - `imaplib`
  - `email`
  - `selenium`
  - `beautifulsoup4`

Install dependencies using:

```bash
pip install selenium beautifulsoup4
```

---

## 📄 Setup Instructions

1. **Enable Gmail API**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Gmail API for the project
   - Create OAuth2 credentials and download the `credentials.json` file

2. **Enable IMAP in Gmail**:
   - Log in to your Gmail account
   - Go to Settings > See all settings > Forwarding and POP/IMAP
   - Enable IMAP access

3. **Run the Script**:
   - Place the `credentials.json` in your project directory
   - Execute the script:

   ```bash
   python unsubscribe_bot.py
   ```

---

## ⚙️ How It Works

1. **Connect to Gmail**:
   - Authenticate using OAuth2
   - Access the inbox via IMAP

2. **Parse Emails**:
   - Fetch emails from the inbox
   - Use the `email` module to parse email content
   - Search for "unsubscribe" links in the email body

3. **Unsubscribe**:
   - Use Selenium to open each unsubscribe link
   - Automate the click on the unsubscribe button

4. **Log Results**:
   - Record the status of each unsubscription attempt
   - Save logs to a file for review

---

## 📌 Notes

- Ensure that the `credentials.json` file is kept secure
- Some unsubscribe links may require additional confirmation steps
- Review the logs to verify successful unsubscriptions

---

## 📚 Resources

- [Automate Your Life Using Python!](https://www.youtube.com/watch?v=rBEQL2tC2xY)
- [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python)
- [IMAP and SMTP with Gmail](https://support.google.com/mail/answer/7126229)

---