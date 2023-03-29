'''
Author: yiyanghu huyiyang@mediway.com
Date: 2022-12-09 17:01:30
LastEditors: yiyanghu huyiyang@mediway.com
LastEditTime: 2022-12-15 10:47:22
FilePath: \nnUNet-master\other\nnUNet_raw_data_base\analyselabel.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from email.base64mime import body_encode
import SimpleITK as sitk
import numpy as np


# path = r'E:\nzl\nnunetbrats2020\nnUNet-master\output\prostate1\prostate_03.nii.gz'
path = r'E:\nzl\vnet_code\vnet_code\output\chongdie_VNet_woDS\hgg_BraTS19_CBICA_ANV_1.nii.gz'
label = sitk.ReadImage(path)
lbarr = sitk.GetArrayFromImage(label)
uni = np.unique(lbarr)
label1 = np.sum(lbarr==1)
label2 = np.sum(lbarr==2)
 
border = sitk.LabelContour(label)
lbarr1 = sitk.GetArrayFromImage(border)
uni1 = np.unique(lbarr1)
label11 = np.sum(lbarr1==1)
label21 = np.sum(lbarr1==2)

print(uni, uni1)