#! python3

import shutil
import notify

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
    notify.line('{:.2f}'.format(hdd[0]))
    
if __name__ == '__main__':
    main()
