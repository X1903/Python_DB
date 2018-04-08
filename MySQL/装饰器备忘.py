# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# def memo(f):
#     memos = {}
#     def helper(x):
#         if x not in memos:
#             memos[x] = f(x)
#         return memos[x]
#     return helper
#
# fib = memo(help)
# fib(10)

from flask import Flask
app = Flask(__name__)

@app.route('/helle')
def hello_world():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)