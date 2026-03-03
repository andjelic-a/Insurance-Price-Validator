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
                        f"[DEDUCTIBLE RULE] '{expensive}' ({fixed[expensive]:.2f}) was priced BELOW '{cheaper}' ({prices[cheaper]:.2f}), "
                        f"but higher deductibles must always be cheaper. "
                        f"Adjusted '{cheaper}' to {new_price:.2f} ({percentage * 100:.0f}% of base '{base_key}' = {fixed[base_key]:.2f})."
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
                        f"[PRODUCT ORDER RULE] '{cheaper}' ({prices[cheaper]:.2f}) was priced ABOVE '{expensive}' ({prices[expensive]:.2f}), "
                        f"but '{expensive}' must always be more expensive than '{cheaper}'. "
                        f"'{cheaper}' appears in more violations, so it is the outlier. "
                        f"Lowered '{cheaper}' from {prices[cheaper]:.2f} to {new_price:.2f} "
                        f"using market ratio {expensive_product}/{cheaper_product} = {ratio:.2f} "
                        f"(market averages: {expensive_product}={MARKET_AVERAGES[expensive_product]}, {cheaper_product}={MARKET_AVERAGES[cheaper_product]})."
                    )
                    fixed[cheaper] = new_price
                    if cheaper.endswith("100"):
                        for ded in ("_200", "_500"):
                            percentage = 0.85 if ded.endswith("200") else 0.8
                            ded_key = cheaper_product + ded
                            old_ded = fixed[ded_key]
                            fixed[ded_key] = fixed[cheaper] * percentage
                            issues.append(
                                f"[DEDUCTIBLE CASCADE] Recalculated '{ded_key}' from {old_ded:.2f} to {fixed[ded_key]:.2f} "
                                f"({percentage * 100:.0f}% of updated base '{cheaper}' = {fixed[cheaper]:.2f}) "
                                f"to keep deductible tiers consistent."
                            )
                else:
                    new_price = fixed[cheaper] * ratio
                    issues.append(
                        f"[PRODUCT ORDER RULE] '{expensive}' ({prices[expensive]:.2f}) was priced BELOW '{cheaper}' ({prices[cheaper]:.2f}), "
                        f"but '{expensive}' must always be more expensive than '{cheaper}'. "
                        f"'{expensive}' appears in more violations, so it is the outlier. "
                        f"Raised '{expensive}' from {prices[expensive]:.2f} to {new_price:.2f} "
                        f"using market ratio {expensive_product}/{cheaper_product} = {ratio:.2f} "
                        f"(market averages: {expensive_product}={MARKET_AVERAGES[expensive_product]}, {cheaper_product}={MARKET_AVERAGES[cheaper_product]})."
                    )
                    fixed[expensive] = new_price
                    if expensive.endswith("100"):
                        for ded in ("_200", "_500"):
                            percentage = 0.85 if ded.endswith("200") else 0.8
                            ded_key = expensive_product + ded
                            old_ded = fixed[ded_key]
                            fixed[ded_key] = fixed[expensive] * percentage
                            issues.append(
                                f"[DEDUCTIBLE CASCADE] Recalculated '{ded_key}' from {old_ded:.2f} to {fixed[ded_key]:.2f} "
                                f"({percentage * 100:.0f}% of updated base '{expensive}' = {fixed[expensive]:.2f}) "
                                f"to keep deductible tiers consistent."
                            )

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
