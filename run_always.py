# coding: utf-8

import scraper

import os
import time
import datetime


def git_add_commit_push(date, filename):

    cmd_git_add = 'git add {filename}'.format(filename = filename)
    cmd_git_commit = 'git commit -m "{date}"'.format(date = date)
    cmd_git_push = 'git push -u origin master'

    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)


# scrape at predefined time, once a day
while True:
    if time.strftime('%H:%M') == '23:30':

        while True:
            scraper.job()

            # git add commit push
            strdate = datetime.datetime.now().strftime('%Y-%m-%d')
            dirname = datetime.datetime.now().strftime('%Y/%m')
            filename = dirname + '/' + '{date}.md'.format(date = strdate)
            git_add_commit_push(strdate, filename)

            time.sleep(24 * 60 * 60)
    
    else:
        time.sleep(60)
