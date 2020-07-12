#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:45:35 2020

@author: mahmood Ghouri
"""
from random import randint
import os
from pathlib import Path
import pdf2image
from tqdm import tqdm

def pdftopil(PDF_PATH):
    DPI = 300
    OUTPUT_FOLDER = None
    FIRST_PAGE = None
    LAST_PAGE = None
    FORMAT = 'tif'
    THREAD_COUNT = 1
    USERPWD = None
    USE_CROPBOX = False
    STRICT = False
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    return pil_images

def pdf_to_tif(pdf_path,tif_save_path):
    pil_images = pdftopil(pdf_path)
    save_images(pil_images, tif_save_path)

def save_images(pil_images, tif_save_path):
    index = 1
    for image in pil_images:
        randum_no = randint(100,999)
        image.save(tif_save_path + "/" + str(randum_no)+"_"+str(index)+'.tif')

if __name__ == '__main__':

    input_path = '/home/zyclyx/Documents/Branch_Development/testing folder/'
    tif_save_path = "/home/zyclyx/Documents/Branch_Development/testing folder/"
    
    Path(tif_save_path).mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(input_path):
        for file in tqdm(files):
            if file.endswith(".pdf"):
                pdf_path  = os.path.join(root,file)
                pdf_to_tif(pdf_path,tif_save_path)
                
    print("..Ends..")