import snowboydecoder
import sys
import signal

import ok



class MAIN:

    def __init__(self):
        self.interrupted = False


    def signal_handler(self, signal, frame):
        self.interrupted = True


    def interrupt_callback(self):
        return self.interrupted


    def Run(self):
       # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)

        detector = snowboydecoder.HotwordDetector('janet.pmdl', sensitivity=0.5)
        print('Listening... Press Ctrl+C to exit')
        print('Start ... \n')

        # main loop
        detector.start(detected_callback=snowboydecoder.play_audio_file,
                       interrupt_check=self.interrupt_callback,
                       sleep_time=0.03)

        detector.terminate()

if __name__ == "__main__":
    MAIN().Run()
