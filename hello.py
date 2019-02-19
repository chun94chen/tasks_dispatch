# -*- coding:utf-8 -*-
"""
{
    "errcode": 0,
    "errmsg": "ok",
    "access_token": "fw8ef8we8f76e6f7s8df8s"
}


"""
import requests

app_key = 'ding4bpmq5gt8nnbivdz'
app_secret = '0SUTtcZcHYsXpvs9yxY0Gs4EEqS9k5DPYQyobELx78bmwtd1PT9mx7L_nZ5jW5Wx'



DING_AGENT_ID = '217793960'
def foo():

    url = 'https://oapi.dingtalk.com/gettoken'
    params = {
        'appkey': app_key,
        'appsecret': app_secret
    }

    resp = requests.get(url, params=params)
    access_token = resp.json()['access_token']
    print('access token:{}'.format(access_token))

    resp = requests.get('https://oapi.dingtalk.com/get_jsapi_ticket', {'access_token': access_token})
    print(resp.text)


def bar():
    corpid = 'ding62362730d4eae8ac35c2f4657eb6378f'
    corpsecret = 'w59CMFLm2BnAncuMaGHVlnQko76nCnz-pVUOvTSWNCbrxduhCwxvLS0OPC051D10'
    resp = requests.get('https://oapi.dingtalk.com/sso/gettoken', params={'corpid': corpid, 'corpsecret': corpsecret})
    access_token = resp.json()['access_token']
    print('access token:{}'.format(access_token))

    resp = requests.get('https://oapi.dingtalk.com/get_jsapi_ticket', {'access_token': access_token})
    print(resp.text)

def zoo():

    url = 'https://oapi.dingtalk.com/gettoken'
    params = {
        'appkey': 'dingfczxhxe5w4oqlakp',
        'appsecret': '0UG1zPQ0UomS4DVP7UOOrIpc1ofMckl6ApXHbm1uMq_IX9Jo7JA1FHFS7Zqq_EnV'
    }

    resp = requests.get(url, params=params)
    print(resp.text)
    access_token = resp.json()['access_token']

    resp = requests.get('https://oapi.dingtalk.com/get_jsapi_ticket', {'access_token': access_token})
    print(resp.text)


if __name__ == '__main__':
    zoo()




