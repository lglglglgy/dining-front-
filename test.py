from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 全局支持跨域
CORS(app)

@app.route('/api/login', methods=['POST'])
def login():
    # 接收前端传来的数据
    data = request.get_json()
    account = data.get('account')
    password = data.get('password')
    
    # 模拟登录逻辑
    if account == 'aaa' and password == '111':
        # 登录成功，返回用户数据
        user_data = {
            'name': '测试用户',
            'avatar': 'https://cdn.logo.com/hotlink-ok/logo-social.png'
        }
        return jsonify({
            'code': 200,
            'msg': '登录成功',
            'success': True,
            'data': user_data
        })
    else:
        # 登录失败
        return jsonify({
            'code': 200,
            'msg': '账号或密码错误',
            'success': False
        })

@app.route('/api/register', methods=['POST'])
def register():
    # 接收前端传来的数据
    data = request.get_json()
    account = data.get('account')
    password = data.get('password')
    
    # 模拟注册逻辑
    if account and password:
        # 注册成功，返回用户数据
        return jsonify({
            'code': 200,
            'msg': '注册成功',
            'success': True,
            'data': {
                'name': '测试用户',
                'avatar': 'https://cdn.logo.com/hotlink-ok/logo-social.png'
            }
        })
    else:
        # 注册失败
        return jsonify({
            'code': 200,
            'msg': '账号或密码不能为空',
            'success': False
        })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)