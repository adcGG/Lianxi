# -*- coding: utf-8 -*-
import scrapy
import json
from Bilibili.items import BilibiliItem
class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['app.bilibili.com']
    # start_urls = ['http://app.bilibili.com/']
    baseurl ='https://app.bilibili.com/x/v2/' \
             'feed/index?ad_extra=2F160688A991F9' \
             'E874393027277D85422F5D26B73238F495' \
             '719706F7F69C8485FF36E2FDEDDDDA0C08' \
             '0EB4FEFCE5AEC82C9AFC0569F4FCF3DD3E' \
             '33EC93D7E653857B7E4DEAD038A38A1042' \
             'A0ED26DA723A0D0BA60C241B4B54420DA' \
             '0BE2E10BD3A948E2B5F44657D491C165F' \
             '1FFD9BF24C7914418063E8B8B71359252' \
             '6A49376055C964BA80A28D46FF88D87AB0' \
             'F5FE2C3E4576D02086EA1F327FE38DDC1' \
             'EB8650A8E30FD203A66D217191413C40F' \
             '3D6313F82BAC30DA18FA10925CFF98F850' \
             '4D52E7764D326958134A8B5270E0651835' \
             '5AA427AFDA3C10F6F42E5D65D1547C5901' \
             '8A5E54FDD7EB04B36E5BBB22ABC7DEB1A4' \
             'D97BDB3A75DAA2E15C35EFCC3073B3BBAD' \
             'C65A3C1DB910ECEA96033B62289966A87C9' \
             '34626F0FD4719724D4F002B05CECCC3F1A' \
             '62A4CFD2E8F98D6D7A94E9757EFB775A5B' \
             '8419E31BEBB1685CC83E8F6BFDE1EA2626C' \
             '0A49A5E284D1032B83BE8945161F834A361' \
             '69B8674D0A5F8A932C3470A0898E42B0E91' \
             'F9EE8CC5E904429FC0F3B890A4205A6150B9D4A1539B9CF' \
             '8183B1A3086E4A562A97300FD4CC1932B46609D98991AF789' \
             '5DB0D2C77F2BD7E9D9271FAF14E6E8DF859A5B4F2C658AD8C' \
             '619933F20251603AB339B0A7FF72A4E345CEC2E53BE217F46' \
             'C8C3F5F10D8E78A0B27A485C15ECE65E438F0A4EA1429A3635E' \
             'A04E9C44994212486E019B35208E84F06AF310170F5B6B462B' \
             'BE1454EA520D4A00506AC08B5BC36FC528F804BB64123FCF0C' \
             'C1382AD77ED35896939335A2F0DD1AB395B9F2DC027B80B3B1' \
             'AB40233EAB4B04F1DE16A8B7EF607CE829F8D96D6FF5EF2216' \
             'D55A81C45812817050E504A3E8EB1862E44A7D72CF1CCAD0FD' \
             'FE71CC295F306869BC0B6E75AE&appkey=1d8b6e7d45233436' \
             '&autoplay_card=0&build=5452100&channel=baidu&colum' \
             'n=2&device_name=MI%202A&device_type=0&flush=0&fnva' \
             'l=16&fnver=0&force_host=0&fourk=0&idx=0&login_even' \
             't=1&mobi_app=android&network=wifi&open_event=cold&' \
             'platform=android&pull=true&qn=32&recsys_mode=0&sta' \
             'tistics=%7B%22abtest%22%3A%22%22%2C%22platform%22%' \
             '3A3%2C%22version%22%3A%225.45.2%22%2C%22appId%22%3' \
             'A1%7D&ts=15653103'

    start_urls = ['https://app.bilibili.co'
                  'm/x/v2/feed/index?ad_ex'
                  'tra=2F160688A991F9E874393027277D85422F5D26B73238F'
                  '495719706F7F69C8485FF36E2FDEDDDDA0C080EB4FEFCE5AEC'
                  '82C9AFC0569F4FCF3DD3E33EC93D7E653857B7E4DEAD038A38'
                  'A1042A0ED26DA723A0D0BA60C241B4B54420DA0BE2E10BD3A9'
                  '48E2B5F44657D491C165F1FFD9BF24C7914418063E8B8B7135'
                  '92526A49376055C964BA80A28D46FF88D87AB0F5FE2C3E4576'
                  'D02086EA1F327FE38DDC1EB8650A8E30FD203A66D21719141'
                  '3C40F3D6313F82BAC30DA18FA10925CFF98F8504D52E7764D'
                  '326958134A8B5270E06518355AA427AFDA3C10F6F42E5D65D'
                  '1547C59018A5E54FDD7EB04B36E5BBB22ABC7DEB1A4D97BDB'
                  '3A75DAA2E15C35EFCC3073B3BBADC65A3C1DB910ECEA96033'
                  'B62289966A87C934626F0FD4719724D4F002B05CECCC3F1A6'
                  '2A4CFD2E8F98D6D7A94E9757EFB775A5B8419E31BEBB1685C'
                  'C83E8F6BFDE1EA2626C0A49A5E284D1032B83BE8945161F83'
                  '4A36169B8674D0A5F8A932C3470A0898E42B0E91F9EE8CC5E'
                  '904429FC0F3B890A4205A6150B9D4A1539B9CF8183B1A3086'
                  'E4A562A97300FD4CC1932B46609D98991AF7895DB0D2C77F2'
                  'BD7E9D9271FAF14E6E8DF859A5B4F2C658AD8C619933F2025'
                  '1603AB339B0A7FF72A4E345CEC2E53BE217F46C8C3F5F10D8'
                  'E78A0B27A485C15ECE65E438F0A4EA1429A3635EA04E9C449'
                  '94212486E019B35208E84F06AF310170F5B6B462BBE1454EA'
                  '520D4A00506AC08B5BC36FC528F804BB64123FCF0CC1382AD'
                  '77ED35896939335A2F0DD1AB395B9F2DC027B80B3B1AB4023'
                  '3EAB4B04F1DE16A8B7EF607CE829F8D96D6FF5EF2216D55A8'
                  '&appkey=1d8b6e7d45233436&autoplay_card=0&build=54'
                  '52100&channel=baidu&column=2&device_name=MI%202A&'
                  'device_type=0&flush=0&fnval=16&fnver=0&force_host'
                  '=0&fourk=0&idx=0&login_event=1&mobi_app=android&n'
                  'etwork=wifi&open_event=cold&platform=android&pull'
                  '=true&qn=32&recsys_mode=0&statistics=%7B%22abtest'
                  '%22%3A%22%22%2C%22platform%22%3A3%2C%22version%22'
                  '%3A%225.45.2%22%2C%22appId%22%3A1%7D&ts=156531037'
                  '4&sign=6998923c0eb6fabc515baa6e4f8d4d9f%20']
    def parse(self, response):
        Info_list = json.loads(response.text)["data"]["items"]

        for i in Info_list:
            if i["card_goto"] == "av":
                item = BilibiliItem()
                item["param"] = i["param"]
                item["cover"] = i["cover"]
                item["title"] = i["title"]
                item["cover_left_text_1"] = i["cover_left_text_1"]
                item["cover_left_text_2"] = i["cover_left_text_2"]
                item["up_name"] = i["args"]["up_name"]
                try:
                    item["rname"] = i["args"]["rname"]
                except:
                    item["rname"] = ''
                try:
                    item["tname"] = i["args"]["tname"]
                except:
                    item["tname"] = ''
                yield item
            else:
                print("广告"*50)

        j = 75
        if j<85:
            print("新的URL"*30)
            urllast= str(j) + '&sign=6998923c0eb6fabc515baa6e4f8d4d9f%20'
            j += 1
            yield scrapy.Request(self.baseurl+urllast,callback=self.parse,dont_filter=True)

# import requests
# from lxml import etree
# import json
# import xml.dom.minidom
# url = 'http://app.bilibili.com/x/v2/feed/index?ad_extra=2F160688A991F9E874393027277D85422F5D26B73238F495719706F7F69C8485FF36E2FDEDDDDA0C080EB4FEFCE5AEC82C9AFC0569F4FCF3DD3E33EC93D7E653857B7E4DEAD038A38A1042A0ED26DA723A0D0BA60C241B4B54420DA0BE2E10BD3A948E2B5F44657D491C165F1FFD9BF24C7914418063E8B8B713592526A493762B0B216CEFC0611FE5A9A5F217A068415184F39FB718A6712C03E3996F14ADCD1EE4BAC0950749E32692415DCC6855D387BEF95B201E7B4E29E50845F8F96931671355E3590A8161400DDFE726EB1B550ADDC2B4B390090A5E229EE0C9112ACF6A00E69A26619B3AE3B9DFD7BEBE2B50493B96B3280D0C468DC89B51FFE30DFC86F21EA4CDF077BCE10112D53841024DFFE0C233C2E896526C7FEC6288ED8C002F10D7AEC376D4D4531063162F1B8534734AA0DB16BC4F608322416A3D3AA59E2BB9CEBCCCAF2459D1091A61C707E281D025B94106853EC2ECA7037C868733FA2EA9782C92420975FAF8E4400036CFB5DB43F9796C19F0868E5F312984FF68B37BCD850EA1AA2362DA2EA529C1E2B141D8043BC7B411656890A31F162AEC8DB7028F2EECA6F4979856853F3DB05A9F985D4CCFD6F417FB61C7968526BF12CEEB966E686AA7F84BE7B3760FC7B5225BC30FDAFE251EB06FF088BBEB63EF430E16760AED3AB47E11C8283633E535C45EF7F02CF04134E4AE3BEF462DBB7510CD3AB9E72C56C33CAEC6426C22C17EE568BF84391D4CECA53B95BA2AD05C52ACF97CD8CE6E6C0BE41720286A328EAE9B599B03EE97A0C4EE70D815841C929031035FDCD5AE92D5775C1E2172E15A61ACE4882D3F1894B8103B231D97E507CDBDB7627C8E44A5FA1A2B6455D2EE2D2AE360A15AD74B80B5D1AAD3E8C8177A187D011B9B653330F63B70EEBE1E9F8673ACB8B4C71DE0BA11FBE45B2A0C14980BA9A2D53BE4CE8C0B8E0CC7E262C351EE1178C074333B2EB2A1622760FC466C0ADD3CE6&appkey=1d8b6e7d45233436&autoplay_card=2&banner_hash=1859392622370587906&build=5452100&channel=baidu&column=3&device_name=MI%202A&device_type=0&flush=0&fnval=16&fnver=0&force_host=0&fourk=0&idx=1565338597&login_event=0&mobi_app=android&network=wifi&open_event=&platform=android&pull=false&qn=32&recsys_mode=0&statistics=%7B%22abtest%22%3A%22507_801%22%2C%22platform%22%3A3%2C%22version%22%3A%225.45.2%22%2C%22appId%22%3A1%7D&ts=1565338883&sign=0d0b7a6fff8621ba6eedcab2666a70cc'
# headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
# res = requests.get(url=url,headers=headers)
# res.encoding = "utf-8"
# html = res.text
# html = json.loads(html)
# f = open('弹幕文字.txt','a',encoding="utf-8")
#
# for i in html["data"]["items"]:
#     if i["card_goto"]=="av":
#         print("视频标题：",i["title"])
#         print("up主名称：",i["args"]["up_name"])
#         print("视频编号：",'av'+str(i["args"]["aid"]))
#         print("弹幕编号：",str(i["player_args"]["cid"]))
#         cid_xml = 'http://comment.bilibili.com/'+str(i["player_args"]["cid"])+'.xml'
#         res_cid = requests.get(url=cid_xml)
#         res_cid.encoding = "utf-8"
#         cid_html = res_cid.content
#         parse_cid_html = etree.HTML(cid_html)
#         comment_list = parse_cid_html.xpath('//d/text()')
#         commentid_list = parse_cid_html.xpath('//d/@p')
#         f.write('视频标题：'+i["title"]+'\n'+'up主名称：'+i["args"]["up_name"]+'\n'+'弹幕数量：'+str(len(comment_list))+'条'+'\n\n')
#         for r in range(len(comment_list)):
#             f.write(commentid_list[r][0:10]+':'+comment_list[r]+'\n\n')
# f.close()


