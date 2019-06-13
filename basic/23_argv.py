# argument 받는 방법
# 예제
# > python 23_argv.py aaa bbb ccc
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')