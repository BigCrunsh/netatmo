from PIL import Image, ImageDraw, ImageFont


def draw_data(stations_data, font_file, image_file):
    im = Image.new(mode='L', size=(600, 800), color='white')
    draw = ImageDraw.Draw(im)

    for i, module_name in enumerate(stations_data.get_module_names()):
        if i > 0:
            draw.rectangle(xy=[15, 4+91 * i, 585, 5 + 91*i])
        module_data = stations_data.get_module_data(module_name)

        draw.text(xy=(15, 30+91*i), text=module_name, font=ImageFont.truetype(font_file, 15))
        if 'Temperature' in module_data['dashboard_data']:
            draw.text(
                xy=(15, 55+91*i),
                text='{}°C'.format(module_data['dashboard_data']['Temperature']),
                font=ImageFont.truetype(font_file, 30)
            )

        if 'sum_rain_1' in module_data['dashboard_data']:
            draw.text(
                xy=(15, 55+91*i),
                text='{}mm'.format(module_data['dashboard_data']['sum_rain_1']),
                font=ImageFont.truetype(font_file, 30)
            )

        if 'WindStrength' in module_data['dashboard_data']:
            draw.text(
                xy=(15, 55+91*i),
                text='{}kph'.format(module_data['dashboard_data']['WindStrength']),
                font=ImageFont.truetype(font_file, 30)
            )

    del draw
    im.save(image_file)

