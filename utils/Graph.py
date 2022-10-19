from cyaron import Graph
from utils.Configs import redirectOutput

"""
graph = Graph.graph(n, m) # 生成一个n点，m边的无向图，边权均为1
graph = Graph.graph(n, m, directed=True, weight_limit=(5, 300)) # 生成一个n点，m边的有向图，边权范围是5到300
graph = Graph.graph(n, m, weight_limit=20) # 生成一个n点，m边的无向图，边权范围是1到20
graph = Graph.graph(n, m, weight_gen=my_func) # 生成一个n点，m边的无向图，使用自定义随机函数my_func的返回值作为边权
graph = Graph.graph(n, m, self_loop=False, repeated_edges=False) # 生成一个n点，m边的无向图，禁止重边和自环
# 以上的directed, weight_limit, weight_gen参数，对如下的所有函数都有效。
graph = Graph.hack_spfa(n) # 生成一个n点，1.5*n(下取整)边的图，具有卡SPFA的特点
graph = Graph.hack_spfa(n, extra_edge=m) # 生成一个n点，1.5*n+m(下取整)边的图，具有卡SPFA的特点
# 下列方法生成的图保证连通
# 支持 self_loop, repeated_edges, weight_limit, weight_gen 参数，但不支持 directed，DAG 的 self_loop 默认为 False
graph = Graph.DAG(n, m) # 生成一个 n 点，m 边的有向无环图
graph = Graph.DAG(n, m, loop=True) # 生成一个 n 点，m 边的有向有环图
graph = Graph.UDAG(n, m) # 生成一个 n 点，m 边的无向联通图
"""


def GenerateGraph(NFP, NFE, Directed, selfLoop=False, repeatedEdges=False, WeightRange=-1):
    if WeightRange == -1:
        graph = Graph.graph(NFP, NFE, directed=Directed, self_loop=selfLoop,
                            repeated_edges=repeatedEdges)
    else:
        graph = Graph.graph(NFP, NFE, directed=Directed, weight_limit=WeightRange, self_loop=selfLoop,
                            repeated_edges=repeatedEdges)
    res = [[str(NFP) + " " + str(NFE)]]
    for i in str(graph).split("\n"):
        res.append([i])
    redirectOutput(res)
    return res


def GenerateGraphHackSpfa(n, Extra_edge=0):
    graph = Graph.hack_spfa(n, extra_edge=Extra_edge)
    res = [[str(n) + " " + str(len(str(graph).split("\n")))]]
    for i in str(graph).split("\n"):
        res.append([i])
    redirectOutput(res)
    return res


def GenerateGraphDAG(NFP, NFE, Directed=False, HasLoop=False):
    if NFE < NFP - 1:
        NFE = NFP - 1
    if Directed:
        graph = Graph.DAG(NFP, NFE, loop=HasLoop)
    else:
        graph = Graph.UDAG(NFP, NFE, loop=HasLoop)
    res = [[str(NFP) + " " + str(NFE)]]
    for i in str(graph).split("\n"):
        res.append([i])
    redirectOutput(res)
    return res


if __name__ == '__main__':
    x = GenerateGraphDAG(5, 0)
    print(x)
    print(type(x))
    x = GenerateGraphHackSpfa(5, 1)
    print(x)
    print(type(x))
    x = GenerateGraph(5, 1, 1)
    print(x)
    print(type(x))
