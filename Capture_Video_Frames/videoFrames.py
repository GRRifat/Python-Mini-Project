import os
import shutil
import sys
import cv2

class FrameCapture:
    '''
        Class definition to capture frames
    '''
    def __init__(self, file_path):
        '''
            Initialize directory where the captured frames will be stored.
            Also truncate the directory if it already exists.
        '''
        self.directory = "captured_frames"
        self.file_path = file_path
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        '''
            This method captures the frames from the video file provided.
            Uses OpenCV library.
        '''
        cv2_object = cv2.VideoCapture(self.file_path)
        frame_number = 0
        frame_found = True

        while frame_found:
            frame_found, image = cv2_object.read()
            if frame_found:
                capture = os.path.join(self.directory, f'frame{frame_number}.jpg')
                cv2.imwrite(capture, image)
                frame_number += 1

        cv2_object.release()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        file_path = "E:/Mini Project/Capture_Video_Frames/Video.mp4"
    else:
        file_path = sys.argv[1]

    fc = FrameCapture(file_path)
    fc.capture_frames()
