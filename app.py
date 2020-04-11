from flask import Flask, request, jsonify, json
from flask_restplus import Resource, Api
from json_data import *

app = Flask(__name__)
api = Api(app, version='1.0', title='Mock Server',
          description='一个粗糙的模拟服务器'
          )

ns = api.namespace(name='', description='模拟三方接口返回')

@ns.route('/in/openapi/verification/v2/account-bind-check')
class aadhaar_bind_pan(Resource):
    def post(self):
        """
            模拟用户Aadhaar卡和Pan卡绑定状态
            Aadhaar卡号第一个数字从1-6有6种不同的返回情况
                example：

                    请求示例:
                    {
                        "pan": "ANTPJ5311R",
                        "aadhaar": "836089714748"
                    }

                    响应示例:
                    {
                        "code": "SUCCESS",
                        "message": "OK",
                        "data": {
                            "bindingStatus": "true"
                        },
                        "extra": "null",
                        "pricingStrategy": "PAY",
                        "transactionId": "xxxxxtrue"
                    }
                """
        data = json.loads(request.get_data(as_text=True))
        print(data["aadhaar"][0])
        if data["aadhaar"][0] == "1":
            return jsonify(advance_pan_aadhaar_true)
        elif data["aadhaar"][0] == "2":
            return jsonify(advance_pan_aadhaar_false)
        elif data["aadhaar"][0] == "3":
            return jsonify(advance_pan_aadhaar_retry)
        elif data["aadhaar"][0] == "4":
            return jsonify(advance_pan_aadhaar_error_1)
        elif data["aadhaar"][0] == "5":
            return jsonify(advance_pan_aadhaar_error_2)
        elif data["aadhaar"][0] == "6":
            return jsonify(advance_pan_aadhaar_error_3)
        else:
            return "你传的参数不对！"

@ns.route('/api/Intelligence/GetToken')
class get_blacklist_token(Resource):
    def get(self):
        """
            aitime黑名单获取token

                example：

                    响应示例:
                    {
                        "Token": "mock_token",
                        "ID": "test",
                        "UserName": "fastcash",
                        "Message": 0,
                        "error": {
                            "ErrorCode": 0,
                            "ErrorMsg": "成功",
                            "Msg": "null"
                        },
                        "pageNum": 0,
                        "pageSize": 0,
                        "pages": 0,
                        "tolal": 0
                    }
                """
        return jsonify(black_list_token)


@ns.route('/api/mydata/GetBlackInfo')
class get_blacklist_info(Resource):
    def post(self):
        """
            aitime黑名单获取击中情况
            pan卡第一位A时，击中；pan卡第一位B时，未击中，不考虑逾期情况

                example：

                    请求示例：
                    {
                        "CardID": "ASJPM5882N",
                        "Mobile": "8000000001"
                    }

                    响应示例:
                    {
                        {
                            "IsBlack": "true",
                            "IsOverDue": "false"
                        },
                        "Message": 0,
                        "error": {
                            "ErrorCode": 0,
                            "ErrorMsg": "成功",
                            "Msg": "测试mock"
                    }
                    """
        data = json.loads(request.get_data(as_text=True))
        if data["CardID"][0] == "A":
            return jsonify(black_list_true)
        else:
            return jsonify(black_list_false)






















ns.add_resource(aadhaar_bind_pan, '/in/openapi/verification/v2/account-bind-check')
ns.route(get_blacklist_token, '/api/Intelligence/GetToken')
ns.route(get_blacklist_info, '/api/mydata/GetBlackInfo')
# class TodoSimple(Resource):
#
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}
#
#     # put方法访问127.0.0.1:5000/todo1，form-data里传"data": "abc"数据
#     # 返回{
#     #       "todo1": "Sean"
#     #     }
#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    if __name__ == "__main__":
        app.run(
            host="0.0.0.0",
            port=5000,
            debug=True
        )
