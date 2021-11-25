import imgkit

with open('./url.txt') as f:
   for line in f:
      filename = str(line.replace("\n", "")+'.jpg')
      try:
       imgkit.from_url(line, filename)
      except:
       print filename
