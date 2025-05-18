from PIL import Image
import piexif
import argparse

# uses PIL to save a version of the photo without metadata
def strip_metadata(input_path, output_path=None):
    with Image.open(input_path) as img:
        data = list(img.getdata())

        clean_image = Image.new(img.mode, img.size)
        clean_image.putdata(data)

        # if no output given, overwrite file
        if output_path is None:
            output_path = input_path

        clean_image.save(output_path)

# for checking before and after of metadata
def read_exif_metadata(path):
    try:
        image = Image.open(path)
        exif_data = image.info.get('exif')

        if not exif_data:
            print(f"No EXIF metadata found in: {path}")
            return
        
        exif_dict = piexif.load(exif_data)
        print(f"EXIF metadata for {path}")

        for ifd in exif_dict:
            if exif_dict[ifd] is None:
                continue
            for tag in exif_dict[ifd]:
                tag_name = piexif.TAGS[ifd].get(tag, {}).get('name', tag)
                value = exif_dict[ifd][tag]
                print(f"\t{tag_name}: {value}")
    
    except Exception as e:
        print(f"Error with {path}: {e}")


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Strips Metadata from given EXIF file")
    parse.add_argument("input_path", help="path or name of file to be cleaned")
    parse.add_argument("--output_path", help="Optional output path for clean image")
    args = parse.parse_args()

    print("--- Reading ---")
    read_exif_metadata(args.input_path)
    print("--- Cleaning ---")
    strip_metadata(args.input_path, args.output_path)
    print("--- Clean ---")
    read_exif_metadata(args.input_path)
