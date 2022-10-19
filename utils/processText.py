import json
from utils.checkType import typeChecker
from utils.Configs import configFun
from utils.Explain import FunctionExplainer


def exportSingle(TextIn: str):
    # print(TextIn)  # """{FunctionName:argsRandomSequences,arg1:[11],arg2:[2],arg3:[3]}"""
    z = json.loads(TextIn)
    functionargList = []
    for i in configFun:
        # print(i['Title'], z['FunctionName'])
        if "args" + i['Title'] == z['FunctionName']:
            functionargList = i["args"]
            break
    # print(functionargList)  # ["图的点数(int)", "多余的边数(int)"]
    if len(functionargList) == 0:
        return "ERROR::未匹配到函数"
    funCnt = 0
    res = []
    for i in functionargList:
        funCnt += 1
        dataType = i[str(i).find("(") + 1: str(i).find(")")]
        argInput = z["arg{}".format(funCnt)]
        # print(i, dataType, argInput)  # 多余的边数(int) int ['12']
        res.append([i.replace(i[str(i).find("("): str(i).find(")")+1], ""), dataType, argInput])
    return res


def checkIfValidate(temp):
    tempNew = []
    # [['单词长度范围(min,max)', 'min,max', ['1,10']], ['字符集(str)', 'str', ['12r']]]
    X = typeChecker("")
    for i in temp:
        if i[1] == '1/0' or i[1] == '0/1':
            Type = 'bool'
        else:
            Type = i[1]
        arg = i[2][0]
        if Type == "min,max":
            X.string = arg.split(",")[0]
            if "int" not in X.check():
                return -1
            first = X.convert("int")
            X.string = arg.split(",")[1]
            if "int" not in X.check():
                return -1
            second = X.convert("int")
            tempNew.append([i[0].replace(i[0][str(i[0]).find("("): str(i[0]).find(")") + 1], ""), "int,int", [first, second]])
        else:
            X.string = arg
            if Type not in X.check():
                return -1
            tempNew.append([i[0].replace(i[0][str(i[0]).find("("): str(i[0]).find(")")+1], ""), Type, X.convert(Type)])
    return tempNew


def translate(FunName, Temp):
    return "DEBUG"


def Validate(TextIn: str):
    lines = TextIn.replace("\r", "").replace(" ", "").split("\n")
    temps = {}
    sucMsg = ["::None::"]
    for i in lines:  # 每一条数据块为i
        if len(i) == 0:
            continue
        FunName = json.loads(i)['FunctionName'].replace("args", "")
        temp = exportSingle(i)
        temp = checkIfValidate(temp)  # 对每一条数据块进行合法性验证
        if temp == -1:  # 如果不合法
            return 0, ["数据格式有误，请检查后再提交"], 0
        else:  # 否则就应该对其进行解释，返回解释文档 TODO:解释文档
            print("数据块合法：{}:{}".format(FunName, temp))
            temps[FunName] = temp
            X = FunctionExplainer(temps)
            print(X.explain())
            sucMsg = X.explain().split("。")
    return 1, sucMsg, temps  # 返回值为：状态码，解释文档，和转换后的数据

"""
temps:
{
    FunName_i: [arg_i: value_i]
}
"""