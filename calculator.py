import math
import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# STREAMLIT CONFIG
# ============================================================

st.set_page_config(
    page_title="Barbie Scientific Calculator",
    page_icon="🎀",
    layout="centered",
)


# Python math module is used for calculator constants.
PI = math.pi
E = math.e


# ============================================================
# BARBIE SCIENTIFIC CALCULATOR
# ============================================================

calculator_html = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<style>

* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    font-family: Arial, Helvetica, sans-serif;
}}

body {{
    background:
        radial-gradient(
            circle at 20% 10%,
            #ffd9ef 0%,
            #ffb1dc 30%,
            #ff70b9 65%,
            #f83d9b 100%
        );

    display: flex;
    justify-content: center;
    align-items: center;
    padding: 12px;
}}

.calculator {{
    width: 100%;
    max-width: 430px;

    background: rgba(255,255,255,0.35);

    border: 2px solid rgba(255,255,255,0.65);

    border-radius: 28px;

    padding: 15px;

    box-shadow:
        0 15px 40px rgba(137, 0, 82, 0.28),
        inset 0 1px 0 rgba(255,255,255,0.7);

    backdrop-filter: blur(14px);
}}

.title {{
    text-align: center;

    color: purple;

    font-size: 16px;

    font-weight: 800;

    margin-bottom: 12px;

    text-shadow:
        0 3px 8px rgba(130,0,70,0.3);
}}

.mode-row {{
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-bottom: 10px;
}}

.mode {{
    border: none;

    padding: 7px 18px;

    border-radius: 20px;

    background: rgba(255,255,255,0.5);

    color: #a00062;

    font-weight: bold;

    cursor: pointer;
}}

.mode.active {{
    background: #ff2f98;
    color: white;
}}

.display {{
    width: 100%;

    height: 65px;

    border: 3px solid #ff3c9e;

    border-radius: 17px;

    background: #fff7fc;

    color: #8d0755;

    font-size: 25px;

    font-weight: 700;

    text-align: right;

    padding: 0 15px;

    outline: none;

    box-shadow:
        inset 0 3px 10px rgba(255,80,170,0.12);
}}

.display:focus {{
    border-color: #e90080;
    box-shadow:
        0 0 0 3px rgba(255,255,255,0.45);
}}

.error {{
    color: #c00050;

    background: #ffe0ee;

    border-radius: 10px;

    padding: 7px 10px;

    margin-top: 7px;

    text-align: center;

    font-size: 13px;

    min-height: 0;
}}

.error:empty {{
    display: none;
}}

.buttons {{
    display: grid;

    grid-template-columns:
        repeat(5, 1fr);

    gap: 7px;

    margin-top: 10px;
}}

button.calc-btn {{
    height: 50px;

    border: 2px solid rgba(255,255,255,0.8);

    border-radius: 15px;

    background: #ff4da7;

    color: white;

    font-size: 16px;

    font-weight: 700;

    cursor: pointer;

    box-shadow:
        0 5px 9px rgba(140,0,80,0.18);

    transition:
        transform 0.08s,
        background 0.08s;
}}

button.calc-btn:hover {{
    background: #ff238f;
}}

button.calc-btn:active {{
    transform: scale(0.94);
}}

button.operator {{
    background: #e92b91;
}}

button.special {{
    background: #d81c84;
}}

button.equals {{
    background: #b90068;

    font-size: 20px;
}}

button.clear {{
    background: #a90061;
}}

.hint {{
    text-align: center;

    color: #a00062;

    font-size: 11px;

    font-weight: 600;

    margin-top: 9px;
}}

</style>

</head>


<body>

<div class="calculator">

    <div class="title">
        🎀 Barbie's Scientific Calculator by Rida Mahmood 🎀
    </div>


    <div class="mode-row">

        <button
            id="degBtn"
            class="mode active"
            onclick="setMode('DEG')">
            DEG
        </button>

        <button
            id="radBtn"
            class="mode"
            onclick="setMode('RAD')">
            RAD
        </button>

    </div>


    <!-- SINGLE EXPRESSION FIELD -->

    <input
        id="display"
        class="display"
        type="text"
        autocomplete="off"
        spellcheck="false"
        placeholder="Enter expression..."
    >


    <div
        id="error"
        class="error">
    </div>


    <div class="buttons">

        <!-- Scientific row -->

        <button
            class="calc-btn"
            onclick="insertFunction('sin')">
            sin
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('cos')">
            cos
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('tan')">
            tan
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('sqrt')">
            √
        </button>

        <button
            class="calc-btn"
            onclick="insert('^')">
            xʸ
        </button>


        <!-- Inverse/scientific -->

        <button
            class="calc-btn"
            onclick="insertFunction('asin')">
            sin⁻¹
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('acos')">
            cos⁻¹
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('atan')">
            tan⁻¹
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('log')">
            log
        </button>

        <button
            class="calc-btn"
            onclick="insertFunction('ln')">
            ln
        </button>


        <!-- Control -->

        <button
            class="calc-btn clear"
            onclick="clearAll()">
            C
        </button>

        <button
            class="calc-btn special"
            onclick="backspace()">
            ⌫
        </button>

        <button
            class="calc-btn"
            onclick="insert('(')">
            (
        </button>

        <button
            class="calc-btn"
            onclick="insert(')')">
            )
        </button>

        <button
            class="calc-btn operator"
            onclick="insert('%')">
            %
        </button>


        <!-- 7 8 9 -->

        <button
            class="calc-btn"
            onclick="insert('7')">
            7
        </button>

        <button
            class="calc-btn"
            onclick="insert('8')">
            8
        </button>

        <button
            class="calc-btn"
            onclick="insert('9')">
            9
        </button>

        <button
            class="calc-btn operator"
            onclick="insert('/')">
            ÷
        </button>

        <button
            class="calc-btn operator"
            onclick="insert('*')">
            ×
        </button>


        <!-- 4 5 6 -->

        <button
            class="calc-btn"
            onclick="insert('4')">
            4
        </button>

        <button
            class="calc-btn"
            onclick="insert('5')">
            5
        </button>

        <button
            class="calc-btn"
            onclick="insert('6')">
            6
        </button>

        <button
            class="calc-btn operator"
            onclick="insert('-')">
            −
        </button>

        <button
            class="calc-btn operator"
            onclick="insert('+')">
            +
        </button>


        <!-- 1 2 3 -->

        <button
            class="calc-btn"
            onclick="insert('1')">
            1
        </button>

        <button
            class="calc-btn"
            onclick="insert('2')">
            2
        </button>

        <button
            class="calc-btn"
            onclick="insert('3')">
            3
        </button>

        <button
            class="calc-btn"
            onclick="insert('.')">
            .
        </button>

        <button
            class="calc-btn special"
            onclick="insertFactorial()">
            x!
        </button>


        <!-- Bottom -->

        <button
            class="calc-btn"
            onclick="insert('0')">
            0
        </button>

        <button
            class="calc-btn"
            onclick="insert('pi')">
            π
        </button>

        <button
            class="calc-btn"
            onclick="insert('e')">
            e
        </button>

        <button
            class="calc-btn special"
            onclick="insert('ANS')">
            Ans
        </button>

        <button
            class="calc-btn equals"
            onclick="calculate()">
            =
        </button>

    </div>


    <div class="hint">
        Enter = Calculate &nbsp; • &nbsp;
        Backspace = Delete &nbsp; • &nbsp;
        Esc = Clear
    </div>

</div>


<script>


// ==========================================================
// STATE
// ==========================================================

let angleMode = "DEG";

let justCalculated = false;

let lastAnswer = "";


// Python math constants
const PI = {PI};
const E = {E};


// ==========================================================
// DOM
// ==========================================================

const display =
    document.getElementById("display");

const errorBox =
    document.getElementById("error");


// ==========================================================
// ERROR
// ==========================================================

function showError(message) {{

    errorBox.textContent = message;

}}


function clearError() {{

    errorBox.textContent = "";

}}


// ==========================================================
// ANGLE MODE
// ==========================================================

function setMode(mode) {{

    angleMode = mode;

    document
        .getElementById("degBtn")
        .classList.toggle(
            "active",
            mode === "DEG"
        );

    document
        .getElementById("radBtn")
        .classList.toggle(
            "active",
            mode === "RAD"
        );

    clearError();

}}


// ==========================================================
// INSERT
// ==========================================================

function insert(value) {{

    clearError();


    /*
       If calculation has just completed:

       Number / decimal / constant / function
       => replace the answer.

       Operator
       => continue from the answer.
    */

    if (justCalculated) {{

        const operators = [
            "+",
            "-",
            "*",
            "/",
            "%",
            "^"
        ];

        if (operators.includes(value)) {{

            display.value += value;

        }} else {{

            display.value = value;

        }}

        justCalculated = false;

    }} else {{

        display.value += value;

    }}

    display.focus();

}}


// ==========================================================
// FUNCTIONS
// ==========================================================

function insertFunction(name) {{

    clearError();


    if (justCalculated) {{

        display.value =
            name + "(";

        justCalculated = false;

    }} else {{

        display.value +=
            name + "(";

    }}

    display.focus();

}}


// ==========================================================
// FACTORIAL
// ==========================================================

function insertFactorial() {{

    clearError();

    if (!display.value.trim()) {{
        showError(
            "Enter a number first"
        );
        return;
    }}

    display.value += "!";

    justCalculated = false;

    display.focus();

}}


// ==========================================================
// BACKSPACE
// ==========================================================

function backspace() {{

    clearError();

    display.value =
        display.value.slice(0, -1);

    justCalculated = false;

    display.focus();

}}


// ==========================================================
// CLEAR
// ==========================================================

function clearAll() {{

    display.value = "";

    lastAnswer = "";

    justCalculated = false;

    clearError();

    display.focus();

}}


// ==========================================================
// FACTORIAL
// ==========================================================

function factorial(n) {{

    if (!Number.isFinite(n)) {{
        throw new Error(
            "Invalid factorial"
        );
    }}

    if (n < 0) {{
        throw new Error(
            "Factorial needs a non-negative number"
        );
    }}

    if (!Number.isInteger(n)) {{
        throw new Error(
            "Factorial needs a whole number"
        );
    }}

    if (n > 170) {{
        throw new Error(
            "Number is too large"
        );
    }}

    let result = 1;

    for (
        let i = 2;
        i <= n;
        i++
    ) {{
        result *= i;
    }}

    return result;

}}


// ==========================================================
// PREPROCESS EXPRESSION
// ==========================================================

function preprocess(expression) {{

    let exp = expression;

    exp = exp
        .replace(/×/g, "*")
        .replace(/÷/g, "/")
        .replace(/−/g, "-")
        .replace(/π/g, "pi")
        .replace(/√/g, "sqrt");


    // ----------------------------------------------
    // Validate characters
    // ----------------------------------------------

    if (
        !/^[0-9a-zA-Z_+\\-*/%^().!\\s]*$/.test(exp)
    ) {{
        throw new Error(
            "Invalid character"
        );
    }}


    // ----------------------------------------------
    // Constants
    // ----------------------------------------------

    exp = exp.replace(
        /\\bpi\\b/g,
        "(" + PI + ")"
    );

    exp = exp.replace(
        /\\be\\b/g,
        "(" + E + ")"
    );


    // ----------------------------------------------
    // Functions
    // ----------------------------------------------

    const functions = [
        "asin",
        "acos",
        "atan",
        "sin",
        "cos",
        "tan",
        "sqrt",
        "log",
        "ln",
        "abs",
        "exp"
    ];


    // ----------------------------------------------
    // Factorial
    // ----------------------------------------------

    let factorialPattern =
        /([0-9]+(?:\\.[0-9]+)?)!/g;

    while (
        factorialPattern.test(exp)
    ) {{
        exp = exp.replace(
            factorialPattern,
            "factorial($1)"
        );
    }}


    // ----------------------------------------------
    // Implicit multiplication
    // ----------------------------------------------

    exp = exp.replace(
        /(\\d|\\))(?=\\()/g,
        "$1*"
    );


    exp = exp.replace(
        /(\\d|\\))(?=(sin|cos|tan|asin|acos|atan|sqrt|log|ln|abs|exp)\\()/g,
        "$1*"
    );


    // ----------------------------------------------
    // Power
    // ----------------------------------------------

    exp = exp.replace(
        /\\^/g,
        "**"
    );


    return exp;

}}


// ==========================================================
// SAFE EXPRESSION CHECK
// ==========================================================

function validateExpression(exp) {{

    if (!exp.trim()) {{
        throw new Error(
            "Enter an expression"
        );
    }}


    // ----------------------------------------------
    // Parentheses
    // ----------------------------------------------

    let balance = 0;

    for (
        const char of exp
    ) {{

        if (char === "(") {{
            balance++;
        }}

        if (char === ")") {{
            balance--;

            if (balance < 0) {{
                throw new Error(
                    "Invalid parentheses"
                );
            }}
        }}

    }}

    if (balance !== 0) {{
        throw new Error(
            "Parentheses are not balanced"
        );
    }}


    // ----------------------------------------------
    // Consecutive operators
    // ----------------------------------------------

    if (
        /[+*/%]{{2,}}/.test(exp)
    ) {{
        throw new Error(
            "Invalid operators"
        );
    }}


    return true;

}}


// ==========================================================
// MATH FUNCTIONS
// ==========================================================

function sinValue(x) {{

    if (angleMode === "DEG") {{
        return Math.sin(
            x * Math.PI / 180
        );
    }}

    return Math.sin(x);

}}


function cosValue(x) {{

    if (angleMode === "DEG") {{
        return Math.cos(
            x * Math.PI / 180
        );
    }}

    return Math.cos(x);

}}


function tanValue(x) {{

    let angle = x;

    if (angleMode === "DEG") {{
        angle =
            x * Math.PI / 180;
    }}

    if (
        Math.abs(
            Math.cos(angle)
        ) < 1e-12
    ) {{
        throw new Error(
            "tan is undefined"
        );
    }}

    return Math.tan(angle);

}}


function asinValue(x) {{

    if (
        x < -1 ||
        x > 1
    ) {{
        throw new Error(
            "asin input must be between -1 and 1"
        );
    }}

    let result = Math.asin(x);

    if (
        angleMode === "DEG"
    ) {{
        result =
            result * 180 / Math.PI;
    }}

    return result;

}}


function acosValue(x) {{

    if (
        x < -1 ||
        x > 1
    ) {{
        throw new Error(
            "acos input must be between -1 and 1"
        );
    }}

    let result = Math.acos(x);

    if (
        angleMode === "DEG"
    ) {{
        result =
            result * 180 / Math.PI;
    }}

    return result;

}}


function atanValue(x) {{

    let result =
        Math.atan(x);

    if (
        angleMode === "DEG"
    ) {{
        result =
            result * 180 / Math.PI;
    }}

    return result;

}}


// ==========================================================
// SAFE EVALUATION
// ==========================================================

function evaluateExpression(expression) {{

    let exp =
        preprocess(expression);

    validateExpression(exp);


    // ------------------------------------------------------
    // Only allow approved names
    // ------------------------------------------------------

    const allowed =
        /^(?:[0-9+\\-*/().%!\\s]|\\*\\*|sin|cos|tan|asin|acos|atan|sqrt|log|ln|abs|exp|factorial)+$/;


    if (!allowed.test(exp)) {{
        throw new Error(
            "Invalid expression"
        );
    }}


    // ------------------------------------------------------
    // Create approved scope
    // ------------------------------------------------------

    const scope = {{

        sin: sinValue,

        cos: cosValue,

        tan: tanValue,

        asin: asinValue,

        acos: acosValue,

        atan: atanValue,

        sqrt: function(x) {{
            if (x < 0) {{
                throw new Error(
                    "sqrt needs a non-negative number"
                );
            }}

            return Math.sqrt(x);
        }},

        log: function(x) {{
            if (x <= 0) {{
                throw new Error(
                    "log needs a positive number"
                );
            }}

            return Math.log10(x);
        }},

        ln: function(x) {{
            if (x <= 0) {{
                throw new Error(
                    "ln needs a positive number"
                );
            }}

            return Math.log(x);
        }},

        abs: Math.abs,

        exp: function(x) {{
            const result =
                Math.exp(x);

            if (
                !Number.isFinite(result)
            ) {{
                throw new Error(
                    "Result is too large"
                );
            }}

            return result;
        }},

        factorial: factorial

    }};


    /*
       The expression is passed only into the
       approved function scope.

       eval is NOT exposed to arbitrary globals.
    */

    let fn = new Function(
        ...Object.keys(scope),
        '"use strict"; return (' +
        exp +
        ');'
    );


    let result = fn(
        ...Object.values(scope)
    );


    if (
        typeof result !== "number" ||
        !Number.isFinite(result)
    ) {{
        throw new Error(
            "Invalid result"
        );
    }}


    return result;

}}


// ==========================================================
// FORMAT RESULT
// ==========================================================

function formatResult(value) {{

    if (
        Math.abs(
            value -
            Math.round(value)
        ) < 1e-12
    ) {{
        return String(
            Math.round(value)
        );
    }}

    return Number(
        value.toPrecision(12)
    ).toString();

}}


// ==========================================================
// CALCULATE
// ==========================================================

function calculate() {{

    clearError();

    let expression =
        display.value.trim();


    if (!expression) {{
        showError(
            "Enter an expression"
        );
        return;
    }}


    try {{

        let result =
            evaluateExpression(
                expression
            );

        let formatted =
            formatResult(result);


        display.value =
            formatted;


        lastAnswer =
            formatted;


        justCalculated =
            true;


        display.focus();

    }} catch (error) {{

        showError(
            error.message ||
            "Invalid expression"
        );

    }}

}}


// ==========================================================
// KEYBOARD SUPPORT
// ==========================================================

display.addEventListener(
    "keydown",
    function(event) {{

        // ----------------------------------------------
        // ENTER
        // ----------------------------------------------

        if (
            event.key === "Enter"
        ) {{

            event.preventDefault();

            event.stopPropagation();

            calculate();

            return;
        }}


        // ----------------------------------------------
        // ESC
        // ----------------------------------------------

        if (
            event.key === "Escape"
        ) {{

            event.preventDefault();

            clearAll();

            return;
        }}


        // ----------------------------------------------
        // BACKSPACE
        // ----------------------------------------------

        if (
            event.key === "Backspace"
        ) {{

            clearError();

            justCalculated =
                false;

            return;
        }}

    }}
);


// ==========================================================
// KEYBOARD INPUT
// ==========================================================

document.addEventListener(
    "keydown",
    function(event) {{

        /*
           If the display isn't focused,
           allow keyboard calculator input.
        */

        if (
            document.activeElement !==
            display
        ) {{

            const allowedKeys =
                "0123456789+-*/().%^";

            if (
                allowedKeys.includes(
                    event.key
                )
            ) {{

                event.preventDefault();

                insert(
                    event.key
                );

            }}

            if (
                event.key === "Enter"
            ) {{

                event.preventDefault();

                calculate();

            }}

            if (
                event.key === "Escape"
            ) {{

                event.preventDefault();

                clearAll();

            }}

        }}

    }}
);


// ==========================================================
// INITIAL FOCUS
// ==========================================================

window.onload = function() {{

    display.focus();

}};

</script>

</body>
</html>
"""


# ============================================================
# RENDER
# ============================================================

components.html(
    calculator_html,
    height=760,
    scrolling=False,
)
