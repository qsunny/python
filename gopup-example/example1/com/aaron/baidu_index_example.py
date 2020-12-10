
import pprint
import gopup as gp

"""百度指数示例"""


def weibo_index(word):
    df_index = gp.weibo_index(word=word, time_type="3month")
    print(df_index)


def baidu_search_index():
    cookie = "BIDUPSID=76F08CC764C192F0FE44661C9F9DC82B; PSTM=1593486980; " \
             "BAIDUID=1BBB90B478E9BC12B46561D8BFF6D0E0:FG=1;" \
             " BDUSS=Es5ODlXMG03RHJNZVJXbFU5TjV1OWdPYTdMQ1dZNmc4VFVqRmhyV3ZHZHJtQ0pmSVFBQUFB" \
             "JCQAAAAAAAAAAAEAAAAjnoArcXN1bm55MjAwNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
             "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGsL-15rC~teV;" \
             " MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0;" \
             " BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; H_PS_PSSID=1455_33222_33059_33261" \
             "_31660_32972_33099_33101_32846_33211_33199_33145_33149_22159; " \
             "BA_HECTOR=2kal8h848hah01a1001ft3kpb0q; BCLID=7217368344433439330;" \
             " BDSFRCVID=F-8OJexroG3SQbJrFoCzhMk5RcpWxY5TDYLEaTkizK" \
             "rm7S8VJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5;" \
             " H_BDCLCKID_SF=tR30WJbHMTrDHJTg5DTjhPrMQmFOWMT-MTryKKORLRokqlQvLn6sXtn00xb" \
             "jLbvkJGnRhlRNKxbOjtcoK4Fb0TkZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot" \
             "5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-D_CjTDb3e; " \
             "bdindexid=aj2sip46egbo1p89rbakuf59g6; Hm_lvt_d101ea4d2a5c67dab98251f0b5" \
             "de24dc=1607586624,1607586626; __yjsv5_shitong=1.0_7_ed7d4ee6e1971be19fd69d3eec" \
             "5e2d2d356f_300_1607586937496_113.91.62.205_b1956d4c;" \
             " Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1607587106; " \
             "RT='z=1&dm=baidu.com&si=7qksgg31mpk&ss=kiijkh5g&sl=g" \
             "&tt=dj4&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf'"
    index_df = gp.baidu_search_index(word="口罩", start_date='2020-12-01', end_date='2020-12-10', cookie=cookie)
    print(index_df)


if __name__ == "__main__":
    print("==========")
    # weibo_index("口罩")
    # baidu_search_index()
    df = gp.realtime_tv()
    print(df)

