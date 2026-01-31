import smtplib
from email.message import EmailMessage

def send_project_email(project):
    msg = EmailMessage()
    msg["Subject"] = f"New Mixing Project: {project.plan}"
    msg["From"] = "your@email.com"
    msg["To"] = "your@email.com"

    msg.set_content(f"""
New project submission:

Plan: {project.plan}
Genre: {project.genre}
Service: {project.service}

Details:
{project.details}
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your@email.com", "APP_PASSWORD")
        smtp.send_message(msg)
