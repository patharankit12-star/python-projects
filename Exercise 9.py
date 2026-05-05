'''import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

l = ["rahul","mohan","Ravi"]

for name in l:
    text = f"Hello {name}, Shoutout you"
    engine.say(text)

# Run the speech engine
engine.runAndWait()'''

'''import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

l = ["rahul", "mohan", "Ravi"]

# Loop through each name
for name in l:
    text = f"Hello {name}, shoutout to you!"
    engine.say(text)

# Run the speech engine
engine.runAndWait()'''

'''import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

l = ["rahul", "mohan", "Ravi"]

# Loop through each name
for name in l:
    text = f"Hello {name}, shoutout to you!"
    engine.say(text)

# Run the speech engine
engine.runAndWait()'''

'''import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

l = ["rahul", "mohan", "Ravi"]

# Combine all names into one shoutout
names = ", ".join(l)
text = f"Hello {names}, shoutout to you all!"

engine.say(text)
engine.runAndWait()'''

'''import pyttsx3
import time

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

l = ["rahul", "mohan", "Ravi"]

# Loop through each name and speak separately
for name in l:
    text = f"Hello {name}, shoutout to you!"
    engine.say(text)
    engine.runAndWait()   # Speak immediately
    #time.sleep(0.4)       # Small pause between names
'''

'''import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

l = ["mohan", "Ravi"]

# Queue all shoutouts
for name in l:
    text = f"Hello {name}, shoutout to you!"
    engine.say(text)

# Speak them all in sequence
engine.runAndWait()'''

'''import pyttsx3
import time

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties
engine.setProperty("rate", 150)   # Speed of speech
engine.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

names = ["rahul", "mohan", "Ravi"]

# Speak each name separately
for name in names:
    text = f"Hello {name}, shoutout to you!"
    engine.say(text)
    engine.runAndWait()   # Force it to finish speaking before next
    time.sleep(0.5)       # Small pause between shoutouts
'''
'''import pyttsx3
#import time

names = [ "mohan", "Ravi"]

for name in names:
    # Create a fresh engine each time
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    text = f"Hello {name}, shoutout to you!"
    engine.say(text)
    engine.runAndWait()   # Speak immediately
        # Pause before next name'''

'''import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

names = ["rahul", "mohan", "Ravi"]

for name in names:
    text = f"Hello {name}, shoutout to you!"
    engine.say(text)
    engine.runAndWait()   # force playback immediately
    engine.stop()         # flush queue before next
    time.sleep(0.5)
'''
'''import pyttsx3
import time

# Initialize the engine
engine = pyttsx3.init()

# Set properties
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

names = ["rahul", "mohan", "Ravi"]

for name in names:
    text = f"Hello {name}, shoutout to you!"
    print(f"Speaking: {text}")  # Visual feedback
    
    engine.say(text)
    
    # runAndWait() processes the current queue and blocks until finished
    engine.runAndWait() 
    
    # Optional: Short sleep between shoutouts
    time.sleep(0.5)

# Optional: clean up after the loop is completely done
# engine.stop()
'''
'''
import pyttsx3
import time

engine = pyttsx3.init()

# Setup properties
engine.setProperty("rate", 100)
engine.setProperty("volume", 1.0)

#names = ["rahul", "mohan", "Ravi"]

#for name in names:
text = f"Hello rahul , shoutout to you!"
    # This prints the output to your console
print(f"Speaking: {text}") 
engine.say(text)
engine.runAndWait() 
    
text = f"Hello mohan , shoutout to you!"
    # This prints the output to your console
print(f"Speaking: {text}")
engine.say(text)
engine.runAndWait() 
    
text = f"Hello Ravi, shoutout to you!"
    # This prints the output to your console
print(f"Speaking: {text}")
    
    # This adds the text to the speech queue
engine.say(text)
    
    # This triggers the engine to speak and waits until finished
engine.runAndWait() 
    
    # Small pause between names
#time.sleep(0.5)'''

import pyttsx3
import time

# 1. Initialize outside the loop
engine = pyttsx3.init()

# 2. Set properties once
engine.setProperty("rate", 140)  # Slightly slower for better clarity
engine.setProperty("volume", 1.0)

names = ["rahul", "mohan", "Ravi"]

try:
    for name in names:
        text = f"Hello {name}, shoutout to you!"
        
        # Print first so you see what is being said
        print(f"Speaking: {text}")
        
        # Add to queue
        engine.say(text)
        
        # 3. Process the queue and block execution until speech is done
        # This is the "Gold Standard" way to use it
        engine.runAndWait() 
        
        # 4. Physical pause to let the audio driver 'breathe'
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Speech interrupted by user.")
finally:
    # 5. Clean up only at the very end of the script
    engine.stop()




