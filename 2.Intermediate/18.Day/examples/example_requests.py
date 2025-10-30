"""
examples/example_requests.py
Day 18 — Working with APIs (requests + JSON)
Run: python examples/example_requests.py
This script demonstrates:
 - GET a single resource
 - GET a list of resources with query params
 - POST new resource
 - Error handling and timeouts

Note: This uses https://jsonplaceholder.typicode.com which is a free test API.
"""

import requests

BASE = "https://jsonplaceholder.typicode.com"

def get_single_post(post_id):
    """GET /posts/{post_id} — return a dict for the post or None on failure"""
    url = f"{BASE}/posts/{post_id}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()  # raise HTTPError for bad codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching post {post_id}: {e}")
        return None
    try:
        data = resp.json()
    except ValueError:
        print("Invalid JSON received")
        return None
    return data

def get_posts_by_user(user_id):
    """GET /posts?userId={user_id} — returns a list of posts"""
    url = f"{BASE}/posts"
    try:
        resp = requests.get(url, params={"userId": user_id}, timeout=5)
        resp.raise_for_status()
        return resp.json()  # list of posts
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def create_post(title, body, user_id):
    """POST /posts — create a new post (JSONPlaceholder will return created data)"""
    url = f"{BASE}/posts"
    payload = {"title": title, "body": body, "userId": user_id}
    try:
        resp = requests.post(url, json=payload, timeout=5)
        resp.raise_for_status()
        return resp.json()  # created object
    except requests.exceptions.RequestException as e:
        print("Error creating post:", e)
        return None

def main():
    print("== Get single post (id=1) ==")
    post = get_single_post(1)
    if post:
        print("Title:", post.get("title"))
        print("Body:", post.get("body")[:60], "...")  # print first 60 chars

    print("\n== Get posts by user (userId=1) ==")
    posts = get_posts_by_user(1)
    print("Number of posts:", len(posts))
    if posts:
        print("First post title:", posts[0].get("title"))

    print("\n== Create a new post (simulate POST) ==")
    new = create_post("Hello from Day 18", "This body was sent via requests.post", user_id=99)
    print("Created post response:", new)

if __name__ == "__main__":
    main()