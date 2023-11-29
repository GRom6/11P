from functools import lru_cache
@lru_cache
def FigureSum(n):
    Figures = [int(x) for x in str(n)]
    return sum(Figures)

def Max_Count(List):
    El = 0
    Count_El = 0
    for i in List:
        if List.count(i) > Count_El:
            El = i
            Count_El = List.count(i)
    return(El)

with open('17_3738') as f:
    Array = [int(x) for x in f.readlines()]
    Answer = []

    for i in range(1, len(Array) - 1):
        FigSum_Li = FigureSum(Array[i - 1])
        FigSum_Ui = FigureSum(Array[i + 1])
        if FigSum_Li == FigSum_Ui:
            summ = FigureSum(Array[i])
            Answer.append(summ)
    print(len(Answer), Max_Count(Answer))


# def Dict_sum(dict):
#     res = 0
#     for i in dict:
#         res += dict[i]
#     return res

# def Max_Value(dict):
#     Key = 0
#     Value = 0
#     for i in dict:
#         if dict[i] > Value:
#             Value = dict[i]
#             Key = i
#     return Key

# with open('17_3738') as f:
#     Array = [int(x) for x in f.readlines()]
#     Answer = {}

#     for i in range(1, len(Array) - 1):
#         FigSum_Li = FigureSum(Array[i - 1])
#         FigSum_Ui = FigureSum(Array[i + 1])
#         if FigSum_Li == FigSum_Ui:
#             summ = FigSum_Li + FigSum_Ui
#             try:
#                 Answer[summ] += 1
#             except:
#                 Answer[summ] = 1

#     print(Dict_sum(Answer),  Max_Value(Answer))