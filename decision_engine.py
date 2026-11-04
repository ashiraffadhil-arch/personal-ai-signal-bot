from dataclasses import dataclass

@dataclass class AnalysisResult: probability: float confidence: str risk_level: str recommendation: str

def analyze_probability(probability, data_quality):

if not 0 <= probability <= 1:
    raise ValueError("Probability must be between 0 and 1")

if not 0 <= data_quality <= 1:
    raise ValueError("Data quality must be between 0 and 1")

if data_quality < 0.5:
    confidence = "LOW"
elif data_quality < 0.8:
    confidence = "MEDIUM"
else:
    confidence = "HIGH"

if probability >= 0.8:
    risk = "LOW"
elif probability >= 0.5:
    risk = "MEDIUM"
else:
    risk = "HIGH"

recommendation = (
    "INSUFFICIENT DATA"
    if data_quality < 0.5
    else "ANALYSIS AVAILABLE"
)

return AnalysisResult(
    probability=round(probability * 100, 2),
    confidence=confidence,
    risk_level=risk,
    recommendation=recommendation
)
