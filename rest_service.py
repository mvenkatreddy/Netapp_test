# -*- coding: utf-8 -*-
"""
Problem 2

Write a short Python script to connect to the REST service
located at: https://news.google.com/news/rss/?ned=us&amp;hl=en

This problem is intended to show how you interact with a REST api.
Script will take as input a date time string that accepts the date and time in the following

format – 2016/Mar/08 14:12:24

Output will be news titles with the Top Stories category that have been posted after the input time stamp.

Example output:
US Military Sending Warship to Israel, Spy Planes to Syria After Chemical
Weapons Report
Trump reportedly unclear on difference between Medicare and Medicaid
"""

# Python modules
import requests
import argparse
from datetime import datetime
import xml.etree.ElementTree as ET


def get_news(time_stamp):
    """
    Output will be news titles with the Top Stories category that have been posted after the input time stamp.
    :param time_stamp: time stamp datetime object
    :returns : Output will be news titles with the Top Stories category
               that have been posted after the input time stamp.
    """
    url = "https://news.google.com/news/rss/?ned=us&amp;hl=en"
    news = []

    # calling the google new url
    response = requests.get(url)
    # Checking the status is 200 and collecting the title and published dates
    if response.status_code == 200:
        root = ET.fromstring(response.text.encode('utf-8'))
        news = [{"title": item.find('title').text,
                 "time": datetime.strptime(item.find("pubDate").text, "%a, %d %b %Y %H:%M:%S %Z")}
                for item in root.findall('*//item')]
    else:
        print "Unable to get the news from: {}".format(url)

    # printing the news titles with the Top Stories category that have been posted after the input time stamp.
    if news:
        for each_new in news:
            if each_new["time"] > time_stamp:
                print each_new.get("title"), '\n'
    else:
        print "Empty new is there in the URL: {}".format(url)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--time_stamp", help="date time string", type=str)
    args = parser.parse_args()
    args.time_stamp = "2016/Mar/08 14:12:24"
    if args.time_stamp:
        try:
            time_stamp = datetime.strptime(args.time_stamp, "%Y/%b/%m %H:%M:%S")
            get_news(time_stamp)
        except Exception as e:
            print e
            print "Acceptable time stamp: '%Y/%b/%m HH:MM:SS'"
    else:
        print "Else: Acceptable time stamp: '%Y/%b/%m HH:MM:SS'"
