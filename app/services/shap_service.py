import shap

from app.services.model_loader import models


# Create explainers once at startup
explainers = {
    name: shap.TreeExplainer(model)
    for name, model in models.items()
}


def get_top_factors(
    model_type,
    features,
    feature_names,
    top_n=5
):

    explainer = explainers[model_type]

    shap_values = explainer(features)

    # RandomForest binary classification handling
    if len(shap_values.values.shape) == 3:
        values = shap_values.values[0, :, 1]
    else:
        values = shap_values.values[0]

    contributions = list(
        zip(feature_names, values)
    )

    contributions = sorted(
        contributions,
        key=lambda x: abs(x[1]),
        reverse=True
    )

    top_factors = []

    for name, val in contributions[:top_n]:

        impact = round(float(val * 100), 3)

        if val > 0:
            text = (
                f"{name} increased risk "
                f"(impact {impact})"
            )
        else:
            text = (
                f"{name} decreased risk "
                f"(impact {impact})"
            )

        top_factors.append(text)

    return top_factors, contributions