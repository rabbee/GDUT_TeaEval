from login import *

teaList_url = url + 'xswjxx!teaList.action'             # 教师是否评价 （JavaScript）
teaDataLinst_url = url + 'xswjxx!getTeaDataList.action' # 教师评价数据 （Json）
noti_url = url + 'notice!getNotice.action?_=1489603985955' # 未知用途
save_evaluate_url = url + 'xswjxx!savePj.action'            # 提交评价

# POST数据，用于获取教师评价列表
teaData = {
    'xnxqdm' : '201602',
    'page' : '1',
    'rows' : '50',
    'sort' : 'pdm',
    'order' : 'asc'
}

def getTeacherEvaluationTable(s):

    # 教师评价数据    (Json)
    res = s.post(teaDataLinst_url, headers=headers, data=teaData)

    return res.text

def getCanEvaluate(s):

    # 教师是否评价 （JavaScript）
    # 未解析
    res = s.get(teaList_url, headers=headers)

    return res.text

def submit(s):
    
    # 教师评价数据
    res = s.post(teaDataLinst_url, headers=headers, data=teaData)

    # 转化为字典dict
    text = eval(res.text)

    # 课程评价参数
    # pdm
    # xnxqdm
    # pjdxlxdm
    # pjlxdm
    # pjdxdm
    # pjdxmc 教师姓名
    # jxhjdm
    # pjdxbh 教师编号
    # kcptdm
    # wjdm
    # jxhjmc 教学环节
    # isyxf
    # yxfbl
    # isyjjy
    # yjjymc 备注
    # wjlx
    # kcmc   课程名称
    # isdczbzl
    # rownum_ 
    print('----------------------------------------------')

    dataList = text['rows']

    for x in dataList:
        evaluate_data = {}
        for key, value in x.items():
            if 'pdm' in key:
                evaluate_data['pdm'] = value
            elif 'wjdm' in key:
                evaluate_data['wjdm'] = value
            elif 'pjdxlxdm' in key:
                evaluate_data['pjdxlxdm'] = value
            elif 'pjlxdm' in key:
                evaluate_data['pjlxdm'] = value
            elif 'kcptdm' in key:
                evaluate_data['kcptdm'] = value
            elif 'pjdxbh' in key:
                evaluate_data['pjdxbh'] = value
            elif 'pjdxdm' in key:
                evaluate_data['pjdxdm'] = value
            elif 'xnxqdm' in key:
                evaluate_data['xnxqdm'] = value
            elif 'pjdxmc' in key:
                evaluate_data['pjdxmc'] = value
            #print(key + ' : ' + value)
        evaluate_data['yxf'] = '95'
        evaluate_data['jy'] = ''
        evaluate_data['wtdms'] = '1,15,19,37,32,8'
        evaluate_data['xmdmvals'] = '0001,0055,0071,0148,0126,0030'
        evaluate_data['xmmcs'] = '否,是,很好,提升很大,经常,是'
        evaluate_data['xzfzs'] = '20.00,14.70,14.70,19.60,14.70,15.00'
        print(evaluate_data)
        res_save = s.post(save_evaluate_url, headers=headers, data=evaluate_data)
        print('评价结果： ' + res_save.text)
        print('--------------')
