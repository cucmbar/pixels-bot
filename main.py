from PIL import Image

def create_canvas(width, height):
    
    #Создает новый холст заданных размеров.
    
    return Image.new("RGB", (width, height), "white")

def draw_pixel(canvas, coordinates, color):
    
    #Рисует пиксель на холсте заданным цветом в указанных координатах.

    canvas.putpixel(coordinates, color)

def main():
    # Запрашиваем у пользователя размеры холста
    width = int(input("Введите ширину холста в пикселях: ")) + 1
    height = int(input("Введите высоту холста в пикселях: ")) + 1
    canvas = create_canvas(width, height)

    while True:
        user_input = input("Введите координаты пикселя и его цвет в формате (x,y,R,G,B), "
                           "или введите 'stop', чтобы завершить: ")

        # Проверяем, если пользователь ввел 'stop', завершаем программу
        if user_input.lower() == "stop":
            break

        try:
            # Разбиваем строку пользователя на координаты и цвет
            x, y, r, g, b = map(int, user_input.split(","))

            # Проверяем, что координаты и цвет заданы корректно
            if not (0 <= x < width) or not (0 <= y < height):
                raise ValueError(f"Координаты выходят за пределы холста (0-{width-1}, 0-{height-1})")
            if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
                raise ValueError("Цвет должен быть задан числами от 0 до 255 включительно")

            # Рисуем пиксель на холсте
            draw_pixel(canvas, (x, y), (r, g, b))  # Уменьшаем координаты на 1

        except Exception as e:
            print("Ошибка:", e)

    # Сохраняем изображение
    canvas.save("result.png")
    print("Изображение сохранено как result.png")

if __name__ == "__main__":
    main()
