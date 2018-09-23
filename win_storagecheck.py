#! python3

import shutil
import notify
import datetime

def remin_hdd(drive):
    """
    >>> remin_hdd('N:\\')
    (300, 15)
    """
    # HDDの使用量を取得。返り値：total,used,free
    du = shutil.disk_usage(drive)
    # 値はバイトなのでGB表示に変換。
    # 今回usedはいらないので計算せず。
    rem_GB = du.free/1024**3
    total_GB = du.total/1024**3
    return total_GB, rem_GB

def main():
    """ 1日1回のチェック。
    指定した容量以下ならアラートを送信。
    指定した容量以上でも週１回は残量を送信。
    """
    hdd_path = 'N:\\' # チェックするHDDのパス。Nドライブ
    alert_GB = 100 # アラートする残量。100GB以下でアラート
    check_day = 4 # チェックする曜日(月曜1~日曜7)。木曜になったら残量の連絡。
    
    hdd = remin_hdd(hdd_path)
    today = datetime.datetime.now()
    if hdd[1] < alert_GB:
        # メッセージは適当に変えてください。
        notify.line('録画HDDの残りが少なくなりました。\nHDDを整理しましょう。残{:.2f}GBです。'.format(hdd[1]))
    elif today.isoweekday() == check_day:
        notify.line('録画HDDの残りは{:.2f}GBです。'.format(hdd[1]))
    
if __name__ == '__main__':
    main()
