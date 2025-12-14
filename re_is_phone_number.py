seen: dict[int, int] = {}
    for idx, key in enumerate(nums):
        comp = target - key
        if comp in seen:
            return[seen[comp], idx]
        seen[key] = idx