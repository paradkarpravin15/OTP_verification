import random
import smtplib
from email.message import EmailMessage

# Function to generate a 6-digit OTP
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Function to send OTP via email
def send_otp(to_email, otp):
    from_email = 'try.pravinparadkar@gmail.com'
    app_password = 'cpij kbkk bulx pwuf'  # Use an app-specific password

    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(f"Your OTP is: {otp}")

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        print(f"OTP sent successfully to {to_email}\n")
    except Exception as e:
        print("Failed to send email:", e)
        exit()

# Function to prompt the user to enter OTP
def prompt_otp_entry():
    return input("🔐 Enter the OTP sent to your email: ").strip()

# Function to verify the entered OTP
def verify_otp(generated_otp, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        user_input = prompt_otp_entry()
        if user_input == generated_otp:
            print("✅ OTP Verified! Access granted.")
            return True
        else:
            print(f"❌ Incorrect OTP. Attempt {attempt} of {max_attempts}.")
    print("🚫 Maximum attempts exceeded. Access denied.")
    return False

# Main function
def main():
    print("📧 Welcome to the OTP Verification System")
    to_email = input("Enter your email address: ").strip()
    
    otp = generate_otp()
    send_otp(to_email, otp)
    verify_otp(otp)

if __name__ == "__main__":
    main()