from cyaron import Sequence
import random
from utils.Configs import redirectOutput


def GenerateRandomSequences(length, maxI, minI=0) -> list:
    S = Sequence(lambda i, f: random.randint(minI, maxI))
    res = [[str(length)], [""]]
    for i in S.get(0, length - 1):
        res[-1][0] += str(i) + " "
    redirectOutput(res)
    return res


def GenerateRecursionSequences2(length, ratioOfFormer, indexOfFormer, constant, startNum: list) -> list:
    if len(startNum) != 2:
        return -1
    S = Sequence(lambda i, f: ratioOfFormer*((i - 1)**indexOfFormer) + constant, startNum)
    res = [[str(length)], [""]]
    for i in S.get(0, length - 1):
        res[-1][0] += str(i) + " "
    redirectOutput(res)
    return res


def GenerateRecursionSequences3(length, ratioOfFormer1, indexOfFormer1, ratioOfFormer2, indexOfFormer2, constant, startNum: list) -> list:
    if len(startNum) != 3:
        return -1
    S = Sequence(lambda i, f: ratioOfFormer1*((i - 1)**indexOfFormer1) + ratioOfFormer2*((i - 2)**indexOfFormer2) + constant, startNum)
    res = [[str(length)], [""]]
    for i in S.get(0, length - 1):
        res[-1][0] += str(i) + " "
    redirectOutput(res)
    return res


if __name__ == '__main__':
    x = GenerateRandomSequences(10, 100)
    print(x)
    print(type(x))
    x = GenerateRecursionSequences2(10, 100, 2, 3, [1, 2])
    print(x)
    print(type(x))
    x = GenerateRecursionSequences3(10, 100, 2, 3, 4, 5, [1, 2, 3])
    print(x)
    print(type(x))
