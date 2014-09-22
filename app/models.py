#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from app import db

class User(db.Model):
    '''用户'''
    userid = db.Column(db.String(22), primary_key = True)
    nickname = db.Column(db.Text)
    password = db.Column(db.Text)
    is_admin = db.Column(db.Boolean)
    ac_count = db.Column(db.Integer, default = 0)
    submit_count = db.Column(db.Integer, default = 0)

    def __init__(self, userid, nickname, password, is_admin = False):
        self.userid = userid
        self.nickname = nickname
        self.password = password
        self.is_admin = is_admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userid

class Problem(db.Model):
    '''题目'''
    pid = db.Column(db.Integer, primary_key = True, default = None)
    title = db.Column(db.Text)
    desc = db.Column(db.Text)
    pinput = db.Column(db.Text)
    poutput = db.Column(db.Text)
    sinput = db.Column(db.Text)
    soutput = db.Column(db.Text)
    hint = db.Column(db.Text)
    time_limit = db.Column(db.Integer)
    memory_limit = db.Column(db.Integer)
    ac_count = db.Column(db.Integer, default = 0)
    submit_count = db.Column(db.Integer, default = 0)
    visable = db.Column(db.Boolean, default = True)

    def __init__(self, title, desc, pinput, poutput, sinput, soutput, hint, time_limit, memory_limit):
        self.title = title
        self.desc = desc
        self.pinput = pinput
        self.poutput = poutput
        self.sinput = sinput
        self.soutput = soutput
        self.hint = hint
        self.time_limit = time_limit
        self.memory_limit = memory_limit

class Submit(db.Model):
    '''提交信息'''
    runid = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(22))
    pid = db.Column(db.Integer)
    result = db.Column(db.String(22), default = 'Pending')
    memory_used = db.Column(db.Integer, default = None)
    time_used = db.Column(db.Integer, default = None)
    language = db.Column(db.String(9))
    src = db.Column(db.Text)
    length = db.Column(db.Integer)
    submit_time = db.Column(db.String(19))
    ce_error = db.Column(db.Text, default = None)

    def __init__(self, runid, userid, pid, language, src, submit_time):
        self.runid = runid
        self.userid = userid
        self.pid = pid
        self.language = language
        self.src = src
        self.length = len(src)
        self.submit_time = submit_time

class Notification(db.Model):
    '''通知信息'''
    mid = db.Column(db.Integer, primary_key = True, default = None)
    content = db.Column(db.Text)
    visable = db.Column(db.Boolean, default = True)
    add_time = db.Column(db.String(22))

    def __init__(self, content, add_time):
        self.content = content
        self.add_time = add_time
