import sys
import binascii


class Bytedecode(bytes):
    def decode(self, bytecode, encoding: int = 16) -> int:
        # b'\xd9\x03\x00\x00' -> (little endian) -> b'\x00\x00\x03\xd9'
        return int.from_bytes(bytecode, byteorder='little')
        return bytecode

class BITMAPCOREHEADER(Bytedecode):
    def __init__(self, bi):
        self.biWidth = self.decode(bi[0:2])
        self.biHeight = self.decode(bi[2:4])
        self.biPlanes = self.decode(bi[4:6])
        self.biBitCount = self.decode(bi[6:8])
    def __str__(self):
        return "[Bitmap Core Header]" + "\n" + \
                "------------------" + "\n" + \
                "biWidth: {}".format(self.biWidth) + "\n" + \
                "biHeight: {}".format(self.biHeight) + "\n" + \
                "biPlanes: {}".format(self.biPlanes) + "\n" + \
                "biBitCount: {}".format(self.biBitCount) + "\n\n"

class BITMAPINFOHEADER(Bytedecode):
    def __init__(self, bi):
        self.biWidth = self.decode(bi[0:4])
        self.biHeight = self.decode(bi[4:8])
        self.biPlanes = self.decode(bi[8:10])
        self.biBitCount = self.decode(bi[10:12])
        self.biCompression = self.decode(bi[12:16])
        self.biSizeImage = self.decode(bi[16:20])
        self.biXPelsPerMeter = self.decode(bi[20:24])
        self.biYPelsPerMeter = self.decode(bi[24:28])
        self.biClrUsed = self.decode(bi[28:32])
        self.biClrImportant = self.decode(bi[32:36])

    def __str__(self):
        return "[Bitmap Info Header]" + "\n" + \
                "------------------" + "\n" + \
                "biWidth: {}".format(self.biWidth) + "\n" + \
                "biHeight: {}".format(self.biHeight) + "\n" + \
                "biPlanes: {}".format(self.biPlanes) + "\n" + \
                "biBitCount: {}".format(self.biBitCount) + "\n" + \
                "biCompression: {}".format(self.biCompression) + "\n" + \
                "biSizeImage: {}".format(self.biSizeImage) + "\n" + \
                "biXPelsPerMeter: {}".format(self.biXPelsPerMeter) + "\n" + \
                "biYPelsPerMeter: {}".format(self.biYPelsPerMeter) + "\n" + \
                "biClrUsed: {}".format(self.biClrUsed) + "\n" + \
                "biClrImportant: {}".format(self.biClrImportant) + "\n\n"
    
class BITMAPV4HEADER(Bytedecode):
    def __init__(self, bi):
        self.biWidth = self.decode(bi[0:4])
        self.biHeight = self.decode(bi[4:8])
        self.biPlanes = self.decode(bi[8:10])
        self.biBitCount = self.decode(bi[10:12])
        self.biCompression = self.decode(bi[12:16])
        self.biSizeImage = self.decode(bi[16:20])
        self.biXPelsPerMeter = self.decode(bi[20:24])
        self.biYPelsPerMeter = self.decode(bi[24:28])
        self.biClrUsed = self.decode(bi[28:32])
        self.biClrImportant = self.decode(bi[32:36])
        self.biRedMask = self.decode(bi[36:40])
        self.biGreenMask = self.decode(bi[40:44])
        self.biBlueMask = self.decode(bi[44:48])
        self.biAlphaMask = self.decode(bi[48:52])
        self.biCSType = self.decode(bi[52:56])
        self.biEndpoints = self.decode(bi[56:72])
        self.biGammaRed = self.decode(bi[72:76])
        self.biGammaGreen = self.decode(bi[76:80])
        self.biGammaBlue = self.decode(bi[80:84])

    def __str__(self):
        return "[Bitmap V4 Header]" + "\n" + \
                "------------------" + "\n" + \
                "biWidth: {}".format(self.biWidth) + "\n" + \
                "biHeight: {}".format(self.biHeight) + "\n" + \
                "biPlanes: {}".format(self.biPlanes) + "\n" + \
                "biBitCount: {}".format(self.biBitCount) + "\n" + \
                "biCompression: {}".format(self.biCompression) + "\n" + \
                "biSizeImage: {}".format(self.biSizeImage) + "\n" + \
                "biXPelsPerMeter: {}".format(self.biXPelsPerMeter) + "\n" + \
                "biYPelsPerMeter: {}".format(self.biYPelsPerMeter) + "\n" + \
                "biClrUsed: {}".format(self.biClrUsed) + "\n" + \
                "biClrImportant: {}".format(self.biClrImportant) + "\n" + \
                "biRedMask: {}".format(self.biRedMask) + "\n" + \
                "biGreenMask: {}".format(self.biGreenMask) + "\n" + \
                "biBlueMask: {}".format(self.biBlueMask) + "\n" + \
                "biAlphaMask: {}".format(self.biAlphaMask) + "\n" + \
                "biCSType: {}".format(self.biCSType) + "\n" + \
                "biEndpoints: {}".format(self.biEndpoints) + "\n" + \
                "biGammaRed: {}".format(self.biGammaRed) + "\n" + \
                "biGammaGreen: {}".format(self.biGammaGreen) + "\n" + \
                "biGammaBlue: {}".format(self.biGammaBlue) + "\n\n"
    
class BITMAPV5HEADER(Bytedecode):
    def __init__(self, bi):
        self.biWidth = self.decode(bi[0:4])
        self.biHeight = self.decode(bi[4:8])
        self.biPlanes = self.decode(bi[8:10])
        self.biBitCount = self.decode(bi[10:12])
        self.biCompression = self.decode(bi[12:16])
        self.biSizeImage = self.decode(bi[16:20])
        self.biXPelsPerMeter = self.decode(bi[20:24])
        self.biYPelsPerMeter = self.decode(bi[24:28])
        self.biClrUsed = self.decode(bi[28:32])
        self.biClrImportant = self.decode(bi[32:36])
        self.biRedMask = self.decode(bi[36:40])
        self.biGreenMask = self.decode(bi[40:44])
        self.biBlueMask = self.decode(bi[44:48])
        self.biAlphaMask = self.decode(bi[48:52])
        self.biCSType = self.decode(bi[52:56])
        self.biEndpoints = self.decode(bi[56:72])
        self.biGammaRed = self.decode(bi[72:76])
        self.biGammaGreen = self.decode(bi[76:80])
        self.biGammaBlue = self.decode(bi[80:84])
        self.biIntent = self.decode(bi[84:88])
        self.biProfileData = self.decode(bi[88:92])
        self.biProfileSize = self.decode(bi[92:96])
        self.biReserved = self.decode(bi[96:100])
    
    def __str__(self):
        return "[Bitmap V5 Header]" + "\n" + \
                "------------------" + "\n" + \
                "biWidth: {}".format(self.biWidth) + "\n" + \
                "biHeight: {}".format(self.biHeight) + "\n" + \
                "biPlanes: {}".format(self.biPlanes) + "\n" + \
                "biBitCount: {}".format(self.biBitCount) + "\n" + \
                "biCompression: {}".format(self.biCompression) + "\n" + \
                "biSizeImage: {}".format(self.biSizeImage) + "\n" + \
                "biXPelsPerMeter: {}".format(self.biXPelsPerMeter) + "\n" + \
                "biYPelsPerMeter: {}".format(self.biYPelsPerMeter) + "\n" + \
                "biClrUsed: {}".format(self.biClrUsed) + "\n" + \
                "biClrImportant: {}".format(self.biClrImportant) + "\n" + \
                "biRedMask: {}".format(self.biRedMask) + "\n" + \
                "biGreenMask: {}".format(self.biGreenMask) + "\n" + \
                "biBlueMask: {}".format(self.biBlueMask) + "\n" + \
                "biAlphaMask: {}".format(self.biAlphaMask) + "\n" + \
                "biCSType: {}".format(self.biCSType) + "\n" + \
                "biEndpoints: {}".format(self.biEndpoints) + "\n" + \
                "biGammaRed: {}".format(self.biGammaRed) + "\n" + \
                "biGammaGreen: {}".format(self.biGammaGreen) + "\n" + \
                "biGammaBlue: {}".format(self.biGammaBlue) + "\n" + \
                "biIntent: {}".format(self.biIntent) + "\n" + \
                "biProfileData: {}".format(self.biProfileData) + "\n" + \
                "biProfileSize: {}".format(self.biProfileSize) + "\n" + \
                "biReserved: {}".format(self.biReserved) + "\n\n"



class BITMAPFILEHEADER(Bytedecode):
    def __init__(self, bf):
        self.bfType = bf[0:2].decode()
        self.bfSize =  self.decode(bf[2:6])
        self.bfReserved1 = self.decode(bf[6:8])
        self.bfReserved2 = self.decode(bf[8:10])
        self.bfOffBits = self.decode(bf[10:14])
    
    def __str__(self):
        return "[Bitmap File Header]" + "\n" + \
                "------------------" + "\n" + \
                "bfType: {}".format(self.bfType) + "\n" + \
                "bfSize: {}".format(self.bfSize) + "\n" + \
                "bfReserved1: {}".format(self.bfReserved1) + "\n" + \
                "bfReserved2: {}".format(self.bfReserved2) + "\n" + \
                "bfOffBits: {}".format(self.bfOffBits) + "\n\n"

class Bmp:
    def __init__(self, infile):
        self.infile = infile

        with open(infile, "rb") as inptr:
            self.bf = BITMAPFILEHEADER(inptr.read(14))
            self.biSize = int.from_bytes(inptr.read(4), byteorder='little')
            if self.biSize == 12:
                self.bi = BITMAPINFOHEADER(inptr.read(8))
            elif self.biSize == 40:
                self.bi = BITMAPINFOHEADER(inptr.read(36))
            elif self.biSize == 108:
                self.bi = BITMAPV4HEADER(inptr.read(104))
            elif self.biSize == 124:
                self.bi = BITMAPV5HEADER(inptr.read(120))

            # Determine padding for scanlines
            self.padding = (4 - self.bi.biWidth * 3) % 4

    def __str__(self):
        return "{}".format(self.bf) + \
                "{}".format(self.biSize) + \
               "{}".format(self.bi) + \
               "padding : {}".format(self.padding) + "\n" + \
               "pixel start ~ end range : {} ~ {}".format(hex(self.bf.bfOffBits), hex(self.bf.bfOffBits + self.bi.biSizeImage)) + "\n" + \
               "last address : {}".format(hex(self.bf.bfSize)) + "\n"
    
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bmp.py infile")
        sys.exit(1)

    bmp = Bmp(sys.argv[1])
    print(bmp)
    sys.exit(0)