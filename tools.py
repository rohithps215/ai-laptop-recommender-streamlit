
import json

# Load laptop dataset
def load_laptops():
    with open("laptop_data.json", "r") as file:
        return json.load(file)


# Tool 1: Filter laptops
def filter_laptops(
    max_budget=None,
    min_ram=None,
    min_storage=None,
    dedicated_gpu=False,
    usage=None
):
    laptops = load_laptops()
    filtered = []

    for laptop in laptops:

        if max_budget is not None and laptop["price"] > max_budget:
            continue

        if min_ram is not None and laptop["ram"] < min_ram:
            continue

        if min_storage is not None and laptop["storage"] < min_storage:
            continue

        if dedicated_gpu and "integrated" in laptop["gpu"].lower():
            continue

        if usage is not None and usage not in laptop["usage"]:
            continue

        filtered.append(laptop)

    return filtered


# Tool 2: Score and rank laptops
def score_laptops(laptops, max_budget=None, usage=None):

    weights = {
        "price": 30,
        "processor": 20,
        "ram": 15,
        "storage": 10,
        "gpu": 15,
        "usage": 10
    }

    results = []

    for laptop in laptops:

        # Lower price gets a higher score within the budget
        if max_budget:
            price_score = max(
                0, 100 - (laptop["price"] / max_budget * 100)
            )
        else:
            price_score = 100 - (
                laptop["price"] / 160000 * 100
            )

        cpu_score = laptop["cpu_score"]

        ram_score = min(laptop["ram"] / 32 * 100, 100)

        storage_score = min(
            laptop["storage"] / 1024 * 100, 100
        )

        gpu_score = laptop["gpu_score"]

        usage_score = (
            100 if usage in laptop["usage"] else 40
        ) if usage else 70

        final_score = (
            price_score * weights["price"] / 100
            + cpu_score * weights["processor"] / 100
            + ram_score * weights["ram"] / 100
            + storage_score * weights["storage"] / 100
            + gpu_score * weights["gpu"] / 100
            + usage_score * weights["usage"] / 100
        )

        laptop_result = laptop.copy()
        laptop_result["score"] = round(final_score, 2)

        results.append(laptop_result)

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )


def recommend_laptops(
    max_budget: int = None,
    min_ram: int = None,
    min_storage: int = None,
    dedicated_gpu: bool = False,
    usage: str = ""
):
    """
    Find and rank laptops based on user requirements.

    Use this tool when the user wants laptop recommendations.
    """

    filtered = filter_laptops(
        max_budget=max_budget,
        min_ram=min_ram,
        min_storage=min_storage,
        dedicated_gpu=dedicated_gpu,
        usage=usage if usage else None
    )

    ranked = score_laptops(
        filtered,
        max_budget=max_budget,
        usage=usage if usage else None
    )

    return ranked[:5]
