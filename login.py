import requests
import pytest
import logging

# idea 1
# url='http://www.test2.quanfangtongvip.com/doLogin'
# content={'account':13990000001,
#          'corUrl':1399,
#          'password':'loW+CZ8Gb6CaGzkBasstMUI98PRGQabqjq0K62cTZXQ6IOAYQdQ/JklOyop98fOHDN0vBpGLdpwI7MxwYXvDbMnHf3SfxpI83KtuhQt6ihBf2argefUG+IKL7IFP5oAfPiNwWzFsII8rT6yOdggVYJBoU0ewgmgg2ElnXEl6gVs=',
#          'loginMode':'false',
#          'smscode':''
#          }
# r = requests.post(url = url,params = content )
# print(r.text)
# if (r.status_code == 200):
#     print("success")
# else:
#     print("false")


#idea2
class TestInterface():

    url='http://www.test2.quanfangtongvip.com/doLogin'
    # content={'account':13990000001,
    #          'corUrl':1399,
    #          'password':'loW+CZ8Gb6CaGzkBasstMUI98PRGQabqjq0K62cTZXQ6IOAYQdQ/JklOyop98fOHDN0vBpGLdpwI7MxwYXvDbMnHf3SfxpI83KtuhQt6ihBf2argefUG+IKL7IFP5oAfPiNwWzFsII8rT6yOdggVYJBoU0ewgmgg2ElnXEl6gVs=',
    #          'loginMode':'false',
    #          'smscode':''
    #          }
    def test_Login(self):
        url=self.url
        # 'http://www.test2.quanfangtongvip.com/doLogin'
        params= {'account':13990000001,
             'corUrl':1399,
             'password':'loW+CZ8Gb6CaGzkBasstMUI98PRGQabqjq0K62cTZXQ6IOAYQdQ/JklOyop98fOHDN0vBpGLdpwI7MxwYXvDbMnHf3SfxpI83KtuhQt6ihBf2argefUG+IKL7IFP5oAfPiNwWzFsII8rT6yOdggVYJBoU0ewgmgg2ElnXEl6gVs=',
             'loginMode':'false',
             'smscode':''
             }
        r = requests.post(url=url,params=params)
        assert r.status_code ==200
        #logging (r.status_code )
        print("success")

if __name__=='__main__':

    a=TestInterface()
    a.test_Login()




