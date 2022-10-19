from utils.Configs import configFun


class FunctionExplainer:
    def __init__(self, temps: dict):
        self.temps = temps
        self.explainText = ""

    @staticmethod
    def explainSingle(startLine: int, FunName: str):
        # temp_i = self.temps[FunName]
        detail_i = ""
        for i in configFun:
            if i["Title"] == FunName:
                detail_i = i["Explain"]
                break
        if FunName in ["RandomGraph", "SpfaHacker", "DAG"]:
            return detail_i.format(startLine, "n", "m", "u", "v", "w")
        elif FunName in ["RandomSequences", "RecursionSequences2", "RecursionSequences3"]:
            return detail_i.format(startLine, "n")
        elif FunName in ["BinTree", "Tree"]:
            return detail_i.format(startLine, "n", "u", "v", "w")
        elif FunName == "Word":
            return detail_i.format(startLine)
        elif FunName == "Sentences":
            return detail_i.format(startLine)

    def explain(self):
        """temps:{
            FunName_i: [arg_i: value_i],
            ...
        }"""
        self.explainText = ""
        curPos = 1
        for i in self.temps:
            self.explainText += self.explainSingle(curPos, i)
            if i in ["RandomGraph", "DAG"]:
                curPos += self.temps[i][1][2] + 1
            elif i in ["RandomSequences", "RecursionSequences2", "RecursionSequences3", "Sentences"]:
                curPos += 2
            elif i in ["BinTree", "Tree"]:
                curPos += self.temps[i][0][2]
            elif i == "Word":
                curPos += 1
            elif i == "SpfaHacker":
                curPos += self.temps[i][0][2] + self.temps[i][1][2]
        return self.explainText
