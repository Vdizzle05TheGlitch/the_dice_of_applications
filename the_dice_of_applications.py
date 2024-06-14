import random2
import time
import subprocess

# List of applications with their respective chances (the smaller the number, the higher the chance)
applications_with_chances = [
    ("E:\SteamLibrary\steamapps\common\Balatro\Balatro.exe", 50),   # 1/50 chance
    ("E:\SteamLibrary\steamapps\common\DuckTales Remastered\executable\DuckTales.exe", 500), # 1/500 chance
    # Add more applications with their chances as needed
]

def open_application(app_path):
    """Opens the given application."""
    subprocess.Popen([app_path])

def main():
    seconds_since_last_roll = 0

    while True:
        roll_happened = False
        
        for app, chance in applications_with_chances:
            if random2.randint(1, chance) == 1:
                print(f"Roll success: Opening {app}")
                open_application(app)
                roll_happened = True
            else:
                print(f"Roll failed: {app} not opened")
        
        if roll_happened:
            seconds_since_last_roll = 0
        else:
            seconds_since_last_roll += 1
            print(f"Seconds since last roll: {seconds_since_last_roll}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
