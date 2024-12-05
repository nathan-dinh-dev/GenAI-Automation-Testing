# test_cases.py

test_cases = [
    {
        "chapter": "Derivatives",
        "tester": "Aaron",
        "cases": [
            {
                "test_case_id": "TC_DER_001",
                "description": "Find the slope of the tangent line to the parabola y = 4x - x^2 at the point (1,3).",
                "prompt": "Find the slope of the tangent line to the parabola y = 4x - x^2 at the point (1,3).",
                "expected": "2"
            },
            {
                "test_case_id": "TC_DER_002",
                "description": "Find an equation of the normal line to the parabola y=x^2-5x+4 that is parallel to the line x-3y=5.",
                "prompt": "Find an equation of the normal line to the parabola y=x^2-5x+4 that is parallel to the line x-3y=5.",
                "expected": "x+3y-1=0"
            },
            {
                "test_case_id": "TC_DER_009",
                "description": "A spherical balloon is being inflated. Find the rate of increase of the surface area (S = 4πr²) with respect to the radius r when r is 1 ft.",
                "prompt": "A spherical balloon is being inflated. Find the rate of increase of the surface area (S = 4πr²) with respect to the radius r when r is 1 ft.",
                "expected": "8π"
            },
            {
                "test_case_id": "TC_DER_010",
                "description": "Find R'(0), where R(x) = (x - 3x^3 + 5x^5) / (1 + 3x^3 + 6x^6 + 9x^9) Hint: Instead of finding R'(x) first, let f(x) be the numerator and g(x) the denominator of R(x) and compute R'(0) from f(0), f'(0), g(0), and g'(0).",
                "prompt": "Find R'(0), where R(x) = (x - 3x^3 + 5x^5) / (1 + 3x^3 + 6x^6 + 9x^9) Hint: Instead of finding R'(x) first, let f(x) be the numerator and g(x) the denominator of R(x) and compute R'(0) from f(0), f'(0), g(0), and g'(0).",
                "expected": "1"
            },
            {
                "test_case_id": "TC_DER_011",
                "description": "Find R'(0), where R(x) = (x - 3x^3 + 5x^5) / (1 + 3x^3 + 6x^6 + 9x^9) Hint: Instead of finding R'(x) first, let f(x) be the numerator and g(x) the denominator of R(x) and compute R'(0) from f(0), f'(0), g(0), and g'(0).",
                "prompt": "Find R'(0), where R(x) = (x - 3x^3 + 5x^5) / (1 + 3x^3 + 6x^6 + 9x^9) Hint: Instead of finding R'(x) first, let f(x) be the numerator and g(x) the denominator of R(x) and compute R'(0) from f(0), f'(0), g(0), and g'(0).",
                "expected": "1"
            },
            {
                "test_case_id": "TC_DER_012",
                "description": "A Cepheid variable star is a star whose brightness alternately increases and decreases. The most easily visible such star is Delta Cephei, for which the interval between times of maximum brightness is 5.4 days. The average brightness of this star is 4.0 and its brightness changes by ±0.35. In view of these data, the brightness of Delta Cephei at time t, where t is measured in days, has been modeled by the function B(t) = 4.0 + 0.35 sin(2πt/5.4). Find the rate of change of the brightness after t days.",
                "prompt": "A Cepheid variable star is a star whose brightness alternately increases and decreases. The most easily visible such star is Delta Cephei, for which the interval between times of maximum brightness is 5.4 days. The average brightness of this star is 4.0 and its brightness changes by ±0.35. In view of these data, the brightness of Delta Cephei at time t, where t is measured in days, has been modeled by the function B(t) = 4.0 + 0.35 sin(2πt/5.4). Find the rate of change of the brightness after t days.",
                "expected": "(7/54)π cos(2πt/5.4)"
            },
            # {
            #     "test_case_id": "TC_DER_013",
            #     "description": "",
            #     "prompt": "",
            #     "expected": "L(x) = -10x - 6"
            # },
            {
                "test_case_id": "TC_DER_014",
                "description": "A runner sprints around a circular track of radius 100 m at a constant speed of 7 m/s. The runner's friend is standing at a distance 200 m from the center of the track. How fast is the distance between the friends changing when the distance between them is 200 m?",
                "prompt": "A runner sprints around a circular track of radius 100 m at a constant speed of 7 m/s. The runner's friend is standing at a distance 200 m from the center of the track. How fast is the distance between the friends changing when the distance between them is 200 m?",
                "expected": "(7/4)√15"
            },
            {
                "test_case_id": "TC_DER_015",
                "description": "Find the derivative of the function using the definition of derivative. State the domain of the function and the domain of its derivative for f(x)=1/2x-1/3",
                "prompt": "Find the derivative of the function using the definition of derivative. State the domain of the function and the domain of its derivative for f(x)=1/2x-1/3",
                "expected": """1/2
(-∞,∞)
(-∞,∞)"""
            },
            {
                "test_case_id": "TC_DER_016",
                "description": "Differentiate the constant function f(x) = 2^40.",
                "prompt": "Differentiate the function f(x) = 2^40.",
                "expected": "0"
            },
            {
                "test_case_id": "TC_DER_017",
                "description": "Differentiate g(t) = t^3 cos(t).",
                "prompt": "Differentiate g(t) = t^3 cos(t).",
                "expected": "3t^2cos(t) - t^3sin(t)"
            },
            {
                "test_case_id": "TC_DER_018",
                "description": "Use quotient rule to solve f(x)=x/(x+(c/x))",
                "prompt": "Use quotient rule to solve f(x)=x/(x+(c/x))",
                "expected": "2cx/(x^2+c)^2"
            },
            {
                "test_case_id": "TC_DER_019",
                "description": "Find the derivative of the function F(x) = (x^4 + 3x^2 - 2)^5.",
                "prompt": "Find the derivative of the function F(x) = (x^4 + 3x^2 - 2)^5.",
                "expected": "10(x^4+3x^2-2)^4(2x^3+3x)"
            },
            {
                "test_case_id": "TC_DER_020",
                "description": "Find dy/dx by implicit differentiation for x^3 + y^3 = 1.",
                "prompt": "Find dy/dx by implicit differentiation for x^3 + y^3 = 1.",
                "expected": "-x^2/y^2"
            },
            {
                "test_case_id": "TC_DER_021",
                "description": "Find the linearization L(x) of the function at a = -1 for f(x) = x^4 + 3x^2.",
                "prompt": "Find the linearization L(x) of the function at a = -1 for f(x) = x^4 + 3x^2.",
                "expected": "L(x)=-10x-6"
            },
            {
                "test_case_id": "TC_DER_022",
                "description": "Given a function f(x) = e^(2x), find the second derivative.",
                "prompt": "Given a function f(x) = e^(2x), find the second derivative.",
                "expected": "4e^(2x)"
            },
            {
                "test_case_id": "TC_DER_023",
                "description": "Find the derivative of f(x) = sin(x).",
                "prompt": "Find the derivative of f(x) = sin(x).",
                "expected": "cos(x)"
            },
            {
                "test_case_id": "TC_DER_024",
                "description": "Differentiate f(x)=x^3.",
                "prompt": "Differentiate f(x)=x^3.",
                "expected": "3x^2"
            },
            {
                "test_case_id": "TC_DER_025",
                "description": "Differentiate f(x)=4x^3-2x^2+x-5 using the power rule.",
                "prompt": "Differentiate f(x)=4x^3-2x^2+x-5 using the power rule.",
                "expected": "12x^2-4x+1"
            }
        ]
    },
    {
        "chapter": "Applications of Differentiation",
        "tester": "Krishna",
        "cases": [
            {
                "test_case_id": "TC_APP_001",
                "description": "Find the critical points of f(x) = x^3 - 3x^2 + 4.",
                "prompt": "Find the critical points of f(x) = x^3 - 3x^2 + 4.",
                "expected": "0, 2"
            },
            {
                "test_case_id": "TC_APP_002",
                "description": "Determine the intervals where f(x) = x^3 - 6x is increasing or decreasing.",
                "prompt": "Determine the intervals where f(x) = x^3 - 6x is increasing or decreasing.",
                "expected": "Increasing: (-∞, -√2) ∪ (√2, ∞) Decreasing: (-√2, √2)"
            },
            {
                "test_case_id": "TC_APP_003",
                "description": "Find the local maxima and minima of f(x) = x^4 - 8x^2.",
                "prompt": "Find the local maxima and minima of f(x) = x^4 - 8x^2.",
                "expected": "Local maxima: 0 Local minima: -2, 2"
            },
            {
                "test_case_id": "TC_APP_004",
                "description": "Find the absolute maximum and minimum of f(x) = x^3 - 3x + 1 on [-2, 2].",
                "prompt": "Find the absolute maximum and minimum of f(x) = x^3 - 3x + 1 on [-2, 2].",
                "expected": "Absolute maximum: 2, Absolute minimum: -1"
            },
            {
                "test_case_id": "TC_APP_005",
                "description": "Determine the concavity and inflection points of f(x) = x^3 - 6x^2 + 9x + 15.",
                "prompt": "Determine the concavity and inflection points of f(x) = x^3 - 6x^2 + 9x + 15.",
                "expected": "Concave up: (2, ∞) Concave down: (-∞, 2) Inflection point: 2"
            },
            {
                "test_case_id": "TC_APP_006",
                "description": "Use Newton's method to approximate the root of f(x) = x^2 - 2 starting at x0 = 1.",
                "prompt": "Use Newton's method to approximate the root of f(x) = x^2 - 2 starting at x0 = 1.",
                "expected": "1.414"
            },
            {
                "test_case_id": "TC_APP_007",
                "description": "Find the point on the curve y = sqrt(x) closest to the point (4, 0).",
                "prompt": "Find the point on the curve y = sqrt(x) closest to the point (4, 0).",
                "expected": "(2, √2)"
            },
            {
                "test_case_id": "TC_APP_008",
                "description": "Determine the maximum area of a rectangle inscribed under the curve y = 4 - x^2.",
                "prompt": "Determine the maximum area of a rectangle inscribed under the curve y = 4 - x^2.",
                "expected": "16/3"
            },
            {
                "test_case_id": "TC_APP_009",
                "description": "A ladder 10 ft long leans against a wall. If the bottom slides away at 1 ft/s, how fast is the top sliding down when the bottom is 6 ft from the wall?",
                "prompt": "A ladder 10 ft long leans against a wall. If the bottom slides away at 1 ft/s, how fast is the top sliding down when the bottom is 6 ft from the wall?",
                "expected": "3/4"
            },
            {
                "test_case_id": "TC_APP_010",
                "description": "Find the rate of change of the volume of a sphere with respect to its radius when r = 5.",
                "prompt": "Find the rate of change of the volume of a sphere with respect to its radius when r = 5.",
                "expected": "100π"
            },
            {
                "test_case_id": "TC_APP_011",
                "description": "Determine the curvature of the curve y = ln(x) at x = 1.",
                "prompt": "Determine the curvature of the curve y = ln(x) at x = 1.",
                "expected": "1"
            },
            {
                "test_case_id": "TC_APP_012",
                "description": "Find the equation of the tangent line to the curve y = x^2 at x = 3.",
                "prompt": "Find the equation of the tangent line to the curve y = x^2 at x = 3.",
                "expected": "y = 6x - 9"
            },
            {
                "test_case_id": "TC_APP_013",
                "description": "A particle moves along a line so that its position at time t is s(t) = t^3 - 6t^2 + 9t. Find the acceleration at t = 2.",
                "prompt": "A particle moves along a line so that its position at time t is s(t) = t^3 - 6t^2 + 9t. Find the acceleration at t = 2.",
                "expected": "6"
            },
            {
                "test_case_id": "TC_APP_014",
                "description": "Determine the intervals of concavity for f(x) = x / (x^2 + 1).",
                "prompt": "Determine the intervals of concavity for f(x) = x / (x^2 + 1).",
                "expected": "Concave up: (-∞, -√3/3) ∪ (√3/3, ∞) Concave down: (-√3/3, √3/3)"
            },
            {
                "test_case_id": "TC_APP_015",
                "description": "Find the dimensions of a rectangle with perimeter 100 m that has the maximum area.",
                "prompt": "Find the dimensions of a rectangle with perimeter 100 m that has the maximum area.",
                "expected": "25 m × 25 m"
            },
            {
                "test_case_id": "TC_APP_016",
                "description": "A cone is formed by rotating a right triangle about one of its legs. For a given hypotenuse length of 10 cm, find the angle that maximizes the volume of the cone.",
                "prompt": "A cone is formed by rotating a right triangle about one of its legs. For a given hypotenuse length of 10 cm, find the angle that maximizes the volume of the cone.",
                "expected": "π/3"
            },
            {
                "test_case_id": "TC_APP_017",
                "description": "Use the Mean Value Theorem to show that the equation x^3 + x + 1 = 0 has exactly one real root.",
                "prompt": "Use the Mean Value Theorem to show that the equation x^3 + x + 1 = 0 has exactly one real root.",
                "expected": "Function is strictly increasing, so one real root"
            },
            {
                "test_case_id": "TC_APP_018",
                "description": "Find the linear approximation of f(x) = sqrt(x) at x = 16.",
                "prompt": "Find the linear approximation of f(x) = sqrt(x) at x = 16.",
                "expected": "y = 0.25x + 2"
            },
            {
                "test_case_id": "TC_APP_019",
                "description": "Determine the maximum profit if the profit function is P(x) = -2x^2 + 80x - 200.",
                "prompt": "Determine the maximum profit if the profit function is P(x) = -2x^2 + 80x - 200.",
                "expected": "Maximum profit is $800 at x = 20"
            },
            {
                "test_case_id": "TC_APP_020",
                "description": "A tank is being filled with water at a rate of 5 m³/min. If the tank has a shape of a cone with radius 2 m and height 6 m, how fast is the water level rising when the water is 3 m deep?",
                "prompt": "A tank is being filled with water at a rate of 5 m³/min. If the tank has a shape of a cone with radius 2 m and height 6 m, how fast is the water level rising when the water is 3 m deep?",
                "expected": "dh/dt ≈ 0.318 m/min"
            },
            {
                "test_case_id": "TC_APP_021",
                "description": "Find the point on the curve y = x^2 closest to the point (0, 3).",
                "prompt": "Find the point on the curve y = x^2 closest to the point (0, 3).",
                "expected": "(√(3/2), 3/2)"
            },
            {
                "test_case_id": "TC_APP_022",
                "description": "A rectangle is inscribed in a circle of radius r. What is the maximum area of such a rectangle?",
                "prompt": "A rectangle is inscribed in a circle of radius r. What is the maximum area of such a rectangle?",
                "expected": "2r²"
            },
            {
                "test_case_id": "TC_APP_023",
                "description": "Use differentials to approximate the value of √(25.5).",
                "prompt": "Use differentials to approximate the value of √(25.5).",
                "expected": "5.05"
            },
            {
                "test_case_id": "TC_APP_024",
                "description": "Find the dimensions of a box with a square base and open top that has a volume of 32 cubic meters and minimal surface area.",
                "prompt": "Find the dimensions of a box with a square base and open top that has a volume of 32 cubic meters and minimal surface area.",
                "expected": "Base: 4 meters, Height: 2 meters"
            },
            {
                "test_case_id": "TC_APP_025",
                "description": "A man walks along a straight path at 4 ft/s. A streetlight is 20 ft above the ground. How fast is the tip of his shadow moving when he is 30 ft from the light?",
                "prompt": "A man walks along a straight path at 4 ft/s. A streetlight is 20 ft above the ground. How fast is the tip of his shadow moving when he is 30 ft from the light?",
                "expected": "8"
            }
        ]
    },
    {
        "chapter": "Integrals",
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
                "expected": "xln(x)-x"
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
