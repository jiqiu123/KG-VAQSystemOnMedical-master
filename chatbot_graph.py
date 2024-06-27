
from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        robot_message = '您好，我是医药智能助理，希望可以帮到您。如果没答上来，可以试着将问题提问更详细一些。祝您身体棒棒！'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return robot_message
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return robot_message
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        user_message = input('用户:')
        robot_message = handler.chat_main(user_message)
        data = handler.classifier.classify(user_message)
        search_keywords = ['disease']
        result = extract_keywords(data, search_keywords)
        for r in result:
            print(r)
        print('问答机器人:', robot_message)



