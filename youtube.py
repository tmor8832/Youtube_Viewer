#pip install pafy
#pip install youtube_dl
import cv2, pafy
from types import FrameType

# function to rescale frame based on a percentage
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

url = "https://www.youtube.com/watch?v=8hgaUUfFS7Y" #various videos or livestreams

video = pafy.new(url)

best  = video.getbest(preftype="any")

cap = cv2.VideoCapture(best.url)

ret, prev_image = cap.read()

while cap.isOpened():

    ret, image = cap.read()

    frame_resized = rescaleFrame(image, 0.6)

    if not ret:
        continue
    cv2.imshow('frame',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('q'): #if the letter q is pressed, break the loop and stop displaying    
        break

cap.release()
cv2.destroyAllWindows()




