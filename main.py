# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:20:23 2020

@author: Eren
"""
import tkinter as tk
import tkinter.filedialog
import cv2
from skimage import io
from skimage import exposure
from skimage.morphology import disk
import numpy as np
from matplotlib import pyplot as plt
from skimage import filters, transform, morphology, measure, color, segmentation
from skimage.morphology import extrema

window = tk.Tk()
window.title("Image Processing Proje 1")
window.geometry("300x225")
label = tk.Label(window, text="Hoşgeldiniz, \nLütfen işlem yapmak istediğiniz dosya türünü seçiniz")
label.pack()
def imageButton():
    ##Filtreler olacak 10 adet
    ##histogram görüntü ve eşitlemesi
    ##5 farklı uzaysal dönüşüm
    #yoğunluk dönüşüm işlemleri (inputlu)
    #morfolojik işlemler 10 adet
    window.destroy()
    imageTkinter = tk.Tk()

    testPath=[]
    
    imageTkinter.title("Image Proccessing Proje 1 Image")
    imageTkinter.geometry("710x500")
    tk.Label(imageTkinter, text="Uygulanacak filtreleri seciniz.").place(x=10, y=25)
    filterVar = tk.IntVar()
    filterNames = ["GaussianBlur","Canny","Roberts","Sato","Scharr","Sobel","Unsharp Mask","Median","Prewitt","Rank(Model)"]
    for i in range(10):
        if(i < 5):
            tk.Radiobutton(imageTkinter, text=filterNames[i], variable=filterVar, value=i+1).place(x=200+(i*100), y =10)
        else:
            tk.Radiobutton(imageTkinter, text=filterNames[i], variable=filterVar, value=i+1).place(x=200+((i-5)*100), y =40)

    
    tk.Label(imageTkinter, text="Histogram.").place(x=10, y = 70)
    
    hEsitleme = tk.IntVar()
    hGrafik = tk.IntVar()
    tk.Checkbutton(imageTkinter, text="Histogram Esitleme     ", variable=hEsitleme, onvalue=1).place(x = 200 ,y = 70)    
    tk.Checkbutton(imageTkinter, text="Histogram grafigi cikar", variable=hGrafik, onvalue=1).place(x = 380, y = 70)    
    
    
    uzaysalVars = []
    uzaysalVarsInputs = []
    for i in range(5):
        uzaysalVars.append(tk.IntVar())
        uzaysalVarsInputs.append(tk.StringVar())
    
    tk.Label(imageTkinter, text="Rescale oranini giriniz.").place(x=10, y = 100)
    tk.Checkbutton(imageTkinter, text="Uygula", variable=uzaysalVars[0], onvalue=1).place(x=200, y =100)
    tk.Entry(imageTkinter, textvariable=uzaysalVarsInputs[0]).place(x = 270, y=100)
    
    tk.Label(imageTkinter, text="Oranlari korumadan downscale.").place(x=10, y = 140)
    tk.Checkbutton(imageTkinter, text="Uygula", variable=uzaysalVars[1], onvalue=1).place(x=200, y =140)
    tk.Label(imageTkinter, text="x ekseni").place(x=270, y = 130)
    tk.Label(imageTkinter, text="y ekseni").place(x=270, y = 150)
    tk.Entry(imageTkinter, textvariable=uzaysalVarsInputs[1]).place(x=330, y=130)
    tk.Entry(imageTkinter, textvariable=uzaysalVarsInputs[2]).place(x=330, y=150)
    tk.Label(imageTkinter, text="kat kucult. (with anti aliasing)").place(x=470, y = 140)


    tk.Label(imageTkinter, text="Swirl.").place(x=10, y = 180)
    tk.Checkbutton(imageTkinter, text="Uygula", variable=uzaysalVars[2], onvalue=1).place(x=200, y =180)
    
    tk.Label(imageTkinter, text="Rotate.").place(x=10, y = 210)
    tk.Checkbutton(imageTkinter, text="Uygula", variable=uzaysalVars[3], onvalue=1).place(x=200, y =210)
    tk.Entry(imageTkinter, textvariable=uzaysalVarsInputs[3]).place(x=270, y=210)
    tk.Label(imageTkinter, text="derece cevir.").place(x=370, y = 210)

    tk.Label(imageTkinter, text="Ayna Goruntusunu al.").place(x=10, y = 240)
    tk.Checkbutton(imageTkinter, text="Uygula", variable=uzaysalVars[4], onvalue=1).place(x=200, y =240)
    
    tk.Label(imageTkinter, text="Rescale Intensity\n (Yogunluk donusumu)").place(x=10, y = 270)
    
    yogunlukVars = []
    for i in range(6):
        if(i < 2):
            yogunlukVars.append(tk.IntVar())
        else:
            yogunlukVars.append(tk.StringVar())
    
    tk.Checkbutton(imageTkinter, text="Uygula Input Sinirlari ", variable=yogunlukVars[0], onvalue=1).place(x=200, y =270 )
    tk.Checkbutton(imageTkinter, text="Uygula Output Sinirlari", variable=yogunlukVars[1], onvalue=1).place(x=200, y =290 )
    tk.Entry(imageTkinter, textvariable=yogunlukVars[2]).place(x=370, y=270)
    tk.Entry(imageTkinter, textvariable=yogunlukVars[3]).place(x=490, y=270)
    tk.Entry(imageTkinter, textvariable=yogunlukVars[4]).place(x=370, y=290)
    tk.Entry(imageTkinter, textvariable=yogunlukVars[5]).place(x=490, y=290)

    tk.Label(imageTkinter, text="Uygulanacak morfolojik \nfiltereleri seciniz.").place(x=10, y=330)
    morfVar = tk.IntVar()
    morfNames = ["Area Closing", "Area Opening", "Erosion", "Dilation", "Opening", "Closing", "White Tophat", "Black Tophat","Extrema(High)","Extrema(Local)"]
    for i in range(10):
        if(i < 5):
            tk.Radiobutton(imageTkinter, text=morfNames[i], variable=morfVar, value=i+1).place(x=200+(i*100), y =320)
        else:
            tk.Radiobutton(imageTkinter, text=morfNames[i], variable=morfVar, value=i+1).place(x=200+((i-5)*100), y =350)
  
    def buttonSave(arg):
        
        copy = arg[1]
        imageTemp = arg[2]
        filterTry  = filterVar.get()
        if(filterTry == 1):
            copy = cv2.GaussianBlur(copy, (5,5), 0)
        elif(filterTry == 2):
            copy = cv2.Canny(copy, 100, 150)
        elif(filterTry == 3):
            copy = filters.roberts(imageTemp)
        elif(filterTry == 4):
            copy = filters.sato(imageTemp)
        elif(filterTry == 5):
            copy = filters.scharr(imageTemp)
        elif(filterTry == 6):
            copy = filters.sobel(imageTemp)
        elif(filterTry == 7):
            copy = filters.unsharp_mask(copy, radius=30, amount=3)
        elif(filterTry == 8):
            #copy = filters.median(imageTemp, disk(5))
            b, g, r = cv2.split(copy)
            b = filters.median(b, disk(5))
            g = filters.median(g, disk(5))
            r = filters.median(r, disk(5))
            copy = cv2.merge((b,g,r))
        elif(filterTry == 9):
            copy = filters.prewitt(imageTemp)
        elif(filterTry == 10):
            copy = filters.rank.modal(imageTemp, disk(5))
        flag = 0
        if(np.ndim(copy) == 2 ):
            flag = 0
        else:
            flag = 1
        
        
        if(hEsitleme.get() or hGrafik.get()):
            if(flag):
                copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY) 
            if(hGrafik.get()):
                plt.hist(copy.ravel(),256,[0,256])
                plt.show()
            if(hEsitleme.get()):
                copy = cv2.equalizeHist(copy)
        
        if(uzaysalVars[0].get()):
            reScaleRatio = float(uzaysalVarsInputs[0].get())
            if(np.ndim(copy) == 3):
                b, g, r = cv2.split(copy)
                b = transform.rescale(b, reScaleRatio)
                g = transform.rescale(g, reScaleRatio)
                r = transform.rescale(r, reScaleRatio)
                copy = cv2.merge((b,g,r))
            else:
                copy = transform.rescale(copy, reScaleRatio)
                
        if(uzaysalVars[1].get()):
            resizeY = float(uzaysalVarsInputs[1].get())
            resizeX = float(uzaysalVarsInputs[2].get())
            if(np.ndim(copy) == 3):
                b, g, r = cv2.split(copy)
                b = transform.resize(b, (b.shape[0] // resizeX, b.shape[1]//resizeY), anti_aliasing=True)
                g = transform.resize(g, (g.shape[0] // resizeX, g.shape[1]//resizeY), anti_aliasing=True)
                r = transform.resize(r, (r.shape[0] // resizeX, r.shape[1]//resizeY), anti_aliasing=True)
                copy = cv2.merge((b,g,r))
            else:
                copy = transform.resize(copy, (copy.shape[0] // resizeX, copy.shape[1]//resizeY), anti_aliasing=True)
        if(uzaysalVars[2].get()):
            copy= transform.swirl(copy, rotation=0, strength=10, radius=120)
        if(uzaysalVars[3].get()):
            copy= transform.rotate(copy, int(uzaysalVarsInputs[3].get()), resize=True)
        if(uzaysalVars[4].get()):
            copy= copy[:, ::-1]
            
        if(yogunlukVars[0].get() or yogunlukVars[1].get()):
            if(yogunlukVars[0].get()):
                startINX = int(yogunlukVars[2].get())
                finishINX = int(yogunlukVars[3].get())
                copy = exposure.rescale_intensity(copy, in_range=(startINX, finishINX))
            if(yogunlukVars[1].get()):
                startOUTX = int(yogunlukVars[4].get())
                finishOUTX = int(yogunlukVars[5].get())
                copy = exposure.rescale_intensity(copy, out_range=(startOUTX, finishOUTX))

        morfoTry  = morfVar.get()
        morfoGirisN = 0
        if(np.ndim(copy) == 3):
            morfoGirisN = 1
        
        if(morfoTry == 1):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.area_closing(b, 128, 9)
                g =  morphology.area_closing(g, 128, 9)
                r =  morphology.area_closing(r, 128, 9)
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.area_closing(copy)
        elif(morfoTry == 2):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.area_opening(b, 128, 9)
                g =  morphology.area_opening(g, 128, 9)
                r =  morphology.area_opening(r, 128, 9)
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.area_opening(copy)
        elif(morfoTry == 3):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.erosion(b, disk(6))
                g =  morphology.erosion(g, disk(6))
                r =  morphology.erosion(r, disk(6))
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.erosion(copy, disk(6))
        elif(morfoTry == 4):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.dilation(b, disk(6))
                g =  morphology.dilation(g, disk(6))
                r =  morphology.dilation(r, disk(6))
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.dilation(copy, disk(6))
        elif(morfoTry == 5):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.opening(b, disk(6))
                g =  morphology.opening(g, disk(6))
                r =  morphology.opening(r, disk(6))
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.opening(copy, disk(6))
        elif(morfoTry == 6):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.closing(b, disk(6))
                g =  morphology.opening(g, disk(6))
                r =  morphology.opening(r, disk(6))
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.opening(copy, disk(6))
        elif(morfoTry == 7):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.white_tophat(b, disk(6))
                g =  morphology.white_tophat(g, disk(6))
                r =  morphology.white_tophat(r, disk(6))
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.white_tophat(copy, disk(6))
        elif(morfoTry == 8):
            if(morfoGirisN):
                b, g, r = cv2.split(copy)
                b =  morphology.black_tophat(b, disk(6))
                g =  morphology.black_tophat(g, disk(6))
                r =  morphology.black_tophat(r, disk(6))
                copy = cv2.merge((b,g,r))
            else:
                copy = morphology.black_tophat(copy, disk(6))
        elif(morfoTry == 10):
            if(morfoGirisN):
                    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)

            copy = exposure.rescale_intensity(copy)
            local_maxima = extrema.local_maxima(copy)
            label_maxima = measure.label(local_maxima)
            copy = color.label2rgb(label_maxima, copy, alpha=0.7, bg_label=0, bg_color=None, colors=[(1, 0, 0)])
        elif(morfoTry == 9):
            if(morfoGirisN):
                    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
            copy = exposure.rescale_intensity(copy)
            h = 0.05
            h_maxima = extrema.h_maxima(copy, h)
            label_h_maxima = measure.label(h_maxima)
            copy = color.label2rgb(label_h_maxima, copy, alpha=0.7, bg_label=0, bg_color=None, colors=[(1, 0, 0)])
        arg[1] = copy
        arg[2] = imageTemp
        cv2.imshow("org", copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """
        hsl = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if hsl is None:
            return
        sv = copy.copy()
        sv.close()
        """
    
    def resimSec(path):
        newPath =tk.filedialog.askopenfilename(filetypes=[("Image File",'.png'),("Image File", ".jpg")])
        filterVar.set(0)
        morfVar.set(0)
        if(len(path) > 0):
            path[0] = newPath
            path[1] = cv2.imread(path[0])
            path[2] = cv2.imread(path[0], 0)
        else:
            path.append(newPath)
            path.append(cv2.imread(path[0]))
            path.append(cv2.imread(path[0], 0))
    
    def resimKaydet(arg):
        if(len(arg) == 0) : 
            return
        uzantiBas = arg[0].rindex(".")
        if(arg[1].dtype == np.float64):
            arg[1] = exposure.rescale_intensity(arg[1], in_range=(0,1), out_range=(0, 255)).astype(np.uint8)
        if(np.ndim(arg[1]) == 3):
            writePath = arg[0][:uzantiBas] + "-edited-3D" + arg[0][uzantiBas:]
            cv2.imwrite(writePath, arg[1])
            """
            writePath = arg[0][:uzantiBas] + "-edited-2D" + arg[0][uzantiBas:]
            cv2.imwrite(writePath, arg[2])
            """
        else:
            writePath = arg[0][:uzantiBas] + "-edited-2D" + arg[0][uzantiBas:]
            cv2.imwrite(writePath, arg[1])    
    
    resimSec(testPath)
    tk.Button(imageTkinter, text="Resim Seç", command=lambda: resimSec(testPath)).place(x=30, y=420)
    tk.Button(imageTkinter, text="Göster", command=lambda: buttonSave(testPath)).place(x=330, y=420)
    tk.Button(imageTkinter, text="Kaydet", command=lambda: resimKaydet(testPath)).place(x=600, y=420)
    

    imageTkinter.mainloop()


def videoButton():
    def camera():
        cap = cv2.VideoCapture(0)
        while(True):
            _, frame = cap.read()
            test =  cv2.Canny(frame, 100, 150)
        
            cv2.imshow('Source', frame)
            cv2.imshow('Edges', test)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    def dosya():
        newPath =tk.filedialog.askopenfilename(filetypes=[("Video File",'.mp4'),("Video File", ".avi")])
        cap = cv2.VideoCapture(newPath)
        while(True):
            _, frame = cap.read()
            test =  cv2.Canny(frame, 100, 150)
        
            cv2.imshow('Source', frame)
            cv2.imshow('Edges', test)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    
    
    window.destroy()
    videoTkinter = tk.Tk()
    videoTkinter.title("Image Proccessing Proje 1 Video")
    videoTkinter.geometry("330x110")
    tk.Label(videoTkinter, text="Kamerayı kullanmak için tıklayınız    =>").place(x=20, y = 20)
    tk.Label(videoTkinter, text="Dosyadan video açmak için tıklayınız  =>").place(x=20, y = 70)
    tk.Button(videoTkinter, text="Kamera", command=camera).place(x=250, y=20)
    tk.Button(videoTkinter, text="Dosya ", command=dosya).place(x=250, y=70)
    videoTkinter.mainloop()


def socialMediaFilter():
    newPath =tk.filedialog.askopenfilename(filetypes=[("Image File",'.png'),("Image File", ".jpg")])
    filterEnd = cv2.imread(newPath)
    filterEnd = cv2.GaussianBlur(filterEnd, (5,5), 0)
    
    b, g, r = cv2.split(filterEnd)
    b =  morphology.erosion(b, disk(6))
    g =  morphology.erosion(g, disk(6))
    r =  morphology.erosion(r, disk(6))
    filterEnd = cv2.merge((b,g,r))
    
    filterEnd = filterEnd[:, ::-1]

    filterEnd = transform.rotate(filterEnd, 180, resize=False)
    
    cv2.imshow("Social Media Filter", filterEnd)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def activeContourTest():
    def test(img, argCircle):
        image_gray = color.rgb2gray(image)

        def image_show(image, nrows=1, ncols=1, cmap='gray'):
            fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
            ax.imshow(image, cmap='gray')
            ax.axis('off')
            return fig, ax
        
        def circle_points(resolution, center, radius):
            """
            Generate points which define a circle on an image.Centre refers to the centre of the circle
            """   
            radians = np.linspace(0, 2*np.pi, resolution)
            c = center[1] + radius*np.cos(radians)#polar co-ordinates
            r = center[0] + radius*np.sin(radians)
            
            return np.array([c, r]).T
    # Exclude last point because a closed path should not have duplicate points
    
    
        if(argCircle == 1):
            points = circle_points(200, [80, 320], 80)[:-1]
        else:
            points = circle_points(200, [90, 250], 70)[:-1]
        
        snake = segmentation.active_contour(image_gray, points)
        fig, ax = image_show(image)
        ax.plot(points[:, 0], points[:, 1], '--r', lw=3)
        ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
        
    print("Py uzantılı dosya ile aynı dizinde active1.jpg ile active2.png dosyası olmalıdır!")
    image = io.imread("active1.jpg")
    test(image,1)
    image = io.imread("active2.png")
    test(image,2)
    print("Plot dosyaları oluşturuldu gui yi kapatınız.")
    return


tk.Label(window, text="Resimleri Düzenlemek için tıklayınız   =>").place(x=20, y = 50)
tk.Label(window, text="Videoları Düzenlemek için tıklayınız   =>").place(x=20, y = 100)
tk.Label(window, text="Sosyal Medya Filtresi için tıklayınız  =>").place(x=20, y = 150)
tk.Label(window, text="Active Contour örneği için tıklayınız  =>").place(x=20, y = 200)
tk.Button(window, text="resim", command=imageButton).place(x=240, y=50)
tk.Button(window, text="video", command=videoButton).place(x=240, y=100)
tk.Button(window, text="filtre", command=socialMediaFilter).place(x=240, y=150)
tk.Button(window, text="active", command=activeContourTest).place(x=240, y=200)

window.mainloop()
"""
path=tk.filedialog.askopenfilename(filetypes=[("Image File",'.png')])
print(path)


img = cv2.imread(r"C:/Users/Eren/Pictures/Screenshots/a.png")
img_filterede = exposure.equalize_hist(img)
cv2.imshow("org", img_filterede)
cv2.waitKey(0)
cv2.destroyAllWindows()

root=tk.Tk()
root.geometry("300x500+500+10")
blue_frame=tk.Frame(root, bg="blue", height=100, width=300)
blue_frame.grid(row=0, columnspan=2, stick="nsew") ## <-- sticky=fill both columns
ixButton = tk.Button(blue_frame, text="ixButton", command=imageButton)
ixButton.pack(expand=True, fill=tk.BOTH)

green_frame=tk.Frame(root, bg="green", height=300, width=200)
green_frame.grid(row=2, column=0)
gxButton = tk.Button(green_frame, text="gxButton", command=imageButton)
gxButton.pack()
agxButton = tk.Button(green_frame, text="agxButton", command=imageButton)
agxButton.pack()
gagxButton = tk.Button(green_frame, text="gagxBon", command=imageButton)
gagxButton.pack()


yellow_frame=tk.Frame(root, bg="yellow", height=300, width=100)
yellow_frame.grid(row=2, column=1)
yxButton = tk.Button(yellow_frame, text="yxButton", command=imageButton)
yxButton.pack()
ayxButton = tk.Button(yellow_frame, text="ayxButton", command=imageButton)
ayxButton.pack()
bayxButton = tk.Button(yellow_frame, text="bayxButton", command=imageButton)
bayxButton.pack()

tk.Button(root, text="Exit", bg="orange",
          command=root.quit).grid(row=20)
root.mainloop()
"""
