# Email_Notification - Automated Resume Email Sender using Python

This project automates sending job application emails with resume attachments to multiple recruiters using Python and SMTP.

## Features

- Send emails automatically to multiple recipients
- Attach resume PDF dynamically
- Gmail SMTP integration
- Personalized email body
- Simple and reusable script
- Suitable for job application automation

---

## Technologies Used

- Python
- SMTP
- MIME
- Gmail App Password
- Databricks / Local Python

---

## Project Structure

```bash
email-automation-job-application/
│
├── README.md
├── requirements.txt
├── send_emails.py
├── sample_resume.pdf
└── screenshots/
```

---

## Setup Instructions

### 1. Enable Gmail App Password

Google blocks normal password login for SMTP.

Steps:

1. Enable 2-Step Verification in your Google Account
2. Generate App Password
3. Use generated password in script

Google Security:
https://myaccount.google.com/security

App Passwords:
https://myaccount.google.com/apppasswords

---

## Python Script
### Run the below code in databricks

```python
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders

sender_email = "your_email@gmail.com"
sender_name = "your_name"
password = "your_16_digit_app_password"

email_list = [
    "example1@gmail.com",
    "example2@gmail.com"
]

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(sender_email, password)

for receiver_email in email_list:

    msg = MIMEMultipart()

    msg["From"] = sender_name
    msg["To"] = receiver_email
    msg["Subject"] = "Application for [add your role]"

    body = f"""
Hi,

I hope you are doing well.

Please find attached my resume for Data Engineer opportunities.

Skills:
- Azure Databricks
- PySpark
- Azure Data Factory
- Delta Lake
- Microsoft Purview

Regards,
[Your Name]
"""

    msg.attach(MIMEText(body, "plain"))

    filename = "sample_resume.pdf"

    with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")

        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        "attachment; filename=resume.pdf"
    )

    msg.attach(part)

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    print(f"Sent to {receiver_email}")

server.quit()
```

---

## Output

```bash
Sent to recruiter1@gmail.com
Sent to recruiter2@gmail.com
```

---

## Future Improvements

- Read recruiter emails from CSV
- Personalized recruiter names
- HTML email templates
- Logging system
- Retry mechanism
- Schedule emails automatically
- Integration with LinkedIn recruiter exports

---

## Author

Bineeta Panja

Data Engineer | Azure Databricks | PySpark | ADF | Purview
