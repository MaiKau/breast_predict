from keras.models import load_model
import cv2
import numpy as np
from keras import optimizers
import glob

model= load_model('Binary_Breast_20210510120454.h5')
model.compile(loss='binary_crossentropy', optimizer=optimizers.Adam(lr=0.01,beta_1=0.9, beta_2=0.999, amsgrad=False), metrics=['accuracy'])
model_summary=model.summary()


def path_list(ind_pic_path,dirpathpatten):
    
      #各圖片路徑陣列
#     ind_pic_path=['G:\\train_image\\other_path_Breast\\0_img1.bmp', 'G:\\train_image\\other_path_Breast\\0_img10.bmp', 'G:\\train_image\\other_path_Breast\\0_img2.bmp', 'G:\\train_image\\other_path_Breast\\0_img3.bmp', 'G:\\train_image\\other_path_Breast\\0_img4.bmp', 'G:\\train_image\\other_path_Breast\\0_img5.bmp', 'G:\\train_image\\other_path_Breast\\0_img6.bmp', 'G:\\train_image\\other_path_Breast\\0_img7.bmp', 'G:\\train_image\\other_path_Breast\\0_img8.bmp', 'G:\\train_image\\other_path_Breast\\0_img9.bmp', 'G:\\train_image\\other_path_Breast\\1_img1.bmp', 'G:\\train_image\\other_path_Breast\\1_img10.bmp', 'G:\\train_image\\other_path_Breast\\1_img2.bmp', 'G:\\train_image\\other_path_Breast\\1_img3.bmp', 'G:\\train_image\\other_path_Breast\\1_img4.bmp', 'G:\\train_image\\other_path_Breast\\1_img5.bmp', 'G:\\train_image\\other_path_Breast\\1_img6.bmp', 'G:\\train_image\\other_path_Breast\\1_img7.bmp', 'G:\\train_image\\other_path_Breast\\1_img8.bmp', 'G:\\train_image\\other_path_Breast\\1_img9.bmp']
      #資料夾陣列
#     dirpathpatten="G:\train_image\other_path_Breast\*.bmp"
    try:
        floder_result=glob.glob(dirpathpatten)
        for path in floder_result:
            ind_pic_path.append(path)
    except:
        print("not found folder")
    
    print(ind_pic_path) #各圖片路徑陣列    
    return ind_pic_path


def predict(ind_pic_path):
    ind_pic_path_num=len(ind_pic_path)
    all_sult=[]
    i=0
    for pic in ind_pic_path:
        if i<ind_pic_path_num:
            img = cv2.imread(ind_pic_path[i])
            img = cv2.resize(img,(224,224))
            img = np.reshape(img,[1,224,224,3])
            img=img/255.0
            predict = model.predict(img)
            predict_sult = np.argmax(predict) #取大者
            all_sult.append(ind_pic_path[i])
            all_sult.append(predict_sult)
            all_sult.append(predict[0,1]) #機率值 type(ndarray)
            i+=1   
    print(all_sult) #結果[path,0/1,1的機率]
    return(all_sult)