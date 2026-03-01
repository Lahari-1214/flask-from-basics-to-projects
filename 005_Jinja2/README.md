### Jinja2 allows you to write dynamic HTML using Python data.
##### Why Template Engine is Needed?
<pre>
Backend → sends data
Frontend → displays data

Jinja2 is the bridge.

Without Jinja:
You mix Python + HTML = messy.

With Jinja:

HTML stays HTML

Python data injected cleanly</pre>

1. Variables in Jinja2
syntax: {{ variable_name }}
 visit code in this folder: app.py

 2. Loops in Jinja2
Syntax: 
{% for item in list %}
{% endfor %}

