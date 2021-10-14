
# #scipy 예제
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import odeint
#
# # Total population, N.
# N = 1000
# # Initial number of infected and recovered individuals, I0 and R0.
# I0, R0 = 1, 0
# # Everyone else, S0, is susceptible to infection initially.
# S0 = N - I0 - R0
# # Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
# beta, gamma = 0.2, 1./10
# # A grid of time points (in days)
# t = np.linspace(0, 160, 160)
#
# # The SIR model differential equations.
# def deriv(y, t, N, beta, gamma):
#     S, I, R = y
#     dSdt = -beta * S * I / N
#     dIdt = beta * S * I / N - gamma * I
#     dRdt = gamma * I
#     return dSdt, dIdt, dRdt
#
# # Initial conditions vector
# y0 = S0, I0, R0
# # Integrate the SIR equations over the time grid, t.
# ret = odeint(deriv, y0, t, args=(N, beta, gamma))
# S, I, R = ret.T
#
# # Plot the data on three separate curves for S(t), I(t) and R(t)
# fig = plt.figure(facecolor='w')
# ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
# ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
# ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
# ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
# ax.set_xlabel('Time /days')
# ax.set_ylabel('Number (1000s)')
# ax.set_ylim(0,1.2)
# ax.yaxis.set_tick_params(length=0)
# ax.xaxis.set_tick_params(length=0)
# ax.grid(b=True, which='major', c='w', lw=2, ls='-')
# legend = ax.legend()
# legend.get_frame().set_alpha(0.5)
# for spine in ('top', 'right', 'bottom', 'left'):
#     ax.spines[spine].set_visible(False)
# plt.show()



# #numpy
# def showGraph(function, arg):
#     fig = plt.figure(facecolor='w')
#     x = arg
#     y = function(x)
#     plt.plot(x, y)
#     plt.show()
#
# x= np.linspace(-np.pi, np.pi, 10)
#
# showGraph(np.cos, x)


# # numpy 연습
# a = np.array([1, 2, 3, 4])
# print(a * 2)
#
# b = np.arange(10)
# print(b)
#
# c = np.linspace(-3.14, 3.14, 10)
# print(c)


# 1차원 라이프게임
def nextGen(curList):
    nextList = curList.copy()

    for i in range(len(curList)):
        prevIdx = i - 1
        nextIdx = i + 1

        if nextIdx == len(curList):
            nextIdx = 0

        if curList[prevIdx] == curList[nextIdx]:
            nextList[i] = curList[i]

        else:
            if curList[i] == '0':
                nextList[i] = '1'
            else:
                nextList[i] = '0'

    return nextList

start = input("초기 패턴을 입력해주세요: ")
currentList = list(start)



while True:
    print("현재 상태는 다음과 같습니다.")
    print(currentList)

    userInput = input("다음 단계를 보시겠습니까 (y/n)")

    if userInput == 'y':
        currentList = nextGen(currentList)

    else:
        print("종료합니다.")
        break

