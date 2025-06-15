import pandas as pd
import matplotlib.pyplot as plt


file_path = r"C:\Users\amand\Desktop\VU magistras\Big data\Individual task\Iowa_Liquor_Sales.csv"
df = pd.read_csv(file_path, low_memory=False)


df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

df['State Bottle Retail'] = df['State Bottle Retail'].replace(r'[\$,]', '', regex=True).astype(float)
df['Sale (Dollars)'] = df['Sale (Dollars)'].replace(r'[\$,]', '', regex=True).astype(float)

top_products = df.groupby('Item Number')['Volume Sold (Liters)'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Total Volume Sold:")
print(top_products)

df['Month'] = df['Date'].dt.to_period('M')
monthly_volume = df.groupby('Month')['Volume Sold (Liters)'].sum()
monthly_volume.index = monthly_volume.index.to_timestamp()

plt.figure(figsize=(12, 6))
monthly_volume.plot(kind='line', marker='o')
plt.title("Monthly Liquor Sales Volume in Iowa")
plt.xlabel("Month")
plt.ylabel("Liters Sold")
plt.grid(True)
plt.tight_layout()
plt.show()

bottle_sizes = df.groupby('Bottle Volume (ml)')['Volume Sold (Liters)'].sum().sort_values(ascending=False)
print("\nTop 10 Bottle Sizes by Total Volume Sold:")
print(bottle_sizes.head(10))

bottle_sizes.head(10).plot(kind='bar', figsize=(10, 5), title='Top Bottle Sizes by Volume Sold')
plt.xlabel("Bottle Volume (ml)")
plt.ylabel("Liters Sold")
plt.tight_layout()
plt.show()

top_stores = df.groupby('Store Name')['Volume Sold (Liters)'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Stores by Volume Sold:")
print(top_stores)

top_stores.plot(kind='barh', figsize=(10, 6), title='Top 10 Stores by Volume Sold')
plt.xlabel("Liters Sold")
plt.tight_layout()
plt.show()

avg_price_vs_volume = df.groupby('Item Number').agg({
    'State Bottle Retail': 'mean',
    'Volume Sold (Liters)': 'sum'
})

print("\nSample of Price vs. Volume Data:")
print(avg_price_vs_volume.head())

avg_price_vs_volume.plot(
    kind='scatter',
    x='State Bottle Retail',
    y='Volume Sold (Liters)',
    alpha=0.3,
    figsize=(10, 6),
    title="Price vs. Total Volume Sold"
)
plt.xlabel("Average Price (USD)")
plt.ylabel("Total Liters Sold")
plt.grid(True)
plt.tight_layout()
plt.show()

if 'Category Name' in df.columns:
    category_volume = df.groupby('Category Name')['Volume Sold (Liters)'].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Categories by Volume Sold:")
    print(category_volume)

    category_volume.plot(kind='bar', figsize=(10, 5), title='Top 10 Categories by Volume Sold')
    plt.ylabel("Liters Sold")
    plt.xlabel("Category Name")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("\nCategory Name column missing — skipping category analysis.")

monthly_volume.plot(kind='line', marker='o')
plt.title("Monthly Liquor Sales Volume in Iowa")
plt.xlabel("Month")
plt.ylabel("Liters Sold")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_volume.png")  # ← Save figure
plt.show()
