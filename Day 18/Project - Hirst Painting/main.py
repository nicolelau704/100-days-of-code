import colorgram

#Extract colors from image
colors = colorgram.extract('image.jpg',15)

first_color = colors[0]

rgb = first_color.rgb

print(rgb)

