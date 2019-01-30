def _save_image(image, matchs, paths):
    from PIL import Image, ImageDraw
    import io

    byteImgIO = io.BytesIO()
    byteImg = Image.open(image)
    byteImg.save(byteImgIO, "JPEG")
    byteImgIO.seek(0)
    byteImg = byteImgIO.read()

    img = Image.open(io.BytesIO(bytearray(byteImg))).convert('RGB')
    img_width, img_height = img.size
    print img_width
    print img_height
    draw = ImageDraw.Draw(img)

    # # Draw custom global region/area
    # if self._area != [0, 0, 1, 1]:
    #     draw_box(draw, self._area,
    #              img_width, img_height, "Detection Area", (0, 255, 255))

    for cat, values in matchs.items():

        # # Draw custom category regions/areas
        # if (cat in self._category_areas
        #     and self._category_areas[cat] != [0, 0, 1, 1]):
        #     label = "{} Detection Area".format(cat.capitalize())
        #     draw_box(
        #         draw, self._category_areas[cat], img_width,
        #         img_height, label, (0, 255, 0))

        # Draw detected objects
        for instance in values:
            label = "{0} {1:.1f}%".format(cat, instance['score'])
            print label
            print instance['box']
            draw_box(
                draw, instance['box'], img_width, img_height, label,
                (255, 255, 0))

    for path in paths:
        print("Saving results image to %s", path)
        img.save(path)

def draw_box(draw, box, img_width,
             img_height, text='', color=(255, 255, 0)):
    """Draw bounding box on image."""
    ymin, xmin, ymax, xmax = box
    print ymin
    print xmax
    (left, right, top, bottom) = (xmin, xmax,
                                  ymin, ymax)
    print left
    print right
    draw.line([(left, top), (left, bottom), (right, bottom),
               (right, top), (left, top)], width=5, fill=color)

    draw.ellipse((20, 20, 180, 180), fill='blue', outline='blue')

    if text:
        draw.text((left, abs(top-15)), text, fill=color)


matches = {}
category = 'person'
if category not in matches.keys():
    matches[category] = []

matches[category].append({
                'score': float(99),
                'box': [90,294,515,450]
                #'box': []
            })

_save_image("test-image3.jpg", matches, ["/tmp/test.jpg"])
