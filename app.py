from zhipuai import ZhipuAI
from flask import Flask, render_template, request, jsonify

# 创建Flask实例
app = Flask(__name__)

# 创建ZhipuAI实例，并传入APIKey
client = ZhipuAI(api_key="297cf1fe512572105c8a18d6c8217507.2JnaNOe5WjKrh7J3") # 请填写您自己的APIKey

# 定义根路由，返回index.html页面
@app.route('/')
def home():
    return render_template('index.html')

# 定义chat路由，接收POST请求，并返回json格式的响应
@app.route('/chat', methods=['POST'])
def chat():
    # 获取表单中的输入
    user_input = request.form.get('input')
    # 调用ZhipuAI的chat.completions.create方法，传入模型名称和输入
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user","content": user_input}
        ],
    )

    # 获取AI的回复
    ai_response = response.choices[0].message.content

    return jsonify(ai_response)

# 启动Flask实例
if __name__ == '__main__':
    app.run(debug=True)
