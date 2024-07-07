from rest_framework.response import Response

def make_response(data, status_code, custom_data = False):
    """ Customise response object according to data and status code """

    if custom_data :
        if not isinstance(data, dict):
            raise ValueError("For custom data, given 'data' should be a dict")
        response_data = data

    elif 400 <= status_code < 600 :
        response_data = { "error": data }

    elif 100 <= status_code < 400 :
        response_data = { "message": data }
    
    else:
        raise ValueError("Invalid status code")
    
    
    return Response( data=response_data, status=status_code )