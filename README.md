# bitmap info
read [BMP file format](https://en.wikipedia.org/wiki/BMP_file_format#Example_1)

![bitmap format image](https://en.wikipedia.org/wiki/BMP_file_format#/media/File:BMPfileFormat.svg)
## Usage
```
python bmp.py infile
```

## Bitmap file info
https://learn.microsoft.com/en-us/windows/win32/gdi/bitmap-header-types
https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapfileheader
```yaml
bimap file header(14):
    bfType(2) : The file type; must be BM.
    bfSize(4) : The size, in bytes, of the bitmap file.
    bfReserved1(2) : Reserved; must be zero.
    bfReserved2(2) : Reserved; must be zero.
    bfOffBits(4) : The offset, in bytes, from the beginning of the BITMAPFILEHEADER structure to the bitmap bits.

bitmap info(12~124):
    BITMAPCOREHEADER (12B):
    BITMAPCOREHEADER2 (64B):
    BITMAPINFOHEADER (40B):
    BITMAPV2INFOHEADER (52B):
    BITMAPV4HEADER (108B):
    BITMAPV5HEADER (124B):
```