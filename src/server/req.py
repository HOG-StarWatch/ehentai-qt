import json

from config import config
from config.setting import Setting
from tools.tool import ToolUtil


def get_url(site=""):
    if not site:
        site = config.CurSite
    if site == "e-hentai":
        return config.Url
    else:
        return config.ExUrl


def get_api(site=""):
    if not site:
        site = config.CurSite
    if site == "e-hentai":
        return config.Url + "/api.php"
    else:
        return config.ExUrl + "/api.php"


class ServerReq(object):
    def __init__(self, url, header=None, params=None, method="POST") -> None:
        self.url = url
        self.headers = header
        self.params = params
        self.method = method
        self.isParseRes = False
        self.isUseHttps = True
        self.timeout = 5
        if Setting.IsHttpProxy.value == 1:
            self.proxy = {"http": Setting.HttpProxy.value, "https": Setting.HttpProxy.value}
        elif Setting.IsHttpProxy.value == 3:
            self.proxy = {}
        else:
            self.proxy = {"http": None, "https": None}

    def __str__(self):
        # if Setting.LogIndex.value == 0:
        #     return self.__class__.__name__
        # elif Setting.LogIndex.value == 1:
        #     return "{}, url:{}".format(self.__class__.__name__, self.url)
        # headers = dict()
        # headers.update(self.headers)
        params = self.params
        if "host" in self.headers:
            host = self.headers["host"]
        else:
            host = ""
        haveProxy = bool(self.proxy) and self.proxy.get("http") != None
        return "{}, url:{}, host:{}, proxy:{}, method:{}, params:{}".format(self.__class__.__name__, self.url, host, haveProxy, self.method, params)


# 下载图片
class DownloadBookReq(ServerReq):
    def __init__(self, url, loadPath="", cachePath="", savePath="", isReload=False):
        method = "Download"
        self.url = url
        self.loadPath = loadPath
        self.cachePath = cachePath
        self.savePath = savePath
        self.isReload = isReload
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method),
                                             {}, method)


# 登陆
class LoginReq(ServerReq):
    def __init__(self, userId, passwd):
        method = "POST"
        url = config.FormUrl + "/index.php?act=Login&CODE=01"

        header = ToolUtil.GetHeader(url, method)
        header["Referer"] = config.Url + "/bounce_login.php?b=d&bt=1-1"
        header["Sec-Fetch-Dest"] = "document"
        header["Sec-Fetch-Mode"] = "navigate"
        header["Sec-Fetch-Site"] = "same-site"
        header["Sec-Fetch-User"] = "?1"
        header["Upgrade-Insecure-Requests"] = "1"
        header["Origin"] = config.Url
        header["Content-Type"] = "application/x-www-form-urlencoded"

        data = dict()
        data["CookieDate"] = "1"
        data["b"] = "d"
        data["bt"] = "1-1"
        data["UserName"] = userId
        data["PassWord"] = passwd
        data["ipb_login_submit"] = "Login!"
        super(self.__class__, self).__init__(url, header, ToolUtil.DictToUrl(data), method)


# 获得Home
class HomeReq(ServerReq):
    def __init__(self):
        method = "GET"
        url = config.Url + "/home.php"

        header = ToolUtil.GetHeader(url, method)
        data = dict()
        super(self.__class__, self).__init__(url, header, data, method)


# 获得UserId
class GetUserIdReq(ServerReq):
    def __init__(self):
        method = "GET"
        url = config.FormUrl + "/index.php?"

        header = ToolUtil.GetHeader(url, method)
        data = dict()
        super(self.__class__, self).__init__(url, header, data, method)


# 检查更新
class CheckUpdateReq(ServerReq):
    def __init__(self, url):
        # url = config.UpdateUrl
        method = "GET"
        super(self.__class__, self).__init__(url, {}, {}, method)
        self.isParseRes = False


# 检查Pre更新
class CheckPreUpdateReq(ServerReq):
    def __init__(self, url=config.UpdateUrl):
        method = "GET"
        super(self.__class__, self).__init__(url.replace("/latest", ""), {}, {}, method)
        self.isParseRes = False
        self.useImgProxy = False

# 本子信息
class BookInfoReq(ServerReq):
    def __init__(self, bookId, page=1, token="", site=""):
        from tools.book import BookMgr
        self.bookId = bookId
        self.page = page
        self.site = config.CurSite
        if site:
            self.site = site
        if token:
            url = get_url(site) + "/g/{}/{}".format(bookId, token)
        else:

            info = BookMgr().GetBookBySite(self.bookId, self.site)
            url = get_url(site) + "/g/{}/{}".format(bookId, info.baseInfo.token)

        params = dict()
        if page > 1:
            params["p"] = str(page - 1)
        else:
            params["hc"] = "1"
            params["nw"] = "always"
        params["inline_set"] = "ts_l"
        data = ToolUtil.DictToUrl(params)
        if data:
            url += "/?" + data
        method = "GET"
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method), {}, method)


# 图片信息
class GetBookImgUrl(ServerReq):
    def __init__(self, bookId, index, site=""):
        from tools.book import BookMgr
        self.bookId = bookId
        self.index = index
        self.site = config.CurSite
        if site:
            self.site = site

        info = BookMgr().GetBookBySite(bookId, self.site)
        url = info.pageInfo.picUrl.get(index)
        method = "Get"
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method), {}, method)


# 图片信息Api
class GetBookImgUrl2(ServerReq):
    def __init__(self, bookId, index, site=""):
        self.bookId = bookId
        self.index = index
        self.site = config.CurSite
        if site:
            self.site = site
        from tools.book import BookMgr
        info = BookMgr().GetBookBySite(bookId, self.site)

        url = get_api(site)

        method = "POST"
        data = {
            'gid': self.bookId,
            'imgkey': info.pageInfo.GetImgKey(index),
            'method': 'showpage',
            'page': self.index,
            'showkey': info.pageInfo.showKey
        }
        header = ToolUtil.GetHeader(url, method)
        header["Content-Type"] = "application/json; charset=UTF-8"
        super(self.__class__, self).__init__(url, header, json.dumps(data), method)


# 获得首页
class GetIndexInfoReq(ServerReq):
    def __init__(self, nextId='', f_search="", f_cats="", f_sh="", f_spf="", f_spt="", f_srdd="", f_sfl="", f_sfu="", f_sft="", site=""):
        self.site = config.CurSite
        if site:
            self.site = site

        url = get_url(site)
        data = {}
        if nextId:
            data['next'] = str(nextId)

        if f_search:
            data['f_search'] = str(f_search)
        if f_cats:
            data["f_cats"] = str(f_cats)
        if f_sh:
            data["f_sh"] = "on"
        if f_spf:
            data["f_spf"] = str(f_spf)
        if f_spt:
            data["f_spt"] = str(f_spt)
        if f_srdd:
            data["f_srdd"] = str(f_srdd)
        if f_sfl:
            data["f_sfl"] = "on"
        if f_sfu:
            data["f_sfu"] = "on"
        if f_sft:
            data["f_sft"] = "on"
        if f_sh or f_spf or f_spt or f_srdd or f_sfl or f_sfu or f_sft:
            data["advsearch"] = "1"

        data["inline_set"] = "dm_l"
        param = ToolUtil.DictToUrl(data)
        if param:
            url += "/?" + param
        method = "GET"
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method),
                                             {}, method)


# 获得排行
class GetRankInfoReq(ServerReq):
    def __init__(self, tl="", p=1, site=""):
        self.site = config.CurSite
        if site:
            self.site = site

        url = config.Url + "/toplist.php"
        data = {}
        if tl:
            data["tl"] = str(tl)
        if p > 1:
            data["p"] = p-1
        param = ToolUtil.DictToUrl(data)
        if param:
            url += "/?" + param
        method = "GET"
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method),
                                             {}, method)


# 获得分类
class GetCategoryInfoReq(ServerReq):
    def __init__(self, nextId="", category=""):
        url = get_url() + "/" + category.replace(" ", "").lower()
        data = {}
        if nextId:
            data['next'] = str(nextId)

        data["inline_set"] = "dm_l"
        param = ToolUtil.DictToUrl(data)
        if param:
            url += "/?" + param
        method = "GET"
        self.site = config.CurSite
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method),
                                             {}, method)


# 获得收藏
class GetFavoritesReq(ServerReq):
    def __init__(self, favcat="", nextId=""):
        url = get_url() + "/favorites.php"
        data = {}
        if nextId:
            data['next'] = str(nextId)
        else:
            data["nw"] = "always"
        if favcat != "":
            data["favcat"] = str(favcat)
        param = ToolUtil.DictToUrl(data)
        if param:
            url += "/?" + param
        method = "GET"
        self.site = config.CurSite
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method),
                                             {}, method)


# 添加收藏
class AddFavoritesReq(ServerReq):
    def __init__(self, bookId=""):
        from tools.book import BookMgr
        info = BookMgr().GetBook(bookId)
        url = get_url() + "/gallerypopups.php?gid={}&t={}&act=addfav".format(bookId, info.baseInfo.token)
        method = "GET"
        super(self.__class__, self).__init__(url, ToolUtil.GetHeader(url, method),
                                             {}, method)


# 添加收藏2
class AddFavorites2Req(ServerReq):
    def __init__(self, bookId="", favcat=0, msg="", isUpdate=False):
        from tools.book import BookMgr
        info = BookMgr().GetBook(bookId)
        url = get_url() + "/gallerypopups.php?gid={}&t={}&act=addfav".format(bookId, info.baseInfo.token)
        method = "POST"
        header = ToolUtil.GetHeader(url, method)
        header["content-type"] = "application/x-www-form-urlencoded"

        data = dict()
        data["favcat"] = favcat
        data["favnote"] = msg
        data["update"] = "1"
        if isUpdate:
            data["apply"] = "Apply Changes"
        else:
            data["apply"] = "Add to Favorites"
        super(self.__class__, self).__init__(url, header,
                                             ToolUtil.DictToUrl(data), method)


# 删除收藏
class DelFavoritesReq(ServerReq):
    def __init__(self, bookId=""):
        url = get_url() + "/favorites.php"
        method = "POST"

        header = ToolUtil.GetHeader(url, method)
        header["content-type"] = "application/x-www-form-urlencoded"
        data = dict()
        data["modifygids[]"] = bookId
        data["apply"] = "Confirm"
        data["ddact"] = "delete"
        super(self.__class__, self).__init__(url, header,
                                             ToolUtil.DictToUrl(data), method)


# 发送评论
class SendCommentReq(ServerReq):
    def __init__(self, bookId, comment):

        from tools.book import BookMgr
        self.bookId = bookId
        self.site = config.CurSite
        self.page = 0
        info = BookMgr().GetBookBySite(bookId, self.site)
        url = get_url() + "/g/{}/{}?hc=1".format(bookId, info.baseInfo.token)
        method = "POST"

        header = ToolUtil.GetHeader(url, method)
        header["content-type"] = "application/x-www-form-urlencoded"
        data = dict()
        data["commenttext_new"] = comment
        super(self.__class__, self).__init__(url, header,
                                             ToolUtil.DictToUrl(data), method)


# 评分
class BookScoreReq(ServerReq):
    # {"rating_avg":4.63,"rating_usr":4,"rating_cnt":6,"rating_cls":"ir irg"}
    def __init__(self, bookId, rating):
        self.bookId = bookId
        from tools.book import BookMgr
        info = BookMgr().GetBook(bookId)
        url = get_api()
        method = "POST"
        data = {
            'gid': self.bookId,
            'apikey': info.pageInfo.apiKey,
            'apiUid': info.pageInfo.apiUid,
            'method': 'rategallery',
            'token': info.baseInfo.token,
            'rating': rating
        }
        header = ToolUtil.GetHeader(url, method)
        header["Content-Type"] = "application/json"
        super(self.__class__, self).__init__(url, header, json.dumps(data), method)


# Doh域名解析
class DnsOverHttpsReq(ServerReq):
    def __init__(self, domain=""):
        url = Setting.DohAddress.value + "?name={}&type=A".format(domain)
        method = "GET"
        header = dict()
        header["accept"] = "application/dns-json"
        super(self.__class__, self).__init__(url, header, {}, method)
        self.timeout = 5
        self.isParseRes = True


# 测试Ping
class SpeedTestPingReq(ServerReq):
    def __init__(self, ip, domain):
        url = "https://{}".format(ip)
        if "api" in domain:
            method = "POST"
            url = "https://api.e-hentai.org/api.php"
        else:
            method = "GET"
        header = ToolUtil.GetHeader(url, method)

        header["host"] = domain
        header['cache-control'] = 'no-cache'
        header['expires'] = '0'
        header['pragma'] = 'no-cache'
        super(self.__class__, self).__init__(url, header,
                                             {}, method)
        self.timeout = 2