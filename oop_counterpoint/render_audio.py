import argparse, wave, struct, math

def synth_chord(sr=22050, seconds=3.0):
    freq = lambda n: 440.0*(2**((n-69)/12))
    N = int(seconds*sr); out=[]
    for i in range(N):
        v=0.0
        for n in [60,64,67]:
            v += math.sin(2*math.pi*freq(n)*(i/sr))*(0.2+0.1*math.sin(i/2000.0))
        out.append(v/3)
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True)   # interface placeholder
    ap.add_argument('--out', dest='out', required=True)
    args = ap.parse_args()
    sr=22050; data = synth_chord(sr=sr, seconds=3.0)
    with wave.open(args.out, 'w') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
        for s in data:
            wf.writeframes(struct.pack('<h', int(max(-1,min(1,s))*32767)))
    print('Wrote', args.out)
