from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if "google.com" in flow.request.pretty_host:
        flow.request.host = "www.youtube.com"
        flow.request.port = 443 if flow.request.scheme == "https" else 80
        flow.request.path = "/"
        flow.request.scheme = "https"  # Assuming you want to redirect to HTTPS YouTube