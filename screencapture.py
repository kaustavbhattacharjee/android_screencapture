import os, time, subprocess,getpass,sys,img2pdf

pages=int(sys.argv[1])+1
adb_path="/Users/"+getpass.getuser()+"/Library/Android/sdk/platform-tools/adb"
for i in range(1,pages):
    subprocess.run([adb_path,"shell","screencap","/sdcard/myimage.png"])
    subprocess.run([adb_path,"pull","/sdcard/myimage.png"])
    os.system("cp myimage.png "+str(i)+".png")
    subprocess.run([adb_path, "shell", "input", "swipe", "530", "1819", "530", "1080"])
    time.sleep(3)
    printed=i
os.system("rm myimage.png")
subprocess.run([adb_path,"shell","rm","/sdcard/myimage.png"])
print("Printed "+str(printed)+"pages ")

#Combines the pages
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(os.getcwd()) if i.endswith(".png")]))



