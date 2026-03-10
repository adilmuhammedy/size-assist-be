# recommendation.py

def select_best_size(ranked_sizes, tightness=2):
    
    """
    tightness:
    0 = very tight
    1 = tight
    2 = regular (default)
    3 = loose
    4 = very loose
    """
    
    best = ranked_sizes[0]
    best_chart_index = best["chart_index"]
    
    shift = tightness - 2
    target_index = best_chart_index + shift  # move up/down the actual size ladder
    target_index = max(0, min(target_index, len(ranked_sizes) - 1))

    # Find the size at that chart position
    target = next(s for s in ranked_sizes if s["chart_index"] == target_index)
    return {
        "recommendedSize": target["size"],
        "goodFit": target["score"] <= 2
    }