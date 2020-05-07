#!/usr/bin/python3
# coding=utf-8
import atexit
from pyVmomi import vim, vmodl
from pyVim.connect import SmartConnectNoSSL, Disconnect
import argparse
import datetime
import db
def get_args():
    parser = argparse.ArgumentParser(
        description='Arguments for talking to vCenter')

    parser.add_argument('-s', '--host',
                        required=True,
                        action='store',
                        help='vSpehre service to connect to')

    parser.add_argument('-o', '--port',
                        type=int,
                        default=443,
                        action='store',
                        help='Port to connect on')

    parser.add_argument('-u', '--user',
                        required=True,
                        action='store',
                        help='User name to use')

    parser.add_argument('-p', '--password',
                        required=True,
                        action='store',
                        help='Password to use')

    args = parser.parse_args()
    return args
def get_obj(content, vimtype, name=None):
    #列表返回,name 可以指定匹配的对象
    container = content.viewManager.CreateContainerView(content.perfManager, vimtype, True)
    obj = [ view for view in container.view]
    return obj
def run(host, user, pwd, port):
    try:
        si = SmartConnectNoSSL(host=host, user=user, pwd=pwd, port=port)
        sitime=si.CurrentTime()
        atexit.register(Disconnect, si)
        content = si.RetrieveContent()
    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return False, error.msg
    return content
def getComputeResource(Folder,computeResourceList):
    if hasattr(Folder, 'childEntity'):
        for computeResource in Folder.childEntity:
           getComputeResource(computeResource,computeResourceList)
    else:
        computeResourceList.append(Folder)
    return computeResourceList

def BuildQuery(content,counterId, instance, entity):
    perfManager = content.perfManager
    startTime = 1557479224
    endTime =1557479224
    metricId = vim.PerformanceManager.MetricId(counterId=counterId, instance=instance)
    query = vim.PerformanceManager.QuerySpec(intervalId=20, entity=entity, metricId=[metricId])
    perfResults = perfManager.QueryPerf(querySpec=[query])
    if perfResults:
        return perfResults
    else:
        return False
def connect_db():
    """ 建立SQL连接
    """
    mydb = db.MyDB(
            host="127.0.0.1",
            user="vmware",
            passwd="asdqwezxc@321",
            db="vmware"
            )
    mydb.db_connect()
    mydb.db_cursor()
    return mydb

def main(args):
    # connect this thing
    host = args.host
    user = args.user
    pwd = args.password
    port = args.port
    # 连接mysql数据
    curdb = connect_db()
    content = run(host, user, pwd, port)
    vcalarm = content.rootFolder.childEntity
    for datacenter in vcalarm:
        # 数据中心名字
        datatorename = datacenter.name
        for databases in datacenter.hostFolder.childEntity:
            for exsi in databases.host:
                # print(,ii.name)
                for exsitriggered in exsi.triggeredAlarmState:
                    # 虚拟机告警事项的名字
                    exsialarmname = exsitriggered.alarm.info.name
                    # 虚拟机告警事项的等级
                    exsialarlevel = exsitriggered.overallStatus
                    # 虚拟机告警事项的时间
                    exsitriggered.time = (exsitriggered.time + datetime.timedelta(hours=8))
                    exsialartime = str(exsitriggered.time).split(".")[0]
                    #插入数据库
                    sql = """
                            REPLACE  into esxi_alarm( vcenterip,
                            datatorename, esxiname, alarmname, alarlevel, alartime)
                            VALUES ("{}", "{}", "{}", "{}", "{}", "{}");""".format(host, datatorename, exsi.name,exsialarmname, exsialarlevel, exsialartime)
                    # print(sql)
                    curdb.db_execute(sql)
        #获取虚拟机告警
        #虚拟机根目录
        vmdir = datacenter.vmFolder.childEntity
        for vms in vmdir:
            # 虚拟机名字
            vmname = vms.name
            #判断有没有属性对象
            if hasattr(vms,"summary"):
                vmip = (vms.summary.guest.ipAddress)
            else:
                vmip = None
            for vmstriggereds in vms.triggeredAlarmState:
                #虚拟机告警事项的名字
                vmalarmname = vmstriggereds.alarm.info.name
                # 虚拟机告警事项的等级
                vmalarlevel = vmstriggereds.overallStatus
                # 虚拟机告警事项的时间,vc时间误差8小时
                vmstriggereds.time = (vmstriggereds.time + datetime.timedelta(hours=8))
                vmalartime = str(vmstriggereds.time).split(".")[0]
                #插入数据库
                sql = """
                    REPLACE  into vm_alarm( vcenterip,
                    datatorename, vmname, alarmname, alarlevel, alartime)
                    VALUES ("{}", "{}", "{}", "{}", "{}", "{}");""".format(host, datatorename, vmname, vmalarmname, vmalarlevel, vmalartime)
                # print(sql)
                curdb.db_execute(sql)
if __name__ == "__main__":
    args = get_args()
    main(args)

