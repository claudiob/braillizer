#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open("./redlogo.png")

bin = im.convert("L").point(lambda px: px < 148) # I might extract the mean

lines = [[[bin.getpixel((x,y)) for x in range(i, i+2) for y in range(j, j+3)] for i in range(0,bin.size[0]-2,2)] for j in range(0,bin.size[1]-3,3)]

values = [[b[0] + 2*b[1] + 4*b[2] + 8*b[3] + 16*b[4] + 32*b[5] for b in line] for line in lines]

hex = '<br />\n'.join([''.join(["&#%s;" % (10240 + v) for v in value]) for value in values])

html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n\
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n\
<html xml:lang="en" lang="en">\n\
  <head>\n\
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n\
    <style>\n\
      body {letter-spacing: -3px; line-height: 1px;  font-size: 8px;}\n\
      large-body   {letter-spacing: -4px; line-height: 14px; font-size: 20px;}\n\
    </style>\n\
  </head>\n\
  <body>\n\
  %s\n\
  </body>\n\
</html>\n' % hex

print html
# See http://en.wikipedia.org/wiki/Braille_ASCII
# " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="

# ⠀ (blank)
# ⠁ A or 1
# ⠂ comma
# ⠃ B or 2
# ⠄ apostrophe
# ⠅ K
# ⠆ semicolon
# ⠇ L
# ⠈
# ⠉ C or 3
# ⠊ I or 9
# ⠋ F or 6
# ⠌ (grade 2) the letters ST
# ⠍ M
# ⠎ S
# ⠏ P
# ⠐
# ⠑ E or 5
# ⠒
# ⠓ H or 8
# ⠔
# ⠕ O
# ⠖ exclamation point
# ⠗ R
# ⠘
# ⠙ D or 4
# ⠚ J or 0
# ⠛ G or 7
# ⠜
# ⠝ N
# ⠞ T
# ⠟ Q
# ⠠ capital letter follows
# ⠡ (grade 2) the letters CH
# ⠢
# ⠣
# ⠤ hyphen
# ⠥ U
# ⠦ opening question/quotation mark
# ⠧ V
# ⠨
# ⠩ (grade 2) the letters SH
# ⠪
# ⠫
# ⠬
# ⠭ X
# ⠮
# ⠯ (grade 2) the word AND
# ⠰
# ⠱
# ⠲ full stop
# ⠳
# ⠴ closing question/quotation mark
# ⠵ Z
# ⠶ bracket (parentheses)
# ⠷
# ⠸
# ⠹ (grade 2) the letters TH
# ⠺ W
# ⠻
# ⠼ number follows
# ⠽ Y
# ⠾
# ⠿

