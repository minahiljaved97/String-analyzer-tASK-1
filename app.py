from flask import Flask, request, render_template_string
import re

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>StringLab | Interactive Strings & Validation</title>

<style>

/* =========================================================
   BASE
========================================================= */

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #eef2ff;
    color: #172033;
    line-height: 1.6;
}

.header {
    background: linear-gradient(135deg, #111827, #312e81, #1d4ed8);
    color: white;
    padding: 50px 7%;
}

.header-inner {
    max-width: 1200px;
    margin: auto;
}

.logo {
    color: #67e8f9;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 3px;
}

.header h1 {
    font-size: 48px;
    margin: 10px 0;
}

.header p {
    color: #dbeafe;
    max-width: 750px;
    font-size: 17px;
}

.container {
    max-width: 1200px;
    margin: 30px auto;
    padding: 0 20px;
}


/* =========================================================
   NAV
========================================================= */

.nav {
    background: white;
    padding: 7px;
    border-radius: 18px;
    display: flex;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(15,23,42,.08);
}

.nav a {
    flex: 1;
    text-align: center;
    padding: 15px;
    text-decoration: none;
    color: #64748b;
    font-weight: bold;
    border-radius: 13px;
}

.nav a.active {
    background: linear-gradient(135deg,#312e81,#2563eb);
    color: white;
}


/* =========================================================
   CARDS
========================================================= */

.card {
    background: white;
    border-radius: 22px;
    padding: 30px;
    margin-bottom: 22px;
    box-shadow: 0 8px 30px rgba(15,23,42,.07);
}

.card h2 {
    margin-top: 0;
    font-size: 27px;
}

.subtitle {
    color: #64748b;
}


/* =========================================================
   INPUT
========================================================= */

.label {
    display: block;
    font-weight: bold;
    margin-bottom: 9px;
}

textarea,
input {
    width: 100%;
    padding: 17px;
    border: 2px solid #dbe2ea;
    border-radius: 14px;
    font-size: 17px;
    outline: none;
}

textarea {
    min-height: 130px;
    resize: vertical;
}

textarea:focus,
input:focus {
    border-color: #6366f1;
    box-shadow: 0 0 0 4px #e0e7ff;
}

button {
    width: 100%;
    margin-top: 14px;
    padding: 16px;
    border: 0;
    border-radius: 14px;
    background: linear-gradient(135deg,#4f46e5,#2563eb);
    color: white;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}


/* =========================================================
   BADGES
========================================================= */

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: bold;
    margin-bottom: 10px;
}

.blue {
    background: #dbeafe;
    color: #1d4ed8;
}

.green {
    background: #dcfce7;
    color: #15803d;
}

.red {
    background: #fee2e2;
    color: #b91c1c;
}

.purple {
    background: #ede9fe;
    color: #6d28d9;
}

.orange {
    background: #ffedd5;
    color: #c2410c;
}


/* =========================================================
   FLOW
========================================================= */

.flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin: 25px 0;
}

.flow-box {
    padding: 18px 20px;
    border-radius: 14px;
    font-weight: bold;
    text-align: center;
    min-width: 125px;
}

.flow-arrow {
    font-size: 25px;
    color: #94a3b8;
}


/* =========================================================
   CONCEPT GRID
========================================================= */

.grid {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 15px;
}

.concept {
    padding: 20px;
    border-radius: 17px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
}

.concept h3 {
    margin-top: 0;
}

.concept p {
    color: #64748b;
    font-size: 14px;
}


/* =========================================================
   CODE
========================================================= */

.code {
    background: #0f172a;
    color: #dbeafe;
    padding: 16px;
    border-radius: 12px;
    font-family: Consolas, monospace;
    overflow-x: auto;
    margin-top: 12px;
}


/* =========================================================
   VALIDATION
========================================================= */

.validation-grid {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 14px;
}

.check {
    padding: 19px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
}

.check.good {
    background: #f0fdf4;
    border-left: 6px solid #22c55e;
}

.check.bad {
    background: #fff1f2;
    border-left: 6px solid #ef4444;
}

.check-title {
    font-weight: bold;
}

.check-text {
    color: #64748b;
    font-size: 13px;
    margin-top: 5px;
}


/* =========================================================
   EMAIL ANATOMY
========================================================= */

.email-anatomy {
    display: flex;
    justify-content: center;
    align-items: stretch;
    flex-wrap: wrap;
    margin: 30px 0;
}

.email-part {
    padding: 22px;
    min-width: 150px;
    text-align: center;
    background: #eff6ff;
    border: 2px solid #93c5fd;
    font-family: Consolas, monospace;
    font-size: 21px;
    font-weight: bold;
}

.email-part small {
    display: block;
    font-family: Arial;
    font-size: 11px;
    color: #2563eb;
    margin-bottom: 5px;
}

.email-symbol {
    display: flex;
    align-items: center;
    padding: 0 15px;
    font-size: 27px;
    font-weight: bold;
    color: #64748b;
}


/* =========================================================
   REGEX VISUAL
========================================================= */

.regex-box {
    background: linear-gradient(135deg,#111827,#312e81);
    color: white;
    border-radius: 20px;
    padding: 25px;
    margin-top: 20px;
}

.regex-pattern {
    background: #020617;
    padding: 20px;
    border-radius: 12px;
    font-family: Consolas, monospace;
    font-size: 16px;
    overflow-x: auto;
    color: #a5f3fc;
}

.regex-parts {
    display: grid;
    grid-template-columns: repeat(5,1fr);
    gap: 10px;
    margin-top: 18px;
}

.regex-part {
    background: rgba(255,255,255,.1);
    padding: 14px;
    border-radius: 12px;
    text-align: center;
}

.regex-part strong {
    display: block;
    color: #67e8f9;
}


/* =========================================================
   DECISION DIAGRAM
========================================================= */

.decision {
    display: grid;
    grid-template-columns: 1fr 130px 1fr;
    align-items: center;
    gap: 15px;
    margin: 25px 0;
}

.decision-card {
    padding: 25px;
    text-align: center;
    border-radius: 17px;
    font-weight: bold;
}

.accept {
    background: #dcfce7;
    border: 2px solid #22c55e;
    color: #15803d;
}

.reject {
    background: #fee2e2;
    border: 2px solid #ef4444;
    color: #b91c1c;
}

.diamond {
    width: 85px;
    height: 85px;
    transform: rotate(45deg);
    background: #ede9fe;
    border: 3px solid #8b5cf6;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
}

.diamond span {
    transform: rotate(-45deg);
    font-size: 11px;
    font-weight: bold;
}


/* =========================================================
   RESULT
========================================================= */

.success {
    padding: 22px;
    border-radius: 15px;
    background: #ecfdf5;
    border-left: 7px solid #10b981;
    color: #047857;
}

.error {
    padding: 22px;
    border-radius: 15px;
    background: #fff1f2;
    border-left: 7px solid #ef4444;
    color: #be123c;
}

.results {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 12px;
}

.metric {
    background: #f8fafc;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
}

.metric small {
    color: #64748b;
}

.metric strong {
    display: block;
    font-size: 23px;
    margin-top: 5px;
}


/* =========================================================
   EXAMPLES
========================================================= */

.example-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.example-card {
    padding: 20px;
    border-radius: 16px;
}

.valid-example {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
}

.invalid-example {
    background: #fff1f2;
    border: 1px solid #fecdd3;
}

.example-email {
    background: white;
    padding: 12px;
    border-radius: 9px;
    font-family: Consolas, monospace;
    margin: 10px 0;
}


/* =========================================================
   FOOTER
========================================================= */

footer {
    text-align: center;
    color: #94a3b8;
    padding: 40px;
}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width:800px) {

    .grid,
    .validation-grid,
    .results,
    .example-grid,
    .regex-parts {
        grid-template-columns: 1fr;
    }

    .decision {
        grid-template-columns: 1fr;
    }

    .header h1 {
        font-size: 36px;
    }

}

</style>

</head>


<body>


<!-- =====================================================
     HEADER
===================================================== -->

<div class="header">

    <div class="header-inner">

        <div class="logo">
            COMPUTER SCIENCE • STRINGS & LANGUAGES
        </div>

        <h1>StringLab</h1>

        <p>
            An interactive visual laboratory for understanding
            strings, input validation, pattern matching,
            regular expressions and string transformations.
        </p>

    </div>

</div>


<div class="container">


<!-- =====================================================
     NAVIGATION
===================================================== -->

<div class="nav">

    <a href="/" class="{{ 'active' if mode == 'string' else '' }}">
        🔤 String Laboratory
    </a>

    <a href="/email" class="{{ 'active' if mode == 'email' else '' }}">
        ✉️ Email & Regex Lab
    </a>

</div>


{% if mode == "string" %}


<!-- =====================================================
     STRING LAB INPUT
===================================================== -->

<div class="card">

    <span class="badge blue">
        STRING INPUT
    </span>

    <h2>🔤 Enter Your String</h2>

    <p class="subtitle">
        Enter a single word, full name, sentence or any text.
        The program will validate and analyze it.
    </p>

    <form method="POST">

        <label class="label">
            Your text
        </label>

        <textarea
            name="text"
            maxlength="500"
            placeholder="Example: Hello World"
        >{{ text }}</textarea>

        <button type="submit">
            Analyze String →
        </button>

    </form>

</div>


{% if error %}

<div class="card">

    <div class="error">

        <strong>✗ INPUT REJECTED</strong>

        <br><br>

        {{ error }}

    </div>

</div>

{% endif %}


<!-- =====================================================
     STRING VALIDATION METHODS
===================================================== -->

<div class="card">

    <span class="badge purple">
        INPUT VALIDATION
    </span>

    <h2>01 — How Does the Program Validate Input?</h2>

    <p class="subtitle">
        Before analyzing a string, the program first checks
        whether the input should be accepted.
    </p>


    <div class="grid">


        <div class="concept">

            <h3>① Empty Check</h3>

            <p>
                Checks whether the user entered anything.
            </p>

            <div class="code">
                if not text:
            </div>

        </div>


        <div class="concept">

            <h3>② Whitespace Check</h3>

            <p>
                Rejects input containing only spaces.
            </p>

            <div class="code">
                if not text.strip():
            </div>

        </div>


        <div class="concept">

            <h3>③ Length Check</h3>

            <p>
                Prevents extremely long input.
            </p>

            <div class="code">
                if len(text) > 500:
            </div>

        </div>

    </div>

</div>


<!-- =====================================================
     STRING FLOW DIAGRAM
===================================================== -->

<div class="card">

    <span class="badge orange">
        PROCESSING FLOW
    </span>

    <h2>02 — String Processing Pipeline</h2>

    <div class="flow">

        <div class="flow-box blue">
            👤 INPUT
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box purple">
            🔍 VALIDATE
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box orange">
            🧹 CLEAN
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box green">
            📊 ANALYZE
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box blue">
            ✅ RESULT
        </div>

    </div>

</div>


{% if result %}


<!-- =====================================================
     STRIP
===================================================== -->

<div class="card">

    <span class="badge orange">
        STRING METHOD
    </span>

    <h2>03 — `strip()` : Clean the Input</h2>

    <div class="concept">

        <h3>What does `strip()` do?</h3>

        <p>
            It removes unnecessary spaces from the beginning
            and end of the string.
        </p>

        <div class="example-grid">

            <div class="example-card invalid-example">

                <b>BEFORE</b>

                <div class="code">
                    "{{ result.original }}"
                </div>

            </div>

            <div class="example-card valid-example">

                <b>AFTER strip()</b>

                <div class="code">
                    "{{ result.cleaned }}"
                </div>

            </div>

        </div>

    </div>

</div>


<!-- =====================================================
     SPLIT
===================================================== -->

<div class="card">

    <span class="badge purple">
        STRING METHOD
    </span>

    <h2>04 — `split()` : Break Text into Words</h2>

    <p class="subtitle">
        `split()` divides a string into separate pieces.
        In our case, those pieces are words.
    </p>

    <div class="flow">

        <div class="flow-box blue">
            "{{ result.cleaned }}"
        </div>

        <div class="flow-arrow">
            →
        </div>

        <div class="flow-box purple">
            split()
        </div>

        <div class="flow-arrow">
            →
        </div>

        <div class="flow-box green">
            {{ result.words }}
        </div>

    </div>

</div>


<!-- =====================================================
     LEN
===================================================== -->

<div class="card">

    <span class="badge blue">
        STRING METHOD
    </span>

    <h2>05 — `len()` : Measure the String</h2>

    <div class="concept">

        <h3>What does `len()` do?</h3>

        <p>
            It counts how many characters are present
            in a string.
        </p>

        <div class="code">

            "Hello"

            <br><br>

            H &nbsp; e &nbsp; l &nbsp; l &nbsp; o

            <br>

            1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5

            <br><br>

            len("Hello") = 5

        </div>

    </div>

</div>


<!-- =====================================================
     STRING PROFILE
===================================================== -->

<div class="card">

    <span class="badge green">
        ANALYSIS RESULT
    </span>

    <h2>06 — Your String Profile</h2>

    <div class="results">

        <div class="metric">

            <small>Type</small>

            <strong>
                {{ result.type }}
            </strong>

        </div>

        <div class="metric">

            <small>Words</small>

            <strong>
                {{ result.word_count }}
            </strong>

        </div>

        <div class="metric">

            <small>Total Characters</small>

            <strong>
                {{ result.total_length }}
            </strong>

        </div>

        <div class="metric">

            <small>Without Spaces</small>

            <strong>
                {{ result.no_space_length }}
            </strong>

        </div>

    </div>

</div>


<!-- =====================================================
     TRANSFORMATIONS
===================================================== -->

<div class="card">

    <span class="badge purple">
        STRING TRANSFORMATIONS
    </span>

    <h2>07 — Change the Representation</h2>

    <p class="subtitle">
        These operations transform how the string is represented.
    </p>


    <div class="grid">


        <div class="concept">

            <h3>UPPERCASE</h3>

            <p>
                Converts letters into uppercase.
            </p>

            <div class="code">
                "Hello".upper()
                <br>
                ↓
                <br>
                "HELLO"
            </div>

        </div>


        <div class="concept">

            <h3>LOWERCASE</h3>

            <p>
                Converts letters into lowercase.
            </p>

            <div class="code">
                "HELLO".lower()
                <br>
                ↓
                <br>
                "hello"
            </div>

        </div>


        <div class="concept">

            <h3>REVERSE</h3>

            <p>
                Reads the string backwards.
            </p>

            <div class="code">
                "Hello"[::-1]
                <br>
                ↓
                <br>
                "olleH"
            </div>

        </div>

    </div>

</div>


{% endif %}


{% else %}


<!-- =====================================================
     EMAIL INPUT
===================================================== -->

<div class="card">

    <span class="badge blue">
        EMAIL VALIDATION
    </span>

    <h2>✉️ Email Validation Laboratory</h2>

    <p class="subtitle">
        This laboratory uses basic conditions, Python string
        methods and Regular Expressions to validate an email.
    </p>

    <form method="POST">

        <label class="label">
            Enter an email address
        </label>

        <input
            type="text"
            name="email"
            value="{{ email }}"
            placeholder="example@gmail.com"
        >

        <button type="submit">
            🔍 Validate Email
        </button>

    </form>

</div>


<!-- =====================================================
     EMAIL ANATOMY
===================================================== -->

<div class="card">

    <span class="badge purple">
        EMAIL STRUCTURE
    </span>

    <h2>01 — First Understand the Structure</h2>

    <p class="subtitle">
        The program expects a simplified structure like this:
    </p>


    <div class="email-anatomy">

        <div class="email-part">

            <small>USERNAME</small>

            student

        </div>

        <div class="email-symbol">
            @
        </div>

        <div class="email-part">

            <small>DOMAIN</small>

            gmail

        </div>

        <div class="email-symbol">
            .
        </div>

        <div class="email-part">

            <small>EXTENSION</small>

            com

        </div>

    </div>


    <div class="code">

        username @ domain . extension

    </div>

</div>


<!-- =====================================================
     VALIDATION TECHNIQUES
===================================================== -->

<div class="card">

    <span class="badge orange">
        IMPORTANT CS CONCEPT
    </span>

    <h2>02 — Input Validation Techniques Used</h2>

    <p class="subtitle">
        Our application does not depend on only one check.
        It combines several techniques.
    </p>


    <div class="grid">


        <div class="concept">

            <h3>① Conditional Validation</h3>

            <p>
                Python `if` statements check basic conditions
                before processing the input.
            </p>

            <div class="code">
                if not email:
                    reject
            </div>

        </div>


        <div class="concept">

            <h3>② String Methods</h3>

            <p>
                Python string functions inspect individual
                parts of the input.
            </p>

            <div class="code">
                count()
                split()
                rsplit()
                len()
                isalpha()
            </div>

        </div>


        <div class="concept">

            <h3>③ Regular Expression</h3>

            <p>
                Regex checks whether the complete string
                follows the required pattern.
            </p>

            <div class="code">
                re.fullmatch(pattern, email)
            </div>

        </div>

    </div>

</div>


<!-- =====================================================
     EMAIL VALIDATION FLOW
===================================================== -->

<div class="card">

    <span class="badge green">
        VALIDATION ALGORITHM
    </span>

    <h2>03 — How Does Email Validation Work?</h2>

    <div class="flow">

        <div class="flow-box blue">
            USER INPUT
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box orange">
            EMPTY?
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box purple">
            SPACES?
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box blue">
            REGEX
        </div>

        <div class="flow-arrow">→</div>

        <div class="flow-box green">
            COMPONENTS
        </div>

    </div>


    <div class="decision">

        <div class="decision-card accept">

            ✓ ACCEPT

            <br><br>

            All important checks pass.

        </div>


        <div class="diamond">

            <span>
                ALL<br>
                RULES<br>
                PASS?
            </span>

        </div>


        <div class="decision-card reject">

            ✗ REJECT

            <br><br>

            One or more checks fail.

        </div>

    </div>

</div>


<!-- =====================================================
     REGEX EXPLANATION
===================================================== -->

<div class="card">

    <span class="badge purple">
        REGULAR EXPRESSION
    </span>

    <h2>04 — Regex: Pattern Matching</h2>

    <p class="subtitle">
        Regex means Regular Expression. It is used to
        search for and validate patterns inside strings.
    </p>


    <div class="regex-box">

        <h3>Our Email Pattern</h3>

        <div class="regex-pattern">
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$
        </div>


        <div class="regex-parts">

            <div class="regex-part">

                <strong>[A-Za-z0-9...]</strong>

                Username characters

            </div>

            <div class="regex-part">

                <strong>@</strong>

                Separator

            </div>

            <div class="regex-part">

                <strong>[A-Za-z0-9.-]+</strong>

                Domain

            </div>

            <div class="regex-part">

                <strong>\\.</strong>
                Dot

            </div>

            <div class="regex-part">

                <strong>[A-Za-z]{2,}</strong>

                Extension

            </div>

        </div>

    </div>


    <div class="concept">

        <h3>Simple Explanation</h3>

        <p>
            Regex does not care whether the provider is Gmail,
            Yahoo or Outlook. It checks whether the characters
            follow the required pattern.
        </p>

        <div class="code">

            minahil@gmail.com
            → Pattern Match ✓

            <br><br>

            minahilgmail.com
            → Pattern Match ✗

        </div>

    </div>

</div>


<!-- =====================================================
     LIVE RESULT
===================================================== -->

{% if email %}


<div class="card">

    <span class="badge blue">
        LIVE ANALYSIS
    </span>

    <h2>05 — Your Email: Rule-by-Rule Check</h2>

    <p class="subtitle">
        Green means the condition passed.
        Red means the condition failed.
    </p>


    <div class="validation-grid">


        <div class="check {{ 'good' if email_checks['not_empty'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['not_empty'] %}
                    ✓ Input Exists
                {% else %}
                    ✗ Input Exists
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['not_empty'] %}
                    Input was provided.
                {% else %}
                    Nothing was entered.
                {% endif %}
            </div>

        </div>


        <div class="check {{ 'good' if email_checks['no_spaces'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['no_spaces'] %}
                    ✓ No Spaces
                {% else %}
                    ✗ No Spaces
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['no_spaces'] %}
                    No spaces detected.
                {% else %}
                    Spaces are not accepted.
                {% endif %}
            </div>

        </div>


        <div class="check {{ 'good' if email_checks['one_at'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['one_at'] %}
                    ✓ Exactly One @
                {% else %}
                    ✗ Exactly One @
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['one_at'] %}
                    One @ symbol found.
                {% else %}
                    Exactly one @ is required.
                {% endif %}
            </div>

        </div>


        <div class="check {{ 'good' if email_checks['username'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['username'] %}
                    ✓ Username
                {% else %}
                    ✗ Username
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['username'] %}
                    Username exists.
                {% else %}
                    Username is missing.
                {% endif %}
            </div>

        </div>


        <div class="check {{ 'good' if email_checks['domain'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['domain'] %}
                    ✓ Domain
                {% else %}
                    ✗ Domain
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['domain'] %}
                    Domain exists.
                {% else %}
                    Domain is missing.
                {% endif %}
            </div>

        </div>


        <div class="check {{ 'good' if email_checks['extension'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['extension'] %}
                    ✓ Extension
                {% else %}
                    ✗ Extension
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['extension'] %}
                    Extension passed.
                {% else %}
                    Extension is missing/invalid.
                {% endif %}
            </div>

        </div>


        <div class="check {{ 'good' if email_checks['regex'] else 'bad' }}">

            <div class="check-title">

                {% if email_checks['regex'] %}
                    ✓ Regex Match
                {% else %}
                    ✗ Regex Match
                {% endif %}

            </div>

            <div class="check-text">
                {% if email_checks['regex'] %}
                    Complete pattern matched.
                {% else %}
                    Complete pattern did not match.
                {% endif %}
            </div>

        </div>

    </div>

</div>


<!-- =====================================================
     FINAL RESULT
===================================================== -->

{% if email_result %}


<div class="card">

    <div class="success">

        <strong>✓ VALID EMAIL STRUCTURE</strong>

        <br><br>

        The input passed the basic validation,
        string checks and Regex pattern check.

    </div>

</div>


<!-- EMAIL DECONSTRUCTION -->

<div class="card">

    <span class="badge green">
        STRING DECONSTRUCTION
    </span>

    <h2>06 — Your Email Broken into Components</h2>

    <div class="email-anatomy">

        <div class="email-part">

            <small>USERNAME</small>

            {{ email_result['username'] }}

        </div>

        <div class="email-symbol">
            @
        </div>

        <div class="email-part">

            <small>DOMAIN</small>

            {{ email_result['domain'] }}

        </div>

        <div class="email-symbol">
            .
        </div>

        <div class="email-part">

            <small>EXTENSION</small>

            {{ email_result['extension'] }}

        </div>

    </div>


    <div class="code">

email.count("@")
→ {{ email.count("@") }}

email.split("@", 1)
→ separates username + domain

domain.rsplit(".", 1)
→ separates domain + extension

extension.isalpha()
→ checks alphabetic extension

    </div>

</div>


{% else %}


<div class="card">

    <div class="error">

        <strong>✗ INVALID EMAIL STRUCTURE</strong>

        <br><br>

        {{ email_error }}

    </div>

</div>


<div class="card">

    <span class="badge red">
        WHY REJECTED?
    </span>

    <h2>06 — Find the Problem</h2>

    <p class="subtitle">
        The red validation cards above show exactly
        which condition failed.
    </p>


    {% if not email_checks['not_empty'] %}

    <div class="concept">

        <h3>🚫 Empty Input</h3>

        <p>
            The program cannot validate an empty string.
        </p>

        <div class="code">
            "" → REJECT
        </div>

    </div>

    {% endif %}


    {% if not email_checks['no_spaces'] %}

    <div class="concept">

        <h3>🚫 Spaces Detected</h3>

        <p>
            Our simplified validator does not accept spaces
            inside the email structure.
        </p>

        <div class="code">
            minahil @gmail.com → REJECT
        </div>

    </div>

    {% endif %}


    {% if not email_checks['one_at'] %}

    <div class="concept">

        <h3>🚫 @ Symbol Problem</h3>

        <p>
            Exactly one @ symbol is required.
        </p>

        <div class="code">

            minahilgmail.com → ✗

            <br>

            minahil@@gmail.com → ✗

            <br>

            minahil@gmail.com → ✓

        </div>

    </div>

    {% endif %}


    {% if not email_checks['username'] %}

    <div class="concept">

        <h3>🚫 Username Missing</h3>

        <p>
            Something must exist before the @ symbol.
        </p>

        <div class="code">
            @gmail.com → REJECT
        </div>

    </div>

    {% endif %}


    {% if not email_checks['domain'] %}

    <div class="concept">

        <h3>🚫 Domain Missing</h3>

        <p>
            Something must exist after @ before the extension.
        </p>

        <div class="code">
            minahil@.com → REJECT
        </div>

    </div>

    {% endif %}


    {% if not email_checks['extension'] %}

    <div class="concept">

        <h3>🚫 Extension Missing</h3>

        <p>
            The email needs an extension such as
            .com, .org, .edu or .pk.
        </p>

        <div class="code">
            minahil@gmail → REJECT
        </div>

    </div>

    {% endif %}


    {% if not email_checks['regex'] %}

    <div class="concept">

        <h3>🚫 Regex Pattern Failed</h3>

        <p>
            The complete email did not match the required
            Regular Expression pattern.
        </p>

        <div class="code">
            username@domain.extension
        </div>

    </div>

    {% endif %}


</div>

{% endif %}


<!-- =====================================================
     VALID / INVALID EXAMPLES
===================================================== -->

<div class="card">

    <span class="badge orange">
        LEARNING EXAMPLES
    </span>

    <h2>07 — What Will the Program Accept?</h2>


    <div class="example-grid">


        <div class="example-card valid-example">

            <h3>✓ VALID</h3>

            <div class="example-email">
                minahil@gmail.com
            </div>

            Username ✓<br>
            @ ✓<br>
            Domain ✓<br>
            Extension ✓<br>
            Regex ✓

        </div>


        <div class="example-card valid-example">

            <h3>✓ VALID</h3>

            <div class="example-email">
                student@yahoo.com
            </div>

            Username ✓<br>
            @ ✓<br>
            Domain ✓<br>
            Extension ✓<br>
            Regex ✓

        </div>


        <div class="example-card valid-example">

            <h3>✓ VALID</h3>

            <div class="example-email">
                student@university.edu
            </div>

            Username ✓<br>
            @ ✓<br>
            Domain ✓<br>
            Extension ✓<br>
            Regex ✓

        </div>


        <div class="example-card invalid-example">

            <h3>✗ INVALID</h3>

            <div class="example-email">
                minahilgmail.com
            </div>

            Missing @ ❌

        </div>


        <div class="example-card invalid-example">

            <h3>✗ INVALID</h3>

            <div class="example-email">
                minahil@gmail
            </div>

            Missing extension ❌

        </div>


        <div class="example-card invalid-example">

            <h3>✗ INVALID</h3>

            <div class="example-email">
                @gmail.com
            </div>

            Missing username ❌

        </div>


        <div class="example-card invalid-example">

            <h3>✗ INVALID</h3>

            <div class="example-email">
                minahil@@gmail.com
            </div>

            Multiple @ symbols ❌

        </div>


        <div class="example-card invalid-example">

            <h3>✗ INVALID</h3>

            <div class="example-email">
                minahil @gmail.com
            </div>

            Contains spaces ❌

        </div>

    </div>

</div>


<!-- =====================================================
     FINAL THEORY
===================================================== -->

<div class="card">

    <span class="badge purple">
        KEY CONCEPT
    </span>

    <h2>08 — What Are We Actually Learning?</h2>

    <div class="grid">


        <div class="concept">

            <h3>🔤 Strings</h3>

            <p>
                Email addresses and text are strings made
                from sequences of characters.
            </p>

        </div>


        <div class="concept">

            <h3>🔍 Validation</h3>

            <p>
                Validation means checking whether input
                satisfies predefined rules.
            </p>

        </div>


        <div class="concept">

            <h3>🧩 Pattern Matching</h3>

            <p>
                Regex identifies whether a string follows
                a particular pattern.
            </p>

        </div>


        <div class="concept">

            <h3>✂️ String Operations</h3>

            <p>
                split(), count(), len(), rsplit() and
                isalpha() help analyze strings.
            </p>

        </div>


        <div class="concept">

            <h3>🔀 Decision Making</h3>

            <p>
                Conditions determine whether the program
                accepts or rejects the input.
            </p>

        </div>


        <div class="concept">

            <h3>🧠 Logic</h3>

            <p>
                Multiple conditions work together to produce
                the final validation result.
            </p>

        </div>

    </div>

</div>


{% endif %}

{% endif %}

</div>


<!-- =====================================================
     FOOTER
===================================================== -->

<footer>

    StringLab • Interactive Strings & Languages Laboratory

    <br>

    Python • String Methods • Input Validation • Regex • Pattern Matching

</footer>


</body>
</html>
"""




@app.route("/", methods=["GET", "POST"])
def string_analyzer():

    text = ""
    error = None
    result = None

    if request.method == "POST":

        text = request.form.get("text", "")

        # 1. Empty input validation
        if not text:

            error = (
                "The input is empty. "
                "Please enter some text."
            )

        # 2. Whitespace validation
        elif not text.strip():

            error = (
                "The input contains only spaces. "
                "Please enter meaningful text."
            )

        # 3. Length validation
        elif len(text) > 500:

            error = (
                "Input is too long. "
                "Maximum allowed length is 500 characters."
            )

        else:

            # Clean input
            cleaned = text.strip()

            # Split into words
            words = cleaned.split()

            # Character count
            total_length = len(cleaned)

            # Remove spaces
            no_space_length = len(
                cleaned.replace(" ", "")
            )

            # Count spaces
            space_count = cleaned.count(" ")

            # Count words
            word_count = len(words)

            # Single or multiple words
            if word_count == 1:
                text_type = "Single Word"
            else:
                text_type = "Multiple Words"

            result = {

                "original": text,

                "cleaned": cleaned,

                "words": words,

                "type": text_type,

                "word_count": word_count,

                "total_length": total_length,

                "no_space_length": no_space_length,

                "space_count": space_count
            }


    return render_template_string(

        HTML,

        mode="string",

        text=text,

        error=error,

        result=result,

        email="",

        email_error=None,

        email_result=None,

        email_checks={
            "not_empty": False,
            "no_spaces": False,
            "one_at": False,
            "username": False,
            "domain": False,
            "extension": False,
            "regex": False
        }

    )


# =========================================================
# EMAIL VALIDATOR
# =========================================================

@app.route("/email", methods=["GET", "POST"])
def email_validator():

    email = ""

    email_error = None

    email_result = None


    # All validation checks
    checks = {

        "not_empty": False,

        "no_spaces": False,

        "one_at": False,

        "username": False,

        "domain": False,

        "extension": False,

        "regex": False
    }


    username = ""

    domain = ""

    extension = ""


    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip()


        
        if email:

            checks["not_empty"] = True



        if email and " " not in email:

            checks["no_spaces"] = True


        
        if email.count("@") == 1:

            checks["one_at"] = True

            username, domain_part = email.split(
                "@",
                1
            )


            
            if username:

                checks["username"] = True


        

            if "." in domain_part:

                domain, extension = domain_part.rsplit(
                    ".",
                    1
                )


                if domain:

                    checks["domain"] = True


                if (
                    extension
                    and extension.isalpha()
                    and len(extension) >= 2
                ):

                    checks["extension"] = True

            else:

                domain = domain_part

                if domain:

                    checks["domain"] = True


        # =================================================
        # CHECK 7 — REGEX
        # =================================================

        pattern = (
    r"^[A-Za-z0-9._%+-]+"
    r"@[A-Za-z0-9.-]+"
    r"[.][A-Za-z]{2,}$"
)

        if email and re.fullmatch(
            pattern,
            email
        ):

            checks["regex"] = True


        # =================================================
        # FINAL DECISION
        # =================================================

        if all(checks.values()):

            email_result = {

                "username": username,

                "domain": domain,

                "extension": extension
            }


        else:

            if not checks["not_empty"]:

                email_error = (
                    "No email was entered."
                )

            elif not checks["no_spaces"]:

                email_error = (
                    "Spaces are not accepted inside "
                    "the email address."
                )

            elif not checks["one_at"]:

                email_error = (
                    "The email must contain exactly "
                    "one @ symbol."
                )

            elif not checks["username"]:

                email_error = (
                    "The username is missing. "
                    "Something must exist before @."
                )

            elif not checks["domain"]:

                email_error = (
                    "The domain is missing."
                )

            elif not checks["extension"]:

                email_error = (
                    "The extension is missing or invalid. "
                    "Examples: .com, .org, .edu, .pk"
                )

            elif not checks["regex"]:

                email_error = (
                    "The complete email did not match "
                    "the required Regex pattern."
                )


    return render_template_string(

        HTML,

        mode="email",

        text="",

        error=None,

        result=None,

        email=email,

        email_error=email_error,

        email_result=email_result,

        email_checks=checks

    )



if __name__ == "__main__":

    app.run(debug=True)
