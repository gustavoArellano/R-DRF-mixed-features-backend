from .mixed_features_api.serialziers import UserSerializer

def my_jwt_response_handler(token, user = None, request = None): 
    return {
        'token': token,
        'user': UserSerializer(user, context = {'request': request}).data
    }