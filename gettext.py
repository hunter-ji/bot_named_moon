#encoGding=utf-8
import wave
import urllib, urllib2, pycurl
import base64
import json
import os

def arecord_voice(filename):
    print "Ok!Let's get video :"
    os.system("arecord -D plughw:1,0 -f S16_LE -d 3 -r 8000 '%s'"%filename)


def get_token():
    apiKey = "GM75YwcRmCtbAZQKoaBfKmSN"
    secretKey = "b03d191ee8dc072d1972d0d98896f0e7"
 
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
 
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']

message = '1'

def dump_res(buf):
    print (buf)
    global message
    a = eval(buf)
#    print type(a)
    if a['err_msg']=='success.':
        #print a['result'][0]
        message = a['result'][0]


def get_message():
    return message

 
## post audio to server
def use_cloud(filename, token):
#    test = raw_input('Please input the name of file :')
#    test1 = test + '.wav'
    fp = wave.open(filename, 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)
 
    cuid = "9619749" 
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]
 
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url)) 
#    c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header) 
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() 
 
if __name__ == "__main__":
    arecord_voice()
    token = get_token()
    use_cloud(token)
    os.system('rm .1.wav -f')
