```python
from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary shifts data
shifts = [
    {"id": 1, "name": "John Doe", "shift": "Morning"},
    {"id": 2, "name": "Jane Smith", "shift": "Afternoon"}
]

@app.route("/")
def index():
    return render_template("index.html", shifts=shifts)

@app.route("/add_shift", methods=["POST"])
def add_shift():
    name = request.form.get("name")
    shift = request.form.get("shift")
    new_shift = {"id": len(shifts) + 1, "name": name, "shift": shift}
    shifts.append(new_shift)
    return render_template("index.html", shifts=shifts)

if __name__ == "__main__":
    app.run(debug=True)
```
