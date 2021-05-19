---環境套件---
Python                             3.7.1
Keras                              2.2.4       
Keras-Applications                 1.0.8       
opencv-python                      4.5.1.48
numpy                              1.16.4
glob2                              0.7

---檔案說明---

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


---使用流程---

1.開啟/掛載 h5py.py檔

2.載入 Binary_Breast_20210510120454.h5

3.給定欲預測圖片路徑 ind_pic_path 或 給定欲預測圖片資料夾路徑 dirpathpatten

4.path_list(ind_pic_path,dirpathpatten) return結果為 指定的圖片清單

5.predict(ind_pic_path) return結果為 預測結果 