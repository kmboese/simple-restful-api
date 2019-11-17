# 200's
HTTP_OK = 200
HTTP_CREATED = 201

# 400's
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404

### HTTP Functions ###

# Returns True if a given error code is an HTTP error, False otherwise
def isError(code):
    return code == HTTP_BAD_REQUEST or code == HTTP_NOT_FOUND

