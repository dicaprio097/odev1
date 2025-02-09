import turtle

for square in range(4):
    turtle.forward(60)
    turtle.right(90)

    turtle.speed(1)

print("Karenin bir kenarının uzunluğunu söyleyebilir misin?")

cvp1 = int(input("\tcm?\t"))

print(f"O halde kare'nin çevresi {(cvp1*4)}. Doğru bilmiş miyim?")


