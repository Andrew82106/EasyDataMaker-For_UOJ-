from cyaron import Graph
from utils.Configs import redirectOutput
"""chain = Graph.chain(n) # 生成一条n个节点的链，是Graph.tree(n, 1, 0)的别名
flower = Graph.flower(n) # 生成一朵n个节点的菊花图，是Graph.tree(n, 0, 1)的别名
tree = Graph.tree(n) # 生成一棵n个节点的随机树
tree = Graph.tree(n, 0.4, 0.35) # 生成一棵n个节点的树，其中40%的节点呈现链状，35%的节点呈现菊花图状，剩余25%的节点随机加入
"""


def GenerateBinTree(NFP, ratioOfLeft, ratioOfRight):
    if ratioOfLeft + ratioOfRight > 1 or ratioOfRight*ratioOfLeft < 0:
        ratioOfRight = 0.5
        ratioOfLeft = 0.5
    binary_tree = Graph.binary_tree(NFP, ratioOfLeft, ratioOfRight)
    res = [[str(NFP)]]
    for i in str(binary_tree).split("\n"):
        res.append([i])
    redirectOutput(res)
    return res


def GenerateTree(NFP, ratioOfChain, ratioOfFlower):
    if ratioOfChain + ratioOfFlower > 1 or ratioOfChain*ratioOfFlower < 0:
        ratioOfChain = 0.5
        ratioOfFlower = 0.5
    tree = Graph.tree(NFP, ratioOfChain, ratioOfFlower)
    res = [[str(NFP)]]
    for i in str(tree).split("\n"):
        res.append([i])
    redirectOutput(res)
    return res


if __name__ == '__main__':
    print(GenerateBinTree(10, 0.9, 0.22))
    print(GenerateTree(10, 0.9, 0.22))
    """
    [['10'], ['1 2 1'], ['2 3 1'], ['2 6 1'], ['3 4 1'], ['4 5 1'], ['5 8 1'], ['5 9 1'], ['6 7 1'], ['8 10 1']]
    [['10'], ['1 2 1'], ['1 6 1'], ['1 7 1'], ['1 8 1'], ['1 9 1'], ['2 3 1'], ['3 4 1'], ['4 5 1'], ['5 10 1']]
    """