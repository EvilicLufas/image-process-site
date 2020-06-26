import image_process_site.request_handler.Request as Request

def main():
    test_url = 'https://v16m.tiktokcdn.com/780146b3b1f98a6af3e32d0a0ee5acaa/5ef57c3b/video/tos/useast2a/tos-useast2a-pve-0068/c8d6110f4f7840059d31028bbb4985a3/?a=1233&br=2904&bt=1452&cr=0&cs=0&dr=0&ds=3&er=&l=20200625224012010189066018368D0D6D&lr=tiktok_m&mime_type=video_mp4&qs=0&rc=am1wb2dzZDV4dTMzMzczM0ApODwzNmZkNGU0Nzw3OzY5OmdlLnA0Yi40XmdfLS0uMTZzcy0zXjVjMy9jXy5iXi1fMjQ6Yw%3D%3D&vl=&vr='
    req = Request(test_url)
    req.get_selenium_res

if __name__ == "__main__":
    main()