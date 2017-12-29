import os
import sys
import argparse

defalut_image = "./zgr.png"

parser = argparse.ArgumentParser()
parser.add_argument("-image",help="",default=defalut_image)





def main():
    args = parser.parse_args()
    image_path = args.image
    if not os.path.exists(image_path):
        print "image not exists!!!"
        exit()




    image_name = str(image_path).split(os.sep)[-1].split(".")[0]

    dir_path = "../images/styles"

    output_path = "build"+os.sep+image_name

    print output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_array = os.listdir(os.path.abspath(os.curdir) + os.sep + dir_path)

    total_task = 0
    for file_item in file_array:
        if file_item.endswith(".jpg") or file_item.endswith(".png") or file_item.endswith(".jpeg"):
            total_task = total_task + 1

    now_task = 0
    for file_item in file_array:
        try:
            if file_item.endswith(".jpg") or file_item.endswith(".png") or file_item.endswith(".jpeg"):
                now_task = now_task+1
                style_image = dir_path + os.sep + file_item
                output_name = output_path+os.sep+file_item
                print "task "+str(now_task)+"/"+str(total_task)
                command = " python2  ../main.py eval --content-image "+image_path+" --style-image " + style_image + " --model ../models/21styles.params  --cuda 0 " \
                          + " --output-image " +  output_name
                os.system(command)
        except:
            print "error transfer!!!"
            break;



if __name__=="__main__":
    main()
