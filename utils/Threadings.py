import threading
import time


class ThreadingPool:
    def __init__(self):
        super().__init__()
        self.threadingList = []

    def CreateThreading(self, Function, Args: tuple = (), Name="-1", Daemon=False):
        if Name == "-1":
            threadName = "Threading{}".format(len(self.threadingList) + 1)
        else:
            threadName = Name
        if len(Args) > 0:
            self.threadingList.append(threading.Thread(target=Function, args=Args, name=threadName, daemon=Daemon))
        else:
            self.threadingList.append(threading.Thread(target=Function, name=threadName, daemon=Daemon))

    def StartAllThreading(self, ToJoin=False):
        cnt = 0
        for threading_i in self.threadingList:
            if "::Started" in threading_i.name:
                continue
            self.threadingList[cnt].name += "::Started"
            self.threadingList[cnt].start()
            if ToJoin:
                for K in self.threadingList:
                    if K.name == self.threadingList[cnt].name:
                        break
                    if K.is_alive():
                        K.join()
            cnt += 1

    def ShowThreadingStatus(self):
        flag = 0
        for threading_i in self.threadingList:
            flag = 1
            print(threading_i.name + ' is ' + str("" if threading_i.is_alive() else "not ") + ' alive ')
        if not flag:
            print("No Threading alive")

    def DelFinishedThreading(self):
        cnt = 0
        for threading_i in self.threadingList:
            if not threading_i.is_alive() and "::Started" in threading_i.name:
                self.threadingList.pop(cnt)
                cnt -= 1
            cnt += 1

    def CleanAllThreading(self):
        self.threadingList = []

    def FindThreading(self, Name: str):
        for threading_i in self.threadingList:
            if threading_i.name == Name:
                return threading_i
        return -1

    def ReturnNotFinishedThreading(self):
        List = []
        for threading_i in self.threadingList:
            if threading_i.is_alive():
                List.append(threading_i)
        return List


def Showlog(T):
    time.sleep(T)
    print("LOG!{}".format(T))


def creatTimeTasks(RunTime: int, Function, Args: tuple = ()):  # 可以实现计时任务
    X = ThreadingPool()
    X.CreateThreading(Function, Args)
    X.StartAllThreading()
    time.sleep(RunTime)


if __name__ == '__main__':
    """t1 = threading.Thread(target=Showlog, args=(2,))
    t2 = threading.Thread(target=Showlog, args=(1, t1))
    t1.start()
    t2.start()"""
    # creatTimeTasks(3)
    pass

