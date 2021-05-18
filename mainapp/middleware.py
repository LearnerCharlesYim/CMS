# -*- coding:utf-8 -*-
# @Time   :2021/5/18 11:43
# @Author :CharlesYim
# @File   :middleware.py
from .models import User


def user_middleware(get_response):
    # 这个中间件初始化的代码

    def middleware(request):
        # request到达view的执行代码
        user_id = request.session.get("user_id")
        user = User.objects.filter(pk=user_id).first()
        if user:
            request.cmsuser = user
        else:
            request.cmsuser = None

        response = get_response(request)

        # response到达浏览器的执行代码

        return response

    return middleware