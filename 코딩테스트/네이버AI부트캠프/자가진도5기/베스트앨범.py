def solution(genres, plays):
    album = dict(); album_cnt = dict()
    answer = []; idx = 0
    
    # 앨범 저장
    for idx , (genre, play) in enumerate(zip(genres,plays)):
        try:
            album[genre].append((idx, play))
        except:
            #print(genre,play)
            album[genre] = [(idx, play)]
        idx+=1    
    print(album)
    
    # 앨범 총 횟수 저장
    for genre in album.keys():
        total = 0
        for instance in album[genre]:
                total +=instance[1]
        album_cnt[genre] = total
    
    for genre,cnt in sorted(album_cnt.items(),key=lambda x:x[1],reverse=True):
        for (idx,v) in sorted(album[genre],key=lambda x:x[1],reverse=True)[:2]:
            answer.append(idx)






    return answer

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    solution(genres,plays)
    