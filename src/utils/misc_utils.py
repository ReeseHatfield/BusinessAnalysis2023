def sort_dict_by_values(dict_to_sort: dict) -> dict:
    sorted_items = sorted(dict_to_sort.items(), key=lambda x: x[1], reverse=True)

    reversed_items = reversed(sorted_items)

    sorted_dict = dict(reversed_items)

    return sorted_dict
