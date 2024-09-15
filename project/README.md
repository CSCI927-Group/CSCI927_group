initialize Project
``` shell
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
```

run
```
flask --app app --debug run
```

Step 1: Add web route in app.py
```python
@app.route("/name")
def name():
  return render_template('name.html')
```

Step 2: Add web template
```html
{% extends 'base.html' %}
{% block title %}main{% endblock %}

{% block body %}
<div>
  content
</div>
{% endblock %}
```

[Python Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

[Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

[Bootstrap Example](https://getbootstrap.com/docs/5.3/examples/)
