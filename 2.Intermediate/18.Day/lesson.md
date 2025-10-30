# Day 18 — Working with APIs (using `requests` and JSON)

## Overview (community-friendly)
This lesson teaches you how to talk to web APIs using Python's `requests` library and how to work with JSON data returned by APIs. We'll keep explanations simple and step-by-step so you can follow along even if you're new to APIs.

**What you'll learn:**
- What an API is (simple explanation)
- How to make HTTP GET and POST requests with `requests`
- How to read and write JSON in Python
- How to handle errors and check response status
- Practical examples using the free JSONPlaceholder test API
- Exercises with answers

---

## 1) What is an API? (Short, simple)
An **API (Application Programming Interface)** is a way for one program to talk to another. For web APIs, you send HTTP requests (like visiting a URL in a browser) and receive data (often JSON) back. Think of an API as a waiter: you tell the waiter what you want, they ask the kitchen (server), and bring the result back to you.

## 2) JSON — the common data format
**JSON** (JavaScript Object Notation) is a text format for structured data. Example JSON for a user:
```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```
In Python, JSON maps to dictionaries and lists. Use `response.json()` in `requests` to convert JSON to Python objects.

## 3) Install `requests`
If you don't have `requests` installed:
```
pip install requests
```

## 4) Basic GET request (step-by-step)
1. Import requests.
2. Call `requests.get(url)` to make a GET request.
3. Check `response.status_code` (200 means OK).
4. Convert JSON using `response.json()` and handle it like a Python dict/list.
```python
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()  # Python dict
    print("Title:", data["title"])
else:
    print("Request failed:", resp.status_code)
```

## 5) POST request (create data)
A POST sends data to the server. JSONPlaceholder simulates creating data and returns what you send back (with an id).
```python
import requests
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "My new post",
    "body": "This is the body.",
    "userId": 5
}
resp = requests.post(url, json=payload)  # requests sets Content-Type: application/json
print(resp.status_code)
print(resp.json())
```

## 6) Common patterns & tips
- Always check `resp.status_code`. Common codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error.
- Use `resp.raise_for_status()` to raise an exception for HTTP errors.
- Use `timeout` parameter to avoid hanging: `requests.get(url, timeout=5)`
- For headers: `resp = requests.get(url, headers={"Accept": "application/json"})`
- Use query parameters: `requests.get(url, params={"userId": 1})` → builds `?userId=1` for you.

## 7) Example walkthrough (full, commented)
See `examples/example_requests.py` for a complete, commented example showing GET, list retrieval, POST, and error handling.

## 8) Security & etiquette
- Do **not** put secret API keys directly in code. Use environment variables.
- Respect API usage limits (rate limits).
- For private APIs, you'll usually need authentication (tokens, keys). We'll cover that later.

## 9) Exercises
See `exercises/README.md` for exercises and `exercises/answers.md` for solutions.

---
Happy learning — ask me to expand any section or to convert examples to other languages!