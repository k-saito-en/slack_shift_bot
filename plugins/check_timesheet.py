# coding: utf-8
#タイムシートの文字列とSlackの投稿日時を比較し、事務メンバーに通知する機能

from importlib import import_module
import gspread #スプレッドシートを操作するAPI
from google.oauth2.service_account import Credentials #Google Cloud Platform で設定したサービスアカウント、認証情報を扱うライブラリ

import sys #インタプリタや実行環境に関する情報を扱うためのライブラリ

sys.path.append("/Users/kotarosaito/Documents/ドキュメント/slack_shift_bot")
import slackbot_settings 

jsonpass = str(slackbot_settings.dic_slackmember_name ['アルバイトメンバーB'] [0])


#jsonファイルを使って認証情報を取得
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    jsonpass,
    scopes=scopes
)

gc = gspread.authorize(credentials)


##conversations.history メソッド

import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from slack_bolt import App

url = "https://slack.com/api/conversations.history"
token = 'xoxb-4006937615492-4044935862070-jEMbdVR4dyXlyxT55DiUxSNR'

# unixtimeに変換
start_time = str(datetime.now() - relativedelta(months=1))
end_time = str(datetime.now())


#データ読み取りのスコープを指定
payload = {
    "token": token,
    "channel": "C0404EJSL6N",
    "count": "1000",
    "oldest": start_time,
    "latest": end_time
}

response = requests.get(url, params=payload)

json_data = response.json()

print(json_data)

#取得したメッセージをメンバーIDを含むかどうかで振り分ける仕組みを実装する

