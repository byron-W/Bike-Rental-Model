import pandas as pd


file_path = '../data/bike.xlsx'
df = pd.read_excel(file_path, sheet_name='SeoulBikeData')

def create_data_dictionary(data):
    rows = []

    for idx, column in enumerate(data.columns):
        col = data[column]
        col_type = str(col.dtype)
        unique_count = col.nunique()
        example = col.dropna().iloc[0] if not col.dropna().empty else None

        if pd.api.types.is_numeric_dtype(col):
            var_type = "Numerical"
        elif pd.api.types.is_datetime64_any_dtype(col):
            var_type = "Datetime"
        else:
            var_type = "Categorical"

        rows.append({
            "Index": idx,
            "Feature Name": column,
            "Description": "...",  # will add descriptions manually
            "Data Type": col_type,
            "Categorical/Numerical": var_type,
            "Missing Values": col.isnull().sum(),
            "# Unique Values": unique_count,
            "Example Value": example
        })

    return pd.DataFrame(rows)

data_dict_df = create_data_dictionary(df)


output_path = '../data/data_dict.xlsx'
data_dict_df.to_csv(output_path, index=False)


