# ❌ This is an example pattern that leads to XSS if run in a real app.
# It is NOT a runnable server and is intentionally incomplete.

user_input = request.GET.get("name")   # Data is untrusted
html = f"<h1>Hello {user_input}</h1>"   # Directly inserted into HTML
return html                             # No escaping --> XSS risk
