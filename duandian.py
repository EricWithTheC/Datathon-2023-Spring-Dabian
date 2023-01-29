import pandas as pd
df = pd.read_csv(r'C:\Users\33668\Desktop\CollegeCourses\Other Stuffs\datathon\Datathon-2023-Spring-Dabian\stateRemain.csv')
all_df = []
tmp_df = pd.DataFrame(df.iloc[0, :]).transpose()
start = df.iloc[0, :].State

for i in range(1, len(df)):
    # try:
    count = 0
    while (df.iloc[i, :].State == start):
        count += 1
        tmp_dict = pd.DataFrame(df.iloc[i, :].to_dict()).transpose()
        pd.concat([tmp_df, tmp_dict], axis=0)
        tmp_df.append(tmp_dict, ignore_index=True)
        i += 1

    print(count)
    all_df.append(tmp_df)
    tmp_df = pd.DataFrame(df.iloc[i, :]).transpose()
    start = df.iloc[i, :].State

    # except:
    #     print(i)
    

