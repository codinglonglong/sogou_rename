'''
批量重命名搜狗输入法词库
'''
import os

def renamelines():
    '''
    批量重命名
    '''
    lines = []
    with open("/home/long/.config/SogouPY/scdlist.ini") as conffile:
        lines = [x.strip() for x in conffile.readlines()]
        lines = [x for x in lines if len(lines) != 0]
    m_id = ""
    m_line = ""
    for line in lines:
        if "id" in line:
            m_id = line.split("=")[1]
        elif "name" in line:
            m_line = line.split("=")[1]
            try:
                os.rename("/home/long/.config/SogouPY/scd/" + str(m_line) + ".scel",
                          "/home/long/.config/SogouPY/scd/" + str(m_id) + ".scel")
            except FileNotFoundError as error:
                print(error)

renamelines()
