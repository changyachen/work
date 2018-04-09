from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def logout(request):
    '''用户退出登录'''
    # 清空用户的session信息
    request.session.flush()
    # 跳转到首页
    return redirect(reverse('books:index'))