from pathlib import Path

def handler(request):
    root = Path(__file__).parent.parent
    index = root / "templates" / "index.html"
    if index.exists():
        content = index.read_text(encoding="utf-8")
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": content,
        }
    return {"statusCode": 404, "body": "Not found"}
