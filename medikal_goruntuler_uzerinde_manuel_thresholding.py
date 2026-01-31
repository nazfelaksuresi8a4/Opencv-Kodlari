import matplotlib.pyplot as plt 
import numpy as np 
import cv2 as cv 
import nibabel as nib 

def getCalibrationLineCoordinates(matlike):
    if isinstance(matlike,np.ndarray):
        shape = (matlike.shape)
        
        if len(shape) == 2:
            x,y = shape
            x,y = x // 2, y // 2

            return (x,y)
        
        else:
            pass
    
    else:
        pass


def toMatrix(path,ptype):
    result_matlike = None
    if ptype == 'img':
        pass

    elif ptype == 'nimage':
        nib_object = nib.load(path).get_fdata()

        h,w,d = None,None,None
        shape = nib_object.shape

        if len(shape) == 3:
            h,w,d = shape

        else:
            print('4D ve 3D görseller desteklenmemektedir')

        hwd_arr = [h,w,d]

        states = ['.' for s in hwd_arr if s is not None]
        count = states.count('.')

        if count == 3:
            maximum_slice = hwd_arr.copy().pop()
            x,y = 0,maximum_slice - 1

            slice_input = str(input(f'kaçıncı sliceı göstersin {x} ile {y} arasında: '))

            if slice_input.isdigit() == True:
                flag = 0

                if int(slice_input) <= y:
                    try:
                        flag = 1
                        nii_matrix = nib_object[:,:,int(slice_input)]

                    except Exception as e0:
                        flag = 0
                        print(f'Hata: {e0}')

                    finally:
                        if flag == 1:
                            calibarate_input = str(input('Kalibrasyon çizgisi çizilsinmi? evet-hayır: '))

                            if calibarate_input.lower() == 'evet':
                                if nii_matrix is not None:
                                    calibartionMetadatas = getCalibrationLineCoordinates(nii_matrix)

                                    if calibartionMetadatas is not None:
                                        if isinstance(calibartionMetadatas,tuple):
                                            if len(calibartionMetadatas) == 2:
                                                x,y = calibartionMetadatas
                                                yQ,xQ = nii_matrix.shape    

                                                line_y = cv.line(nii_matrix.copy(),(y,yQ),(y,0),(1.0, 1.0, 1.0),thickness=2)
                                                result_matlike = cv.line(line_y,(xQ,x),(0,x),(1.0, 1.0, 1.0),thickness=2)

                                else:
                                    print('e0')

                            elif calibarate_input.lower() == 'hayır':
                                result_matlike = nii_matrix
                        
                        else:
                            print('e2')

                else:
                    print('e3')
            
            else:
                print('e4')

        else:
            print('not passed',count)
        
        if result_matlike is not None:
            if len(result_matlike.shape) == 2:
                plt.imshow(result_matlike // 255 ,cmap='gray',vmin=0,vmax=1)
                plt.show()
            
            else:
                print('4D ve 3D görseller desteklenmemektedir' + '\n' + 'Görsel boyutu: ' + str(result_matlike.shape))
        
        else:
            print('Çıktı matrisi bulunamadı')

toMatrix(r"C:\Users\alper\Desktop\testing_zone\32-Flair.nii",'nimage')            
