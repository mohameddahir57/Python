s/answers.md — Solutions (concise)

Exercise 1 — Fetch post title
```python
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/3", timeout=5)
r.raise_for_status()
print(r.json()["title"])
```

Exercise 2 — List titles by user
```python
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 2}, timeout=5)
r.raise_for_status()
for p in r.json():
    print(p["title"])
```

Exercise 3 — Create a post
```python
import requests
payload = {"title":"Test","body":"Body text","userId": 10}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, timeout=5)
r.raise_for_status()
print("Created id:", r.json().get("id"))
```

Exercise 4 — Handle 404
```python
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/999999", timeout=5)
if r.status_code == 404:
    print("Post not found")
else:
    r.raise_for_status()
    print(r.json())
```

Exercise 5 — Query params and filtering
```python
import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId":1}, timeout=5)
r.raise_for_status()
posts = r.json()
print("Returned posts:", len(posts))
```

Notes:
- These are example solutions. You can expand error handling and wrap into functions.
- If running in an offline environment, these requests will fail — run where HTTP access is allowed.