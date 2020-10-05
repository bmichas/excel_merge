import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def variables():
    global buy, sell, connect_file
    buy = 'buy.xlsx'
    sell = 'sell.xlsx'
    connect_file = 'main_data.xlsx'


def df_generator(file):
    excel = pd.ExcelFile(file)
    df = excel.parse('Arkusz1')
    df = df.loc[2:]
    df = df.reset_index(drop=True)
    header_row = 0
    df.columns = df.iloc[header_row]
    df = df.drop(header_row)

    return df


def file_merge(main_file, first, second):
    first_connect_file = pd.merge(first, main_file)
    merge_file = pd.merge(first_connect_file, second)
    merge_file.to_excel("merge.xlsx")
    return merge_file


def main():
    variables()
    # generowanie DataFrame
    df_buy = df_generator(buy)
    df_sell = df_generator(sell)
    df_connect_file = df_generator(connect_file)
    # print(df_buy)
    # print(df_sell)
    # print(df_connect_file)
    df_merge_file = file_merge(df_connect_file, df_buy, df_sell)
    print(df_merge_file)


if __name__ == "__main__":
    main()
