month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

while True:
    date_old = input("Дата: ")
    date_old_list = date_old.split(" ")

    if len(date_old_list) < 3:
     date_old_list = date_old.split(".")

    m_old = date_old_list[1]
    d_old = date_old_list[0]
    y_old = date_old_list[2]

    try:
        if not m_old.isdigit():
            m = month.index(m_old) + 1
            m_old = m
        m_old = int(m_old)
        d_old = int(d_old)
        y_old = int(y_old)
        if m_old < 13 and m_old > 0 and d_old > 0 and d_old < 32:
         break
    except ValueError:
            pass
    except TypeError:
            pass

print(f"{y_old}-{m_old:02d}-{d_old:02d}")

