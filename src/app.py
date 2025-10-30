from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, NEU!'  # 作业要求修改为 NEU，不是 World

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 端口 5000，后续预览要用
