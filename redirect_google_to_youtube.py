from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if "google.com" in flow.request.pretty_host:
        flow.request.host = "www.youtube.com"
        flow.request.path = "/"