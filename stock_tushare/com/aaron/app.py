import tushare as ts


token = '19c3a898e510a566d1bed1df579407af9bdf9bf0c3255f1eac99c05b';

if __name__ == "__main__":
    print(ts.__version__)
    ts.set_token(token)
    pro = ts.pro_api()

    # df = pro.trade_cal(exchange='', start_date='20200701', end_date='20200723',
    #                    fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
    df = pro.query('daily', ts_code='600522.SH', start_date='20200701', end_date='20200723')
    print(df)
