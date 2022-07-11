from flask import url_for

def test_app(app):
    with app.app_context(), app.test_client() as client:
        resp = client.get(url_for("index"))
        assert resp.status_code == 200
