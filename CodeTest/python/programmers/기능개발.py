progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    index = -1
    while index < len(progresses) - 1:
        
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        for i in range(len(progresses)):
            if progresses[i] < 100:
                if index != i - 1:                    
                    answer.append(i - 1 - index)     
                    index = i - 1
                break
            if i == len(progresses) - 1:
                answer.append(i - index)
                index = i
    
    return answer

print(solution(progresses, speeds))