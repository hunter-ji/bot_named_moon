#!/usr/bin/python
# -*- coding: utf-8 -*-
from aip  import AipSpeech


class BAIDUAIP:

    def __init__(self):
        APP_ID="your_app_id"
        API_KEY="your_api_key"
        SECRET_KEY="your_secret_key"
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(sel, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def getText(self, file):
        results = self.aipSpeech.asr(self.get_file_content(file), 'wav', 8000, {
            'lan': 'zh',
        })
        print results
        if results["err_no"] == 0:
            return results["result"][0]
        else:
            return "主人，刚刚的语音出错啦！"

    def getAudio(self, text):
        result  = self.aipSpeech.synthesis(text, 'zh', 1, {
            'vol': 7,
            'per': 4,
        })

        if not isinstance(result, dict):
            with open('audio.mp3', 'wb') as f:
                f.write(result)


if __name__ == "__main__":
    choice = raw_input('enter >>>')
#    if choice == "1":
#    print BAIDUAIP().getText('audio.wav')
#    elif choice == "2":
#        BAIDUAIP().getAudio('主人，您好，我们终于又见面了。')
    BAIDUAIP().getAudio(choice)
