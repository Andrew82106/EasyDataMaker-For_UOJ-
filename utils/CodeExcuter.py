import os
from utils.Configs import configLocationPythonCodeExecute
import time
from utils.Threadings import ThreadingPool, creatTimeTasks


class PythonExecuter:
    def __init__(self, FunLocation=configLocationPythonCodeExecute(), StdinLocation=configLocationPythonCodeExecute(), StdoutLocation=configLocationPythonCodeExecute(), FunName="demo.py", StdinName="datain.txt", StdoutName="dataout.txt"):
        self.FunLocation = FunLocation
        self.StdinLocation = StdinLocation
        self.StdoutLocation = StdoutLocation
        self.FunRoute = os.path.join(self.FunLocation, FunName)
        self.StdinRoute = os.path.join(self.StdinLocation, StdinName)
        self.StdoutRoute = os.path.join(self.StdoutLocation, StdoutName)
        self.FunName = FunName
        self.InputFileName = StdinName
        self.OutputFileName = StdoutName

    def writeCode(self, codeIn: str):
        with open(self.FunRoute, "w", encoding="utf-8") as f:
            f.write(codeIn)

    def writeDatain(self, TextIn: str):
        with open(self.StdinRoute, "w", encoding="utf-8") as f:
            f.write(TextIn)

    def writeDataout(self, TextIn: str):
        with open(self.StdoutRoute, "w", encoding="utf-8") as f:
            f.write(TextIn)

    def ChangeStdin(self, StdinLocation=-1, StdinName=-1):
        if StdinLocation != -1:
            self.StdinLocation = StdinLocation
        if StdinName != -1:
            self.InputFileName = StdinName
        self.StdinRoute = os.path.join(self.StdinLocation, self.InputFileName)

    def ChangeStdout(self, StdoutLocation=-1, StdoutName=-1):
        if StdoutLocation != -1:
            self.StdoutLocation = StdoutLocation
        if StdoutName != -1:
            self.OutputFileName = StdoutName
        self.StdoutRoute = os.path.join(self.StdoutLocation, self.OutputFileName)
        with open(self.StdoutRoute, "w", encoding="utf-8") as f:
            f.write("EMPTY")

    def Execute(self, codeIn: str, dataIn_: str):
        self.writeDatain(dataIn_)
        self.writeCode(codeIn)
        os.chdir(self.FunLocation)
        content = os.popen("python {} < {}".format(self.FunName, self.StdinRoute)).read()
        self.writeDataout(content)
        return content

    def ThreadingExecute(self, TimeLimit: int, CodeIn: str, IODir: str, IOFileNameList: list):
        # Pool = ThreadingPool()
        self.ChangeStdin(StdinLocation=IODir)
        self.ChangeStdout(StdoutLocation=IODir)
        cnt = 0
        for IO in IOFileNameList:
            InputName = IO[0]
            OutputName = IO[1]
            self.ChangeStdin(StdinName=InputName)
            self.ChangeStdout(StdoutName=OutputName)
            with open(self.StdinRoute, "r", encoding="utf-8") as f:
                DataIn = f.read()
            print("::debug:: 执行第{}组数据生成中\n 输入文件为{} 输出文件为{}".format(cnt, InputName, OutputName))
            creatTimeTasks(TimeLimit, self.Execute, (CodeIn, DataIn))
            print("::debug:: 执行第{}组数据生成中\n 输入数据loca为：{}\n输出数据loca为：{}".format(cnt, self.StdinRoute, self.StdoutRoute))
            cnt += 1
            # Pool.CreateThreading(self.Execute, (CodeIn, DataIn), Daemon=True)
            # Pool.StartAllThreading(True)
        # time.sleep(TimeLimit)


class OnlineExecuter:
    def __init__(self, codeText: str):
        self.codeText = codeText


if __name__ == '__main__':
    X = PythonExecuter()
    codeLine = "x=eval(input())\nfor i in range(10):\n  print(\"Hello World!{}\\n\".format(x))"
    dataIn = "123"
    print(X.Execute(codeLine, dataIn))