###
## NIKAKO NE SLATI SA IMPORTOM OVOGA DOLE, TO JE SAMO ZA TEST CASE (POGLEDAJ KOMENTAR U MAIN-u)

from data import test_cases  # pyright: ignore[reportUnusedImport]


# TELETABISI.py
def validate_and_fix_prices(
    prices: dict[str, float],
) -> dict:  # pyright: ignore[reportMissingTypeArgument]
    """
    Validates and fixes motor insurance pricing rules.
    Args:
    prices: dict with keys like "mtpl", "limited_casco_100", "casco_500"
    Returns:
    {
    "fixed_prices": dict[str, float],
    "issues": list[str]
    }
    """

    # TODO: FIX PLACEHOLDER
    fixed: dict[str, float] = prices.copy()
    issues: list[str] = []

    rules = [
        ("mtpl", "limited_casco_100", "inter"),
        ("mtpl", "casco_100", "inter"),
        #
        ("mtpl", "limited_casco_200", "inter"),
        ("mtpl", "limited_casco_500", "inter"),
        #
        ("mtpl", "casco_200", "inter"),
        ("mtpl", "casco_500", "inter"),
        #
        ("limited_casco_100", "casco_100", "inter"),
        ("limited_casco_200", "casco_200", "inter"),
        ("limited_casco_500", "casco_500", "inter"),
        #
        ("limited_casco_200", "limited_casco_100", "deductible"),
        ("limited_casco_500", "limited_casco_200", "deductible"),
        #
        ("casco_200", "casco_100", "deductible"),
        ("casco_500", "casco_200", "deductible"),
    ]

    MARKET_AVERAGES = {
        "mtpl": 500,
        "limited_casco": 900,
        "casco": 1200,
    }

    def get_product(key: str) -> str:
        parts = key.rsplit("_", 1)
        return parts[0] if parts[-1] in ("100", "200", "500") else key

    for cheaper, expensive, rule_type in rules:
        if not fixed[cheaper] < fixed[expensive]:
            if rule_type == "deductible":
                base_key: str = cheaper[:-3] + "100"
                percentage = 0.85 if cheaper.endswith("200") else 0.8

                if base_key in prices:
                    new_price = fixed[base_key] * percentage
                    fixed[cheaper] = new_price
                    issues.append(
                        f"{expensive} was below {cheaper} ({fixed[expensive]:.2f} < {fixed[cheaper]:.2f}). "
                    )

            elif rule_type == "inter":
                expensive_product = get_product(expensive)
                cheaper_product = get_product(cheaper)

                ratio = (
                    MARKET_AVERAGES[expensive_product]
                    / MARKET_AVERAGES[cheaper_product]
                )

                cheaper_violation_count = sum(
                    1
                    for c, e, r in rules
                    if r == "inter" and c == cheaper and fixed[c] >= fixed[e]
                )
                expensive_violation_count = sum(
                    1
                    for c, e, r in rules
                    if r == "inter" and e == expensive and fixed[c] >= fixed[e]
                )

                if cheaper_violation_count > expensive_violation_count:
                    new_price = fixed[expensive] / ratio
                    issues.append(
                        f"{cheaper} was above {expensive} ({fixed[cheaper]:.2f} > {fixed[expensive]:.2f}). "
                        f"Lowered {cheaper} to {new_price:.2f} using market ratio of {ratio:.2f}."
                    )
                    fixed[cheaper] = new_price
                else:
                    new_price = fixed[cheaper] * ratio
                    issues.append(
                        f"{expensive} was below {cheaper} ({fixed[expensive]:.2f} < {fixed[cheaper]:.2f}). "
                        f"Raised {expensive} to {new_price:.2f} using market ratio of {ratio:.2f}."
                    )
                    fixed[expensive] = new_price

    return {  # pyright: ignore[reportUnknownVariableType]
        "fixed_prices": fixed,
        "issues": issues,
    }


example_prices = {
    "mtpl": 400,
    "limited_casco_100": 850,
    "limited_casco_200": 900,
    "limited_casco_500": 700,
    "casco_100": 780,
    "casco_200": 950,
    "casco_500": 830,
}


if __name__ == "__main__":
    result = validate_and_fix_prices(  # pyright: ignore[reportUnknownVariableType]
        example_prices  # pyright: ignore[reportArgumentType]
    )
    print(example_prices)
    print(
        "Fixed prices:",
        result["fixed_prices"],  # pyright: ignore[reportUnknownArgumentType]
    )

    print("Issues found:")
    for issue in result["issues"]:
        # print("-", example_prices)
        print(issue)  # pyright: ignore[reportUnknownArgumentType]

    # --------------------------------------------------------------------
    ## NIKAKO OVO ISPOD NE SLATI, TO SU NASI TEST PRIMERI
    #    ovde ide test
    for i, test in enumerate(test_cases):
        print(f"\nCASE-----------------{i}----------------------------------")
        print(test)
        res = validate_and_fix_prices(test)
        for r, issue in res.items():
            # print("-", example_prices)
            print(r)
            print(issue)  # pyright: ignore[reportUnknownArgumentType]
    ##
