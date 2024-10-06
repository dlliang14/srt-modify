# srt-modify
srt字幕工具箱微软商店竟然还收费！自己用python写了个脚本 统一修改srt字幕时间轴 偏移

# SRT Delay

这是一个用于调整 SRT 字幕文件时间的 Python 脚本。

## 使用方法

```sh
python [srt_delay.py](https://github.com/dlliang14/srt-modify/blob/main/srt_delay.py) <srt_file> <delay_time>
```

## 或者直接修改我的脚本 

```python
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
```
