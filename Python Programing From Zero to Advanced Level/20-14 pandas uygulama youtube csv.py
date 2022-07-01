import pandas as pd

data=pd.read_csv("csv files/youtube-UK.csv")
df=pd.DataFrame(data)

# print(data.head())
# print(data.tail(20))
# print(len(data.columns))
# print(df.columns)
# df=df.drop(["thumbnail_link",'comments_disabled', 'ratings_disabled',
#        'video_error_or_removed'],axis=1)
# print(len(df.columns))
# print(df["likes"].mean(),"\n",df["dislikes"].mean())
# print(df[["likes","dislikes"]].head(50))
# print(df[df["views"]==df["views"].max()][["title","views"])
# print(df[df["views"]==df["views"].min()][["title","views"]])
# print(df[["title","views"]].sort_values("views",ascending=False).drop_duplicates(subset=["title"]).head(10))
# print(df.columns)
# print(df.groupby("category_id")["likes"].mean())
# print(df.groupby("category_id").nunique()["video_id"].sum())
# print(df["category_id"].value_counts().sum())
# titlelenlst=[]
# def titlelen():
#     for title in df["title"]:
#         titlelenlst.append(len(title))
# df["titlelenght"]=df["title"].apply(len)
# print(df["titlelenght"])
# titlelen()
# df["titlelenght"]=pd.DataFrame(titlelenlst)
# print(df.columns)
# print(df["titlelenght"])
# for i in df["tags"]:
#     i.split("|")
#     print(len(i.split("|"))) #["tags"].value_counts("tags")

# df["taglen"]=[len(i) for i in [i.split("|") for i in df["tags"]]]
# #or
# df["taglen"]=df["tags"].apply(lambda x: len(x.split("|")))
# print(df["taglen"])
# df["likesviewsratio"]=df["likes"]/df["views"]
# print(df.groupby("title").head(10).sort_values("likesviewsratio",ascending=False)[["title","views","likes","likesviewsratio"]])
# df1=df.sort_values("views",ascending=False)
# # print(df1["views"])
# df1=df1[0:20]
# # print(df1["views"])
# df1["likesviewsratio"]=df1["likes"]/df1["views"]
# print(df1.sort_values("likesviewsratio",ascending=False)[["views","likes","likesviewsratio"]])