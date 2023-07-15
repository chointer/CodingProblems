def ymd2d(ymd):
    Y2M = 12
    M2D = 28
    YEAR = 2000
    
    y, m, d = map(int, ymd.split("."))
    return (y - YEAR) * Y2M * M2D + m * M2D + d


def solution(today, terms, privacies):
    M2D = 28
    answer = []
    
    # dictionary
    term = {}
    for te in terms:
        t, month = te.split()
        term[t] = int(month) * M2D
    
    today_days = ymd2d(today)
    
    for i, privacy in enumerate(privacies):
        collect, term_type = privacy.split()
        collect_days = ymd2d(collect)
        
        if today_days - collect_days >= term[term_type]:
            answer.append(i + 1)

    return answer