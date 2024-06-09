import requests
import os

def post_to_linkedin():
    access_token = os.getenv('A1B2C3D4E5')
    url = 'https://api.linkedin.com/v2/ugcPosts'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    post_data = {
        "author": "urn:li:person:https://www.linkedin.com/in/marcia-xavier-moreira/",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "Hello, this is a test post from a GitHub Action!"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(url, headers=headers, json=post_data)
    
    if response.status_code == 201:
        print("Post created successfully!")
    else:
        print(f"Failed to create post: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    post_to_linkedin()
