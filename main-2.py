import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import winsound as wn
import keyboard
import subprocess
import os

freq = 41010
duration = 5
stop = 0
while stop == 0:
    print("\033[1;35mWelcome to the Beep Boop Box!")
    print("\033[1;30m=============================")
    print("\033[1;3mDo you want to...")
    print('\033[1;0m')
    print("\033[1;34mPlay the Syth? (Press 1)")
    print("\033[1;34mRecord and play your own files? (Press 2)")
    print("\033[1;31mQuit? (Press 3)")
    user = input("\033[1;32m>> ")
    print("")
    if user == str('1'):
        '''
        print("Please select what you want to do:")
        print("Press 1 to play and record (esc to stop)")
        print("Press 2 to simply play away!")
        print(">> ")
        '''
        print("\033[1;35mEnjoy the Retro Synth! Press 'Esc' at any time to stop and save!")
        notes = []
        while True:
            try:
                if keyboard.is_pressed('a'):
                        wn.PlaySound("A1", wn.SND_FILENAME)
                    
                        notes.append("A1")
                if keyboard.is_pressed('s'):
                        wn.PlaySound("B1", wn.SND_FILENAME)
                     
                        notes.append("B1")
                        
                if keyboard.is_pressed('d'):
                        wn.PlaySound("C1", wn.SND_FILENAME)
                       
                        notes.append("C1")
                        
                if keyboard.is_pressed('f'):
                        wn.PlaySound("D1", wn.SND_FILENAME)
                       
                        notes.append("D1")
                        
                if keyboard.is_pressed('g'):
                        wn.PlaySound("E1", wn.SND_FILENAME)
                     
                        notes.append("E1")
                        
                if keyboard.is_pressed('h'):
                        wn.PlaySound("F1", wn.SND_FILENAME)
                       
                        notes.append("F1")
                        
                if keyboard.is_pressed('j'):
                        wn.PlaySound("G1", wn.SND_FILENAME)
                       
                        notes.append("G1")
                        
                if keyboard.is_pressed('k'):
                        wn.PlaySound("A2", wn.SND_FILENAME)
                       
                        notes.append("A2")
                        
                if keyboard.is_pressed('l'):
                        wn.PlaySound("B2", wn.SND_FILENAME)
                     
                        notes.append("B2")
                        
                if keyboard.is_pressed(';'):
                        wn.PlaySound("C2", wn.SND_FILENAME)
                    
                        notes.append("C2")
                        
                if keyboard.is_pressed('esc'):
                        synth_end = input("\033[1;34mPlease type a file name for your song! If you don't want to save, type 'none' >>")
                        if synth_end == 'none':
                            break
                        notesfile = open(synth_end + '.txt', 'w')
                        for element in notes:
                            notesfile.write(element + "\n")
                        notesfile.close()
                        print("")
                        print("")
                        break
            except:
                print("")
                print("")
                break
        if synth_end != 'none':
            print("\033[1;0mPlaying song:" + synth_end + "...")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            for i in range(len(notes)):
                wn.PlaySound(notes[i], wn.SND_FILENAME)
    
    if user == str('2'):
        while stop == 0:
            print("\033[1;30mPlease select what you wish to do:")
            print("\033[1;34mPress 1 to record a sound")
            print("Press 2 to play your previous sound (must have recorded first)")
            print("\033[1;31mPress 3 to end the program")
            user = input("\033[1;32m>> ")
            print("")
            if user == str('1'):
                name = input("\033[1;0mName for file (Please do not use 'output1' or 'initial, it will not save!) >> ")
                try:
                    duration = int(input("Duration of recording(Number of seconds)>> "))
                except ValueError:
                    print("Please only input an integer value, defaulted to 5 seconds")
                wn.Beep(700, 1000)
                print("Recording...")
                recording = sd.rec(int(duration * freq),
                                   samplerate=freq, channels=2)
                sd.wait()
                #write("outputinit.wav", freq, recording)
                wv.write("initial.wav", recording, freq, sampwidth=2)
                print("Recording Stopped...")
                
                #RETROFY IT
                
                subprocess.call("ffmpeg -i initial.wav -af acrusher=1:.5:51:0:log output1.wav")
                subprocess.call("sox output1.wav {} bandreject 80 1000 downsample 5 treble 10 pitch 350".format(name))
                #Cleanup temp files.
                if os.path.exists("output1.wav"):
                    os.remove("output1.wav")
                else:
                    pass
                if os.path.exists("initial.wav"):
                    os.remove("initial.wav")
                else:
                    pass
                wn.Beep(37, 1000)
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            elif user == str('2'):
                print("\033[1;0mPlaying sound...")
                filename = name
                wn.PlaySound(filename, wn.SND_FILENAME)
                print("Ending playback...")
                wn.Beep(37, 1000)
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            elif user == str('3'):
                stop = 1
                break
            else:
                print("Please only enter 1, 2, or 3...")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    if user == str('3'):
        print("Sad to see you go!")
        print("Boop Beep...")
        stop = 1
    
    
