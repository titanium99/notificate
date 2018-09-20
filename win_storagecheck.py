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
    rem_GB = du.free/1024**3
    total_GB = du.total/1024**3
    return total_GB, rem_GB

def main():
    hdd = remin_hdd('N:\\')
    today = datetime.datetime.now()
    if hdd[1] < 200:
        notify.line('録画HDDの残りが少なくなりました。\nHDDを整理しましょう。残{:.2f}GBです。'.format(hdd[1]))
    elif today.isoweekday() == 4:
        notify.line('録画HDDの残りは{:.2f}GBです。'.format(hdd[1]))
    
if __name__ == '__main__':
    main()
