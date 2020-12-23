# txt file filled with my tweets (line by line, must be less than 280 char)
file = open("/Users/anishjampana/Downloads/tweets.txt", "r")

# reads line by line
filelines = file.readlines()

# closes once program reaches end of file
file.close()

# for loop to tweet each line by line every 24 hours (86400 seconds)
for line in filelines:
  print(line)
  if line != '\n':
      api.update_status(line)
  else:
      pass
  sleep(86400)
