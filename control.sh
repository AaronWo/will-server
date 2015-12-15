#!/bin/bash

function help()
{
    echo "Usage: sh control.sh start|stop|restart"
}

function start()
{
    echo "in start commond"
    nohup python manage.py runserver >> django.log 2>&1 &
    touch running.tag
    echo "start OK"
}

function stop()
{
    echo "in stop commond"
    ps aux | grep manage.py | grep -v "grep"
    ret=$?
    if [ $ret -ne 0 ]; then
        echo "django not started"
        exit 1
    fi
    pid=$(ps aux | grep manage.py | grep -v "grep" | awk '{print $2}')
    echo "pid:$pid"
    kill -9 $pid
    rm running.tag
    echo "stop [OK]"
}

cmd=$1
case $cmd in 
start)
    start
    ;;
stop)
    stop
    ;;
restart)
    stop
    start
    ;;
*)
    help
    exit 1
    ;;
esac
