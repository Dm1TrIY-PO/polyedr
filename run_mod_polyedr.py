#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.mod_polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["prism", "holey_box", "ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        poly = Polyedr(f"data/{name}.geom")
        poly.shadow()
        poly.draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print(f"Cумма длин проекций указанных рёбер: {round(poly.find_mod_par(), 3)}")
        poly.find_projection_angle()
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
