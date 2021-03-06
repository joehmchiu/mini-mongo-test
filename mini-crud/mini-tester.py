#!/usr/bin/env python3

import os, sys
import json

def ret(cmd):
    req = os.popen(cmd)
    res = req.read()
    return res

mode = sys.argv[1]
test = sys.argv[2]
if not mode: mode = 'read'
if not test: test = 'none'

api = ret("ssh mac 'cat /tmp/api'").rstrip()
jsonfile = "/tmp/test-result.json"

def dumps(j):
    print(json.dumps(j, indent=4, sort_keys=True))

def ok(j):
    global mode
    h = {}
    h["mode"] = mode
    h["test"] = test
    try:
        try: h["id"] = j["id"]
        except: h["id"] = j["_id"]
        h["ok"] = True
    except Exception as e:
        h["ok"] = False

    f = open(jsonfile, "a")
    json.dump(h, f)
    f.write('\n')
    f.close()        
    return h["ok"]

def mid():
    mf = "/tmp/mini-id"
    try:
        res = ret("[ -e %s ] || touch %s; cat %s" % (mf, mf, mf))
    except:
        res = " unknown"
    return res

def show():
    cmd = "curl -s " + api
    res = ret(cmd)
    print(res)

def read():
    res = ret("curl -s " + api + mid())
    j = json.loads(res)
    dumps(j)
    ok(j["list"][0])

def update():
    res = ret("./test/update.sh " + api + " " + mid())
    j = json.loads(res)
    dumps(j)
    ok(j)

def create():
    res = ret("./test/create.sh " + api)
    j = json.loads(res)
    dumps(j)
    if ok(j):
        res = ret("echo " + j["id"] + " > /tmp/mini-id")
    else:
        res = ret("echo unknown > /tmp/mini-id")


def delete():
    res = ret("./test/delete.sh " + api + " " + mid())
    j = json.loads(res)
    dumps(j)
    ok(j)

if mode == 'all':
    show()
if mode == 'create':
    create()
if mode == 'read':
    read()
if mode == 'update':
    update()
if mode == 'delete':
    delete()
