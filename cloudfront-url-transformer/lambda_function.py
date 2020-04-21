import re


FILE_MATCHER = re.compile(".*/[^/]+\\.[^/]+$")


def lambda_handler(event, context):

    request = event["Records"][0]["cf"]["request"]

    # Redirect www.emended.com to emended.com
    if request["headers"]["host"] == "www.emended.com":
        return redirect_to("https://emended.com" + request["uri"])

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
