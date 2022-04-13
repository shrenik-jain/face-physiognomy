import cv2
import numpy as np

from utils.model import FacialExpressionRecognizer


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionRecognizer("model_config/model.json", "model_config/model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        '''
        returns camera frames along with bounding boxes and predictions
        '''
        _, frames = self.video.read()
        gray_frames = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_frames, 1.3, 5)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            fc = gray_frames[y:y+h, x:x+w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            cv2.putText(frames, pred, (x+20, y-8), font, 1, (255, 255, 0), 2)
            cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)

        _, jpeg = cv2.imencode('.jpg', frames)

        return jpeg.tobytes()


class FileUpload(object):

    def __init__(self):
        self.image = cv2.imread('static/image.jpg')

    def get_roi(self):
        '''
        returns image with bounding boxes and predictions
        '''
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_image, 1.3, 5)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces: 
            fc = gray_image[y:y+h, x:x+w]
            cv2.rectangle(self.image,(x,y),(x+w,y+h),(255,0,0),2)
            
        roi = cv2.resize(fc, (48, 48))
        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
        
        cv2.imwrite('static/image_with_bb.jpg', self.image)
        cv2.imwrite('static/gray_image.jpg', gray_image)
        cv2.imwrite('static/roi.jpg', roi)

        return pred

