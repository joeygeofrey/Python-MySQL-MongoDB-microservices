import os, requests

# create login route to communicate with auth service
def login(request):
    auth = request.authorization
    if not auth:
        return None, ('missing credentials', 401)

    # create basic auth tuple
    basicAuth = (auth.username, auth.password)

    # send http call to auth service
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login",
        auth=basicAuth
    )

    # check response
    if response.status_code == 200:
        return response.txt, None
    else:
        return None, (response.text, response.status_code) 