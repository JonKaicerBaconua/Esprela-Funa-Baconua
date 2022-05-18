def lap():
global time_elapsedl,time_elapsed2,time_elapsed3,timel,self_job,time2,i,j
if i<9:
    create_label ((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsedl).zfill(2)),20+(110*1),400+(1*50))
else:
    j += 1
    i = 0
    create_label ((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsedl).zfill(2)),20+(110*i),400+(1*50))
    i += 1