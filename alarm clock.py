import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    sound_file = "mixkit-digital-clock-digital-alarm-buzzer-992.wav"  # Replace with the path to your alarm sound file
    
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)    
    pygame.mixer.init()
    