def count_between(star_ip, end_ip):
    star_parts = map(int, star_ip.split('.'))
    start_num = sum(part << (8 * i) for i, part in enumerate(reversed(list(star_parts))))

    end_parts = map(int, end_ip.split('.'))
    end_num = sum(part << (8 * i) for i, part in enumerate(reversed(list(end_parts))))

    return end_num - start_num

a = count_between("10.0.0.0", "10.0.0.50")# 50
b = count_between("10.0.0.0", "10.0.1.0")# 256
c = count_between("20.0.0.10", "20.0.1.0")# 246

print(a)
print(b)
print(c)