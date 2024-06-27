from flask import Flask, render_template,request
from py2neo import Graph
from view import non_recursive_query
from chatnet import ChatBotGraph
import webbrowser

app = Flask(__name__)

# 连接到Neo4j数据库
uri = "bolt://localhost:7687"
username = "neo4j"
password = "hzw147536928"
graph = Graph(uri, auth=(username, password))

handler = ChatBotGraph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    search_term = request.args.get('search_term', '')
    links = []
    non_recursive_query(search_term, 3, links)
    return render_template('view.html', links=links)


@app.route('/question')
def search():
    return render_template('question.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    robot_message = handler.chat_main(user_message)
    return {'user_message': user_message, 'robot_message': robot_message}

if __name__ == '__main__':
    app.run(debug=True)
