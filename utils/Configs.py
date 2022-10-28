import os

configFun = [
    {
        "Title": "RandomGraph", "Dis": "生成一个随机的图", "args":
        ["图的最多点数(int)", "图的最多边数(int)", "有向/无向图(1/0)", "是否有自环(1/0)", "是否有重边(1/0)",
         "边权范围(min,max)"],
        "Explain": "输入第{0}行为两个数{1} {2}，代表点数和边数。之后的{2}行中每一行三个数{3} {4} {5}分别代表边的起点、边的终点和边的权值。"
    },
    {
        "Title": "SpfaHacker", "Dis": "生成一个Spfa Hacker(网格图)", "args":
        ["图的最多点数(int)", "最多的多余的边数(int)"],
        "Explain": "输入第{0}行为两个数{1} {2}，代表点数和边数。之后的{2}行中每一行三个数{3} {4} {5}分别代表边的起点、边的终点和边的权值。"
    },
    {
        "Title": "DAG", "Dis": "生成一个DAG(有向无环图)", "args":
        ["图的最多点数(int)", "图的最多边数(int)", "有向/无向图(1/0)", "是否有自环(1/0)"],
        "Explain": "输入第{0}行为两个数{1} {2}，代表点数和边数。之后的{2}行中每一行三个数{3} {4} {5}分别代表边的起点、边的终点和边的权值。"
    },
    {
        "Title": "RandomSequences", "Dis": "生成一个随机的序列", "args":
        ["序列最长长度(int)", "序列最大值(int)", "序列最小值(int)"],
        "Explain": "输入第{0}行为一个数，表示序列的长度{1}。接下来一行为{1}个整数表示整个序列。"
    },
    {
        "Title": "Word", "Dis": "从字符集中选取字符生成一个单词", "args":
        ["单词长度范围(min,max)", "字符集(str)"],
        "Explain": "输入第{0}行为一个单词。"
    },
    {
        "Title": "Sentences", "Dis": "从字符集中选取字符生成一个句子", "args":
        ["句子长度范围(min,max)", "字符集(str)", "首字符是否大写(0/1)"],
        "Explain": "输入第{0}行为一个数，代表句子的单词数量。之后的1行为这个句子，用空格隔开。"
    },
    {
        "Title": "BinTree", "Dis": "生成一棵二叉树", "args":
        ["点的最多个数(int)", "每一个节点是左儿子的概率(float)", "每一个节点是右儿子的概率(float)"],
        "Explain": "输入第{0}行为一个数{1}，代表数的点数。之后的{1}-1行中每一行三个数{2} {3} {4}分别代表树边的两个端点和边的权值。"
    },
    {
        "Title": "Tree", "Dis": "生成一棵树", "args":
        ["点的最多个数(int)", "节点以菊花形式分布的概率(float)", "节点以链形式分布的概率(float)"],
        "Explain": "输入第{0}行为一个数{1}，代表数的点数。之后的{1}-1行中每一行三个数{2} {3} {4}分别代表树边的两个端点和边的权值。"
    }
]
""",
    {
        "Title": "RecursionSequences2", "Dis": "生成一个满足公式f[i]=A*(i-1)^B+C的序列", "args":
        ["序列的最长长度(int)", "A的值(int)", "B的值(int)", "C的值(int)", "序列首项值最大为(int)"],
        "Explain": "输入第{0}行为一个数，表示序列的长度{1}。接下来一行为{1}个整数表示整个序列。"
    },
    {
        "Title": "RecursionSequences3", "Dis": "生成一个满足公式f[i]=A*(i-1)^B+C*(i-1)^D+E的序列", "args":
        ["序列的最长长度(int)", "A的值(int)", "B的值(int)", "C的值(int)", "D的值(int)", "E的值(int)", "序列首项值最大为(int)"],
        "Explain": "输入第{0}行为一个数，表示序列的长度{1}。接下来一行为{1}个整数表示整个序列。"
    },
    这玩意儿参数列表不对劲，但是一时半会儿改不了"""


def configLocationRoot() -> str:
    location = os.getcwd().replace("utils", "").replace("Datapool", "").replace("static", "").replace("templates", "").replace("/pythonCodeExcute", "")
    return location


def configLocationPythonCodeExecute() -> str:
    return os.path.join(configLocationRoot(), "utils", "pythonCodeExcute")


def configLocationDataPool() -> str:
    return os.path.join(configLocationRoot(), "DataPool")


def redirectOutput(res, ifClear=False):
    if ifClear:
        with open(os.path.join(configLocationRoot(), "utils", "pythonCodeExcute", "datain.txt"), "w",
                  encoding="utf-8") as f:
            f.write("")
        return
    with open(os.path.join(configLocationRoot(), "utils", "pythonCodeExcute", "datain.txt"), "a", encoding="utf-8") as f:
        for i in res:
            f.write(i[0] + "\n")

