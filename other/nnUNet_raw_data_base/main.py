# '''
# Author: yiyanghu huyiyang@mediway.com
# Date: 2022-12-08 11:39:12
# LastEditors: yiyanghu huyiyang@mediway.com
# LastEditTime: 2022-12-08 11:40:41
# FilePath: \nnUNet-master\other\nnUNet_raw_data_base\main.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# '''
import os


base = os.environ['nnUNet_raw_data_base']
base1 = os.environ.get['nnUNet_raw_data_base']

print(base, base1)
