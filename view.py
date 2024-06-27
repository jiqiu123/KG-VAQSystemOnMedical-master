from flask import Flask, render_template, jsonify
from py2neo import Graph

app = Flask(__name__)

# 连接到Neo4j数据库
uri = "bolt://localhost:7687"
username = "neo4j"
password = "hzw147536928"
graph = Graph(uri, auth=(username, password))

Max_num=200  #可视化界面生成最多的节点数
depth=3      #递归深度

'''def recursive_query(source, n, links):
    if n <= 0:
        return
    query = f"""
    MATCH (n {{name: '{source}'}})-[r]->(m)
    RETURN n.name AS source, type(r) AS rela, m.name AS target
    """
    result = graph.run(query)
    for record in result:
     if len(links)<=Max_num:
        target = record["target"]
        links.append({
            "source": source,
            "rela": record["rela"],
            "target": target
        })
        recursive_query(target, n - 1, links)
        print(links)'''#递归方法


def non_recursive_query(source, n, links):
    stack = [(source, n)]
    visited = set()  # 记录已经访问过的节点

    while stack:
        current_node, depth = stack.pop()

        # 如果当前节点已经访问过或者达到了指定的深度，直接跳过
        if current_node in visited or depth <= 0:
            continue

        # 执行查询
        query = f"""
            MATCH (n {{name: '{current_node}'}})-[r]->(m)
            RETURN n.name AS source, type(r) AS rela, m.name AS target
        """
        result = graph.run(query)
        # 将当前节点标记为已访问
        visited.add(current_node)

        for record in result:
            if len(links) >= Max_num:
                break  # 达到最大节点数，跳出循环
            target = record["target"]
            links.append({
                "source": current_node,
                "rela": record["rela"],
                "target": target
            })
            stack.append((target, depth - 1))

    return links


@app.route('/')
def index():
    # 初始化links列表
    links = []
    # 非递归查询
    non_recursive_query('感冒', depth, links)
    # 将数据传递给模板
    return render_template('view.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
