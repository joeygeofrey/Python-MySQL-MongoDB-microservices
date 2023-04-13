import os, requests

# take request to validate token
def token(request):
    if not "Authorization" in request.headers:
        return None, ("missing credentials", 401)
    
    # set token from request
    token = request.headers["Authorization"]

    # return none if token is empty
    if not token:
        return None, ("missing credentials", 401)
    
    # send http call to auth service
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization": token},
    )

    # check response
    if response.status_code == 200:
        return response.txt, None
    else:
        return None, (response.text, response.status_code)