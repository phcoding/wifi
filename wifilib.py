import base64
from urllib import request, parse

def parse_to_array(data_text):
    lines = data_text.splitlines()
    data_array = []
    for l in lines:
        data_array.append(tuple(l.split(':',1)))
    return data_array

def parse_to_dicts(data_text):
    dict_lines = data_text.splitlines()
    data_dicts = {}
    for l in dict_lines:
        k, v = tuple(l.split(':',1))
        data_dicts[k] = v
    return data_dicts

def array_to_dicts(array):
    return dict(array)

def dicts_to_array(dicts):
    return list(dicts.items())

def add_request_headers(reqs, headers):
    """Add request header according of headers text."""
    
    dict_data = parse_to_array(headers)
    for k, v in dict_data:
        reqs.add_header(k, v)

def wifi_login(username, password):
    """Login function"""
    form_text = """action:login
username:%s
password:{B}%s
ac_id:1
user_ip:
nas_ip:
user_mac:
save_me:1
ajax:1""" % (
    parse.quote(username), 
    parse.quote(base64.b64encode(password.encode('utf8'))))
    form_data = parse_to_array(form_text)
    login_data = parse.urlencode(form_data)
    reqs = request.Request('http://10.62.65.185/include/auth_action.php')
    reqs_headers = """Accept:*/*
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Content-Length:107
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
Cookie:login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYf0isl5GaB5uMTzomA09BR1mvhVbDjUpZ2M\
pGPBJ1XBXWAFkQGh90C7EzEpnDy1lPr61j2GrVWn1%252BS42uOsVtvD8dtm8nxKgIZsIjTlGhkj6dTy\
K4U%252BZmr6Zwq4XODLOlu3e%252FYy%252FnTdBtTgsVgMFYa8jDtASy4%252BCrw%253D%253D; l\
anguage=en; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYf0isl5GaB5uMTzomA09BR1mvhVbDj\
UpZ2MpGPBJ1XBXWAFkQGh90C7EzEpnDy1lPr61j2GrVWn1%252BS42uOsVtvD8dtm8nxKgIZsIjTlGhk\
j6dTyK4U%252BZmr6Zwq4XODLOlu3e%252FYy%252FnTdBtTgsVgMFYa8jDtASy4%252BCrw%253D%25\
3D
Host:10.62.65.185
Origin:http://10.62.65.185
Referer:http://10.62.65.185/srun_portal_pc.php?ac_id=1&url=http://www.baidu.com
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/61.0.3163.100 Safari/537.36
X-Requested-With:XMLHttpRequest"""
    add_request_headers(reqs, reqs_headers)
    with request.urlopen(reqs, login_data.encode('utf-8')) as resp:
        return resp.read().decode('utf-8')
    return ''

def wifi_logout(username, password):
    """Logout function"""
    form_text = """action:logout
username:%s
password:%s
ajax:1""" % (username, password)
    form_data = parse_to_array(form_text)
    login_data = parse.urlencode(form_data)
    reqs = request.Request('http://10.62.65.185/include/auth_action.php')
    reqs_headers = """Accept:*/*
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
Host:10.62.65.185
Origin:http://10.62.65.185
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/61.0.3163.100 Safari/537.36
X-Requested-With:XMLHttpRequest"""
    add_request_headers(reqs, reqs_headers)
    with request.urlopen(reqs, login_data.encode('utf-8')) as resp:
        return resp.read().decode('utf-8')
    return ''