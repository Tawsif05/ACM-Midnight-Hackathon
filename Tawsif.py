import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont

df = pd.read_excel (r'C:\Users\Personal\OneDrive\Desktop\ACM Python\MidNightHackathon212.1.xlsx')

number_of_rows = np.arange(len(df))

for i in number_of_rows:
    r = int(i)
    img = Image.open(r'E:\ACM Python\wp6431925.jpg')
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial", 150)
    
    d1.text((900,650 ),df.iloc[r]['Name'],(0,0,0),font=font)
    
    d1.text((1800, 225),str(df.iloc[r]['Unique Id']),(0,0,0),font=font)
    
    img.save(r'E:\ACM Python\All Results' +"\\" + str(df.iloc[r]['Unique Id']) + '.png')
    
    

