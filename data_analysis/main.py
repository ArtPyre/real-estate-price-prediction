import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

path = os.path.join(os.path.abspath('data_acquisition'), 'all_infos_processed.csv')
df = pd.read_csv(path)

#Create a bar graph that displays all the rows and columns from a dataframe
def get_rows_columns_graph(df) :
    names = ['Rows', 'Columns']
    values = df.shape

    plt.figure(figsize=(12, 3))
    plt.bar(names, values)
    plt.title('Number of rows and columns', fontsize=20)
    plt.xticks(fontsize=10)
    plt.savefig("./data_analysis/graphs/Size_graph.png")
    plt.show()

#Create a bar graph that shows all the properties in sale from a region in Belgium
def get_region_properties(df):
    mask_wallonia = (df['Locality'] >= 1300) & (df['Locality'] < 1500) | (df['Locality'] >= 4000) & (df['Locality'] < 8000)
    df_wallonia = df[mask_wallonia]
    mask_flandre = (df['Locality'] >= 1500) & (df['Locality'] < 4000) | (df['Locality'] >= 8000) & (df['Locality'] < 10000)
    df_flandre = df[mask_flandre]
    mask_brussels = (df['Locality'] <  1300)
    df_brussels = df[mask_brussels]

    names = ['wallonia', 'Flandre', 'Brussels', 'all']
    values = [df_wallonia.shape[0], df_flandre.shape[0], df_brussels.shape[0], df.shape[0]]

    plt.figure(figsize=(15, 8))
    plt.bar(names, values)
    plt.title('Propertie sales by region', fontsize=20)
    plt.xticks(fontsize=10)
    plt.xlabel('Region', fontsize=15)
    plt.ylabel('Number', fontsize=15)
    plt.savefig("./data_analysis/graphs/Region_graph.png")
    plt.show()

#Create a bar graph that shows the mean of price by subtypes of properties
def get_price_by_subtype(df) :
    df = df[~df["Subtype_of_property"].isin(["HOUSE_GROUP", "APARTMENT_GROUP"])]
    datas = df.groupby('Subtype_of_property')['Price'].mean().sort_values()
    names = datas.axes[0]
    values = datas.array

    plt.figure(figsize=(20, 10))
    plt.barh(names, values)
    plt.title('Prices by subtypes', fontsize=20)
    plt.xlabel('Subtypes', fontsize=15)
    plt.ylabel('Prices', fontsize=15)
    plt.xticks(fontsize=10)
    plt.savefig("./data_analysis/graphs/Subtype_graph.png")
    plt.show()

#Create a bar graph that displays the mean price by kitchen types
def get_price_by_kitchen_type (df) :
    datas_grouped = df.groupby(['Fully_equipped_kitchen'])
    datas_count = datas_grouped['Fully_equipped_kitchen'].value_counts()
    datas = datas_grouped['Price'].mean().sort_values()
    names = datas.index.tolist()
    values = datas.array
    plt.figure(figsize=(18, 5))
    plt.bar(names, values, color='red')
    plt.title('Mean price by kitchen types', fontsize=20)
    plt.xlabel('Types of kitchen', fontsize=15)
    plt.ylabel('Prices(€)', fontsize=15)
    plt.grid(axis='y')
    plt.xticks(fontsize=9)
    for i,v in enumerate(datas_count.array) :
        index = names.index(datas_count.index.tolist()[i][1])
        plt.annotate(v, (index,0), ha='center',xytext=(0,10), textcoords="offset points", fontsize=10)
    plt.savefig("./data_analysis/graphs/Kitchen_graph.png", bbox_inches="tight")
    plt.show()

#Create a dot graph that shows all the prices and the terrace surface from houses and appartements
def get_price_by_terrace_area(df):

    df = df[~df["Subtype_of_property"].isin(["HOUSE_GROUP", "APARTMENT_GROUP"])]
    sns.set_theme(style="darkgrid")
    df["Types of property"] = df["Type_of_property"].map({"APARTMENT":"Apartments", "HOUSE":"Houses"})
    sns.scatterplot(df, x="Price", y="Terrace_Area", hue="Types of property")
    plt.title('Terrace area and price correlation', fontsize=20)
    plt.xlabel('Prices(€)', fontsize=15)
    plt.ylabel('Terrace areas(m²)', fontsize=15)
    plt.xlim(0,1001000)
    plt.ylim(0,105)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
    plt.gcf().set_size_inches(15, 8)
    plt.savefig("./data_analysis/graphs/Terrace_graph.png", bbox_inches="tight")
    plt.show()

def get_multi_graph (df) :
    int_array_df = ["Price", "Locality", "Living_Area", "Number_of_facades"]
    sns.pairplot(df, x_vars=int_array_df, y_vars=int_array_df,)
    plt.savefig("./data_analysis/graphs/Multi_graph.png", bbox_inches="tight")
    plt.show()

get_price_by_kitchen_type(df)
get_price_by_terrace_area(df)
get_price_by_subtype(df)
get_region_properties(df)
get_rows_columns_graph(df)
get_multi_graph(df)
