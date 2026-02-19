import pandas as pd
import matplotlib.pyplot as plt
import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))                   # File Base directory
data_path = os.path.join(base_dir, "..", "data") # Path to the output Parquet file (Silver Layer)
chart_path = os.path.join(base_dir, "..", "chart_images") # Path to the output Parquet file (Silver Layer)
db_path = os.path.join(base_dir, "..", "data", "brewery_case.db")

def load_gold_layer_data(db_path):
    conn = sqlite3.connect(db_path)
    try:
        df_country_state_type = pd.read_sql_query(
            "SELECT * FROM aggr_brewery_by_country_state_brewery_type ORDER BY n_of_breweries DESC",
            conn
        )
        df_country_type = pd.read_sql_query(
            "SELECT * FROM aggr_brewery_by_country_brewery_type ORDER BY n_of_breweries DESC",
            conn
        )
        
        return df_country_state_type, df_country_type
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None
    finally:
        conn.close()

def plot_breweries_by_country_type(df_country_type, top_n=15):
    """Plot top N breweries by country and brewery type."""
    df_top = df_country_type.head(top_n)
    
    plt.figure(figsize=(12, 6))
    plt.barh(
        [f"{row['country']} - {row['brewery_type']}" for _, row in df_top.iterrows()],
        df_top['n_of_breweries'],
        color='steelblue'
    )
    plt.xlabel('Number of Breweries', fontsize=12)
    plt.ylabel('Country - Brewery Type', fontsize=12)
    plt.title(f'Top {top_n} Breweries by Country and Type', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(chart_path, 'top_breweries_by_country_type.png'), dpi=300)
    print(f"Saved: top_breweries_by_country_type.png")
    plt.show()

def plot_breweries_by_country(df_country_state_type, top_n=15):
    """Plot top N countries by total brewery count."""
    df_by_country = df_country_state_type.groupby('country')['n_of_breweries'].sum().reset_index()
    df_by_country = df_by_country.sort_values('n_of_breweries', ascending=False).head(top_n)
    
    plt.figure(figsize=(12, 6))
    plt.bar(df_by_country['country'], df_by_country['n_of_breweries'], color='coral')
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Number of Breweries', fontsize=12)
    plt.title(f'Top {top_n} Countries by Total Brewery Count', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(chart_path, 'top_countries_by_brewery_count.png'), dpi=300)
    print(f"Saved: top_countries_by_brewery_count.png")
    plt.show()

def plot_brewery_types_distribution(df_country_state_type):
    """Plot distribution of brewery types across all countries."""
    df_by_type = df_country_state_type.groupby('brewery_type')['n_of_breweries'].sum().reset_index()
    df_by_type = df_by_type.sort_values('n_of_breweries', ascending=False)
    
    plt.figure(figsize=(10, 6))
    plt.pie(
        df_by_type['n_of_breweries'],
        labels=df_by_type['brewery_type'],
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title('Distribution of Breweries by Type', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(chart_path, 'brewery_types_distribution.png'), dpi=300)
    print(f"Saved: brewery_types_distribution.png")
    plt.show()

def plot_state_province_distribution(df_country_state_type, country_filter=None, top_n=10):
    """Plot state/province distribution for a specific country."""
    if country_filter:
        df_filtered = df_country_state_type[df_country_state_type['country'] == country_filter]
    else:
        df_filtered = df_country_state_type
    df_by_state = df_filtered.groupby('state_province')['n_of_breweries'].sum().reset_index()
    df_by_state = df_by_state.sort_values('n_of_breweries', ascending=False).head(top_n)
    
    title = f'Top {top_n} States/Provinces by Brewery Count'
    if country_filter:
        title += f' ({country_filter})'
    
    plt.figure(figsize=(12, 6))
    plt.barh(df_by_state['state_province'], df_by_state['n_of_breweries'], color='mediumseagreen')
    plt.xlabel('Number of Breweries', fontsize=12)
    plt.ylabel('State/Province', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    filename = f'top_states_by_brewery_count.png'
    if country_filter:
        filename = f'top_states_{country_filter}_by_brewery_count.png'
    plt.savefig(os.path.join(chart_path, filename), dpi=300)
    print(f"Saved: {filename}")
    plt.show()

if __name__ == "__main__":
    df_country_state_type, df_country_type = load_gold_layer_data(db_path)
    if df_country_state_type is not None and df_country_type is not None:
        print(f"\nCountry-State-Type records: {len(df_country_state_type)}")
        print(f"Country-Type records: {len(df_country_type)}")
        plot_breweries_by_country_type(df_country_type, top_n=15)
        plot_breweries_by_country(df_country_state_type, top_n=15)
        plot_brewery_types_distribution(df_country_state_type)
        plot_state_province_distribution(df_country_state_type, top_n=10)
        plot_state_province_distribution(df_country_state_type, country_filter="United States", top_n=15)
    else:
        print("Failed to load data from database.")