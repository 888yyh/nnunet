'''
Author: yiyanghu huyiyang@mediway.com
Date: 2022-12-09 17:16:08
LastEditors: yiyanghu huyiyang@mediway.com
LastEditTime: 2022-12-09 18:34:25
FilePath: \nnUNet-master\other\getoverlap.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
import cv2


path = r'E:\nzl\nnunetbrats2020\nnUNet-master\nnUNet_raw_data_base\nnUNet_raw_data\Task005_Prostate\imagesTs\prostate_03_0000.nii.gz'
spath = r'E:\nzl\nnunetbrats2020\nnUNet-master\output\prostate1\prostate_03.nii.gz'

img = sitk.ReadImage(path) 
arr = sitk.GetArrayFromImage(img)

seg = sitk.ReadImage(spath)
sarr = sitk.GetArrayFromImage(seg)

img255 = sitk.Cast(sitk.RescaleIntensity(img), sitk.sitkUInt8)
arr255 = sitk.GetArrayFromImage(img255)
# sitk.Show(img255)
# sitk.Show(sitk.LabelOverlay(img255, seg))

lap = sitk.LabelOverlay(img255, seg)
laparr = sitk.GetArrayFromImage(lap)

for i in range(arr.shape[0]):
    
    max = np.max(sarr[i])
    
    if max != 0:
    

        plt.figure()
        plt.subplot(1,3,1)
        plt.imshow(arr255[i])

        plt.subplot(1,3,2)
        b = sarr[i]
        plt.imshow(sarr[i])

        plt.subplot(1, 3, 3)
        plt.imshow(laparr[i])
        a = sitk.GetImageFromArray(laparr[i])
        plt.savefig('1.png')
        cv2.imwrite('lap.png', laparr[i])

        plt.show()

