#5 test cases
test_cases = [
    {"prompt": "Find the derivative of the function, F(x) = (x^4 + 3x^2 - 2)^5. ", 
     "expected": "$5(x^4 + 3x^2 - 2)^4(4x^3 + 6x)$"},
    {"prompt": "Differentiate the function, f(x) = 2^40. ", 
     "expected": "$0$"},
    {"prompt": "Differentiate g(t) = t^3 cos t.", 
    "expected": "$3t^2\cos t - t^3\sin t$"},
    {"prompt": "Find dy/dx by implicit differentiation for x^3 + y^3 = 1.", 
     "expected": "$-x^2/y^2$"},
    {"prompt": "Find the linearization L(x) of the function at a = -1 for f(x) = x^4 + 3x^2.", 
     "expected": "$L(x) = -10x - 6$"},
    
    # Integration Test Cases
    {"prompt": "Compute the definite integral of y=3x^2 over [1,3]", "expected": "26"},
    {"prompt": "What is the volume of the solid obtained by revolving y=x^3 about the x-axis over [1,2]?", "expected": "(127π)/7"},
    {"prompt": "Find the area under the curve y=sin(x) over [0,π]", "expected": "2"},

    # Application of Differentiation Test Cases
    {"prompt": "Find the maximum value of f(x) = -x^2 + 4x + 5 over x ∈ [0,5]", "expected": "9"},
    {"prompt": "Determine the slope of the tangent line to the curve y=ln(x) at x=e ", "expected": "1/e"},

    # Additional Integration Test Cases
    {"prompt": "Compute the definite integral of y=ln(x) over [1,e^2]", "expected": "e^2 + 1"},
    {"prompt": "What is the volume of the solid obtained by revolving y=cos(x) about the x-axis over [0, π/2]?", "expected": "(π^2)/4"},
    {"prompt": "Find the area under the curve y=1/(1 + x^2) over [0,1]", "expected": "π/4"},

    # Additional Application of Differentiation Test Cases
    {"prompt": "Find the maximum value of f(x) = x * e^(-x) over x ∈ [0, ∞)", "expected": "1/e"},
    {"prompt": "Determine the slope of the tangent line to the curve y=√x at x=4", "expected": "0.25"}
]
