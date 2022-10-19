class typeChecker:
    def __init__(self, strings: str):
        self.string = strings
        self.possibleType = []

    def _checkIfBool(self):
        if self.string == '0' or self.string == '1':
            return True
        else:
            return False

    def _checkIfNum(self):
        try:
            _k = int(self.string)
            return True
        except Exception as e:
            return False

    def _checkIfFloat(self):
        try:
            _k = float(self.string)
            return True
        except Exception as e:
            return False

    def _checkIfList(self):
        try:
            _k = list(self.string)
            return self.string[0] == '[' and self.string[-1] == ']'
        except Exception as e:
            return False

    def _checkIfTuple(self):
        try:
            _k = tuple(self.string)
            return self.string[0] == '(' and self.string[-1] == ')'
        except Exception as e:
            return False

    def _checkIfDict(self):
        try:
            _k = eval(self.string)
            return self.string[0] == '{' and self.string[-1] == '}'
        except Exception as e:
            return False

    def check(self):
        self.possibleType = []
        if self._checkIfBool():
            self.possibleType.append("bool")
        if self._checkIfNum():
            self.possibleType.append("int")
        if self._checkIfFloat():
            self.possibleType.append("float")
        if self._checkIfList():
            self.possibleType.append("list")
        if self._checkIfDict():
            self.possibleType.append("dict")
        if self._checkIfTuple():
            self.possibleType.append("tuple")
        self.possibleType.append("str")
        return self.possibleType

    def convert(self, Type: str):
        if (Type not in self.check()) or (Type not in ["bool", "int", "float", "str"]):
            return "FAIL::不支持的类型转换"
        if Type == 'bool':
            return self.string == '1'
        elif Type == 'int':
            return int(self.string)
        elif Type == 'float':
            return float(self.string)
        else:
            return self.string


if __name__ == '__main__':
    z = "[\"1\",1.21]"
    print(z)
    checker = typeChecker(z)
    print(checker.check())