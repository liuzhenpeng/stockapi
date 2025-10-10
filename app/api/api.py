# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: api路由
"""
from fastapi import APIRouter

from app.api import stock

api_router = APIRouter(prefix="/api")
api_router.include_router(stock.router, tags=["baostock"])

