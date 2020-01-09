from AipOcr import client

# 链接
# http://ai.baidu.com/ai-doc/OCR/3k3h7yeqa#%E9%80%9A%E7%94%A8%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB


""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('H:/Python/PycharmProjects/baidu-ocr/pic/2017.jpg')

# """ 调用通用文字识别, 图片参数为本地图片 """
# res_general = client.basicGeneral(image)
# print(res_general)
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# res_with_para = client.basicGeneral(image, options)
# print(res_with_para)
#
# url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1578462533938&di=962e22fc98b0b546928b4c6414f80ca6&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20180105%2Fa0720068bea9436d92fd76b198fd40da.jpeg"
#
# """ 调用通用文字识别, 图片参数为远程url图片 """
# res_general_url = client.basicGeneralUrl(url)
# print(res_general_url)

# """ 调用通用文字识别（高精度版） """
# res_accurate = client.basicAccurate(image)
# print(res_accurate)

""" 调用车牌识别 """
image_car = get_file_content('H:/Python/PycharmProjects/baidu-ocr/pic/car.jpg')
res_car = client.licensePlate(image_car)
print(res_car)
