import cv2
import pytesseract
import imutils


pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/pytesseract.exe"
image = cv2.imread("image/input1.jpg")
image = imutils.resize(image, width= 500)
gray = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralfilter(gray,11,17,17)
edge = cv2.canny(gray,170,200)
cnts ,new =cv2.findcontoers(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1 =image.copy()
cv2.drowcontours(image1,cnts,-1,(0,255,0),3)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[: 30]
NumberPlateCount= None
image2 = image.copy()
cv2.drowcontours(image2,cnts,-1,(0,255,0),3)
count= 0
name =1
for i in cnts:
    perimeter =cv2.arcLenght(i, True)
    approx = cv2.approxPolyDP(i,0.02* perimeter, True)
    if(len(approx) == 4):
        NumberPlateCount= approx
        x,y,w,h =cv2.boundingRect(i)
        crp_img =image[y:y+h, x:x+w]
        cv2.imwrite(str(name)+'.png', crp_img)
        name +=1
        break
cv2.drawcontours(image,[NumberPlateCount],-1 ,(0,225,0),3)
crpImg ='1.png'
cv2.imshow("Croped image", cv2.imread(crpImg))
text = pytesseract.image_to_string(crpImg, lang='eng')
print("number is: ", text)



cv2.imshow("original image", image)
cv2.imshor("Gray image", gray)
cv2.imshor("Smooth image", gray)
cv2.imshor("canny image", edge)
cv2.imshor("Canny after counters image", image1)
cv2.imshor("croped image", image2)
cv2.imshor("Final image", image)


cv2.waitkey(0)
