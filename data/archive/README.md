# 📱 Instagram Reels Performance & Virality Intelligence (2026)

## Overview
A real-world empirical dataset capturing authentic short-form video dynamics across prominent digital creators and diverse content niches. Extracted directly from live public profiles, this dataset is tailored for **content virality forecasting**, **engagement rate regression**, and **NLP multimodal caption modeling**.

---

## 📊 Dataset Statistics

| Metric | Value |
|---|---|
| Total Authentic Reels | 88 |
| Monitored Creators | 9 |
| Content Niches | 5 |
| Earliest Publication | 2024-03-09 11:20:14+00:00 |
| Latest Publication | 2026-09-08 13:18:09+00:00 |
| Aggregated View Count | 40,966,919 |
| Average Engagement Rate | 7.58% |

---

## 🔬 Core Columns

| Column | Type | Description |
|---|---|---|
| `post_id` | String | Unique Instagram media identifier |
| `shortcode` | String | URL permalink slug (`/reel/<shortcode>/`) |
| `creator_handle` | String | Anonymized or public creator account handle |
| `niche` | String | Categorized content vertical |
| `caption` | String | Full text caption including hashtags and emojis |
| `timestamp_utc` | DateTime | Timestamp of video publication (UTC) |
| `video_duration_sec`| Float | Video duration in seconds |
| `caption_word_count`| Integer | Word count of caption (excluding hashtags) |
| `hashtag_count` | Integer | Total hashtags detected |
| `views` | Integer | Recorded video view count |
| `likes` | Integer | Recorded like interaction count |
| `comments` | Integer | Total user comments posted |
| `engagement_rate_pct`| Float | Derived interaction metric: `((likes + comments) / views) * 100` |
| `virality_score` | Float | Multi-attribute composite score (0-100) |
| `virality_tier` | Category | Classification label (`Viral Hit`, `High Reach`, `Moderate Reach`, `Standard`) |

---

## 💡 Machine Learning & Analytics Use Cases
1. **Virality Classification:** Train Random Forest or XGBoost classifiers to predict whether a Reel reaches `Viral Hit` tier based on duration, caption length, and posting hour.
2. **Engagement Rate Modeling:** Multi-variable regression predicting audience participation intensity.
3. **NLP & Topic Discovery:** Extract keywords, emoji sentiment, and hashtag clustering to correlate linguistic tone with viewer retention.

---

## ⚠️ Source & Fair Use Compliance
* **Data Source:** Publicly accessible metrics collected via Apify Instagram Scraper API.
* **Ethics & Privacy:** Only aggregated, public account engagement metrics are indexed. No private messages, user personal data, or restricted media were collected. Intended strictly for non-commercial research, machine learning benchmarking, and educational analytics.