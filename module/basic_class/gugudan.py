# while True:
#     gugu = int(input('please enter number'))
#     for a in range(1,10):
#         print(f'{gugu} X {a} = {gugu*a}')


def solution(hp):
    gen = hp // 5
    remainder = hp % 5

    while remainder % 3 != 0 and gen > 0:
        gen -= 1
        remainder += 5

    return gen + remainder // 3 + remainder % 3
print(solution(40))