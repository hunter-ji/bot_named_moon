环境是python 2.7

流程是这样的：
1.pyaudio实时录音，当声音高于设定的值时进行录音，为时三秒并保存声音；
2.将声音文件调用百度api进行识别，将变量传到本地；
3.目前只写了个字典，进行存储，并写了几个正则，语音是别的文本在本地进行匹配，得出回应文本；
4.将本地匹配的文本调用百度api进行合成，合成的语音保存；
5.播放合成的语音。

功能：
1.简单的对话；
2.讲笑话；
3.播报今天、明天、后天的天气；
4.播放音乐。

运行方式：
python main.py

*注:运行环境比较复杂的，需要注意安装。


