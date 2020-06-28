import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(10))

print(ad_clicks.groupby("utm_source").user_id.count().reset_index())

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(10))

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()

print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns = "is_click", index = "utm_source", values = "user_id")

clicks_pivot["percent_clicked"] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot)

# Analysing an A/B test

print(ad_clicks.groupby("experimental_group").user_id.count().reset_index())

ab_clicks_pivot = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index().pivot(columns = "is_click", index = "experimental_group", values = "user_id")

ab_clicks_pivot["percent_clicked"] = ab_clicks_pivot[True]/(ab_clicks_pivot[True]+ab_clicks_pivot[False])
print(ab_clicks_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]

b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

def row_percentages(a_clicks):
  a_clicks_pivot = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index().pivot(columns = "is_click", index = "day", values = "user_id")

  a_clicks_pivot["percent_clicked"] = a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False])
  print(a_clicks_pivot)
  return a_clicks_pivot

row_percentages(a_clicks)
row_percentages(b_clicks)
