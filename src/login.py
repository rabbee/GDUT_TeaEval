import requests

# 校园网账号
account = 'YourUsername'
  
# 校园网密码  
pwd = 'YourPassword'

url = 'http://222.200.98.147/'

login_url = url + 'login!doLogin.action'                # 登录        
welcome_url = url + 'login!welcome.action'              # 主页面内容   （Html）

headers = {
        '(Request-Line)':'POST /login!doLogin.action HTTP/1.1',
        'Host':'222.200.98.147',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'en-US,en;q=0.5',
        'Accept-Encoding':'gzip, deflate',
}

def login():

    s = requests.Session()

    login_html = s.get(url)

    data_login = {
        'account' : account,
        'pwd' : pwd,
        'verifycode' : ''
    }

    res = s.post(login_url, data=data_login, headers=headers)    # 登录

    dict_res = eval(res.text)

    if 'y' in dict_res['status']:
        print('登录成功！')
    else:
        print('登录失败... 请检查用户名与密码')

    main_html = s.get(welcome_url, headers=headers)                 # 进入主界面
    
    return s
