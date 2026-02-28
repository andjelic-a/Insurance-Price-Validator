###
## NIKAKO NE SLATI SA IMPORTOM OVOGA DOLE, TO JE SAMO ZA TEST CASE (POGLEDAJ KOMENTAR U MAIN-u)
from .data import test_cases


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
    fixed = prices.copy()
    issues = []

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

    result = validate_and_fix_prices(
        example_prices  # pyright: ignore[reportArgumentType]
    )

    ### NIKAKO OVO ISPOD NE SLATI, TO SU NASI TEST PRIMERI
    # ovde ide test
    ###
    print("Fixed prices:", result["fixed_prices"])
    print("Issues found:")

    for issue in result["issues"]:
        print("-", issue)
