import insert_query

import time

if __name__ == '__main__':
    start_time = time.time()

    for i in range(1, 1000):
        insert_query.insertUser()
        print(i)
        
    print("--- %s seconds ---" % (time.time() - start_time))


# --- 733.3959465026855 seconds ---







