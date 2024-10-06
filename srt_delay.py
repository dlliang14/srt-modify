import sys
import re
from datetime import datetime, timedelta


# 00:01:00,310 --> 00:01:01,680
def delay_srt(srt_file, delay_time):
    # delay_time单位为秒
    with open(srt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        new_name = srt_file.split('.')[0] + '_delay.srt'
        with open(new_name, 'a', encoding='utf-8') as f:
            for line in lines:
                if re.match(r'^\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+$', line):
                    time1, time2 = line.strip().split(' --> ')
                    h1, m1, s1, ms1 = parse_time(time1)
                    h2, m2, s2, ms2 = parse_time(time2)
                    h1, m1, s1, ms1 = time_change([h1, m1, s1, ms1], delay_time)
                    h2, m2, s2, ms2 = time_change([h2, m2, s2, ms2], delay_time)
                    msg = '%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d\n' % (int(h1), int(m1), int(s1), int(ms1), int(h2), int(m2), int(s2), int(ms2))
                    print(msg)
                    f.write(msg)
                else:
                    f.write(line)


# 解析 00:01:00,310 --> 00:01:01,680
def parse_time(time_str):
    h, m, s = map(str, re.split(r'[:]', time_str))
    # print(h, m, s)
    s, ms = map(str, re.split(r'[,.]', s))
    # print(s, ms)
    return h, m, s, ms


# 转换成时间格式 增减时间 然后转换回去
def time_change(raw_list,delay_time):
    # raw_list = [h1, m1, s1, ms1]
    h, m, s, ms = raw_list
    # 转换数字
    h = int(h)
    m = int(m)
    s = int(s)
    time_obj = datetime(1, 1, 1, h, m, s)
    print(time_obj)
    time_obj = time_obj + timedelta(seconds=delay_time)
    print(time_obj)
    # 提取新的 h m s 记得转换字符串 不足2位补0
    h = str(time_obj.hour).zfill(2)
    m = str(time_obj.minute).zfill(2)
    s = str(time_obj.second).zfill(2)
    return h, m, s, ms


if __name__ == '__main__':
    
    ## 方法一 直接在代码中指定文件和延迟时间
    # delayfile = r"xxx.srt"
    # delaytime = -30
    # delay_srt(delayfile, delaytime)

    # 方法二 通过命令行参数传入文件和延迟时间
    if len(sys.argv) != 3:
        print('Usage: python srt_delay.py xxx.srt -30')
        sys.exit(1)
    delayfile = sys.argv[1]
    delaytime = int(sys.argv[2])
    delay_srt(delayfile, delaytime)
    print('Done')
