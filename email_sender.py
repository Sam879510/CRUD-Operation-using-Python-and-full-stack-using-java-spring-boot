# email_sender.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule
import time
from dashboard import generate_dashboard

def send_dashboard_email():
    # Email configuration
    sender_email = "sameerkumar.k.k40@gmail.com"
    sender_password = "Sameer123@"  # Use app-specific password
    receiver_email = "sameerkumarkk6@gmail.com"
    
    # Generate dashboard
    dashboard = generate_dashboard()
    if not dashboard:
        print("No sales data to report")
        return
    
    html_report, img_buffer = dashboard
    
    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Daily Sales Dashboard"
    
    # Attach HTML
    msg.attach(MIMEText(html_report, 'html'))
    
    # Attach image
    img = MIMEImage(img_buffer.read())
    img.add_header('Content-ID', '<sales_chart>')
    msg.attach(img)
    
    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
    
    print("Dashboard email sent successfully")

# Schedule daily at 5 PM
schedule.every().day.at("17:00").do(send_dashboard_email)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)