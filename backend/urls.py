from .djangoapps.main import views as MainViews
from .djangoapps.login import views as LoginViews
from .djangoapps.regist import views as RegistViews
from .djangoapps.upload import views as UploadViews
from .djangoapps.memo import views as MemoViews
from django.urls import path
from django.conf.urls import url

urlpatterns = [


    url('^main$',MainViews.main,name='main'),
    url('^write$',MainViews.write,name='write'),
    url('modify$',MainViews.modify,name='modify'),

    url('api_write_create$',MainViews.api_write_create,name='api_write_create'),
    url('^api_write_read',MainViews.api_write_read,name='api_write_read'),
    url('api_write_update$',MainViews.api_write_update,name='api_write_update'),
    url('api_write_delete$',MainViews.api_write_delete,name='api_write_delete'),

    url('login$',LoginViews.login,name='login'),
    url('login_check$',LoginViews.login_check,name='login_check'),
    url('logout$',LoginViews.logout,name='logout'),

    url('regist$',RegistViews.regist,name='regist'),
    url('api_regist_create$',RegistViews.api_regist_create,name='api_regist_create'),

    url('upload_main$',UploadViews.upload_main,name='upload_main'),
    url('upload_write$',UploadViews.upload_write,name='upload_write'),
    url('api_upload_write_create$',UploadViews.api_upload_write_create,name='api_upload_write_create'),

    url('memo_main$',MemoViews.memo_main,name='memo_main'),
    url('^api_memo_create$',MemoViews.api_memo_create,name='api_memo_create'),

    url('$',MainViews.main,name='main'),



]
