import pandas as pd

data=pd.read_csv("csv files/nba.csv")
df=pd.DataFrame(data)
# print(data.columns)
# print(data.head(10))
# print(data.info)
# print(f'Total Salary mean: $ {data["Salary"].mean():,}')
# print(data["Salary"].max())
# print(df[["Name","Team"]][df["Salary"]==df["Salary"].max()])
# print(df[(df["Age"]>=20) & (df["Age"]<25)][["Name","Team","Age"]].sort_values('Age',ascending=False))
# print(df["Team"][df["Name"]=="Jordan Mickey"])
#print(f' {list(df.groupby("Team").groups.keys())[0]} $ {df["Salary"][df["Team"]==(list(df.groupby("Team").groups.keys())[0])].mean():,.2f}')
# print((df.groupby("Team").mean()["Salary"]))
# print(df.groupby("Team").count())
# print(len(df.groupby("Team")))
# print(df.groupby("Team").nunique())
# print(df["Team"].value_counts())
df=df.dropna(how="any")
# print(df["Name"][df["Name"].str.contains("and")])
def str_find(name):
    if "and" in name.lower():
        return True
    return False
print(df[df["Name"].apply(str_find)])

