import cv2
import numpy as np

keyboard=np.zeros((1000,1500,3),np.uint8)

key_set={0:"Q",1:"W",2:"E",3:"R",4:"T",5:"Y",6:"U",7:"I",8:"O",9:"P",10:"A",11:"S",12:"D",
         13:"F",14:"G",15:"H",16:"J",17:"K",18:"L",19:"Z",20:"X",21:"C",22:"V",23:"B",24:"N",25:"M",
         26:"+",27:"-",28:"*",29:"/",30:"0",31:"1",32:"2",33:"3",34:"4",35:"5",36:"6",37:"7",38:"8",39:"9"}

def letter_box(letter_index,text):
    if letter_index==0:
        x=0
        y=0
    elif letter_index==1:
        x=135
        y=0
    elif letter_index==2:
        x=270
        y=0
    elif letter_index==3:
        x=405
        y=0
    elif letter_index==4:
        x=540
        y=0
    elif letter_index==5:
        x=675
        y=0
    elif letter_index==6:
        x=810
        y=0
    elif letter_index==7:
        x=945
        y=0
    elif letter_index==8:
        x=1080
        y=0
    elif letter_index==9:
        x=1215
        y=0
    elif letter_index==10:
        x=0
        y=135
    elif letter_index==11:
        x=135
        y=135
    elif letter_index==12:
        x=270
        y=135
    elif letter_index==13:
        x=405
        y=135
    elif letter_index==14:
        x=540
        y=135
    elif letter_index==15:
        x=675
        y=135
    elif letter_index==16:
        x=810
        y=135
    elif letter_index==17:
        x=945
        y=135
    elif letter_index==18:
        x=1080
        y=135
    elif letter_index==19:
        x=1215
        y=135
    elif letter_index==20:
        x=0
        y=270
    elif letter_index==21:
        x=135
        y=270
    elif letter_index==22:
        x=270
        y=270
    elif letter_index==23:
        x=405
        y=270
    elif letter_index==24:
        x=540
        y=270
    elif letter_index==25:
        x=675
        y=270
    elif letter_index==26:
        x=810
        y=270
    elif letter_index==27:
        x=945
        y=270
    elif letter_index==28:
        x=1080
        y=270
    elif letter_index==29:
        x=1215
        y=270
    elif letter_index==30:
        x=0
        y=405
    elif letter_index==31:
        x=135
        y=405
    elif letter_index==32:
        x=270
        y=405
    elif letter_index==33:
        x=405
        y=405
    elif letter_index==34:
        x=540
        y=405
    elif letter_index==35:
        x=675
        y=405
    elif letter_index==36:
        x=810
        y=405
    elif letter_index==37:
        x=945
        y=405
    elif letter_index==38:
        x=1080
        y=405
    elif letter_index==39:
        x=1215
        y=405

    ht = 135
    wt = 135
    th = 3  # thickness
    cv2.rectangle(keyboard, (x + th, y + th), (x + wt - th, y + ht - th), (255, 0, 0), th)

    # text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 8
    font_th = 3
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, hight_text = text_size[0], text_size[1]
    text_x = int((wt - width_text) / 2) + x
    text_y = int((ht + hight_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_th)


for i in range(40):
    letter_box(i,key_set[i])
cv2.imshow("Keyboard",keyboard)
cv2.waitKey(0)
cv2.destroyAllWindows()