# N <= 1e4
# sort. N log N * 1e2 = 1e7

from collections import defaultdict
import heapq as hq

def solution(genres, plays):
    count_dict = defaultdict(int)
    song_dict = defaultdict(list)
    
    # survey
    for i, (genre, play) in enumerate(zip(genres, plays)):
        count_dict[genre] += play
        hq.heappush(song_dict[genre], (-play, i))
    
    # sort genre
    count_genres = []
    for genre, count_total in count_dict.items():
        hq.heappush(count_genres, (-count_total, genre))
    
    # make answer
    answer = []
    while count_genres:
        i, genre = hq.heappop(count_genres)
        song_count = 0
        while song_dict[genre] and song_count < 2:
            answer.append(hq.heappop(song_dict[genre])[1])
            song_count += 1
        
    return answer