import configparser 
import os

#Section 1 - configparser
#Initializes the variable that will store the config file during execution.
#Use the absolute path if the config file is NOT located in the same directory as this script.
conf = configparser.ConfigParser()
conf.read("testConfig.cfg")

#Section 2 - Import Configurations
#Creates variables from the config file that this script will use to define folder locations & version #s.
#If you would like to test without the config file, use absolute paths in Section 3 and comment
#out the following four lines of code.
print("Reading config...")
temp = conf.get("Test", "tempLocation")
file1 = conf.get("Test", "testText")
file2 = conf.get("Test", "audiPic")
confFile = conf.get("Test", "ownLocation")
currVer = int(conf.get("Versions", "current"))
prevVer = int(conf.get("Versions", "previous"))

#Section 3 - File Operations
#Uses the variables created in Section 2 to run specified commands. If you would like to test
#without the config file, remove the variables and use absolute paths.
print("Copying files...")
os.system("mkdir " + temp)
os.system("cp " + file1 + " " + temp)
os.system("cp " + file2 + " " + temp)

#Section 4 - Compress/Send Tarball, Update Version Numbers
#Creates tarball and uses SCP to transfer it to specified VM. Replace IP address with your own.
#NOTE: SSH needs to be installed and configured on the remote machine (the one you are copying to),
#and you will need to create SSH keys, since you can't enter the remote machine's password.
#NOTE: Reset version numbers to 0 in config file before making first bundle.
print("Updating version numbers...")
prevVer = (str(currVer))
currVer += 1
currVer = (str(currVer))
conf.set("Versions", "previous", prevVer)
conf.set("Versions", "current", currVer)

#Updates config file with new version numbers and copies it into .../temp to be zipped.
print("Writing config...")
with open('testConfig.cfg', 'w+') as configfile:
    conf.write(configfile)
os.system("cp " + confFile + " " + temp)

print("Zipping files...")
os.system("tar -cvzf /home/vm164/Desktop/testCompressV" + currVer + ".tgz -C /home/vm164/Desktop/temp .")
#print("Copying to bundle server...")
#os.system("scp /home/vm164/Desktop/testCompress.tgz 192.168.2.21:/home/vm164/Desktop")

#Section 5 - Cleanup
#Removes the temp folder and the tarball.
print("Cleaning up temp files...")
os.system("rm -r " + temp)
#os.system("rm -r /home/vm164/Desktop/testCompressV" + str(currVen) + ".tgz")


os.system("echo")
os.system("echo Operation completed successfully.")
os.system("exit")
