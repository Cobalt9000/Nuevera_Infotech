import os
import speech_recognition as sr

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Function to record voice command
def record_voice():
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to create a folder in a specified directory
def create_folder(folder_name, directory):
    try:
        os.makedirs(os.path.join(directory, folder_name))
        print(f"Folder '{folder_name}' created in '{directory}'.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists in '{directory}'.")

# Function to create a file in a specified directory
def create_file(file_name, directory):
    with open(os.path.join(directory, file_name), 'w'):
        print(f"File '{file_name}' created in '{directory}'.")

# Function to open a file in a specified directory
def open_file(file_name, directory):
    file_path = os.path.join(directory, file_name)
    try:
        os.startfile(file_path)
        print(f"Opened file '{file_name}' in '{directory}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found in '{directory}'.")

if __name__ == "__main__":
    while True:
        user_input = input("Press 'S' to start recording the voice command or 'Q' to quit: ").lower()
        if user_input == 's':
            voice_command = record_voice()
            if voice_command:
                parts = voice_command.split()
                action = parts[0].lower()
                if action == 'create' and parts[1] == 'folder' and parts[3] == 'in':
                    folder_name = parts[2]
                    directory = parts[4]
                    create_folder(folder_name, directory)
                elif action == 'create' and parts[1] == 'file' and parts[3] == 'in':
                    file_name = parts[2]
                    directory = parts[4]
                    create_file(file_name, directory)
                elif action == 'open' and parts[1] == 'file' and parts[3] == 'in':
                    file_name = parts[2]
                    directory = parts[4]
                    open_file(file_name, directory)
                else:
                    print("Invalid command. Please try again.")
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Press 'R' to record a voice command or 'Q' to quit.")