import re
from flask import Flask, render_template, request
from chatbot_graph import *

# 定义读取关键字和链接的函数
def generate_keyword_links_from_file(file_path):
    # 创建一个空的字典来存储关键字和链接的映射
    keyword_links = {}

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        # 遍历文件中的每一行
        for line in file:
            # 去除行中的空格和换行符
            disease = line.strip()
            # 跳过空行
            if not disease:
                continue
            # 生成对应的链接，但不直接跳转
            link = f"http://127.0.0.1:5000/view?search_term={disease}"
            # 将疾病名称和链接添加到字典中
            keyword_links[disease] = link

    return keyword_links


# 指定文件路径
file_path = './dict/disease.txt'  # 确保路径正确

# 生成关键字和链接的映射
keyword_links = generate_keyword_links_from_file(file_path)

# 问答类
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def replace_keywords_with_links(self, text):
        # 根据关键字长度从长到短排序，避免嵌套问题
        sorted_keywords = sorted(keyword_links.items(), key=lambda x: len(x[0]), reverse=True)

        # 使用正则表达式确保单词边界匹配
        for keyword, link in sorted_keywords:
            # 使用\b确保单词边界
            pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)
            text = pattern.sub(f'<a href="{link}" target="_blank">{keyword}</a>', text)

        return text

    def chat_main(self, sent):
        robot_message = '您好，我是医药智能助理，希望可以帮到您。如果没答上来，可以试着将问题提问更详细一些。祝您身体棒棒！'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return robot_message

        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)

        if not final_answers:
            return robot_message

        # 使用替换函数处理最终答案
        final_answers = [self.replace_keywords_with_links(answer) for answer in final_answers]

        return '\n'.join(final_answers)  # 将答案合并为一个字符串返回

# Flask应用
app = Flask(__name__)

handler = ChatBotGraph()

@app.route('/')
def index():
    return render_template('question.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    robot_message = handler.chat_main(user_message)
    return {'user_message': user_message, 'robot_message': robot_message}

if __name__ == '__main__':
    app.run(debug=True)
