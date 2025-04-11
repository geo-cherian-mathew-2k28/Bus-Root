import cv2
import easyocr
import numpy as np
import gtts
import pygame
import os

# Initialize OCR reader
reader = easyocr.Reader(['en'])

# Predefined bus number plate to route mapping (translated to Malayalam)
bus_routes = {
    "KL01AB1234": "ഈ ബസ് എറണാകുളത്തേക്ക് പോകുന്നു.",
    "KL07CD5678": "ഈ ബസ് തിരുവനന്തപുരം പോകുന്നു.",
    "KL10EF9101": "ഈ ബസ് കോട്ടയത്തേക്ക് പോകുന്നു.",
             }

# Initialize pygame for playing speech
pygame.mixer.init()

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform OCR on the whole frame
    result = reader.readtext(gray, detail=0)
    
    if result:
        for text in result:
            detected_text = text.replace(" ", "").upper()
            
            # Fix misinterpretation of 'O' as '0' and 'I' as '1' in the 3rd and 4th positions
            if len(detected_text) >= 4:
                detected_text = detected_text[:2] + detected_text[2:4].replace('O', '0').replace('I', '1') + detected_text[4:]
            
            print(f"Detected Text: {detected_text}")  # Print detected text
            
            # Check if the number plate is in the predefined routes
            if detected_text in bus_routes:
                announcement = bus_routes[detected_text]
                print(f"Bus Detected: {detected_text} - {announcement}")
                
                # Convert text to speech in Malayalam
                tts = gtts.gTTS(announcement, lang="ml")
                tts.save("announcement.mp3")
                
                # Play the announcement
                pygame.mixer.music.load("announcement.mp3")
                pygame.mixer.music.play()
                
                # Wait for the announcement to finish
                while pygame.mixer.music.get_busy():
                    continue
                
                # Stop and unload music before deleting the file
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()

                # Remove the audio file after playing
                os.remove("announcement.mp3")
    
    # Display the frame
    cv2.imshow("OCR Detection", frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
