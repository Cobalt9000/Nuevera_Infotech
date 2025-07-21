import speech_recognition as sr
import yagmail
from email.message import EmailMessage

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a command:")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None

# Function to send email using Yagmail
def send_email(recipient_email, subject, body):
    yag = yagmail.SMTP('username(email_ID)', 'password')

    # Send the email
    yag.send(
        to=recipient_email,
        subject=subject,
        contents=body
    )

    # Close the connection
    yag.close()

if __name__ == "__main__":
    while True:
        command = recognize_speech()

        if command:
            if 'send email' in command:
                recipient_email = input("Enter the recipient's email address: ")
                subject = input("Enter the email subject: ")
                body = input("Enter the email body: ")

                send_email(recipient_email, subject, body)
                print("Email sent successfully!")
            elif 'exit' in command:
                break
            else:
                print("Command not recognized. Try again.")
