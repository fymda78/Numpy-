import numpy as np
import librosa
import matplotlib.pyplot as plt
import speech_recognition

signal, sample_rate = librosa.load ('travel10.wav',sr = None, mono = True)
threshold = 0.000163868
a = np.abs(signal) > threshold
b = a.astype(int)
#print(signal[a])
#print(np.where(b == 0))
c = np.where(a[:-1]!=a[1:])[0]
d = c.tolist()
d.insert(0,0)
e = [(d[i], d[i+1], d[i+1] - d[i]-1) for i in range(0, len(d)-1, 1)]
print(d)
print(e)
'''f = []
for i in range(1, len(e)-1):
    if e[i][2] < e[i+1][2] and e[i][2] < e[i-1][2]:
        f.append((e[i-1][0],e[i+1][0]))'''
#print(f)

'''for boolvalue in a:
    bool_list.append(np.where(a[:-1]!=a[1:])[0])'''




'''window_size = 5

weights = np.ones(window_size) / window_size

avg_signal = np.convolve(signal, weights, 'same')
r = speech_recognition.Recognizer()
myaudio = speech_recognition.AudioFile("travel10.wav")
with myaudio as source:
    googleaudio = r.record(source)
text = r.recognize_google(googleaudio)'''





'''fig = plt.figure()
plt.title("hhh")
#plt.xlim(0,10000)
lineplot = plt.plot (signal, color = 'blue')

#plt.show()'''
