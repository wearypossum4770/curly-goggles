

jpg = '163fb48961d533656a4f0c8f3d608a2f374cf739.jpg'


class WebP(object):
	"""
	Usage:
		cwebp [options] -q quality input.png -o output.webp

		where quality is between 0 (poor) to 100 (very good).
		Typical value is around 80.
	"""

	def help(self):
		"""
		an exhaustive list of advanced options.
		"""
	def cwebp(self):
		"""
		Direct conversion will ask for a file.
		"""
		from pathlib import Path
		current_dir = Path('.')
		parent_dir = current_dir.parent
		test_file =  parent_dir / 'sample.png'
		f"webp {test_file} -o {test_file.stem}.webp"

if __name__=='__main__':
	print(WebP().cwebp())
	# Usage:
 # cwebp [-preset <...>] [options] in_file [-o out_file]

# If input size (-s) for an image is not specified, it is
# assumed to be a PNG, JPEG, TIFF or WebP file.

# Options:
  # -h / -help ............. short help
  # -H / -longhelp ......... long help
  # -q <float> ............. quality factor (0:small..100:big), default=75
  # -alpha_q <int> ......... transparency-compression quality (0..100),
                           # default=100
  # -preset <string> ....... preset setting, one of:
                            # default, photo, picture,
                            # drawing, icon, text
     # -preset must come first, as it overwrites other parameters
  # -z <int> ............... activates lossless preset with given
                           # level in [0:fast, ..., 9:slowest]

  # -m <int> ............... compression method (0=fast, 6=slowest), default=4
  # -segments <int> ........ number of segments to use (1..4), default=4
  # -size <int> ............ target size (in bytes)
  # -psnr <float> .......... target PSNR (in dB. typically: 42)

  # -s <int> <int> ......... input size (width x height) for YUV
  # -sns <int> ............. spatial noise shaping (0:off, 100:max), default=50
  # -f <int> ............... filter strength (0=off..100), default=60
  # -sharpness <int> ....... filter sharpness (0:most .. 7:least sharp), default=0
  # -strong ................ use strong filter instead of simple (default)
  # -nostrong .............. use simple filter instead of strong
  # -sharp_yuv ............. use sharper (and slower) RGB->YUV conversion
  # -partition_limit <int> . limit quality to fit the 512k limit on
                           # the first partition (0=no degradation ... 100=full)
  # -pass <int> ............ analysis pass number (1..10)
  # -crop <x> <y> <w> <h> .. crop picture with the given rectangle
  # -resize <w> <h> ........ resize picture (after any cropping)
  # -mt .................... use multi-threading if available
  # -low_memory ............ reduce memory usage (slower encoding)
  # -map <int> ............. print map of extra info
  # -print_psnr ............ prints averaged PSNR distortion
  # -print_ssim ............ prints averaged SSIM distortion
  # -print_lsim ............ prints local-similarity distortion
  # -d <file.pgm> .......... dump the compressed output (PGM file)
  # -alpha_method <int> .... transparency-compression method (0..1), default=1
  # -alpha_filter <string> . predictive filtering for alpha plane,
                           # one of: none, fast (default) or best
  # -exact ................. preserve RGB values in transparent area, default=off
  # -blend_alpha <hex> ..... blend colors against background color
                           # expressed as RGB values written in
                           # hexadecimal, e.g. 0xc0e0d0 for red=0xc0
                           # green=0xe0 and blue=0xd0
  # -noalpha ............... discard any transparency information
  # -lossless .............. encode image losslessly, default=off
  # -near_lossless <int> ... use near-lossless image
                           # preprocessing (0..100=off), default=100
  # -hint <string> ......... specify image characteristics hint,
                           # one of: photo, picture or graph

  # -metadata <string> ..... comma separated list of metadata to
                           # copy from the input to the output if present.
                           # Valid values: all, none (default), exif, icc, xmp

  # -short ................. condense printed message
  # -quiet ................. don't print anything
  # -version ............... print version number and exit
  # -noasm ................. disable all assembly optimizations
  # -v ..................... verbose, e.g. print encoding/decoding times
  # -progress .............. report encoding progress

# Experimental Options:
  # -jpeg_like ............. roughly match expected JPEG size
  # -af .................... auto-adjust filter strength
  # -pre <int> ............. pre-processing filter
