def evaluate_application(score, documents_complete, age, interview_score):
    if score < 70:
        return False, f"Score {score} is below the minimum of 70."
    if not documents_complete:
        return False, "Required documents are incomplete."
    if age < 18:
        return False, f"Age {age} is below the minimum of 18."
    if interview_score < 60:
        return (
            False,
            f"Interview score {interview_score} is below the minimum "
            f"of 60.",
        )
    return True, "All four conditions passed."


test_cases = [
    {
        "name": "Pass",
        "input": {
            "score": 82,
            "documents_complete": True,
            "age": 22,
            "interview_score": 75,
        },
        "expected": True,
    },
    {
        "name": "Fail minimum-age condition",
        "input": {
            "score": 82,
            "documents_complete": True,
            "age": 17,
            "interview_score": 75,
        },
        "expected": False,
    },
    {
        "name": "Fail interview-score condition",
        "input": {
            "score": 82,
            "documents_complete": True,
            "age": 22,
            "interview_score": 59,
        },
        "expected": False,
    },
    {
        "name": "Score threshold boundary",
        "input": {
            "score": 70,
            "documents_complete": True,
            "age": 18,
            "interview_score": 60,
        },
        "expected": True,
    },
]



for case in test_cases:
    actual, reason = evaluate_application(**case["input"])
    print(f"\nCase: {case['name']}")
    print(f"Input: {case['input']}")
    print(f"Expected result: {case['expected']}")
    print(f"Actual result: {actual}")
    print(f"Reason: {reason}")
