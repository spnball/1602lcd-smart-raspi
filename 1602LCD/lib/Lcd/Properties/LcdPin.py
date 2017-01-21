class LcdPin:
    # Raspberry Pi pin configuration:
    lcd_rs = 12,  # (15) Note this might need to be changed to 21 for older revision Pi's.
    lcd_en = 16,  # (13)
    lcd_d4 = 26,  # (22 - Red)
    lcd_d5 = 19,  # (18 - Orange)
    lcd_d6 = 13,  # (16 - Yello)
    lcd_d7 = 6,   # (12 - Green)
    lcd_back_light = 20

    def __init__(self):
        pass