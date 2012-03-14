from mutagen.mp3 import MP3
import os, subprocess, re


args=['ffmpeg', '-i', '','-ab', '320k', '-ac', '2', '']
path='d:\\Music'
os.chdir(path)
directory=os.listdir(path)

def formatSongName(name):
    return re.sub(r'[\?\\\/\*\:\"\>\<\|]', '', name)

def convertM4AtoMP3(path):
    args[2] = path
    args[7] = re.sub(r'.m4a', '.mp3', path)
    (dirname, filename) = os.path.split(path)
    print 'Converting %s to ' % filename
    print '\t  ', re.sub(r'.m4a', '.mp3', filename)
    sts = subprocess.Popen(args, shell=True)
    sts.wait()
    os.remove(path)

def convertFLACtoMP3(path):
    args[2] = path
    args[7] = re.sub(r'.flac', '.mp3', path)
    (dirname, filename) = os.path.split(path)
    print 'Converting %s to ' % filename
    print '\t  ', re.sub(r'.flac', '.mp3', filename)
    sts = subprocess.Popen(args, shell=True)
    sts.wait()
    os.remove(path)
    
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.m4a'):
            convertM4AtoMP3(os.path.join(root, file))
        elif file.endswith('.flac'):
            convertFLACtoMP3(os.path.join(root, file))
        path = os.path.join(root, file)
        #if file.endswith('.mp3') or file.endswith('.Mp3'):
            #try:
                #audio = MP3(path)
                #f = str(audio['TIT2']) + '.mp3'
                #f = formatSongName(f)

                #print path
                #print os.path.join(root, f)
                #if os.rename(path, os.path.join(root, f)):
                    #print 'yay'
           # except KeyError:
                #print 'key error'
