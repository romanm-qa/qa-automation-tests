import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["userId"] == 1
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)
    assert body["title"] != ""
    assert body["body"] != ""