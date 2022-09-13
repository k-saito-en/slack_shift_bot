# coding: utf-8

from slackbot.bot import respond_to #@slack_shift_bot のメンションに反応するデコーダ
from slackbot.bot import listen_to #＠メンバーのslack IDでを読み取るデコーダ

# SlackのAPIを利用するためのトークン
# Botの設定ページから「OAuth & Permissions」のページに遷移し、
# 「Bot User OAuth Access Token」をコピーして貼り付ける
API_TOKEN = "<xoxb-4006937615492-4044935862070-jEMbdVR4dyXlyxT55DiUxSNR>"


# dictionaryの作成（ slack nameとスプレッドシートの IDを紐付ける）
dic_slackmember_name = {}
#アルバイトメンバーAの情報を追加
dic_slackmember_name ['アルバイトメンバーA'] = ['/Users/kotarosaito/Documents/ドキュメント/slack_shift_bot/members_id/slack-shift-bot-a-964a24ac6818.json' , '1W-o7PbNLgWfgaNYw_Xl7tbC9YxZHdeB1FfmjkTwOobY']
#アルバイトメンバーBの情報を追加
dic_slackmember_name ['アルバイトメンバーB'] = ['/Users/kotarosaito/Documents/ドキュメント/slack_shift_bot/members_id/slack-shift-bot-b-b1d9bb6e5e5e.json' , '129JjNfNBzw-7qIbh3RgNBl2yMOfKH7F_oK1XFNW5Fww']
#認証鍵のパス（文字列）を取得
print(dic_slackmember_name ['@アルバイトメンバーB'] [0])



# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

#pliginsにメンバーIDと紐づいた情報を渡す関数
#課題　listen_toなしでもメンションで文字列が取得可能か検証の必要あり
@respond_to('^(.*)$')
@listen_to('^(.*)$')
def getjson (message):
    slackid = message
    return(slackid)

