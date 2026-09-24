# 🔬 Feature Engineering & Verification Methodology

### 1. Data Collection & Sanitization
* Profiles were sampled across Food, Tech, Fitness, and Finance niches.
* Ingestion handled via Apify headless browser instances parsing OpenGraph metadata.
* Missing values coerced to standardized numerical formats; exact duplicate rows removed.

### 2. Feature Definitions & Mathematical Formulations

#### A. Engagement Rate Formula
$$\text{Engagement Rate (\%)} = \left( \frac{\text{Likes} + \text{Comments}}{\max(\text{Views}, 1)} \right) \times 100$$

#### B. Log-Normalized Virality Index (0-100 Scale)
To balance massive outlier view counts against high engagement percentages:
$$\text{Virality Score} = 60 \times \left( \frac{\ln(1 + \text{Views})}{\ln(1 + \text{Views}_{\max})} \right) + \min(40, 4 \times \text{Engagement Rate})$$

Where:
* **75.0 - 100.0:** `Viral Hit`
* **50.0 - 74.9:** `High Reach`
* **30.0 - 49.9:** `Moderate Reach`
* **0.0 - 29.9:** `Standard`