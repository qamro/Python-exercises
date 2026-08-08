import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    
    sound_file = "mixkit-digital-clock-digital-alarm-buzzer-992.wav"  # Replace with the path to your alarm sound file
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKE UP NIGGA!")
            
            pygame.mixer.init()    # initialize the mixer(module for loading and playing sounds)
            pygame.mixer.music.load(sound_file)   # load our sound file
            pygame.mixer.music.play()   # play our sound
            
            # Keep the program running while the alarm sound is playing.
            # get_busy() returns True while the music is still playing until the music finishes then it will return False.
            while pygame.mixer.music.get_busy():   # Without this loop, the program may terminate before the sound finishes. 
                time.sleep(1)                      # wait 1 second and check again if the music is still playing.
            
            is_running = False     # exit the while loop after the alarm music finishes
            
            
        time.sleep(1) # the current time will be updated after each 1 second
        
        
        
        
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)    
    