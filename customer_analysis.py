import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sales_path = os.path.join(base_dir, "sales_data.csv")
    customers_path = os.path.join(base_dir, "customer_data.csv")

    try:
        sales = pd.read_csv(sales_path)
        customers = pd.read_csv(customers_path)
    except FileNotFoundError as e:
        print("Error: data file not found.")
        print(e)
        raise

    return sales, customers


def main():
    sales, customers = load_data()

    print("Sales dataset preview:")
    print(sales.head(), "\n")

    print("Customers dataset preview:")
    print(customers.head(), "\n")

    print("Missing values in sales data:")
    print(sales.isnull().sum(), "\n")

    sales = sales.dropna().copy()
    sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])
    sales["Total_Sales"] = sales["Quantity"] * sales["Price"]

    top_customers = sales.groupby("Customer_ID")["Total_Sales"].sum()
    print("Top Customers:")
    print(top_customers.sort_values(ascending=False).head(), "\n")

    sales["Month"] = sales["Order_Date"].dt.month
    monthly_sales = sales.groupby("Month")["Total_Sales"].sum()
    print("Monthly Sales:")
    print(monthly_sales, "\n")

    pivot = pd.pivot_table(
        sales,
        values="Total_Sales",
        index="Region",
        columns="Category",
        aggfunc="sum",
    )
    print("Pivot Table:")
    print(pivot, "\n")

    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette="Blues_d")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

    print("Total Revenue:", sales["Total_Sales"].sum())


if __name__ == "__main__":
    main()
