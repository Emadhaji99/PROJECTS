import os 
import shutil
def serial_movie_sorter():

#statics variable 

    main_path="C:\\project\\layer 1\\cinema"
    movie_path=os.path.join(main_path,"Movie")
    if not os.path.exists(movie_path):
        os.makedirs(movie_path)
    File_list=[]
# finding the algorithem for sort the videose 
    while True:
        for index,(dirpath, dirnames, filenames) in enumerate(os.walk(main_path)):
            if index==0:     
                for file_index,file in enumerate(filenames):
                    root,ext= os.path.splitext(file)
                    base_deteremination=root.lower()[0:8]
                    if ext==".mkv":
                        if file_index==0:
                            First_file_name=file
                            File_list.append(file)
                            continue
                    change_formt=File_list[0].lower()[0:8]
                    if change_formt==base_deteremination:
                        File_list.append(file)
# movies 
        if len(File_list)==1:                                                  
            shutil.move(os.path.join(main_path,First_file_name),movie_path) 
            File_list.clear()
            continue
# serial
        elif len(File_list)!=1:
            Serial_root ,ext= os.path.splitext(File_list[0]).lower()
            s_index=Serial_root.find(".s")
            serial_name=Serial_root[:s_index]
            serial_path=os.path.join(main_path,serial_name)
            if not os.path.exists(serial_path):
                os.makedirs(serial_path)
            for episodes in File_list:
                  shutil.move(os.path.join(main_path,episodes),serial_path)
            File_list.clear()
# end the process 
        if len(filenames)==0:
            break
        else:
            continue
serial_movie_sorter()
