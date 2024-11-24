import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))

most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(most_views)

#create a new column 'is_click' - note that it requires '~' to reverse the result, since isnull will return True
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head(10))

# 'clicks_by_source' - percent of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
#print(clicks_by_source)

# Pivot 'clicks_by_source' to become 'clicks_pivot'
clicks_pivot = clicks_by_source.pivot(index = 'utm_source', columns = 'is_click', values = 'user_id')
#print(clicks_pivot)

# new column in 'clicks_pivot' - percent_clicked
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)

experimental_group_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(experimental_group_count)

experimental_group_is_click_count = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
#print(experimental_group_is_click_count)

#pivot experimental_group_is_click_count
experimental_group_is_click_pivot = experimental_group_is_click_count.pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
)
#print(experimental_group_is_click_pivot)

#create dataframes that separates A group and B group
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_click_day = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
#print(a_click_day)

a_click_day_pivot = a_click_day.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
)
#print(a_click_day_pivot)
a_click_day_pivot['percent_clicked'] = a_click_day_pivot[True] / (a_click_day_pivot[True] + a_click_day_pivot[False])
print(a_click_day_pivot)
#-----------------------
b_click_day = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
#print(b_click_day)

b_click_day_pivot = b_click_day.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
)
#print(b_click_day_pivot)
b_click_day_pivot['percent_clicked'] = b_click_day_pivot[True] / (b_click_day_pivot[True] + b_click_day_pivot[False])
print(b_click_day_pivot)