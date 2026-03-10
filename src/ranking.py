# ranking.py

def evaluate_range(body_value: float, size_range):
    if size_range is None:
        return 0

    lower, upper = size_range

    if lower <= body_value <= upper:
        return 0

    if body_value < lower:
        return lower - body_value
    else:
        return body_value - upper


def generate_ranking(body, size_chart):
    ranked = []

    for size in size_chart:
        total_score = 0
        count = 0

        if size.chest:
            total_score += evaluate_range(body.chest, size.chest)
            count += 1

        if size.waist:
            total_score += evaluate_range(body.waist, size.waist)
            count += 1

        if size.shoulder:
            total_score += evaluate_range(body.shoulder, size.shoulder)
            count += 1

        avg_score = total_score / count if count else 999

        ranked.append({
            "size": size.name,
            "score": round(avg_score, 2),
            "chart_index": size_chart.index(size)  # preserves S < M < L order
        })

    # 🔥 Sort by actual score (lower = better)
    ranked.sort(key=lambda x: x["score"])

    return ranked