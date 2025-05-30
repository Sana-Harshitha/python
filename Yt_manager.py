import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
           return  json.load(file)

    except FileNotFoundError:
         return []

def save_data_helpper(videos):
    with open("youtube.txt",'w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("-"*40)
    for index,video in  enumerate(videos,start=1):
        print(f"index:{index} video_name:{video['name']}")
    # print(list(enumerate(videos,start=1)))
    print("-"*40)
   

def add_video(videos):
    name=input("Add video Name: ")
    time=input("Add Video Time: ")
    videos.append({'name':name,'time':time})
    save_data_helpper(videos)


def update_video(videos):
    print("which of the following videos you want to update")
    list_all_videos(videos)
    index=int(input("Enter the index: "))
    if 1<= index <= len(videos):
        name=input("enter the new name: ")
        time=input("enter the new time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helpper(videos)
    else:
        print("Enter Valid Index")


def delete_video(videos):
    print("which of the following videos you want to delete")
    list_all_videos(videos)
    index=int(input("Enter the index: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helpper(videos)
    else:
        print("Enter Valid Index")


def main():
    videos=load_data()
    
    print("\n Youtube Manger | choose an option")
    print("1.List all youtube videos")
    print("2.Add a Youtube video")
    print("3.Update a youtube video details")
    print("4.Delete a youtube video")
    print("5.Exit the app")
    print("list of videos are : ",videos)
    while True:
        
        choice = input("Enter your choise: ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                    break
            case _:
                print("Invalid-Choice!")


if __name__== "__main__":
    main()