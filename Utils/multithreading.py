import threading                                                                

def concurrent_job(items, start, end, task, res):                                                 
    for item in items[start:end]:                                               
        try:                                                                    
            res.append(task(item))
        except Exception:                                                       
            print('error with item')                                            

def split_processing(items, task, num_splits = 4):                                      
    split_size = len(items) // num_splits                                       
    threads = []
    res = []                                                                  
    
    for i in range(num_splits):                                                            
        start = i * split_size                                                           
        end = None if i+1 == num_splits else (i+1) * split_size                                                                    
        threads.append(                                                         
            threading.Thread(target=concurrent_job, args=(items, start, end, task, res)))         
        threads[-1].start()                 
                                   
    for t in threads:                                                           
        t.join()
    return res 