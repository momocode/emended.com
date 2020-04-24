import re


FILE_MATCHER = re.compile(".*/[^/]+\\.[^/]+$")

OLD_URIS = {
    "/user-guide-for-instructors.pdf": "/guides/user-guide-for-instructors.pdf",
    "/user-guide-for-students.pdf": "/guides/user-guide-for-students.pdf",
    "/user-guide-for-team-admins.pdf": "/guides/user-guide-for-team-admins.pdf",
}


def lambda_handler(event, context):

    request = event["Records"][0]["cf"]["request"]

    # Compatibility redirectors for old uris
    if request["uri"] in OLD_URIS:
        return redirect_to(OLD_URIS[request["uri"]])

    # Canonicalize uris
    new_uri = redirect_uri(request["uri"])
    if new_uri != request["uri"]:
        return redirect_to(new_uri)

    if request["uri"].endswith("/"):
            request["uri"] += "index.html"

    return request


def redirect_to(new_uri):
        return {
            "status": "301",
            "statusDescription": "Moved Permanently",
            "headers": {
                "location": [{
                    "key": "Location",
                    "value": new_uri
                }]
            }
        }


def redirect_uri(uri):

    if not is_a_file(uri) and not uri.endswith("/"):
        uri += "/"

    return uri


def is_a_file(uri):
    return FILE_MATCHER.match(uri) is not None
