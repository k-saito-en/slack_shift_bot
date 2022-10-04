# プロジェクト概要
某IT企業の勤怠管理の煩わしさを解消するため、１つのコマンド入力のみで勤怠管理、アルバイト給与確認が完了するボットの作成が命題となります。

従来、私のインターン先である某IT企業では、[slack](https://slack.com/intl/ja-jp/trials?remote_promo=f4d95f0b&utm_medium=ppc&utm_source=google&utm_campaign=cd_ppc_google_jp_ja_brand_slack_single_word_selfserve&utm_term=ss_slack_single_word_._スラック_._e_._c&utm_content=617976811340&gclid=CjwKCAjwhNWZBhB_EiwAPzlhNhZ0fWW_2S90B-URfKadz1t3UPWcIWSR2BBZDrJa7dDWcvMjc30CbxoCt4AQAvD_BwE&gclsrc=aw.ds)の専用チャンネルでの各メンバーの日時投稿によるコメント、Googleスプレッドシートの記入によるタイムシート作成による勤怠管理をしてきました。また、アルバイトメンバーの勤怠確認のため、月末に各メンバーのコメントとタイムシートを照合する必要がありました。
これを、ウェブサーバー上で動作するボットへのコマンド命令１つで完結させる機能を開発、提案していきます。

想定している開発
- pythonとboltフレームワークによるボット作成
- 認証鍵をデータベースに保管する、また、ボット動作のためのウェブサーバー構築（AWS）
- 二次対応としての機能拡張

# 一時開発全体スケジュール
<img width="1288" alt="スクリーンショット 2022-09-29 19 40 21" src="https://user-images.githubusercontent.com/111550856/193028830-86b5744a-94ac-4f9f-a2fe-e04dbdf41f5c.png">

# システム構成図（暫定版）
![システム設計図 drawioのコピー-2-2](https://user-images.githubusercontent.com/111550856/193788685-7b265d18-e405-4d41-8fa8-8829a99162ba.png)





# RULE

- プッシュする際は必ずプッシュ先を確認し、プロジェクトリーダーの許可なしに「本番環境」にプッシュしないこと
- コミットコメントは「Prefix」をつけること
  - feat: 新しい機能
  - fix: バグの修正
  - docs: ドキュメントのみの変更
  - style: 空白、フォーマット、セミコロン追加など
  - refactor: 仕様に影響がないコード改善(リファクタ)
  - perf: パフォーマンス向上関連
  - test: テスト関連
  - chore: ビルド、補助ツール、ライブラリ関連
 
# DEMO
 
"hoge"の魅力が直感的に伝えわるデモ動画や図解を載せる
 
# Features
 
"hoge"のセールスポイントや差別化などを説明する
 
# Requirement
 
"hoge"を動かすのに必要なライブラリなどを列挙する
 
* huga 3.5.2
* hogehuga 1.0.2
 
# Installation
 
Requirementで列挙したライブラリなどのインストール方法を説明する
 
```bash
pip install huga_package
```
 
# Usage
 
DEMOの実行方法など、"hoge"の基本的な使い方を説明する
 
```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```
 
# Note
 
注意点などがあれば書く
 
# Author
 
作成情報を列挙する
 
* 作成者
* 所属
* E-mail
 
# License
ライセンスを明示する
 
"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
 
社内向けなら社外秘であることを明示してる
 
"hoge" is Confidential.
