# 단순히 한 바퀴 돌 때마다 체크해볼까.
# 아니면 더 쉽게 1초마다 체크할까.
# 셋이 동시에 만나는 경우는?
# 360도를 늘려야할 것 같은데. 360 * 60 * 60 sec 로?

# t0 <= t1
def hms2sec(h, m, s):
    return 60*60*h + 60*m + s
def sec2hms(s):
    h = s//3600
    m = (s%3600)//60
    s = s%60
    return h, m ,s 

def solution(h1, m1, s1, h2, m2, s2):
    t1 = hms2sec(h1, m1, s1)
    t2 = hms2sec(h2, m2, s2)
    
    #h = (h1%12) * 30 * (60 * 60)
    #m = m1 * 6 * (60 * 60)
    #s = s1 * 6 * (60 * 60)
    # (각도 sec / 시간 sec)
    dh = 30                     # [sec/sec] 1시간에 30도. 3600초에 30*3600초
    dm = 6 * 60                 # [sec/sec] 1분에 360/60=6도. 60초에 6*3600초
    ds = 6 * 60 * 60            # [sec/sec] 1초에 360/60=6도. 1초에 6*3600초
    sec_360 = 360 * 60 * 60     # 1296000
    h = (t1 * dh)%sec_360
    m = (t1 * dm)%sec_360
    s = s1 * ds
    
    count = 0
    if h == s or h == s:
        count += 1

    for t in range(t1, t2):

        if s < h and s + ds >= h + dh:
            count += 1
        
        if s < m and s + ds >= m + dm:
            count += 1
        if h + dh == m + dm:
            count -= 1

        s = (s + ds)%sec_360
        m = (m + dm)%sec_360
        h = (h + dh)%sec_360
        
    return count