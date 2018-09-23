# remaining HDD
ハードディスクの容量が少なくなったら、LINEにアラートを送信するやつ。

## 使い方
1. Python3を使えるようにする
自身のWindowsにpyhtonをインストール。バージョンは3.4以上であれば大丈夫だと思います。

### インストール
```
> git clone https://github.com/titanium99/notificate.git
> cd notificate
```

### 必要なモジュール追加
```python3
> pip install -f requirements.txt
```

### LINE Notifyでアクセストークンを発行する
ログイン後、マイページの「アクセストークンの発行」の「トークンを発行」から発行する。
「サービスを登録」と間違いやすいので注意。
また、トークンは１回発行したら再発行できないので注意。
忘れてしまったら既存のnotifyを削除し、再度作成し直し。

### iniファイルにアクセストークンを転記
linenotify.ini.sampleのファイル名の".sample"以降を削除して、自身のアクセストークンを転記する。

### テスト
コマンドプロンプト等でwin_storagechek.pyを実行して、LINEに通知が行くかどうか確認する。

### win_storagechek.pyの編集
main()内のhdd_path,alert_GB,check_dayを自身の環境に応じ修正。

### Windowsのタスクスケジューラに登録
自分は1日ごとの実行で良いと思う。この辺はお好きなように。


