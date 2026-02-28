test_cases: list[dict[str, float]] = [
    # === CASE 0: The provided example ===
    {
        "ntpl": 400,
        "limited_casco_100": 850,
        "limited_casco_200": 900,
        "limited_casco_500": 700,
        "casco_100": 780,
        "casco_200": 950,
        "casco_500": 830,
    },
    # === CASE 1: Everything perfectly valid ===
    {
        "ntpl": 500,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 2: All prices identical (all rules violated) ===
    {
        "ntpl": 500,
        "limited_casco_100": 500,
        "limited_casco_200": 500,
        "limited_casco_500": 500,
        "casco_100": 500,
        "casco_200": 500,
        "casco_500": 500,
    },
    # === CASE 3: Product hierarchy completely inverted ===
    {
        "ntpl": 1500,
        "limited_casco_100": 1000,
        "limited_casco_200": 900,
        "limited_casco_500": 800,
        "casco_100": 600,
        "casco_200": 500,
        "casco_500": 400,
    },
    # === CASE 4: Deductible ordering inverted for limited_casco only ===
    {
        "ntpl": 300,
        "limited_casco_100": 600,
        "limited_casco_200": 700,
        "limited_casco_500": 800,
        "casco_100": 1100,
        "casco_200": 935,
        "casco_500": 880,
    },
    # === CASE 5: Deductible ordering inverted for casco only ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1000,
        "casco_200": 1100,
        "casco_500": 1200,
    },
    # === CASE 6: Deductible ordering inverted for BOTH limited_casco and casco ===
    {
        "ntpl": 350,
        "limited_casco_100": 700,
        "limited_casco_200": 750,
        "limited_casco_500": 800,
        "casco_100": 1000,
        "casco_200": 1050,
        "casco_500": 1100,
    },
    # === CASE 7: ntpl > limited_casco_100 (hierarchy violation at bottom) ===
    {
        "ntpl": 950,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 8: limited_casco_100 > casco_100 (hierarchy violation at top) ===
    {
        "ntpl": 400,
        "limited_casco_100": 1300,
        "limited_casco_200": 1100,
        "limited_casco_500": 1000,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 9: ntpl > casco_100 (extreme hierarchy inversion) ===
    {
        "ntpl": 1500,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 10: Very low prices, all valid ===
    {
        "ntpl": 50,
        "limited_casco_100": 100,
        "limited_casco_200": 85,
        "limited_casco_500": 80,
        "casco_100": 150,
        "casco_200": 127.5,
        "casco_500": 120,
    },
    # === CASE 11: Very high prices, all valid ===
    {
        "ntpl": 5000,
        "limited_casco_100": 9000,
        "limited_casco_200": 7650,
        "limited_casco_500": 7200,
        "casco_100": 12000,
        "casco_200": 10200,
        "casco_500": 9600,
    },
    # === CASE 12: limited_casco 200 == 500 (tie in deductibles) ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 750,
        "limited_casco_500": 750,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 13: casco 200 == 500 (tie in deductibles) ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1000,
        "casco_500": 1000,
    },
    # === CASE 14: ntpl == limited_casco_500 (hierarchy tie) ===
    {
        "ntpl": 720,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 15: limited_casco_500 == casco_500 (cross-product tie) ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 960,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 16: Only deductible 100 vs 200 swapped in limited_casco ===
    {
        "ntpl": 400,
        "limited_casco_100": 750,
        "limited_casco_200": 800,
        "limited_casco_500": 700,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 17: Only deductible 200 vs 500 swapped in casco ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 950,
        "casco_500": 1000,
    },
    # === CASE 18: ntpl barely above limited_casco_500 ===
    {
        "ntpl": 721,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 19: casco_100 barely below limited_casco_100 ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 899,
        "casco_200": 850,
        "casco_500": 800,
    },
    # === CASE 20: Multiple hierarchy violations + deductible violations ===
    {
        "ntpl": 1000,
        "limited_casco_100": 800,
        "limited_casco_200": 850,
        "limited_casco_500": 900,
        "casco_100": 700,
        "casco_200": 750,
        "casco_500": 780,
    },
    # === CASE 21: Prices in descending order by key (worst case) ===
    {
        "ntpl": 2000,
        "limited_casco_100": 1800,
        "limited_casco_200": 1600,
        "limited_casco_500": 1400,
        "casco_100": 1200,
        "casco_200": 1000,
        "casco_500": 800,
    },
    # === CASE 22: All deductible prices equal within each product ===
    {
        "ntpl": 300,
        "limited_casco_100": 700,
        "limited_casco_200": 700,
        "limited_casco_500": 700,
        "casco_100": 1000,
        "casco_200": 1000,
        "casco_500": 1000,
    },
    # === CASE 23: Minimal spread, everything just barely valid ===
    {
        "ntpl": 499,
        "limited_casco_100": 500,
        "limited_casco_200": 499,
        "limited_casco_500": 498,
        "casco_100": 501,
        "casco_200": 500,
        "casco_500": 499,
    },
    # === CASE 24: ntpl = 0 (edge case: free product) ===
    {
        "ntpl": 0,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 25: Very tiny prices with violations ===
    {
        "ntpl": 10,
        "limited_casco_100": 8,
        "limited_casco_200": 9,
        "limited_casco_500": 11,
        "casco_100": 7,
        "casco_200": 12,
        "casco_500": 15,
    },
    # === CASE 26: Only casco hierarchy broken (limited_casco_100 > casco_100) ===
    {
        "ntpl": 400,
        "limited_casco_100": 1250,
        "limited_casco_200": 1062,
        "limited_casco_500": 1000,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 27: ntpl == casco_500 ===
    {
        "ntpl": 960,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 28: Realistic valid mid-range ===
    {
        "ntpl": 450,
        "limited_casco_100": 850,
        "limited_casco_200": 722.5,
        "limited_casco_500": 680,
        "casco_100": 1100,
        "casco_200": 935,
        "casco_500": 880,
    },
    # === CASE 29: ntpl slightly above limited_casco_200 ===
    {
        "ntpl": 770,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 30: Casco deductible 100 < 200 only ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 950,
        "casco_200": 1020,
        "casco_500": 900,
    },
    # === CASE 31: limited_casco_100 == casco_100 (tie at product boundary) ===
    {
        "ntpl": 400,
        "limited_casco_100": 1200,
        "limited_casco_200": 1020,
        "limited_casco_500": 960,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 32: One single violation — limited_casco_200 > limited_casco_100 ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 910,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 33: One single violation — casco_500 > casco_200 ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 1050,
    },
    # === CASE 34: ntpl > everything ===
    {
        "ntpl": 5000,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 35: Everything less than ntpl except casco_100 ===
    {
        "ntpl": 1100,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 36: Deductible percentages exactly at guide values (valid) ===
    {
        "ntpl": 500,
        "limited_casco_100": 1000,
        "limited_casco_200": 850,
        "limited_casco_500": 800,
        "casco_100": 1500,
        "casco_200": 1275,
        "casco_500": 1200,
    },
    # === CASE 37: Deductible 200 priced same as 100 (no discount applied) ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 900,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1200,
        "casco_500": 960,
    },
    # === CASE 38: Deductible 500 priced same as 100 (no discount applied) ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 900,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 1200,
    },
    # === CASE 39: Cross-product: limited_casco_200 > casco_500 ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 980,
        "limited_casco_500": 700,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 40: All casco prices below all limited_casco prices ===
    {
        "ntpl": 200,
        "limited_casco_100": 1000,
        "limited_casco_200": 900,
        "limited_casco_500": 800,
        "casco_100": 700,
        "casco_200": 600,
        "casco_500": 500,
    },
    # === CASE 41: Prices are large round numbers, all valid ===
    {
        "ntpl": 1000,
        "limited_casco_100": 2000,
        "limited_casco_200": 1700,
        "limited_casco_500": 1600,
        "casco_100": 3000,
        "casco_200": 2550,
        "casco_500": 2400,
    },
    # === CASE 42: Prices with decimal precision, valid ===
    {
        "ntpl": 327.50,
        "limited_casco_100": 612.75,
        "limited_casco_200": 520.84,
        "limited_casco_500": 490.20,
        "casco_100": 899.99,
        "casco_200": 765.00,
        "casco_500": 720.00,
    },
    # === CASE 43: ntpl just barely valid (ntpl < limited_casco_500 by 1) ===
    {
        "ntpl": 719,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 44: Swap limited_casco_100 and casco_500 ===
    {
        "ntpl": 400,
        "limited_casco_100": 960,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 900,
    },
    # === CASE 45: Extremely wide spread ===
    {
        "ntpl": 10,
        "limited_casco_100": 5000,
        "limited_casco_200": 4250,
        "limited_casco_500": 4000,
        "casco_100": 50000,
        "casco_200": 42500,
        "casco_500": 40000,
    },
    # === CASE 46: Narrow spread, multiple violations ===
    {
        "ntpl": 100,
        "limited_casco_100": 102,
        "limited_casco_200": 103,
        "limited_casco_500": 104,
        "casco_100": 101,
        "casco_200": 105,
        "casco_500": 106,
    },
    # === CASE 47: Only hierarchy violation: ntpl > limited_casco_500 but < limited_casco_200 ===
    {
        "ntpl": 750,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
    # === CASE 48: casco_100 == limited_casco_200 (cross-product edge) ===
    {
        "ntpl": 400,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 765,
        "casco_200": 700,
        "casco_500": 650,
    },
    # === CASE 49: All valid, prices at market averages exactly ===
    {
        "ntpl": 500,
        "limited_casco_100": 900,
        "limited_casco_200": 765,
        "limited_casco_500": 720,
        "casco_100": 1200,
        "casco_200": 1020,
        "casco_500": 960,
    },
]
