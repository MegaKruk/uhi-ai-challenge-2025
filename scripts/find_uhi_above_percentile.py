#!/usr/bin/env python

import pandas as pd


def main():
    # 1. Read the CSV (adjust path if needed)
    csv_path = r"..\data\Training_data_uhi_index 2025-02-04.csv"
    df = pd.read_csv(csv_path)

    # 2. Compute the 90th percentile of UHI Index
    p90 = df["UHI Index"].quantile(0.90)
    print(f"90th percentile of UHI Index is: {p90:.4f}")

    # 3. Filter rows where UHI Index >= 90th percentile
    df_high = df[df["UHI Index"] >= p90]
    print(f"Number of rows with UHI Index >= {p90:.4f}: {len(df_high)}\n")

    # 4. (Optional) Print or examine the filtered rows
    print("Top 5 rows where UHI is in 90th percentile or higher:")
    print(df_high.head())

    # 5. (Optional) Save to a new CSV
    output_path = "UHI_90th_percentile.csv"
    df_high.to_csv(output_path, index=False)
    print(f"\nFiltered rows saved to: {output_path}")


if __name__ == "__main__":
    main()
