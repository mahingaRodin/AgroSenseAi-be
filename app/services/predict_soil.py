def predict_soil_fertility(nitrogen: float, phosphorus: float, potassium: float) -> dict:
    if nitrogen < 50 or phosphorus < 30 or potassium < 40:
        fertility = "Poor"
        recommendation = "Add organic compost and NPK-rich fertilizers."
    elif 50 <= nitrogen <= 120 and 30 <= phosphorus <= 70 and 40 <= potassium <= 100:
        fertility = "Fertile"
        recommendation = "Good nutrient balance for most crops."
    else:
        fertility = "Excessive"
        recommendation = "Too much fertilizer. Consider soil dilution or crop rotation."

    return {
        "fertility": fertility,
        "recommendation": recommendation
    }
