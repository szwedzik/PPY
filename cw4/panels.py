import math

def calculate_panels(length, width):
    room_area = length * width
    room_area = room_area + (room_area * 0.1)

    panel_length = float(input("Podaj długość panela: "))
    panel_width = float(input("Podaj szerokość panela: "))
    panel_count = int(input("Podaj ilość paneli: "))

    panel_area = panel_length * panel_width
    panels_needed = room_area / panel_area
    packs_count = math.ceil(panels_needed / panel_count)

    print("Potrzeba:", packs_count, "paczek")


lenght = float(input("Podaj długość podłogi: "))
width = float(input("Podaj szerokość podłogi: "))
calculate_panels(lenght, width)