from datetime import datetime

def calc_wrkHrs(arrive, lunch_out, lunch_in, leave):
    """calculate work and reduced work week hrs based on
       8 hour work day
       all input formats are %H:%M
    :param arrive: time arrived at work
    :param lunch_out: time out for lunch
    :param lunch_in: time in from lunch
    :param leave: time leave from work
    :return: wrk_hrs: decimal hours of worked hours
    :return: rww_hrs: decimal hours of reduced work week
    """

    l_hrFormat = "%H:%M"
    t_arr = datetime.strptime(arrive, l_hrFormat)
    t_olun = datetime.strptime(lunch_out, l_hrFormat)
    t_ilun = datetime.strptime(lunch_in, l_hrFormat)
    t_leav = datetime.strptime(leave, l_hrFormat)
    l_totHrs = ((t_olun - t_arr) + (t_leav - t_ilun))

    wrk_hrs = l_totHrs.seconds//3600 + l_totHrs.seconds//60%60/60
    wrk_hrs = round(wrk_hrs, 2)
    rww_hrs = round(8.0 - wrk_hrs, 2)

    return wrk_hrs, rww_hrs

