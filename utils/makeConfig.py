conf = """n_tests 10
n_sample_tests 0
n_ex_tests 0
input_pre w
input_suf in
output_pre w
output_suf out
time_limit {}
memory_limit {}
output_limit 64
use_builtin_judger on
use_builtin_checker {}
"""

"""
如果输出结果为整数序列，那么用 ncmp 就够了。
ncmp 会比较标准答案的整数序列和选手输出的整数序列。
如果是忽略所有空白字符，进行字符串序列的比较，可以用 wcmp。
如果你想按行比较（不忽略行末空格，但忽略文末回车），可以使用 fcmp。
"""

from utils.Configs import configLocationDataPool
import os


def processConf(time_limit: int, memory_limit: int, checker: str):
    with open(os.path.join(configLocationDataPool(), "problem.conf"), "w", encoding="utf-8") as f:
        f.write(conf.format(time_limit, memory_limit, checker))
