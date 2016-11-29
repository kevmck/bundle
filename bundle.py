import configparser 
import os

os.system("clear")

conf = configparser.ConfigParser()
conf.read("bundleConfig.cfg")

ver = (os.popen("php /home/vm164/bundle/bundle/rabbitMQClient.php bundleRequest").read())
ver = ver.strip()
print("The next bundle version is " + ver)

print("Reading config...")
temp = conf.get("apiBundleConfig", "tempLocation")
apiLocation = conf.get("apiBundleConfig", "apiCode")
logLocation = conf.get("apiBundleConfig", "logCode")
cfgLocation = conf.get("apiBundleConfig", "cfgCode")
bundleStore = conf.get("apiBundleConfig", "bundleStoreLoc")

print("Copying files...")
os.system("mkdir " + temp + "/api")
os.system("cp " + apiLocation + " " + temp + "/api")
os.system("cp " + logLocation + " " + temp + "/api")
os.system("cp " + cfgLocation + " " + temp + "/api")

print("Zipping files...")
os.system("tar -cvzf /home/vm164/temp/APIv" + ver + ".tgz -C /home/vm164/temp/api .")

print("Copying to bundle server...")
os.system("scp " + temp + "/APIv" + ver + ".tgz " + bundleStore)
#os.system("scp " + temp + "/APIv.tgz vm164@192.168.2.21:/home/vm164/Desktop")

os.system("php /home/vm164/bundle/bundle/rabbitMQClient.php updateBundleVer") 

print("Cleaning up temp files...")
os.system("rm -rf " + temp + "/api")
#os.system("rm -r " + temp + "/APIv" + ver + ".tgz")

os.system("echo")
os.system("echo Operation completed successfully.")
os.system("exit")
