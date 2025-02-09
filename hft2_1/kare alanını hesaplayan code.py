import turtle

for square in range(4):
    turtle.forward(60)
    turtle.right(90)

    turtle.speed(1)

print("Karenin bir kenarının uzunluğunu söyleyebilir misin? Alanını hesaplayacağım.")

cvp1 = int(input("\tcm?\t"))

print(f"O halde kare'nin alanı {(cvp1*cvp1)}. Doğru bilmiş miyim?")


