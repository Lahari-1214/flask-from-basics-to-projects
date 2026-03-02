## Template Inheritance
In Jinja (used by Flask), template inheritance allows you to:
<b>>Create one base layout and reuse it across multiple pages.</b>

Instead of repeating: html, head,navbar,footer,css links etc on every page... you define it once.

<b>Basic Structure:</b>
<pre>
templates/
│
├── base.html
├── home.html
├── login.html
└── dashboard.html
</pre>

follow the steps to define template inheritance:
1. Create base.html (Parent Template) --> follow base.html
2. Create home.html (Child Template) --> follow home.html,login.html


<pre>
Flask renders:
home.html → which extends → base.html
Jinja merges them internally.
</pre>



## Styling
1. Create CSS File : 'static/css/style.css'
2. Link CSS in base.html : '<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">'

<strong>IMPORTANT</strong>
* Never Write: 
        <link rel="stylesheet" href="static/css/style.css">
* Always use:
        {{ url_for('static', filename='css/style.css') }}
        



