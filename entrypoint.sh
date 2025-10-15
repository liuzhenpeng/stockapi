#!/bin/bash
MODULE_NAME="main.py"
LOG_DIR="/var/log/stockapi"
LOG_FILE="/var/log/stockapi/log.txt"
BUILT_FILE="/stockapi/app/${MODULE_NAME}"
#保存pid的临时文件,可按情况进行修改，比如放到/run/passport.pid
RUN_COMMAND="uv run python "${BUILT_FILE}"  >> "${LOG_FILE}" 2>&1" 
#==============全局变量定义 end=========================
#有任何错误都退出
set -e
 
start(){
        echo "start stockapi"
 
 
        if [ ! -e $LOG_FILE ]; then
                mkdir -p $LOG_DIR
                touch $LOG_FILE
        else
                time=`date +%m%d%H%M`
                mv $LOG_FILE $LOG_FILE"-"$time
                touch $LOG_FILE
        fi
 
 
        eval $RUN_COMMAND
 
 
        echo "start stockapi OK."
}
 
start $ENVIRONMENT
 
exit 0

