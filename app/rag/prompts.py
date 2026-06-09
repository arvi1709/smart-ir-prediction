def build_explanation_prompt(
    label,
    risk_category,
    risk_probability,
    contributions,
    context
):

    top_features = ", ".join(
        feature
        for feature, _ in contributions[:3]
    )

    return f"""
    explain to the user.

    Prediction Result:
    {label}

    Risk Category:
    {risk_category}

    Risk Probability:
    {risk_probability}%

    Top Contributing Factors:
    {top_features}

    Medical Context:
    {context}

    Instructions:

    1. First explain THIS patient's result.
    2. If the result is Normal or Low Risk, clearly reassure the patient.
    3. If the result is Insulin Resistant, explain what that means.
    4. Mention the most important contributing factors from this prediction.
    5. Use simple non-medical language.
    6. Suggest practical lifestyle improvements.
    7. Keep the explanation under 200 words.
    """