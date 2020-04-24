TEXT = "text"
FULLTEXT = "full_text"
EXTENDEDTWEET = "extended_tweet"
RETWEETEDSTATUS = "retweeted_status"

def getTweetText(jsonData):
    text = ""
    if TEXT in jsonData: 
        text = jsonData[TEXT]
    if EXTENDEDTWEET in jsonData and \
       FULLTEXT in jsonData[EXTENDEDTWEET]:
        text = jsonData[EXTENDEDTWEET][FULLTEXT]
    if RETWEETEDSTATUS in jsonData and \
       EXTENDEDTWEET in jsonData[RETWEETEDSTATUS] and \
       FULLTEXT in jsonData[RETWEETEDSTATUS][EXTENDEDTWEET]:
        text = jsonData[RETWEETEDSTATUS][EXTENDEDTWEET][FULLTEXT]
    return(text)

from datetime import datetime, timedelta

DATEFORMATTWITTER = "%a %b %d %H:%M:%S %z %Y"
DATEFORMATGTD = "%Y%m%d"
SUMMERTIMEDATE = datetime.strptime("Sun Mar 29 02:00:00 +0000 2020",DATEFORMATTWITTER)
WINTERTIMEDATE = datetime.strptime("Sun Oct 25 03:00:00 +0000 2020",DATEFORMATTWITTER)

def getTweetDate(jsonData,dateFormat=DATEFORMATGTD):
    dateString = jsonData["created_at"]
    dateData = datetime.strptime(dateString,DATEFORMATTWITTER)+timedelta(hours=1)
    if dateData >= SUMMERTIMEDATE:
        if dateData >= WINTERTIMEDATE: sys.exit("cannot happen")
        dateData += timedelta(hours=1)
    return(dateData.strftime(dateFormat))

DATEFORMATSATD = "%Y%m%d"

def stringArrayToDates(stringList,dateFormat=DATEFORMATSATD):
    return([datetime.strptime(str(date),dateFormat) for date in stringList])

def main(argv): pass

if __name__ == "__main__":
    sys.exit(main(sys.argv))
