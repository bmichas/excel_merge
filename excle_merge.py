import pandas as pd


def df_generator(file):
    excel = pd.ExcelFile(file)
    df = excel.parse('Arkusz1')
    df = df.loc[2:]
    df = df.reset_index(drop=True)
    header_row = 0
    df.columns = df.iloc[header_row]
    df = df.drop(header_row)

    return df


def variables():
    global buy, sell, merge_file
    buy = 'buy.xlsx'
    sell = 'sell.xlsx'
    merge_file = 'main_data.xlsx'


def main():
    variables()
    # generowanie DataFrame
    df_buy = df_generator(buy)
    df_sell = df_generator(sell)
    df_merge_file = df_generator(merge_file)
    print(df_buy)
    print(df_sell)
    print(df_merge_file)


if __name__ == "__main__":
    main()
