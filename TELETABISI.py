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
        # gotovo
        ("casco_200", "casco_100"),
        ("casco_500", "casco_200"),
        #
        ("mtpl", "limited_casco_100"),
        ("mtpl", "limited_casco_200"),
        ("mtpl", "limited_casco_500"),
        #
        ("mtpl", "casco_100"),
        ("mtpl", "casco_200"),
        ("mtpl", "casco_500"),
        #
        ("limited_casco_100", "casco_100"),
        ("limited_casco_200", "casco_200"),
        ("limited_casco_500", "casco_500"),
        #
        # gotovo
        ("limited_casco_200", "limited_casco_100"),
        ("limited_casco_500", "limited_casco_200"),
    ]

    for cheaper, expensive in rules:
        if not prices[cheaper] < prices[expensive]:
            issues.append(
                f"Rule violated: {cheaper} must be strictly less than {expensive}!"
            )

            if (
                cheaper.endswith("200")
                or cheaper.endswith("500")
                and cheaper[:-3] == expensive[:-3]
            ):
                base_key: str = cheaper[:-3] + "100"
                percentage = 0.85 if cheaper.endswith("200") else 0.8

                if base_key in prices:
                    new_price = prices[base_key] * percentage
                    fixed[cheaper] = new_price

            elif cheaper[:-3] != expensive[:-3]:
                # TODO: uradi inter-proizvodni kurac
                print(cheaper + "," + expensive)
                print(abs(fixed[cheaper] - fixed[expensive]))
                continue

    return {  # pyright: ignore[reportUnknownVariableType]
        "fixed_prices": fixed,
        "issues": issues,
    }


"""
Product Hierarchy Rules

The general cost relationship must hold: MTPL < Limited Casco < Casco

Specifically:

    mtpl < limited_casco_100
    mtpl < limited_casco_200
    mtpl < limited_casco_500
    limited_casco_100 < casco_100
    limited_casco_200 < casco_200
    limited_casco_500 < casco_500

Deductible Ordering Rules

A higher deductible means a lower premium: price(500€) < price(200€) < price(100€)

For Limited Casco:

    limited_casco_200 < limited_casco_100
    limited_casco_500 < limited_casco_200

For Casco:

    casco_200 < casco_100
    casco_500 < casco_200
"""

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

    print(
        "Fixed prices:",
        result["fixed_prices"],  # pyright: ignore[reportUnknownArgumentType]
    )

    print("Issues found:")
    for issue in result["issues"]:
        # print("-", example_prices)
        print(issue)  # pyright: ignore[reportUnknownArgumentType]

    # --------------------------------------------------------------------
    ### NIKAKO OVO ISPOD NE SLATI, TO SU NASI TEST PRIMERI
    # ovde ide test
    # for test in test_cases:
    #     res = validate_and_fix_prices(test)
    #     for r, issue in res.items():
    #         # print("-", example_prices)
    #         print(r)
    #         print(issue)  # pyright: ignore[reportUnknownArgumentType]
    ###
