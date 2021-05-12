other_path_Breast資料夾：測試用照片(10張有病 1_* ; 10張沒病 0_*)

Binary_Breast_20210510024822.h5.ipynb：jupter程式檔

Binary_Breast_20210510120454.h5 ： model 檔

h5py.py：包h5的py檔

def_test.ipynb：副程式測試用，無須理會

---變數說明---

[ ind_pic_path：Input圖片實體路徑 ]

[ dirpathpatten：Input整個圖片資料夾的實體路徑 ]

[ all_sult：Output結果{path,0/1,1的機率} ]


---input 範例樣式---
ind_pic_path = ['G:\\train_image\\other_path_Breast\\0_img1.bmp', 'G:\\train_image\\other_path_Breast\\0_img10.bmp', 'G:\\train_image\\other_path_Breast\\0_img2.bmp', 'G:\\train_image\\other_path_Breast\\0_img3.bmp', 'G:\\train_image\\other_path_Breast\\0_img4.bmp', 'G:\\train_image\\other_path_Breast\\0_img5.bmp', 'G:\\train_image\\other_path_Breast\\0_img6.bmp', 'G:\\train_image\\other_path_Breast\\0_img7.bmp', 'G:\\train_image\\other_path_Breast\\0_img8.bmp', 'G:\\train_image\\other_path_Breast\\0_img9.bmp', 'G:\\train_image\\other_path_Breast\\1_img1.bmp', 'G:\\train_image\\other_path_Breast\\1_img10.bmp', 'G:\\train_image\\other_path_Breast\\1_img2.bmp', 'G:\\train_image\\other_path_Breast\\1_img3.bmp', 'G:\\train_image\\other_path_Breast\\1_img4.bmp', 'G:\\train_image\\other_path_Breast\\1_img5.bmp', 'G:\\train_image\\other_path_Breast\\1_img6.bmp', 'G:\\train_image\\other_path_Breast\\1_img7.bmp', 'G:\\train_image\\other_path_Breast\\1_img8.bmp', 'G:\\train_image\\other_path_Breast\\1_img9.bmp']
dirpathpatten = r"G:\train_image\other_path_Breast\*.bmp"