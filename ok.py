# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
import time


class GetAudio:

    def __init__(self):
        self.t = 0
        self.sum = 0
        self.NUM_SAMPLES = 2000
        self.SAMPLING_RATE = 8000
        self.LEVEL = 1500
        self.COUNT_NUM = 20
        self.SAVE_LENGTH = 8
        self.pa = PyAudio()
        self.stream = self.pa.open(format=paInt16, channels=1, rate=8000, input=True,frames_per_buffer=2000)
        self.save_count = 0
        self.save_buffer = []

    def save_wave_file(sel, filename, data):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(8000)
        wf.writeframes("".join(data))
        wf.close()

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

    def Run(self):
        while True:
            string_audio_data = self.stream.read(self.NUM_SAMPLES)
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            large_sample_count = np.sum( audio_data > self.LEVEL )
            temp =  np.max(audio_data)
            if temp > 4000 and self.t == 0:
                self.t = 1
                print 'begin...\n'
                begin = time.time()
            if self.t:
                print np.max(audio_data)
                if np.max(audio_data) < 1000:
                    self.sum += 1
                end = time.time()
                if end-begin>1:
                    self.t = 0
                    print 'end...\n'

            if large_sample_count > self.COUNT_NUM:
                self.save_count = self.SAVE_LENGTH
            else:
                self.save_count -= 1

            if self.save_count < 0:
                self.save_count = 0

            if self.save_count > 0:
                self.save_buffer.append( string_audio_data )
            else:
                if len(self.save_buffer) > 0:
                    filename = "audio.wav"
                    self.save_wave_file(filename, self.save_buffer)
                    self.save_buffer = []
                    self.t = 0
                    self.sum = 0
                    print filename, "saved\n"
                    self.terminate()
                    break

if __name__ == "__main__":
   GetAudio().Run()
