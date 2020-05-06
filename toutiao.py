#coding:utf-8

import time
import requests
from apis import TTApi
from tools import *
from deco import fetch
from encrypt import encrypt

class TTBot:

    def __init__(self,username=None,password=None):
        self.API = TTApi()
        self.session = requests.Session()
        self.username = username
        self.password = password

    @fetch
    def send_sms_code(self,phone,kind='LOGIN'):
        """
        发送验证码至手机号，以备下一步的登录或者修改密码
        :param phone: 接收验证码的手机号账户 中国大陆 例如：13988889995
        :param kind: 此次操作的类型，登录/LOGIN 修改密码/PASSWORD,修改密码需要登录账户后才能发送验证码
        :return: 发送成功的标识
        """
        KIND = {
            'LOGIN':'3731',
            'PASSWORD':'3436',
        }
        return {
            'params':{
                'account_sdk_version':'341',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}',
                'tma_jssdk_version': '1.5.4.5',

            },
            'data':{
                'mix_mode': '1',
                'check_register': '1',
                'type': f'{KIND.get(kind,"3731")}',
                'mobile': f'{encrypt(phone)}',
                'unbind_exist': '35',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'kwargs':{
                'session':self.session,
            },
            'method':'post',
            'url':self.API.SEND_SMS_CODE
        }

    @fetch
    def login_by_sms_code(self,phone,code):
        """
        使用短信验证码登录
        :param phone: 需要登录的手机号账户  中国大陆 例如：13988889995
        :param code: 接收到的短信验证码  例如：9456
        :return: 登录后的账户信息
        """
        return {
            'params':{
                'account_sdk_version': '341',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}',
                'tma_jssdk_version': '1.5.4.5',
            },
            'data':{
                'mix_mode': '1',
                'mobile': f'{encrypt(phone)}',
                'code': f'{encrypt(code)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'kwargs':{
                'session':self.session,
            },
            'method':'post',
            'url':self.API.SMS_LOGIN,
        }

    @fetch
    def set_password_by_sms_code(self,password,code):
        """
        登录后 修改/设置 账户密码，需要先发送 修改密码短信验证码给手机，获取验证码code
        :param password: 需要设置的新密码
        :param code: 获取到的修改密码短信验证码
        :return: 登录后的账户信息
        """
        return {
            'params': {
                'account_sdk_version': '341',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}',
                'tma_jssdk_version': '1.5.4.5',
            },
            'data': {
                'mix_mode': '1',
                'password': f'{encrypt(password)}',
                'code': f'{encrypt(code)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'kwargs': {
                'session': self.session,
            },
            'method': 'post',
            'url': self.API.SMS_RESET_PWD,
        }

    @fetch
    def login_by_password(self,username,password):
        """
        使用账户密码登录
        :param username:  账户/手机号
        :param password:  密码
        :return: 登录账户信息
        """
        username = self.username if self.username else username
        password = self.password if self.password else password
        return {
            'params': {
                'account_sdk_version': '341',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}',
                'tma_jssdk_version': '1.5.4.5',
            },
            'data': {
                'mix_mode': '1',
                'password': f'{encrypt(password)}',
                'mobile': f'{encrypt(username)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'kwargs': {
                'session': self.session,
            },
            'method': 'post',
            'url': self.API.PWD_LOGIN,
        }

    @fetch
    def get_user_info(self,uid):
        """
        采集用户信息
        :param uid: 用户user_id
        """
        return {
            'params':{
                'user_id': uid,
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': f'{fake_device_type().upper()}',
                'device_brand': f'{fake_device_type().lower()}',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.USER_INFO
        }

    @fetch
    def get_user_posts(self,uid,count=20,offset=0,kind='ARTICLE'):
        """
       采集用户作品
       :param uid:  用户uid
       :param count: 本次采集数量，默认20
       :param offset: 翻页游标，初始第一页0，后续页数根据返回结果的offset值传入翻页
       :param kind: 采集作品类型，有视频VIDEO/文章ARTICLE/问答WENDA/所有ALL/小视频SHORTVIDEO
       """
        cate = {
            'VIDEO':'profile_video',
            'ARTICLE':'profile_article',
            'ALL':'profile_all',
            'WENDA':'profile_wenda',
            'SHORTVIDEO':'profile_short_video',
        }
        return {
            'params':{
                'category': cate.get(kind, 'VIDEO'),
                'visited_uid': uid,
                'stream_api_version': '88',
                'count': count,
                'offset': offset,
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': f'{fake_device_type().upper()}',
                'device_brand': f'{fake_device_type().lower()}',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'fp': 'a_fake_fp',
                'tma_jssdk_version': '1.5.3.0',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.USER_POSTS,
        }

    @fetch
    def get_item_info(self,item_id):
        """
        采集文章信息
        :param item_id: 文章id
        """
        return {
            'params':{
                'group_id': item_id,
                'item_id': item_id,
                'aggr_type': '1',
                'context': '1',
                'from_category': '__all__',
                'article_page': '0',
                'is_low_actived': '0',
                'search_id': '',
                'query': '',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': f'{fake_device_type().upper()}',
                'device_brand': f'{fake_device_type().lower()}',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.ARTICLE_INFO
        }

    @fetch
    def get_item_comments(self,item_id,offset=0,count=20):
        """
        采集头条文章/视频 评论
        :param item_id: 文章/视频 的id
        :param offset: 翻页游标，初始第一页0，后续逐步加上count的值，如count为20，第二页为20，第三页为40
        :param count: 每次采集的条数
        """
        return {
            'params':{
                'group_id': item_id,
                'item_id': item_id,
                'aggr_type': '1',
                'fold': '1',
                'count': count,
                'offset': offset,
                'tab_index': '0',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': f'{fake_device_type().upper()}',
                'device_brand': f'{fake_device_type().lower()}',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.VIDEO_COMMENTS
        }

    @fetch
    def get_user_followers(self,uid,count=20,offset=0):
        """
        获取用户粉丝列表
        :param uid:  用户user_id
        :param count: 每次获取粉丝列表的个数
        :param offset: 翻页游标，根据返回结果的offset值进行下一页操作
        """
        return {
            'params':{
                'user_id': uid,
                'count': count,
                'offset': offset,
                'cursor': '0',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': f'{fake_device_type().upper()}',
                'device_brand': f'{fake_device_type().lower()}',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.USER_FOLLOWERS
        }

    @fetch
    def get_user_followings(self,uid,count=20,offset=0):
        """
        获取用户关注列表
        :param uid:  用户user_id
        :param count: 每次获取关注列表的个数
        :param offset: 翻页游标，根据返回结果的offset值进行下一页操作
        """
        return {
            'params':{
                'user_id': uid,
                'count': count,
                'offset': offset,
                'cursor': '0',
                'device_id': f'{random.randrange(10 ** 10, 10 ** 11)}',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'device_type': f'{fake_device_type().upper()}',
                'device_brand': f'{fake_device_type().lower()}',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.USER_FOLLOWINGS
        }

    @fetch
    def get_recommend_users(self,uid):
        """
        推荐与传入uid用户相似的用户
        :param uid: 需要的类型用户user_id
        """
        return {
            'params':{
                'follow_user_id': uid,
                'source': 'homepage',
                'scene': 'follow',
                'ac': 'wifi',
                'channel': 'baidu',
                'aid': '13',
                'app_name': 'news_article',
                'version_code': '700',
                'version_name': '7.0.0',
                'device_platform': 'android',
                'abflag': '3',
                'ssmix': 'a',
                'os_api': '22',
                'os_version': '5.1.1',
                'manifest_version_code': '700',
                'update_version_code': '70011',
                '_rticket': f'{int(time.time() * 1000)}',
                'rom_version': '22',
                'plugin': '26958',
                'ts': f'{int(time.time())}'
            },
            'url':self.API.USER_RECOMMEND,
        }

