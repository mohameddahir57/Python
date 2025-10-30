# Exercises — Day 18 (Working with APIs)

Each exercise is short. Try to solve them by writing small Python scripts using `requests`.

1. **Exercise 1 — Fetch post title**
   - Make a function that fetches post id 3 from JSONPlaceholder and prints its title.

2. **Exercise 2 — List titles by user**
   - Fetch all posts by userId=2 and print the title of each post (one per line).

3. **Exercise 3 — Create a post**
   - Use POST to create a post with a title and body. Print the `id` field from the response.

4. **Exercise 4 — Handle 404**
   - Try to GET `/posts/999999`. If the response is 404, print "Post not found".

5. **Exercise 5 — Query params and filtering**
   - Use the `params` argument to fetch posts for userId=1 and show how many posts returned.

Answers are in `answers.md`.