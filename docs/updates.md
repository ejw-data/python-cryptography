# Project Improvements

- Change repo to have two flask servers that interact with each other.  Set each app to run from a different port.

```
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
```