import time
from utils.Threadings import ThreadingPool
from utils import Graph, Strings, Sequences, Tree
from utils import checkType
from utils.Configs import redirectOutput, configLocationRoot, configLocationDataPool, configLocationPythonCodeExecute
import os
import random
from utils.CodeExcuter import PythonExecuter


class Generator:
    def __init__(self):
        pass

    @staticmethod
    def ChooseFunction(FunName: str):
        if FunName == "RandomGraph":
            return Graph.GenerateGraph
        elif FunName == "SpfaHacker":
            return Graph.GenerateGraphHackSpfa
        elif FunName == "DAG":
            return Graph.GenerateGraphDAG
        elif FunName == "RandomSequences":
            return Sequences.GenerateRandomSequences
        elif FunName == "RecursionSequences2":
            return Sequences.GenerateRecursionSequences2
        elif FunName == "RecursionSequences3":
            return Sequences.GenerateRecursionSequences3
        elif FunName == "Word":
            return Strings.GenerateWord
        elif FunName == "Sentences":
            return Strings.GenerateSentences
        elif FunName == "BinTree":
            return Tree.GenerateBinTree
        elif FunName == "Tree":
            return Tree.GenerateTree

    def GenerateMini(self, FunctionList: dict):  # 函数列表
        # FunctionList: {"SpfaHacker":[['图的最多点数', 'int', 1], ['最多的多余的边数', 'int', 1]], ...}
        # 返回值大概长这样 [["1 2"], ['1 2 4 11 2 4 11 2 4 11 2 4 11 2 4 11 2 4 11 2 4 1 end'], ['1 4 53 2']]
        dataList = []
        Pool = ThreadingPool()
        redirectOutput(1, 1)
        for FunctionName in FunctionList:
            # Do Args
            Args = []
            for arg in FunctionList[FunctionName]:
                if "int" in checkType.typeChecker(str(arg[2])).check() and arg[2] > 5:
                    Args.append(5)
                else:
                    Args.append(arg[2])
            Pool.DelFinishedThreading()
            Pool.CreateThreading(self.ChooseFunction(FunctionName), tuple(Args), FunctionName, True)
            Pool.StartAllThreading(True)
            time.sleep(0.2)
        with open(os.path.join(configLocationRoot(), "utils", "pythonCodeExcute", "datain.txt"), "r",
                  encoding="utf-8") as f:
            x = f.read()
            for i in str(x).split("\n"):
                dataList.append([i])
        return dataList

    def GenerateInput(self, FunctionList: dict, amount: int):  # 函数列表，数据份数
        # FunctionList: {"SpfaHacker":[['图的最多点数', 'int', 1], ['最多的多余的边数', 'int', 1]], ...}
        Pool = ThreadingPool()
        for Bach in range(1, amount + 1, 1):
            redirectOutput(1, 1)
            for FunctionName in FunctionList:
                # Do Args
                Args = []
                for arg in FunctionList[FunctionName]:
                    if arg[1] == 'int':
                        Args.append(random.randint(1, arg[2]))
                    else:
                        Args.append(arg[2])
                Pool.CreateThreading(self.ChooseFunction(FunctionName), tuple(Args), FunctionName, True)
                Pool.StartAllThreading(True)
                while len(Pool.threadingList):
                    Pool.DelFinishedThreading()
            with open(os.path.join(configLocationPythonCodeExecute(), "datain.txt"), "r", encoding="utf-8") as F:
                with open(os.path.join(configLocationDataPool(), "w{}.in".format(Bach)), "w", encoding="utf-8") as f:
                    f.write(F.read())

    @staticmethod
    def GenerateOutput(CodeIn: str, amount: int):
        PyRunner = PythonExecuter()
        IOFileNameList = [["w{}.in".format(ID), "w{}.out".format(ID)] for ID in range(1, amount + 1, 1)]
        print("开始生成输出数据")
        PyRunner.ThreadingExecute(2, CodeIn, configLocationDataPool(), IOFileNameList)
        print("生成输出数据成功")
        for Input, Output in IOFileNameList:
            with open(os.path.join(configLocationDataPool(), Output), "r", encoding='utf-8') as f:
                X = f.read()
                if X == "EMPTY":
                    print("输出数据存在空项")
                    return 0
        return 1

    def GenerateDataFiles(self, FunctionList: dict, amount: int, CodeIn: str):
        self.GenerateInput(FunctionList, amount)
        print("生成输出文件成功")
        try:
            x = self.GenerateOutput(CodeIn, amount)
        except:
            x = 0
        return x


