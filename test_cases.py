# test_cases.py

test_cases = [
    {
        "chapter": "Derivatives",
        "tester": "Aaron",
        "cases": [
            {
                "test_case_id": "TC_DER_001",
                "description": "Find the derivative of the function F(x) = (x^4 + 3x^2 - 2)^5.",
                "prompt": "Find the derivative of the function F(x) = (x^4 + 3x^2 - 2)^5.",
                "expected": "5(x^4+3x^2-2)^4(4x^3+6x)"
            },
            {
                "test_case_id": "TC_DER_002",
                "description": "Differentiate the constant function f(x) = 2^40.",
                "prompt": "Differentiate the function f(x) = 2^40.",
                "expected": "0"
            },
            {
                "test_case_id": "TC_DER_003",
                "description": "Differentiate g(t) = t^3 cos(t).",
                "prompt": "Differentiate g(t) = t^3 cos(t).",
                "expected": "3t²cos(t) - t³sin(t)"
            },
            {
                "test_case_id": "TC_DER_004",
                "description": "Find dy/dx by implicit differentiation for x^3 + y^3 = 1.",
                "prompt": "Find dy/dx by implicit differentiation for x^3 + y^3 = 1.",
                "expected": "-x²/y²"
            },
            {
                "test_case_id": "TC_DER_005",
                "description": "Find the linearization L(x) of the function at a = -1 for f(x) = x^4 + 3x^2.",
                "prompt": "Find the linearization L(x) of the function at a = -1 for f(x) = x^4 + 3x^2.",
                "expected": "L(x) = -10x - 6"
            }
        ]
    },
    {
        "chapter": "Integration",
        "tester": "Krishna",
        "cases": [
            {
                "test_case_id": "TC_INT_001",
                "description": "Evaluate the indefinite integral ∫ x^2 dx.",
                "prompt": "Evaluate the indefinite integral ∫ x^2 dx.",
                "expected": "x³/3"
            },
            {
                "test_case_id": "TC_INT_002",
                "description": "Compute the integral ∫ (1 / x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ (1 / x) dx.",
                "expected": "ln|x|"
            },
            {
                "test_case_id": "TC_INT_003",
                "description": "Find the integral ∫ e^(3x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ e^(3x) dx.",
                "expected": "(1/3)e^(3x)"
            },
            {
                "test_case_id": "TC_INT_004",
                "description": "Compute the definite integral ∫₀^π sin(x) dx.",
                "prompt": "Evaluate the definite integral ∫₀^π sin(x) dx.",
                "expected": "2"
            },
            {
                "test_case_id": "TC_INT_005",
                "description": "Evaluate the integral ∫ (2x + 3) dx.",
                "prompt": "Evaluate the indefinite integral ∫ (2x + 3) dx.",
                "expected": "x² + 3x"
            },
            {
                "test_case_id": "TC_INT_006",
                "description": "Find the integral ∫ (1 / (x^2 + 1)) dx.",
                "prompt": "Evaluate the indefinite integral ∫ (1 / (x^2 + 1)) dx.",
                "expected": "arctan(x)"
            },
            {
                "test_case_id": "TC_INT_007",
                "description": "Compute the integral ∫ x e^(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ x e^(x) dx.",
                "expected": "xeˣ - eˣ"
            },
            {
                "test_case_id": "TC_INT_008",
                "description": "Evaluate the integral ∫ ln(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ ln(x) dx.",
                "expected": "xln(x) - x"
            },
            {
                "test_case_id": "TC_INT_009",
                "description": "Compute the definite integral ∫₁² (3x^2 - 2x + 1) dx.",
                "prompt": "Evaluate the definite integral ∫₁² (3x^2 - 2x + 1) dx.",
                "expected": "5"
            },
            {
                "test_case_id": "TC_INT_010",
                "description": "Find the integral ∫ cos^2(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ cos^2(x) dx.",
                "expected": "x/2 + sin(2x)/4"
            },
            {
                "test_case_id": "TC_INT_011",
                "description": "Evaluate the integral ∫ 1 / sqrt(1 - x^2) dx.",
                "prompt": "Evaluate the indefinite integral ∫ 1 / sqrt(1 - x^2) dx.",
                "expected": "arcsin(x)"
            },
            {
                "test_case_id": "TC_INT_012",
                "description": "Compute the integral ∫ sec^2(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ sec^2(x) dx.",
                "expected": "tan(x)"
            },
            {
                "test_case_id": "TC_INT_013",
                "description": "Evaluate the definite integral ∫₀^{π/2} cos(x) dx.",
                "prompt": "Evaluate the definite integral ∫₀^{π/2} cos(x) dx.",
                "expected": "1"
            },
            {
                "test_case_id": "TC_INT_014",
                "description": "Find the integral ∫ (2x) / (x^2 + 1) dx.",
                "prompt": "Evaluate the indefinite integral ∫ (2x) / (x^2 + 1) dx.",
                "expected": "ln|x²+1|"
            },
            {
                "test_case_id": "TC_INT_015",
                "description": "Compute the integral ∫ tan(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ tan(x) dx.",
                "expected": "-ln|cos(x)|"
            },
            {
                "test_case_id": "TC_INT_016",
                "description": "Evaluate the integral ∫ e^(2x) sin(3x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ e^(2x) sin(3x) dx.",
                "expected": "(3e^(2x)cos(3x) - 2e^(2x)sin(3x))/13"
            },
            {
                "test_case_id": "TC_INT_017",
                "description": "Compute the integral ∫ dx / (x sqrt(x^2 - 1)).",
                "prompt": "Evaluate the indefinite integral ∫ dx / (x sqrt(x^2 - 1)) dx.",
                "expected": "arcsec(|x|)"
            },
            {
                "test_case_id": "TC_INT_018",
                "description": "Find the area under the curve y = x^2 from x = 0 to x = 3.",
                "prompt": "Compute the definite integral ∫₀^3 x^2 dx.",
                "expected": "9"
            },
            {
                "test_case_id": "TC_INT_019",
                "description": "Evaluate the integral ∫ dx / (1 + e^x).",
                "prompt": "Evaluate the indefinite integral ∫ dx / (1 + e^x).",
                "expected": "ln|1 + e^(-x)| + C"
            },
            {
                "test_case_id": "TC_INT_020",
                "description": "Compute the integral ∫ sin^2(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ sin^2(x) dx.",
                "expected": "x/2 - sin(2x)/4"
            },
            {
                "test_case_id": "TC_INT_021",
                "description": "Evaluate the integral ∫ x / (x^2 + 1) dx.",
                "prompt": "Evaluate the indefinite integral ∫ x / (x^2 + 1) dx.",
                "expected": "(1/2)ln|x²+1|"
            },
            {
                "test_case_id": "TC_INT_022",
                "description": "Find the integral ∫ e^(x) cos(x) dx.",
                "prompt": "Evaluate the indefinite integral ∫ e^(x) cos(x) dx.",
                "expected": "(e^x/2)(sin(x) + cos(x))"
            },
            {
                "test_case_id": "TC_INT_023",
                "description": "Compute the definite integral ∫₀¹ (2x^3 - x^2 + x - 1) dx.",
                "prompt": "Evaluate the definite integral ∫₀¹ (2x^3 - x^2 + x - 1) dx.",
                "expected": "-1/4"
            },
            {
                "test_case_id": "TC_INT_024",
                "description": "Evaluate the integral ∫ ln(x) / x dx.",
                "prompt": "Evaluate the indefinite integral ∫ ln(x) / x dx.",
                "expected": "ln(x))²/2"
            },
            {
                "test_case_id": "TC_INT_025",
                "description": "Find the integral ∫ (x^2 + 2x + 1) / (x + 1) dx.",
                "prompt": "Evaluate the indefinite integral ∫ (x^2 + 2x + 1) / (x + 1) dx.",
                "expected": "x^2"
            }
        ]
    }
]
