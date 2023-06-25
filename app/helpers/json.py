from flask import jsonify

class Json:
    @staticmethod
    def response(data=None, message=None, status_code=200, error=None):
        response = {}
        
        if data is not None:
            response['data'] = data
        if message is not None:
            response['message'] = message
        
        if status_code >= 400:
            if error is not None:
                response['error'] = error
        
        return jsonify(response), status_code

