import re


FILE_MATCHER = re.compile(".*/[^/]+\\.[^/]+$")

OLD_ARTICLES = [
    "top-10-most-useful-websites-for-everything-english-language",
    "top-5-english-grammar-sites-making-your-feedback-more-actionable",
    "top-5-english-language-game-sites-making-your-feedback-more-actionable",
    "top-5-english-writing-sites-making-your-feedback-more-actionable",
]

OLD_URIS = {
    "/en/": "/",
    "/en": "/",
    "/user-guide-for-instructors.pdf": "/guides/user-guide-for-instructors.pdf",
    "/user-guide-for-students.pdf": "/guides/user-guide-for-students.pdf",
    "/user-guide-for-team-admins.pdf": "/guides/user-guide-for-team-admins.pdf",
}

for slug in OLD_ARTICLES:
    old_new_uri = '/old/{0}/'.format(slug)
    OLD_URIS['/{0}'.format(slug)]  = old_new_uri
    OLD_URIS['/{0}/'.format(slug)] = old_new_uri

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

    # Normalize paths with trailing slash
    if not is_a_file(uri) and not uri.endswith("/"):
        uri += "/"

    # If someone were to request index.html directly, remove it
    if uri.endswith("/index.html"):
        uri = uri[:-10]

    return uri


def is_a_file(uri):
    return FILE_MATCHER.match(uri) is not None
