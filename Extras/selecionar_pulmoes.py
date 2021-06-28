# -*- coding: utf-8 -*-
"""
Selecionar um CT aleatóriamente e desenhar a região do pulmão nos mesmos
"""

import cv2
import nibabel as nib
import numpy as np
import os
import pickle

# font
FONT = cv2.FONT_HERSHEY_SIMPLEX

def normImage(image):
    image-=np.min(image)
    image = (image/np.max(image))*255
    return image.astype('uint8')

selPts = []
def selPoint(event, x, y, flags, param):
    # grab references to the global variables
    global selPts
    # Selecionar os pontos
    if event == cv2.EVENT_LBUTTONDOWN:
        selPts.append([x, y])        
    

#
ct0_path = "E:\Lucas_Documentos\Doutorado\materias_UFES_doutorado\DeepLearning\TrabalhoFinal\COVID19_1110\studies\CT-0"
ct1_path = "E:\Lucas_Documentos\Doutorado\materias_UFES_doutorado\DeepLearning\TrabalhoFinal\COVID19_1110\studies\CT-1"
ct2_path = "E:\Lucas_Documentos\Doutorado\materias_UFES_doutorado\DeepLearning\TrabalhoFinal\COVID19_1110\studies\CT-2"
#
masks_path = "E:\Lucas_Documentos\Doutorado\materias_UFES_doutorado\DeepLearning\TrabalhoFinal\COVID19_1110\masks"
# 
mask_files = os.listdir(masks_path)
#
ct0_files = os.listdir(ct0_path)
ct1_files = os.listdir(ct1_path)
ct2_files = os.listdir(ct2_path)



file_idx = 9

#for file in ct2_files:
full_image_path = os.path.join(ct2_path, ct2_files[file_idx]) 
ct_image = nib.load(full_image_path)

print(ct2_files[file_idx])

n_ponts = 0
img_pts = []
for scn in range(ct_image.dataobj.shape[-1]):
    print("\nFrame",str(scn))
    orig_img = ct_image.dataobj[:,:,scn].copy()
    norm_img = normImage(orig_img) 
    backup_img = norm_img.copy()       
    # load the image, clone it, and setup the mouse callback function
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", selPoint)
    # keep looping until the 'q' key is pressed
    mask_lungs = []
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", norm_img)
        key = cv2.waitKey(1) & 0xFF
        if len(selPts)>n_ponts:
            cv2.circle(norm_img,(selPts[-1][0],selPts[-1][1]), 5, (0,0,255), -1)
            
            if len(selPts)>1:
                cv2.line(norm_img,(selPts[-2][0],selPts[-2][1]),
                                  (selPts[-1][0],selPts[-1][1]),(0,0,255),2)
        # if the 'q' key is pressed, break from the loop
        if key == ord("n"):
            mask_lungs.append(selPts.copy())
            selPts = []
            print('N ROIs:',len(mask_lungs))
            
        # if the 'q' key is pressed, break from the loop
        if key == ord("q"):
            img_pts.append(mask_lungs.copy())
            print("Frame", scn, "ROIS do frame:", len(mask_lungs))
            break
    cv2.destroyAllWindows()
    
    
save_masks = []
for i,pts in enumerate(img_pts):   
    blank_img = np.zeros((512,512),dtype='uint8')
    for mask in pts:
        blank_img = cv2.fillPoly(blank_img, [np.int32(mask)], 1)
    save_masks.append((blank_img).astype('bool'))
    while True:
        # display the image and wait for a keypress
        orig_img = ct_image.dataobj[:,:,i].copy()
        norm_img = normImage(orig_img) 
        show_img = (norm_img*blank_img).astype('uint8')
        cv2.imshow("blank_img", show_img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    
if len(save_masks) == ct_image.dataobj.shape[-1]:
    with open(os.path.join('lungs_masks', ct2_files[file_idx]+'.pickle'), 'wb') as handle:
        pickle.dump(save_masks, handle, protocol=pickle.HIGHEST_PROTOCOL)



# lungs_masks
    
    