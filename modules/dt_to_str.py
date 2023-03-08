import pytz
import datetime

TPTZ = pytz.timezone('Asia/Taipei')


def date_to_display_str(date_time):
    """
    date_to_display_str [
        根據傳入Datetime 輸出%Y-%m-%d 格式字串]

    Args:
        date_time (datetime): [日期]

    Returns:
        [str]: [輸出字串]
    """
    return date_time.strftime("%Y-%m-%d")
