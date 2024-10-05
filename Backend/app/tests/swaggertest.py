from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger UI 配置
SWAGGER_URL = '/swagger'  # 将 Swagger UI 注册到根路径
API_URL = '/static/swagger.json'  # 指定 Swagger 文档的路径，通常是一个 JSON 文件
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI 的 URL
    API_URL,  # Swagger 文档的 URL
    config={
        'app_name': "My API"  # 配置 Swagger UI 的应用名称
    }
)

# 注册 Swagger UI 蓝图到应用中
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)  # 将 Swagger UI 蓝图注册到应用中

@app.route('/', methods=['GET'])  # 定义一个新的路由，响应 GET 请求

def a():
    return jsonify(message="Hello, World!")  # 返回一个 JSON 响应，包含消息 "Hello, World!"

if __name__ == '__main__':  # 检查是否在主程序中运行
    app.run(debug=True)  # 启动 Flask 应用，开启调试模式
