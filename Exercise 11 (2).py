# water drinking reminder to 1 -1 minit 

import time
import winsound
from plyer import notification
import pyttsx3

def remind_water(interval_minutes=1,repeat=5):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    
    while True:
        # Show desktop notification (right corner)
        for i in range(repeat):
         notification.notify(
            title="💧 Water Reminder",
            message="Time to drink water!",
            timeout=10
        )

        # Speak the reminder
        engine.say("Please drink water now!")
        engine.runAndWait()

        # Play beep sound
        winsound.Beep(1000, 1000)  # frequency=1000Hz, duration=1 sec

        # Wait for the next reminder
        time.sleep(interval_minutes * 60)

# Example: reminder every 1 minute
remind_water(interval_minutes=1,repeat=5)
