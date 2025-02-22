import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

def fetch_and_print_posts():
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
        else:
            print("Failed to fetch posts")

def fetch_and_save_posts():
    if response.status_code == 200:
        posts = response.json()

        posts_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)

        print("Data has been writen to posts.csv")
    else:
        print("Failed to fetch posts")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
