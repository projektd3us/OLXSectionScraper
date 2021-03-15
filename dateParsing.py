from datetime import *


def dateConvert(undate):
    """
    Converts the olx post date/time to a datetime variable, by finding its form (out of 3)

    :param str undate: unparsed date

    :rtype: datetime
    :return: datetime from parsing olx date

    :raise parse error, parsed an ad or method obsolete
    """
    try:
        newDate = ""
        if undate.find("Azi") != -1:  # case one AZI with time
            newDate = str(date.today()) + ' ' + undate.split()[1]
        else:
            if undate.find("Ieri") != -1:  # case two IERI with time
                newDate = str((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")) + ' ' + undate.split()[1]
            else:  # case three date with assumed time
                switcher = dict(ian="01", feb="02", mar="03", apr="04", mai="05", iun="06", iul="07", aug="08",
                                sep="09", oct="10", noi="11", dec="12")  # possible months, only used in case 3
                for month in switcher:  # iterate switcher for finding post month
                    if undate.find(month) != -1:
                        newDate = str(date(2020, int(switcher[month]), int(undate.split()[0]))) + ' ' + "12:00"
        return datetime.strptime(newDate, "%Y-%m-%d %H:%M")
    except:
        print('Error')  # poor but working err handling - might mean OLX changed website generating


def howLongAgo(datePast):  # how long ago from now was a date
    """
    Returns how long ago from now was a given date.

    :param datetime datePast: past date

    :rtype: datetime
    :return: time difference
    """
    return datetime.now() - datePast


def howLongSec(datePast):  # how long ago - in seconds
    """
    Returns how long ago from now was a given date, but in seconds.

    :param datetime datePast: past date

    :rtype: datetime
    :return: time difference in seconds
    """
    return (datetime.now() - datePast).total_seconds()
