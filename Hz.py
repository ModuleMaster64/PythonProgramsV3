def Sample(Hz):
    if Hz == 44100:
        print("CD Quality")
    if Hz < 44100:
        print("Low quality")
    if Hz > 44100:
        print("Compress")

Sample(48000)
