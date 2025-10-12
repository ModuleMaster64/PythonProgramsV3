def Sample(Hz):
    if Hz == 44100:
        print("CD Quality")
    if Hz < 44100:
        print("Low Quality")
    if Hz > 44100:
        print("Compressed Quality")

Sample(48000)
