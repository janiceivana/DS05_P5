

import pandas as pd
import datetime as dt

calendar = pd.read_csv(r"C:\Users\Nguyen\Desktop\calendar.csv")
price = pd.read_csv(r"C:\Users\Nguyen\Desktop\sell_price.csv")
dept = pd.read_csv(r"C:\Users\Nguyen\Desktop\sales_train_evaluation.csv")

dates = calendar[["date", "wm_yr_wk"]]


dept = dept[["item_id", "dept_id"]]


joint = dates.merge(price, how="left", on = "wm_yr_wk")

joint['date'] = pd.to_datetime(joint['date'], format="%Y-%m-%d")


joint.insert(0, 'yr-wk', joint['date'].dt.strftime("%Y-%W"))





joint.groupby(["item_id", "date"])

print(joint.head(10))


joint = joint.merge(dept, how="left", on = "item_id")



r'''
res = joint[["store_id", "item_id", "dept_id", "sell_price", "date"]]


res = res.groupby(["store_id", "item_id"])

res.to_csv(r"C:\Users\Nguyen\Desktop", index = False)
'''