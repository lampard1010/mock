tasks = {
    "data": {
        "loginName": "admin",
        "roles": 1,
        "permissions": 1,
        "active": 1
    },
    "stateCode": {
        "code": 0,
        "desc": "成功"
    },
    "statusText": "成功",
    "timestamp": "1500531770453",
    "success": 1
}

crif_init_s06 = {
    "data": {
        "reportId": "reportId00000000",
        "orderId": "india_(00000000)",
        "bizStatus": "S06"
    },
    "message": "SUCCESS",
    "status": 200
}

crif_s08 = {
    "data": {
        "reportId": "reportId00000000",
        "orderId": "india_(00000000)",
        "bizStatus": "S08"
    },
    "message": "SUCCESS",
    "status": 200
}

advance_pan_aadhaar_true = {
    "code": "SUCCESS",
    "message": "OK",
    "data": {
        "bindingStatus": "true"
    },
    "extra": "null",
    "pricingStrategy": "PAY",
    "transactionId": "xxxxxtrue"
}

advance_pan_aadhaar_false = {
    "code": "SUCCESS",
    "message": "OK",
    "data": {
        "bindingStatus": "false"
    },
    "extra": "null",
    "pricingStrategy": "PAY",
    "transactionId": "xxxxxfalse"
}

advance_pan_aadhaar_retry = {
    "code": "RETRY_LATER",
    "message": "Query failed,please retry later",
    "data": "null",
    "extra": "null",
    "transactionId": "xxxxxretry",
    "pricingStrategy": "FREE"
}

advance_pan_aadhaar_error_1 = {
    "code": "PARAMETER_ERROR",
    "message": "Parameter should not be empty",
    "data": "null",
    "extra": "null",
    "transactionId": "xxxxxerror1",
    "pricingStrategy": "FREE"
}

advance_pan_aadhaar_error_2 = {
    "code": "PARAMETER_ERROR",
    "message": "Please check PAN",
    "data": "null",
    "extra": "null",
    "transactionId": "xxxxxerror2",
    "pricingStrategy": "FREE"
}

advance_pan_aadhaar_error_3 = {
    "code": "PARAMETER_ERROR",
    "message": "Please check Aadhaar number",
    "data": "null",
    "extra": "null",
    "transactionId": "xxxxxerror3",
    "pricingStrategy": "FREE"
}

black_list_token = {
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

black_list_true = {
    "blackmodel": {
        "IsBlack": "true",
        "IsOverDue": "false"
    },
    "Message": 0,
    "error": {
        "ErrorCode": 0,
        "ErrorMsg": "成功",
        "Msg": "测试mock"
    }
}

black_list_false = {
    "blackmodel": {
        "IsBlack": "false",
        "IsOverDue": "false"
    },
    "Message": 0,
    "error": {
        "ErrorCode": 0,
        "ErrorMsg": "成功",
        "Msg": "测试mock"
    }
}