import argparse
import re


def solve(t):
    rex = re.compile(r"watch\?v=[^\"※\\\\&\.]*")  # ※ \\\\ &
    res = rex.findall(t)
    res_n = list(set(res))
    return ['http://wwww.youtube.com/'+i for i in res_n if len(i)>=18] # 提取长度19以上的字符串，去掉废串


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='youtube_rex.py')
    parser.add_argument('-f', type=str, default='', help='File path')
    opt = parser.parse_args()
    try:
        file = open(opt.f)
        for i in solve(file.read()): print(i)
    except:
        print("File does not exist.")

