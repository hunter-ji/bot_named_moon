# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import re
import time
import os
from gettext import arecord_voice, get_token, use_cloud, get_message
from getvoice import get_voice, play_voice
from music import music
from qiushi import qiushi
from weather import weather


t = 0
sum = 0
file = 0
save_count = 0 
save_buffer = [] 


L = {'你好，':'主人，您好呀','介绍下自己，':'您好，我是小美，很高兴为您服务，我现在，能和您聊天，还能够讲笑话，播放音乐，播报天气，祝您有愉快的一天','银华，':'啦啦啦啦，套马的汉子威武雄壮', '念首诗，':'窗前明月光，疑是地上霜'}
C = []


def output_message(message):
    print '-----------------------------------'
    print '主人，您说的是：' + message
    print '-----------------------------------\n' + \
          ' '


pipei = re.compile(r'.*?介绍.*?自己.*?')
play_music = re.compile(r'.*?播放.*?音乐.*?')
get_joy = re.compile(r'.*?讲.*?笑话.*?')
weather_jt = re.compile(r'.*?今[天日].*?天气.*?')
weather_mt = re.compile(r'.*?明[天日].*?天气.*?')
weather_ht = re.compile(r'.*?后[天日].*?天气.*?')


def ans():
    test = voice(message)
    get_voice(token, test)
    play_voice()

def C_append():
    date_l = weather()
    for d in date_l:
        C.append(d[0].encode('UTF-8'))
        C.append(d[1].encode('UTF-8'))
        C.append(d[2].encode('UTF-8'))
        C.append(d[3].encode('UTF-8'))
        C.append(d[4].encode('UTF-8'))
        C.append(d[5].encode('UTF-8'))
        C.append(d[6].encode('UTF-8'))


def voice(message):
    if message in L.keys():
        test = L[message]
        return test
#        return test.encode('UTF-8')
    elif pipei.search(message):
        test = L['介绍下自己，']
        return test
    elif play_music.search(message):
        music() 
        test = ''
        return test
    elif get_joy.search(message):
        joy = qiushi()
        print joy.encode('utf-8').strip()
        print ''
        return joy.encode('utf-8').strip()
    elif weather_jt.search(message):
        C_append()
        return '主人，今天天气是' + C[1] + '，温度为' + C[2] + '到' + C[3] + '，' + C[4] + C[5] + '到' + C[6]
    elif weather_mt.search(message):
        C_append()
        return '主人，明天天气是' + C[8] + '，温度为' + C[9] + '到' + C[10] + '，' + C[11] + C[12] + '到' + C[13]
    elif weather_ht.search(message):
        C_append()
        return '主人，后天天气是' + C[15] + '，温度为' + C[16] + '到' + C[17] + '，' + C[18] + C[19] + '到' + C[20]
    elif message == '再见，':
        os.system('time.sleep(10)')
        return ''
    else:
        print '################################################################'
        print '#   [Warning]Faild to understand what you are speaking ! ! !   #'
        print '################################################################'
        print ' '
        return '主人，您能不能走点心，我都不知道你在说什么呀?'

# 将data中的数据保存到名为filename的WAV文件中
def save_wave_file(filename, data): 
    wf = wave.open(filename, 'wb') 
    wf.setnchannels(1) 
    wf.setsampwidth(2) 
    wf.setframerate(SAMPLING_RATE) 
    wf.writeframes("".join(data)) 
    wf.close() 



NUM_SAMPLES = 2000      
SAMPLING_RATE = 8000    
LEVEL = 1500            
COUNT_NUM = 20          
SAVE_LENGTH = 8         


while True: 

    pa = PyAudio() 
    stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
                    frames_per_buffer=NUM_SAMPLES) 
    string_audio_data = stream.read(NUM_SAMPLES) 
    audio_data = np.fromstring(string_audio_data, dtype=np.short) 
    large_sample_count = np.sum( audio_data > LEVEL ) 
    temp = np.max(audio_data) 
    if temp > 5500 and t == 0:
        t = 1
        print ' '
        print '检测到声音，开始录音。。。\n' + \
              ' '
        begin = time.time()
 #       print temp
    if t:
        print np.max(audio_data)
        if np.max(audio_data) < 1000:
            sum += 1
#            print sum
        end = time.time()
        if end-begin>3:
            print ' '
            print '三秒到了，要结束了。\n' + \
                  ' '
    # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
    if large_sample_count > COUNT_NUM: 
        save_count = SAVE_LENGTH 
    else: 
        save_count -= 1 
    if save_count < 0: 
        save_count = 0 
    if save_count > 0: 
        save_buffer.append( string_audio_data ) 
    else: 
        if len(save_buffer) > 0: 
#            filename = str(file) + ".wav" 
            filename = '.1.wav'
            save_wave_file(filename, save_buffer) 
            file += 1
            save_buffer = [] 
            t = 0
            sum = 0
            print '主人，我已经牢牢记住了哦～'
            token = get_token()
            use_cloud(filename, token)
            message = get_message()
            output_message(message)
            voice(message)
            ans()
            os.system('rm .1.wav')
            print '主人，结束啦。。。'
