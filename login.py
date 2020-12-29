import  requests
url='http://www.test2.quanfangtongvip.com/doLogin'
content={'account':13990000001,
         'corUrl':1399,
         'password':'loW+CZ8Gb6CaGzkBasstMUI98PRGQabqjq0K62cTZXQ6IOAYQdQ/JklOyop98fOHDN0vBpGLdpwI7MxwYXvDbMnHf3SfxpI83KtuhQt6ihBf2argefUG+IKL7IFP5oAfPiNwWzFsII8rT6yOdggVYJBoU0ewgmgg2ElnXEl6gVs=',
         'loginMode':'false',
         'smscode':''
         }

r = requests.post(url,params=content)
print(r.text)
