#
# import pandas as pd
#
# data = {
#     "City": [
#         "Tehran",
#         "Mashhad",
#         "Isfahan",
#         "Karaj",
#         "Shiraz",
#         "Tabriz",
#         "Qom",
#         "Ahvaz",
#         "Kermanshah",
#         "Urmia"
#     ],
#     "Latitude": [
#         35.694, 36.298, 32.652, 35.833, 29.610,
#         38.080, 34.640, 31.319, 34.314, 37.553
#     ],
#     #طول جغرافیایی موقعیت رو نسبت به نصف‌النهار مبدأ مشخص می‌کنه. مقادیر این مثال برای ایران مثبت هستن.
#     "Longitude": [
#         51.422, 59.606, 51.675, 50.992, 52.531,
#         46.292, 50.876, 48.684, 47.065, 45.076
#     ],
#     "Population": [
#         8693706, 3001184, 1961260, 1592492, 1565572,
#         1558693, 1201158, 1184788, 946651, 736224
#     ]
# }
# #DataFrame = df ----> مخفف
# df = pd.DataFrame(data)
# df.to_csv("iran_cities.csv", index=False, encoding="utf-8-sig")
# print(df)
# print("CSV file created successfully!")

import pandas as pd

data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    "City": [
        "Tehran",
        "Mashhad",
        "Isfahan",
        "Shiraz",
        "Tabriz",
        "Karaj",
        "Qom",
        "Ahvaz",
        "Kermanshah",
        "Urmia"
    ],

    "Latitude": [
        35.694, 36.298, 32.652, 29.610, 38.080,
        35.833, 34.640, 31.319, 34.314, 37.553
    ],
 #طول جغرافیایی موقعیت رو نسبت به نصف‌النهار مبدأ مشخص می‌کنه. مقادیر این مثال برای ایران مثبت هستن.
    "Longitude": [
        51.422, 59.606, 51.675, 52.531, 46.292,
        50.992, 50.876, 48.684, 47.065, 45.076
    ],

    "Population_2026": [
        9882527,
        3532584,
        2196430,
        1798531,
        1694340,
        1549130,
        1502321,
        1344918,
        1170300,
        895630
    ]
}

df = pd.DataFrame(data)

 # index=False مشخص می‌کند شماره ردیف‌های pandas به‌عنوان ستون اضافی ذخیره نشوند.
 # encoding="utf-8-sig" کمک می‌کند متن فارسی هنگام باز کردن فایل CSV در Excel درست نمایش داده شود.

df.to_csv(
    "iran_cities.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df)
print("CSV file created successfully!")

