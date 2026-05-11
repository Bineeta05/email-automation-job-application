import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders

# Sender Credentials
sender_email = "your_email@gmail.com"
sender_name = "your_name"
# Use Gmail App Password here
password = "your_16_digit_app_password"

# Recruiter Email List
email_list = [
    "recruiter1@gmail.com",
    "recruiter2@gmail.com"
]

# Resume Path
filename = "sample_resume.pdf"

# Connect to Gmail SMTP
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

# Login
server.login(sender_email, password)

# Loop through recruiter emails
for receiver_email in email_list:

    # Create Email
    msg = MIMEMultipart()

    msg["From"] = sender_name

    msg["To"] = receiver_email

    msg["Subject"] = "Application for - [add your role]"

    # Email Body
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
Your Name
"""

    # Attach body
    msg.attach(MIMEText(body, "plain"))

    # Attach Resume
    with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")

        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}"
    )

    msg.attach(part)

    # Send Email
    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    print(f"Email sent successfully to: {receiver_email}")

# Close SMTP connection
server.quit()

print("All emails sent successfully.")
